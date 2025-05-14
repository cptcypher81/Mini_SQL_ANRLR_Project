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
        4,1,17,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,0,1,0,1,
        1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,37,8,2,1,3,1,3,1,3,1,3,5,3,
        43,8,3,10,3,12,3,46,9,3,3,3,48,8,3,1,4,1,4,1,4,1,4,1,5,1,5,3,5,56,
        8,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,
        16,18,0,2,1,0,4,9,1,0,14,15,60,0,21,1,0,0,0,2,27,1,0,0,0,4,30,1,
        0,0,0,6,47,1,0,0,0,8,49,1,0,0,0,10,55,1,0,0,0,12,57,1,0,0,0,14,59,
        1,0,0,0,16,61,1,0,0,0,18,63,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,
        22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,25,1,0,0,0,25,26,5,
        0,0,1,26,1,1,0,0,0,27,28,3,4,2,0,28,29,5,1,0,0,29,3,1,0,0,0,30,31,
        5,10,0,0,31,32,3,6,3,0,32,33,5,11,0,0,33,36,3,16,8,0,34,35,5,12,
        0,0,35,37,3,8,4,0,36,34,1,0,0,0,36,37,1,0,0,0,37,5,1,0,0,0,38,48,
        5,2,0,0,39,44,3,14,7,0,40,41,5,3,0,0,41,43,3,14,7,0,42,40,1,0,0,
        0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,48,1,0,0,0,46,44,
        1,0,0,0,47,38,1,0,0,0,47,39,1,0,0,0,48,7,1,0,0,0,49,50,3,10,5,0,
        50,51,3,12,6,0,51,52,3,10,5,0,52,9,1,0,0,0,53,56,3,14,7,0,54,56,
        3,18,9,0,55,53,1,0,0,0,55,54,1,0,0,0,56,11,1,0,0,0,57,58,7,0,0,0,
        58,13,1,0,0,0,59,60,5,13,0,0,60,15,1,0,0,0,61,62,5,13,0,0,62,17,
        1,0,0,0,63,64,7,1,0,0,64,19,1,0,0,0,5,23,36,44,47,55
    ]

class MiniSQLParser ( Parser ):

    grammarFileName = "MiniSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "','", "'='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'SELECT'", "'FROM'", "'WHERE'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SELECT", "FROM", "WHERE", 
                      "IDENTIFIER", "NUMBER", "STRING", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_selectStmt = 2
    RULE_columnList = 3
    RULE_condition = 4
    RULE_expression = 5
    RULE_comparator = 6
    RULE_columnName = 7
    RULE_tableName = 8
    RULE_literal = 9

    ruleNames =  [ "program", "statement", "selectStmt", "columnList", "condition", 
                   "expression", "comparator", "columnName", "tableName", 
                   "literal" ]

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
    IDENTIFIER=13
    NUMBER=14
    STRING=15
    WS=16
    COMMENT=17

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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10):
                    break

            self.state = 25
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
            self.state = 27
            self.selectStmt()
            self.state = 28
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
            self.state = 30
            self.match(MiniSQLParser.SELECT)
            self.state = 31
            self.columnList()
            self.state = 32
            self.match(MiniSQLParser.FROM)
            self.state = 33
            self.tableName()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 34
                self.match(MiniSQLParser.WHERE)
                self.state = 35
                self.condition()


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
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MiniSQLParser.AllColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(MiniSQLParser.T__1)
                pass
            elif token in [13]:
                localctx = MiniSQLParser.SpecificColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.columnName()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 40
                    self.match(MiniSQLParser.T__2)
                    self.state = 41
                    self.columnName()
                    self.state = 46
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.ExpressionContext,i)


        def comparator(self):
            return self.getTypedRuleContext(MiniSQLParser.ComparatorContext,0)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniSQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.expression()
            self.state = 50
            self.comparator()
            self.state = 51
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
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.columnName()
                pass
            elif token in [14, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
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
        self.enterRule(localctx, 12, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
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
        self.enterRule(localctx, 14, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
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
        self.enterRule(localctx, 16, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
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
        self.enterRule(localctx, 18, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            _la = self._input.LA(1)
            if not(_la==14 or _la==15):
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





