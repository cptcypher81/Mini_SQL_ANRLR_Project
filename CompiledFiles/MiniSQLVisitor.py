# Generated from MiniSQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniSQLParser import MiniSQLParser
else:
    from MiniSQLParser import MiniSQLParser

# This class defines a complete generic visitor for a parse tree produced by MiniSQLParser.

class MiniSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniSQLParser#program.
    def visitProgram(self, ctx:MiniSQLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#statement.
    def visitStatement(self, ctx:MiniSQLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#selectStmt.
    def visitSelectStmt(self, ctx:MiniSQLParser.SelectStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#allColumns.
    def visitAllColumns(self, ctx:MiniSQLParser.AllColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#specificColumns.
    def visitSpecificColumns(self, ctx:MiniSQLParser.SpecificColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#condition.
    def visitCondition(self, ctx:MiniSQLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#expression.
    def visitExpression(self, ctx:MiniSQLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#comparator.
    def visitComparator(self, ctx:MiniSQLParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#columnName.
    def visitColumnName(self, ctx:MiniSQLParser.ColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#tableName.
    def visitTableName(self, ctx:MiniSQLParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#literal.
    def visitLiteral(self, ctx:MiniSQLParser.LiteralContext):
        return self.visitChildren(ctx)



del MiniSQLParser