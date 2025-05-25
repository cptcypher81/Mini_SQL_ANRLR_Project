from antlr4 import *
from CompiledFiles.MiniSQLParser import MiniSQLParser
from CompiledFiles.MiniSQLVisitor import MiniSQLVisitor

class MiniSQLVisitorImpl(MiniSQLVisitor):

    def visitProgram(self, ctx: MiniSQLParser.ProgramContext):
        results = []
        for stmt in ctx.statement():
            result = self.visit(stmt)
            if result is not None:
                results.append(result)
        return results[0] if results else None

    def visitStatement(self, ctx: MiniSQLParser.StatementContext):
        return self.visit(ctx.selectStmt())

    def visitSelectStmt(self, ctx: MiniSQLParser.SelectStmtContext):
        print("Visiting selectStmt")
        columns = self.visit(ctx.columnList())
        print("Columns parsed:", columns)

        table = self.visit(ctx.tableName())
        where_condition = self.visit(ctx.condition()) if ctx.condition() else None

        return {
            "type": "SELECT",
            "columns": columns,
            "table": table,
            "where": where_condition
        }

    # Handle SELECT * 
    def visitAllColumns(self, ctx: MiniSQLParser.AllColumnsContext):
        return "*"

    # Handle SELECT name, age
    def visitSpecificColumns(self, ctx: MiniSQLParser.SpecificColumnsContext):
        return [col.getText() for col in ctx.columnName()]

    def visitTableName(self, ctx: MiniSQLParser.TableNameContext):
        return ctx.getText()

    def visitOrCondition(self, ctx: MiniSQLParser.OrConditionContext):
        return {
            "type": "or",
            "left": self.visit(ctx.condition()),
            "right": self.visit(ctx.andCond())
        }

    def visitAndCondition(self, ctx: MiniSQLParser.AndConditionContext):
        return {
            "type": "and",
            "left": self.visit(ctx.andCond()),
            "right": self.visit(ctx.baseCond())
        }

    def visitSingleAnd(self, ctx: MiniSQLParser.SingleAndContext):
        return self.visit(ctx.andCond())

    def visitSingleBase(self, ctx: MiniSQLParser.SingleBaseContext):
        return self.visit(ctx.baseCond())

    def visitBaseCondition(self, ctx: MiniSQLParser.BaseConditionContext):
        left = self.visit(ctx.expression(0))
        op = self.visit(ctx.comparator())
        right = self.visit(ctx.expression(1))
        return {
            "type": "condition",
            "left": left,
            "op": op,
            "right": right
        }

    def visitExpression(self, ctx: MiniSQLParser.ExpressionContext):
        if ctx.columnName():
            return ctx.columnName().getText()
        return ctx.literal().getText()

    def visitComparator(self, ctx: MiniSQLParser.ComparatorContext):
        return ctx.getText()
