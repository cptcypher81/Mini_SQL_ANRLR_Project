import json
import os

def load_table(table_name):
    filename = f"{table_name}.json"
    if not os.path.exists(filename):
        print(f"Error: Table '{table_name}' not found (expected file: {filename})")
        return []
    with open(filename, 'r') as f:
        return json.load(f)

def save_table(table_name, data):
    filename = f"{table_name}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def evaluate_condition(row, condition):
    if condition['type'] == 'condition':
        left = condition['left']
        op = condition['op']
        right = condition['right']

        # Normalize value types
        if isinstance(right, str):
            if right.startswith("'") and right.endswith("'"):
                right = right[1:-1]
            if right.isdigit():
                right = int(right)
            elif right.replace('.', '', 1).isdigit():
                right = float(right)

        left_value = row.get(left)

        if op == '=': return left_value == right
        if op == '!=': return left_value != right
        if op == '<': return left_value < right
        if op == '<=': return left_value <= right
        if op == '>': return left_value > right
        if op == '>=': return left_value >= right
        return False

    elif condition['type'] == 'between':
        field = condition['field']
        val = row.get(field)
        lower = condition['lower']
        upper = condition['upper']

        try:
            val = float(val)
            lower = float(lower)
            upper = float(upper)
        except:
            pass  # Keep string comparison fallback

        return lower <= val <= upper

    elif condition['type'] == 'and':
        return evaluate_condition(row, condition['left']) and evaluate_condition(row, condition['right'])

    elif condition['type'] == 'or':
        return evaluate_condition(row, condition['left']) or evaluate_condition(row, condition['right'])
    
    elif condition['type'] == 'not':
        return not evaluate_condition(row, condition['condition'])

    return False

def run_query(query):
    table_name = query.get("table")
    if not table_name:
        print("No table specified.")
        return []

    table_data = load_table(table_name)

    if query['type'] == 'SELECT':
        if query['where']:
            table_data = [row for row in table_data if evaluate_condition(row, query['where'])]

        group_by = query.get("group_by")
        if group_by:
            grouped_data = {}
            for row in table_data:
                # Use a tuple of group-by column values as the key
                key = tuple(row.get(col) for col in group_by)
                if key not in grouped_data:
                    grouped_data[key] = []
                grouped_data[key].append(row)
        
            # Simplest form: just return the first row from each group
            table_data = [group[0] for group in grouped_data.values()]


        if 'order_by' in query and query['order_by']:
            def normalize(val):
                if isinstance(val, str):
                    if val.isdigit():
                        return int(val)
                    try:
                        return float(val)
                    except ValueError:
                        return val
                return val

            for col, direction in reversed(query['order_by']):
                table_data.sort(
                    key=lambda row: normalize(row.get(col, None)),
                    reverse=(direction.upper() == "DESC")
                )
        
        if query.get("limit") is not None:
            try:
                limit = int(query["limit"])
                table_data = table_data[:limit]
            except ValueError:
                print("Invalid LIMIT value.")

        columns = query['columns']

        # Check if it's a pure '*' selection
        if columns == '*':
            selected_data = table_data

        # Check for aggregation
        elif any(isinstance(col, dict) and 'agg_func' in col for col in columns):
            agg_result = {}
            for col in columns:
                if isinstance(col, dict):
                    func = col['agg_func'].upper()
                    field = col['column']
                    values = [row.get(field) for row in table_data if row.get(field) is not None]

                    try:
                        values = list(map(float, values))
                    except:
                        values = []

                    if func == "COUNT":
                        agg_result[f"COUNT({field})"] = len(values)
                    elif func == "AVG":
                        agg_result[f"AVG({field})"] = round(sum(values) / len(values), 2) if values else None
                    elif func == 'SUM':
                        agg_result[f"SUM({field})"] = sum(values) if values else None
                    elif func == 'MIN':
                        agg_result[f"MIN({field})"] = min(values) if values else None
                    elif func == 'MAX':
                        agg_result[f"MAX({field})"] = max(values) if values else None

                else:
                    agg_result[col] = None
            selected_data = [agg_result]  # One row result

        # Regular column selection
        else:
            selected_data = [{col: row.get(col, None) for col in columns} for row in table_data]

        # Apply DISTINCT if specified
        if query.get("distinct"):
            seen = set()
            distinct_rows = []
            for row in selected_data:
                normalized = tuple(str(v) for v in row.values())
                if normalized not in seen:
                    seen.add(normalized)
                    distinct_rows.append(row)
            selected_data = distinct_rows
        
        return selected_data

    elif query['type'] == 'INSERT':
        new_row = dict(zip(query['columns'], query['values']))
        table_data.append(new_row)
        save_table(table_name, table_data)
        print("Row inserted.")
        return []

    elif query['type'] == 'DELETE':
        original_count = len(table_data)
        table_data = [row for row in table_data if not evaluate_condition(row, query['where'])]
        save_table(table_name, table_data)
        print(f"{original_count - len(table_data)} row(s) deleted.")
        return []

    elif query['type'] == 'UPDATE':
        updated_count = 0
        for row in table_data:
            if evaluate_condition(row, query['where']):
                for col, val in query['assignments']:
                    row[col] = val
                updated_count += 1
        save_table(table_name, table_data)
        print(f"{updated_count} row(s) updated.")
        return []

    else:
        print(f"Unsupported query type: {query['type']}")
        return []
