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


    # Visit a parse tree produced by MiniSQLParser#aggFuncExpr.
    def visitAggFuncExpr(self, ctx:MiniSQLParser.AggFuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#simpleColumn.
    def visitSimpleColumn(self, ctx:MiniSQLParser.SimpleColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#aggregateFunction.
    def visitAggregateFunction(self, ctx:MiniSQLParser.AggregateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#insertStmt.
    def visitInsertStmt(self, ctx:MiniSQLParser.InsertStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#deleteStmt.
    def visitDeleteStmt(self, ctx:MiniSQLParser.DeleteStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#updateStmt.
    def visitUpdateStmt(self, ctx:MiniSQLParser.UpdateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#assignment.
    def visitAssignment(self, ctx:MiniSQLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#orCondition.
    def visitOrCondition(self, ctx:MiniSQLParser.OrConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#singleAnd.
    def visitSingleAnd(self, ctx:MiniSQLParser.SingleAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#andCondition.
    def visitAndCondition(self, ctx:MiniSQLParser.AndConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#singleBase.
    def visitSingleBase(self, ctx:MiniSQLParser.SingleBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#notCondition.
    def visitNotCondition(self, ctx:MiniSQLParser.NotConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#baseCondition.
    def visitBaseCondition(self, ctx:MiniSQLParser.BaseConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#betweenCondition.
    def visitBetweenCondition(self, ctx:MiniSQLParser.BetweenConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#orderList.
    def visitOrderList(self, ctx:MiniSQLParser.OrderListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#orderItem.
    def visitOrderItem(self, ctx:MiniSQLParser.OrderItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#distinctModifier.
    def visitDistinctModifier(self, ctx:MiniSQLParser.DistinctModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniSQLParser#groupByClause.
    def visitGroupByClause(self, ctx:MiniSQLParser.GroupByClauseContext):
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