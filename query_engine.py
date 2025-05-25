import json

def load_table(table_name):
    filename = f"{table_name}.json"
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Table '{table_name}' not found (expected file: {filename})")
        return []

def evaluate_condition(row, condition):
    if condition['type'] == 'condition':
        left = condition['left']
        op = condition['op']
        right = condition['right']

        # Convert right value to int/float if numeric
        if isinstance(right, str):
            if right.isdigit():
                right = int(right)
            elif right.replace('.', '', 1).isdigit():
                right = float(right)
            elif right.startswith("'") and right.endswith("'"):
                right = right[1:-1]

        left_value = row.get(left)

        # Apply comparison
        if op == '=': return left_value == right
        if op == '!=': return left_value != right
        if op == '<': return left_value < right
        if op == '<=': return left_value <= right
        if op == '>': return left_value > right
        if op == '>=': return left_value >= right
        return False

    elif condition['type'] == 'and':
        return evaluate_condition(row, condition['left']) and evaluate_condition(row, condition['right'])

    elif condition['type'] == 'or':
        return evaluate_condition(row, condition['left']) or evaluate_condition(row, condition['right'])

    return False


def run_query(query):
    if query['type'] != 'SELECT':
        print("Only SELECT statements are supported.")
        return []

    table_data = load_table(query['table'])
    if not table_data:
        return []

    # Filter rows if there's a WHERE clause
    if query['where']:
        table_data = [row for row in table_data if evaluate_condition(row, query['where'])]

    # Select columns
    if query['columns'] == '*':
        result = table_data
    else:
        columns = query.get("columns", "*")
        if columns == "*" or columns is None:
            result = table_data
        else:
            result = [{col: row.get(col, None) for col in columns} for row in table_data]

    return result