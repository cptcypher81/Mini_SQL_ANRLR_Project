from antlr4 import *
from CompiledFiles.MiniSQLParser import MiniSQLParser
from CompiledFiles.MiniSQLVisitor import MiniSQLVisitor

class MiniSQLVisitorImpl(MiniSQLVisitor):

    def visitProgram(self, ctx: MiniSQLParser.ProgramContext):
        # Handle one or more statements
        results = []
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if result is not None:
                results.append(result)
        return results[0] if results else None  # Return first statement's result


    def visitStatement(self, ctx: MiniSQLParser.StatementContext):
        return self.visit(ctx.selectStmt())

    def visitSelectStmt(self, ctx: MiniSQLParser.SelectStmtContext):
        columns = self.visit(ctx.columnList())
        table = self.visit(ctx.tableName())
        where_condition = self.visit(ctx.condition()) if ctx.condition() else None

        return {
            "type": "SELECT",
            "columns": columns,
            "table": table,
            "where": where_condition
        }

    def visitColumnList(self, ctx: MiniSQLParser.ColumnListContext):
        if ctx.getChildCount() == 1 and ctx.getChild(0).getText() == "*":
            return "*"
    
        # Defensive check
        column_nodes = ctx.columnName()
        if not column_nodes:
            return []

        columns = [col.getText() for col in column_nodes]
        return columns


    def visitTableName(self, ctx: MiniSQLParser.TableNameContext):
        return ctx.getText()

    def visitCondition(self, ctx: MiniSQLParser.ConditionContext):
        left = self.visit(ctx.expression(0))
        comparator = self.visit(ctx.comparator())
        right = self.visit(ctx.expression(1))
        return {
            "left": left,
            "op": comparator,
            "right": right
        }

    def visitExpression(self, ctx: MiniSQLParser.ExpressionContext):
        if ctx.columnName():
            return ctx.columnName().getText()
        return ctx.literal().getText()

    def visitComparator(self, ctx: MiniSQLParser.ComparatorContext):
        return ctx.getText()
