from flask import Flask, request, jsonify, render_template
from antlr4 import *
from CompiledFiles.MiniSQLLexer import MiniSQLLexer
from CompiledFiles.MiniSQLParser import MiniSQLParser
from MiniSQLVisitorImpl import MiniSQLVisitorImpl
from query_engine import run_query
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-query', methods=['POST'])
def run_query_from_input():
    try:
        content = request.json
        query_text = content.get("query", "")

        input_stream = InputStream(query_text)
        lexer = MiniSQLLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = MiniSQLParser(token_stream)
        tree = parser.program()

        visitor = MiniSQLVisitorImpl()
        parsed_queries = visitor.visit(tree)

        results = []
        for pq in parsed_queries:
            res = run_query(pq)
            if pq['type'] == 'INSERT':
                res = "Add successful"
            elif pq['type'] == 'UPDATE':
                res = "Update successful"
            elif pq['type'] == 'DELETE':
                res = "Delete successful"
            results.append(res)

        # Save all results to result.json
        with open("result.json", "w") as f:
            json.dump(results, f, indent=2)

        print("RESULT:", results)
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
