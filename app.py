from flask import Flask, request, jsonify, render_template
from antlr4 import InputStream, CommonTokenStream
from CompiledFiles.MiniSQLLexer import MiniSQLLexer
from CompiledFiles.MiniSQLParser import MiniSQLParser
from MiniSQLVisitorImpl import MiniSQLVisitorImpl
from query_engine import run_query

app = Flask(__name__)

# Route giao diện chính (home page)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_query():
    try:
        sql_input = request.json.get("query", "")
        if not sql_input:
            return jsonify({"error": "No query provided."}), 400

        # Lexing and parsing
        input_stream = InputStream(sql_input)
        lexer = MiniSQLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = MiniSQLParser(stream)
        tree = parser.program()

        # Visiting tree
        visitor = MiniSQLVisitorImpl()
        parsed_queries = visitor.visit(tree)

        # Run and gather results
        results = []
        for query in parsed_queries:
            result = run_query(query)
            results.append(result)

        return jsonify({"result": results})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
