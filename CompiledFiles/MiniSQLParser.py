# Generated from MiniSQL.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,19,92,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,41,8,2,
        1,3,1,3,1,3,1,3,5,3,47,8,3,10,3,12,3,50,9,3,3,3,52,8,3,1,4,1,4,1,
        4,1,4,1,4,1,4,5,4,60,8,4,10,4,12,4,63,9,4,1,5,1,5,1,5,1,5,1,5,1,
        5,5,5,71,8,5,10,5,12,5,74,9,5,1,6,1,6,1,6,1,6,1,7,1,7,3,7,82,8,7,
        1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,11,0,2,8,10,12,0,2,4,6,8,10,
        12,14,16,18,20,22,0,2,1,0,4,9,1,0,16,17,86,0,25,1,0,0,0,2,31,1,0,
        0,0,4,34,1,0,0,0,6,51,1,0,0,0,8,53,1,0,0,0,10,64,1,0,0,0,12,75,1,
        0,0,0,14,81,1,0,0,0,16,83,1,0,0,0,18,85,1,0,0,0,20,87,1,0,0,0,22,
        89,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,
        0,27,28,1,0,0,0,28,29,1,0,0,0,29,30,5,0,0,1,30,1,1,0,0,0,31,32,3,
        4,2,0,32,33,5,1,0,0,33,3,1,0,0,0,34,35,5,10,0,0,35,36,3,6,3,0,36,
        37,5,11,0,0,37,40,3,20,10,0,38,39,5,12,0,0,39,41,3,8,4,0,40,38,1,
        0,0,0,40,41,1,0,0,0,41,5,1,0,0,0,42,52,5,2,0,0,43,48,3,18,9,0,44,
        45,5,3,0,0,45,47,3,18,9,0,46,44,1,0,0,0,47,50,1,0,0,0,48,46,1,0,
        0,0,48,49,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,51,42,1,0,0,0,51,43,
        1,0,0,0,52,7,1,0,0,0,53,54,6,4,-1,0,54,55,3,10,5,0,55,61,1,0,0,0,
        56,57,10,2,0,0,57,58,5,14,0,0,58,60,3,10,5,0,59,56,1,0,0,0,60,63,
        1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,9,1,0,0,0,63,61,1,0,0,0,64,
        65,6,5,-1,0,65,66,3,12,6,0,66,72,1,0,0,0,67,68,10,2,0,0,68,69,5,
        13,0,0,69,71,3,12,6,0,70,67,1,0,0,0,71,74,1,0,0,0,72,70,1,0,0,0,
        72,73,1,0,0,0,73,11,1,0,0,0,74,72,1,0,0,0,75,76,3,14,7,0,76,77,3,
        16,8,0,77,78,3,14,7,0,78,13,1,0,0,0,79,82,3,18,9,0,80,82,3,22,11,
        0,81,79,1,0,0,0,81,80,1,0,0,0,82,15,1,0,0,0,83,84,7,0,0,0,84,17,
        1,0,0,0,85,86,5,15,0,0,86,19,1,0,0,0,87,88,5,15,0,0,88,21,1,0,0,
        0,89,90,7,1,0,0,90,23,1,0,0,0,7,27,40,48,51,61,72,81
    ]

