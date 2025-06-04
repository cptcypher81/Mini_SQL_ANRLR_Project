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
        is_distinct = ctx.distinctModifier() is not None
        columns = self.visit(ctx.columnList())
        table = self.visit(ctx.tableName())
        where_condition = self.visit(ctx.condition()) if ctx.condition() else None
        order_by = self.visit(ctx.orderList()) if ctx.orderList() else None
        limit = int(ctx.NUMBER().getText()) if ctx.LIMIT() else None
        group_by = self.visit(ctx.groupByClause()) if ctx.groupByClause() else None

        return {
            "type": "SELECT",
            "distinct": is_distinct,
            "columns": columns,
            "table": table,
            "where": where_condition,
            "order_by": order_by,
            "limit": limit,
            "group_by": group_by
        }

    def visitAllColumns(self, ctx: MiniSQLParser.AllColumnsContext):
        return "*"

    def visitSpecificColumns(self, ctx: MiniSQLParser.SpecificColumnsContext):
        return [self.visit(col) for col in ctx.columnExpr()]

    def visitColumnExpr(self, ctx: MiniSQLParser.ColumnExprContext):
        if ctx.columnName():
            return ctx.columnName().getText()
        return self.visit(ctx.aggregateFunction())

    def visitAggregateFunction(self, ctx: MiniSQLParser.AggregateFunctionContext):
        return {
            "agg_func": ctx.getChild(0).getText().upper(),
            "column": ctx.columnName().getText()
        }

    def visitTableName(self, ctx: MiniSQLParser.TableNameContext):
        return ctx.getText()

    def visitOrCondition(self, ctx: MiniSQLParser.OrConditionContext):
        left = self.visit(ctx.condition()) if ctx.condition() else None
        right = self.visit(ctx.andCond()) if ctx.andCond() else None
        return {
            "type": "or",
            "left": left,
            "right": right
        }

    def visitAndCondition(self, ctx: MiniSQLParser.AndConditionContext):
        left = self.visit(ctx.andCond()) if ctx.andCond() else None
        right = self.visit(ctx.baseCond()) if ctx.baseCond() else None
        return {
            "type": "and",
            "left": left,
            "right": right
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
        direction = "ASC"
        if ctx.ASC():
            direction = ctx.ASC().getText()
        elif ctx.DESC():
            direction = ctx.DESC().getText()
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

    def visitGroupByClause(self, ctx: MiniSQLParser.GroupByClauseContext):
        return [col.getText() for col in ctx.columnName()]

    def visitExpression(self, ctx: MiniSQLParser.ExpressionContext):
        if ctx.columnName():
            return ctx.columnName().getText()
        return ctx.literal().getText()

    def visitComparator(self, ctx: MiniSQLParser.ComparatorContext):
        return ctx.getText()
