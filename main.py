from antlr4 import *
from CompiledFiles.MiniSQLLexer import MiniSQLLexer
from CompiledFiles.MiniSQLParser import MiniSQLParser
from MiniSQLVisitorImpl import MiniSQLVisitorImpl
from query_engine import execute_query

def main():
    print("MiniSQL Engine Ready.")
    query = input("Enter your SQL query:\n")

    # Prepare ANTLR input
    input_stream = InputStream(query)
    lexer = MiniSQLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MiniSQLParser(token_stream)

    # Parse and visit
    tree = parser.program()
    visitor = MiniSQLVisitorImpl()
    parsed_query = visitor.visit(tree)

    # Output visitor result (debug)
    print("\nParsed Query String:")
    print(parsed_query)

    # Evaluate using your query engine
    print("\nQuery Result:")
    result = execute_query(parsed_query, "students.json")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
