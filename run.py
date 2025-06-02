import sys
import os
import subprocess
from antlr4 import *

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/antlr/antlr-4.13.1-complete.jar'
CPL_Dest = 'CompiledFiles'
SRC = 'MiniSQL.g4'

def printUsage():
    print('python run.py gen')
    print('python run.py test')

def printBreak():
    print('-----------------------------------------------')

def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-visitor', '-Dlanguage=Python3', SRC])
    print('Generate successfully')

def runTest():
    print('Running testcases...')

    from CompiledFiles.MiniSQLLexer import MiniSQLLexer
    from CompiledFiles.MiniSQLParser import MiniSQLParser
    from MiniSQLVisitorImpl import MiniSQLVisitorImpl
    from query_engine import run_query  # Import your engine here

    from antlr4.error.ErrorListener import ErrorListener

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg}")
            exit(1)

    input_path = os.path.join(DIR, 'tests', '001.txt')

    # Token display
    print("List of token: ")
    lexer = MiniSQLLexer(FileStream(input_path))
    tokens = []
    token = lexer.nextToken()
    while token.type != Token.EOF:
        if token.text.strip() and token.text != ",":
            tokens.append(token.text)
        token = lexer.nextToken()
    tokens.append('<EOF>')
    print(','.join(tokens))

    # Parse and visit
    input_stream = FileStream(input_path)
    lexer = MiniSQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniSQLParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    tree = parser.program()

    visitor = MiniSQLVisitorImpl()
    queries = visitor.visit(tree)
    print("Visitor result:", queries)

    if not isinstance(queries, list):
        queries = [queries]

    for idx, query in enumerate(queries):
        print(f"\nExecuting Query {idx + 1}:")
        result = run_query(query)
        if result:
            print("Query Results:")
            for row in result:
                print(row)


    print(tree.toStringTree(recog=parser))
    print("Input accepted")
    printBreak()
    print("Run tests completely")

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    printBreak()

    if len(argv) < 1:
        printUsage()
    elif argv[0] == 'gen':
        generateAntlr2Python()
    elif argv[0] == 'test':
        runTest()
    else:
        printUsage()

if __name__ == '__main__':
    main(sys.argv[1:])