class MiniSQLParser ( Parser ):

    grammarFileName = "MiniSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "','", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'SELECT'", "'FROM'", "'WHERE'", 
                     "'AND'", "'OR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SELECT", "FROM", "WHERE", 
                      "AND", "OR", "IDENTIFIER", "NUMBER", "STRING", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_selectStmt = 2
    RULE_columnList = 3
    RULE_condition = 4
    RULE_andCond = 5
    RULE_baseCond = 6
    RULE_expression = 7
    RULE_comparator = 8
    RULE_columnName = 9
    RULE_tableName = 10
    RULE_literal = 11

    ruleNames =  [ "program", "statement", "selectStmt", "columnList", "condition", 
                   "andCond", "baseCond", "expression", "comparator", "columnName", 
                   "tableName", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    SELECT=10
    FROM=11
    WHERE=12
    AND=13
    OR=14
    IDENTIFIER=15
    NUMBER=16
    STRING=17
    WS=18
    COMMENT=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniSQLParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.StatementContext,i)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniSQLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

            self.state = 29
            self.match(MiniSQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectStmt(self):
            return self.getTypedRuleContext(MiniSQLParser.SelectStmtContext,0)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniSQLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.selectStmt()
            self.state = 32
            self.match(MiniSQLParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(MiniSQLParser.SELECT, 0)

        def columnList(self):
            return self.getTypedRuleContext(MiniSQLParser.ColumnListContext,0)


        def FROM(self):
            return self.getToken(MiniSQLParser.FROM, 0)

        def tableName(self):
            return self.getTypedRuleContext(MiniSQLParser.TableNameContext,0)


        def WHERE(self):
            return self.getToken(MiniSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_selectStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStmt" ):
                return visitor.visitSelectStmt(self)
            else:
                return visitor.visitChildren(self)




    def selectStmt(self):

        localctx = MiniSQLParser.SelectStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selectStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(MiniSQLParser.SELECT)
            self.state = 35
            self.columnList()
            self.state = 36
            self.match(MiniSQLParser.FROM)
            self.state = 37
            self.tableName()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 38
                self.match(MiniSQLParser.WHERE)
                self.state = 39
                self.condition(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniSQLParser.RULE_columnList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AllColumnsContext(ColumnListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.ColumnListContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAllColumns" ):
                return visitor.visitAllColumns(self)
            else:
                return visitor.visitChildren(self)


    class SpecificColumnsContext(ColumnListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.ColumnListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.ColumnNameContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecificColumns" ):
                return visitor.visitSpecificColumns(self)
            else:
                return visitor.visitChildren(self)



    def columnList(self):

        localctx = MiniSQLParser.ColumnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_columnList)
        self._la = 0 # Token type
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MiniSQLParser.AllColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.match(MiniSQLParser.T__1)
                pass
            elif token in [15]:
                localctx = MiniSQLParser.SpecificColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.columnName()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 44
                    self.match(MiniSQLParser.T__2)
                    self.state = 45
                    self.columnName()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniSQLParser.RULE_condition

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class OrConditionContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def condition(self):
            return self.getTypedRuleContext(MiniSQLParser.ConditionContext,0)

        def OR(self):
            return self.getToken(MiniSQLParser.OR, 0)
        def andCond(self):
            return self.getTypedRuleContext(MiniSQLParser.AndCondContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrCondition" ):
                return visitor.visitOrCondition(self)
            else:
                return visitor.visitChildren(self)


    class SingleAndContext(ConditionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.ConditionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def andCond(self):
            return self.getTypedRuleContext(MiniSQLParser.AndCondContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleAnd" ):
                return visitor.visitSingleAnd(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniSQLParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniSQLParser.SingleAndContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 54
            self.andCond(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 61
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniSQLParser.OrConditionContext(self, MiniSQLParser.ConditionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 56
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 57
                    self.match(MiniSQLParser.OR)
                    self.state = 58
                    self.andCond(0) 
                self.state = 63
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AndCondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniSQLParser.RULE_andCond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndConditionContext(AndCondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.AndCondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def andCond(self):
            return self.getTypedRuleContext(MiniSQLParser.AndCondContext,0)

        def AND(self):
            return self.getToken(MiniSQLParser.AND, 0)
        def baseCond(self):
            return self.getTypedRuleContext(MiniSQLParser.BaseCondContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndCondition" ):
                return visitor.visitAndCondition(self)
            else:
                return visitor.visitChildren(self)


    class SingleBaseContext(AndCondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.AndCondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def baseCond(self):
            return self.getTypedRuleContext(MiniSQLParser.BaseCondContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleBase" ):
                return visitor.visitSingleBase(self)
            else:
                return visitor.visitChildren(self)



    def andCond(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniSQLParser.AndCondContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_andCond, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniSQLParser.SingleBaseContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 65
            self.baseCond()
            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniSQLParser.AndConditionContext(self, MiniSQLParser.AndCondContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andCond)
                    self.state = 67
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 68
                    self.match(MiniSQLParser.AND)
                    self.state = 69
                    self.baseCond() 
                self.state = 74
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BaseCondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniSQLParser.RULE_baseCond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BaseConditionContext(BaseCondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.BaseCondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.ExpressionContext,i)

        def comparator(self):
            return self.getTypedRuleContext(MiniSQLParser.ComparatorContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBaseCondition" ):
                return visitor.visitBaseCondition(self)
            else:
                return visitor.visitChildren(self)



    def baseCond(self):

        localctx = MiniSQLParser.BaseCondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_baseCond)
        try:
            localctx = MiniSQLParser.BaseConditionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.expression()
            self.state = 76
            self.comparator()
            self.state = 77
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MiniSQLParser.ColumnNameContext,0)


        def literal(self):
            return self.getTypedRuleContext(MiniSQLParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniSQLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.columnName()
                pass
            elif token in [16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniSQLParser.RULE_comparator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparator" ):
                return visitor.visitComparator(self)
            else:
                return visitor.visitChildren(self)




    def comparator(self):

        localctx = MiniSQLParser.ComparatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniSQLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniSQLParser.RULE_columnName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnName" ):
                return visitor.visitColumnName(self)
            else:
                return visitor.visitChildren(self)




    def columnName(self):

        localctx = MiniSQLParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(MiniSQLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniSQLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniSQLParser.RULE_tableName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableName" ):
                return visitor.visitTableName(self)
            else:
                return visitor.visitChildren(self)




    def tableName(self):

        localctx = MiniSQLParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MiniSQLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(MiniSQLParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(MiniSQLParser.NUMBER, 0)

        def getRuleIndex(self):
            return MiniSQLParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniSQLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.condition_sempred
        self._predicates[5] = self.andCond_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def andCond_sempred(self, localctx:AndCondContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




