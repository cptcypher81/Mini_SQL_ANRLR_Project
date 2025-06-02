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
        return results

    def visitStatement(self, ctx: MiniSQLParser.StatementContext):
        if ctx.selectStmt():
            return self.visit(ctx.selectStmt()) 
        elif ctx.insertStmt():
            return self.visit(ctx.insertStmt())
        elif ctx.deleteStmt():
            return self.visit(ctx.deleteStmt())
        elif ctx.updateStmt():
            return self.visit(ctx.updateStmt())


    def visitSelectStmt(self, ctx: MiniSQLParser.SelectStmtContext):
        print("Visiting selectStmt")
        is_distinct = ctx.distinctModifier() is not None  # check if DISTINCT exists
        columns = self.visit(ctx.columnList())
        print("Columns parsed:", columns)

        table = self.visit(ctx.tableName())
        where_condition = self.visit(ctx.condition()) if ctx.condition() else None

        order_by = self.visit(ctx.orderList()) if ctx.orderList() else None
        limit = int(ctx.NUMBER().getText()) if ctx.LIMIT() else None

        return {
            "type": "SELECT",
            "distinct": is_distinct,
            "columns": columns,
            "table": table,
            "where": where_condition,
            "order_by": order_by,
            "limit": limit
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
    
    def visitInsertStmt(self, ctx: MiniSQLParser.InsertStmtContext):
        table = ctx.tableName().getText()
        columns = [col.getText() for col in ctx.columnName()]
        values = [lit.getText().strip("'") for lit in ctx.literal()]
        return {
            "type": "INSERT",
            "table": table,
            "columns": columns,
            "values": values
        }

    def visitDeleteStmt(self, ctx: MiniSQLParser.DeleteStmtContext):
        table = ctx.tableName().getText()
        condition = self.visit(ctx.condition()) if ctx.condition() else None
        return {
            "type": "DELETE",
            "table": table,
            "where": condition
        }

    def visitUpdateStmt(self, ctx: MiniSQLParser.UpdateStmtContext):
        table = ctx.tableName().getText()
        assignments = []

        for assign in ctx.assignment():
            column = assign.columnName().getText()
            value = assign.literal().getText().strip("'")
            assignments.append((column, value))

        condition = self.visit(ctx.condition()) if ctx.condition() else None
        return {
            "type": "UPDATE",
            "table": table,
            "assignments": assignments,
            "where": condition
        }

    def visitOrderList(self, ctx: MiniSQLParser.OrderListContext):
        return [self.visit(order) for order in ctx.orderItem()]

    def visitOrderItem(self, ctx: MiniSQLParser.OrderItemContext):
        col = ctx.columnName().getText()
        direction = ctx.ASC().getText() if ctx.ASC() else ctx.DESC().getText() if ctx.DESC() else "ASC"
        return (col, direction)
    
    def visitBetweenCondition(self, ctx: MiniSQLParser.BetweenConditionContext):
        field = self.visit(ctx.expression(0))
        lower = self.visit(ctx.expression(1))
        upper = self.visit(ctx.expression(2))
        return {
            "type": "between",
            "field": field,
            "lower": lower,
            "upper": upper
    }

    def visitNotCondition(self, ctx: MiniSQLParser.NotConditionContext):
        return {
            "type": "not",
            "condition": self.visit(ctx.baseCond())
    }


    def visitExpression(self, ctx: MiniSQLParser.ExpressionContext):
        if ctx.columnName():
            return ctx.columnName().getText()
        return ctx.literal().getText() 

    def visitComparator(self, ctx: MiniSQLParser.ComparatorContext):
        return ctx.getText()
