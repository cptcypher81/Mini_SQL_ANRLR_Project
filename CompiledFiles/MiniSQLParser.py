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
        4,1,31,183,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,4,0,38,8,0,11,0,12,0,
        39,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,56,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,3,2,64,8,2,1,2,1,2,1,2,3,2,69,8,2,1,
        3,1,3,1,3,1,3,5,3,75,8,3,10,3,12,3,78,9,3,3,3,80,8,3,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,5,4,89,8,4,10,4,12,4,92,9,4,1,4,1,4,1,4,1,4,1,4,
        1,4,5,4,100,8,4,10,4,12,4,103,9,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,3,
        5,112,8,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,120,8,6,10,6,12,6,123,9,6,
        1,6,1,6,3,6,127,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,
        139,8,8,10,8,12,8,142,9,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,150,8,9,10,
        9,12,9,153,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,162,8,11,
        10,11,12,11,165,9,11,1,12,1,12,3,12,169,8,12,1,13,1,13,3,13,173,
        8,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,17,0,2,16,18,18,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,3,1,0,25,26,1,0,
        6,11,1,0,28,29,182,0,37,1,0,0,0,2,55,1,0,0,0,4,57,1,0,0,0,6,79,1,
        0,0,0,8,81,1,0,0,0,10,106,1,0,0,0,12,113,1,0,0,0,14,128,1,0,0,0,
        16,132,1,0,0,0,18,143,1,0,0,0,20,154,1,0,0,0,22,158,1,0,0,0,24,166,
        1,0,0,0,26,172,1,0,0,0,28,174,1,0,0,0,30,176,1,0,0,0,32,178,1,0,
        0,0,34,180,1,0,0,0,36,38,3,2,1,0,37,36,1,0,0,0,38,39,1,0,0,0,39,
        37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,5,0,0,1,42,1,1,0,0,
        0,43,44,3,4,2,0,44,45,5,1,0,0,45,56,1,0,0,0,46,47,3,8,4,0,47,48,
        5,1,0,0,48,56,1,0,0,0,49,50,3,10,5,0,50,51,5,1,0,0,51,56,1,0,0,0,
        52,53,3,12,6,0,53,54,5,1,0,0,54,56,1,0,0,0,55,43,1,0,0,0,55,46,1,
        0,0,0,55,49,1,0,0,0,55,52,1,0,0,0,56,3,1,0,0,0,57,58,5,12,0,0,58,
        59,3,6,3,0,59,60,5,17,0,0,60,63,3,32,16,0,61,62,5,18,0,0,62,64,3,
        16,8,0,63,61,1,0,0,0,63,64,1,0,0,0,64,68,1,0,0,0,65,66,5,23,0,0,
        66,67,5,24,0,0,67,69,3,22,11,0,68,65,1,0,0,0,68,69,1,0,0,0,69,5,
        1,0,0,0,70,80,5,2,0,0,71,76,3,30,15,0,72,73,5,3,0,0,73,75,3,30,15,
        0,74,72,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,80,
        1,0,0,0,78,76,1,0,0,0,79,70,1,0,0,0,79,71,1,0,0,0,80,7,1,0,0,0,81,
        82,5,13,0,0,82,83,5,14,0,0,83,84,3,32,16,0,84,85,5,4,0,0,85,90,3,
        30,15,0,86,87,5,3,0,0,87,89,3,30,15,0,88,86,1,0,0,0,89,92,1,0,0,
        0,90,88,1,0,0,0,90,91,1,0,0,0,91,93,1,0,0,0,92,90,1,0,0,0,93,94,
        5,5,0,0,94,95,5,15,0,0,95,96,5,4,0,0,96,101,3,34,17,0,97,98,5,3,
        0,0,98,100,3,34,17,0,99,97,1,0,0,0,100,103,1,0,0,0,101,99,1,0,0,
        0,101,102,1,0,0,0,102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,5,0,
        0,105,9,1,0,0,0,106,107,5,16,0,0,107,108,5,17,0,0,108,111,3,32,16,
        0,109,110,5,18,0,0,110,112,3,16,8,0,111,109,1,0,0,0,111,112,1,0,
        0,0,112,11,1,0,0,0,113,114,5,19,0,0,114,115,3,32,16,0,115,116,5,
        20,0,0,116,121,3,14,7,0,117,118,5,3,0,0,118,120,3,14,7,0,119,117,
        1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,126,
        1,0,0,0,123,121,1,0,0,0,124,125,5,18,0,0,125,127,3,16,8,0,126,124,
        1,0,0,0,126,127,1,0,0,0,127,13,1,0,0,0,128,129,3,30,15,0,129,130,
        5,6,0,0,130,131,3,34,17,0,131,15,1,0,0,0,132,133,6,8,-1,0,133,134,
        3,18,9,0,134,140,1,0,0,0,135,136,10,2,0,0,136,137,5,22,0,0,137,139,
        3,18,9,0,138,135,1,0,0,0,139,142,1,0,0,0,140,138,1,0,0,0,140,141,
        1,0,0,0,141,17,1,0,0,0,142,140,1,0,0,0,143,144,6,9,-1,0,144,145,
        3,20,10,0,145,151,1,0,0,0,146,147,10,2,0,0,147,148,5,21,0,0,148,
        150,3,20,10,0,149,146,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,
        152,1,0,0,0,152,19,1,0,0,0,153,151,1,0,0,0,154,155,3,26,13,0,155,
        156,3,28,14,0,156,157,3,26,13,0,157,21,1,0,0,0,158,163,3,24,12,0,
        159,160,5,3,0,0,160,162,3,24,12,0,161,159,1,0,0,0,162,165,1,0,0,
        0,163,161,1,0,0,0,163,164,1,0,0,0,164,23,1,0,0,0,165,163,1,0,0,0,
        166,168,3,30,15,0,167,169,7,0,0,0,168,167,1,0,0,0,168,169,1,0,0,
        0,169,25,1,0,0,0,170,173,3,30,15,0,171,173,3,34,17,0,172,170,1,0,
        0,0,172,171,1,0,0,0,173,27,1,0,0,0,174,175,7,1,0,0,175,29,1,0,0,
        0,176,177,5,27,0,0,177,31,1,0,0,0,178,179,5,27,0,0,179,33,1,0,0,
        0,180,181,7,2,0,0,181,35,1,0,0,0,16,39,55,63,68,76,79,90,101,111,
        121,126,140,151,163,168,172
    ]

class MiniSQLParser ( Parser ):

    grammarFileName = "MiniSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "','", "'('", "')'", "'='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'SELECT'", "'INSERT'", 
                     "'INTO'", "'VALUES'", "'DELETE'", "'FROM'", "'WHERE'", 
                     "'UPDATE'", "'SET'", "'AND'", "'OR'", "'ORDER'", "'BY'", 
                     "'ASC'", "'DESC'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SELECT", "INSERT", "INTO", "VALUES", "DELETE", "FROM", 
                      "WHERE", "UPDATE", "SET", "AND", "OR", "ORDER", "BY", 
                      "ASC", "DESC", "IDENTIFIER", "NUMBER", "STRING", "WS", 
                      "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_selectStmt = 2
    RULE_columnList = 3
    RULE_insertStmt = 4
    RULE_deleteStmt = 5
    RULE_updateStmt = 6
    RULE_assignment = 7
    RULE_condition = 8
    RULE_andCond = 9
    RULE_baseCond = 10
    RULE_orderList = 11
    RULE_orderItem = 12
    RULE_expression = 13
    RULE_comparator = 14
    RULE_columnName = 15
    RULE_tableName = 16
    RULE_literal = 17

    ruleNames =  [ "program", "statement", "selectStmt", "columnList", "insertStmt", 
                   "deleteStmt", "updateStmt", "assignment", "condition", 
                   "andCond", "baseCond", "orderList", "orderItem", "expression", 
                   "comparator", "columnName", "tableName", "literal" ]

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
    T__9=10
    T__10=11
    SELECT=12
    INSERT=13
    INTO=14
    VALUES=15
    DELETE=16
    FROM=17
    WHERE=18
    UPDATE=19
    SET=20
    AND=21
    OR=22
    ORDER=23
    BY=24
    ASC=25
    DESC=26
    IDENTIFIER=27
    NUMBER=28
    STRING=29
    WS=30
    COMMENT=31

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
            self.state = 37 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.statement()
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 602112) != 0)):
                    break

            self.state = 41
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


        def insertStmt(self):
            return self.getTypedRuleContext(MiniSQLParser.InsertStmtContext,0)


        def deleteStmt(self):
            return self.getTypedRuleContext(MiniSQLParser.DeleteStmtContext,0)


        def updateStmt(self):
            return self.getTypedRuleContext(MiniSQLParser.UpdateStmtContext,0)


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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.selectStmt()
                self.state = 44
                self.match(MiniSQLParser.T__0)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.insertStmt()
                self.state = 47
                self.match(MiniSQLParser.T__0)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.deleteStmt()
                self.state = 50
                self.match(MiniSQLParser.T__0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.updateStmt()
                self.state = 53
                self.match(MiniSQLParser.T__0)
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


        def ORDER(self):
            return self.getToken(MiniSQLParser.ORDER, 0)

        def BY(self):
            return self.getToken(MiniSQLParser.BY, 0)

        def orderList(self):
            return self.getTypedRuleContext(MiniSQLParser.OrderListContext,0)


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
            self.state = 57
            self.match(MiniSQLParser.SELECT)
            self.state = 58
            self.columnList()
            self.state = 59
            self.match(MiniSQLParser.FROM)
            self.state = 60
            self.tableName()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 61
                self.match(MiniSQLParser.WHERE)
                self.state = 62
                self.condition(0)


            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 65
                self.match(MiniSQLParser.ORDER)
                self.state = 66
                self.match(MiniSQLParser.BY)
                self.state = 67
                self.orderList()


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
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MiniSQLParser.AllColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(MiniSQLParser.T__1)
                pass
            elif token in [27]:
                localctx = MiniSQLParser.SpecificColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.columnName()
                self.state = 76
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 72
                    self.match(MiniSQLParser.T__2)
                    self.state = 73
                    self.columnName()
                    self.state = 78
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


    class InsertStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(MiniSQLParser.INSERT, 0)

        def INTO(self):
            return self.getToken(MiniSQLParser.INTO, 0)

        def tableName(self):
            return self.getTypedRuleContext(MiniSQLParser.TableNameContext,0)


        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.ColumnNameContext,i)


        def VALUES(self):
            return self.getToken(MiniSQLParser.VALUES, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.LiteralContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.LiteralContext,i)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_insertStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertStmt" ):
                return visitor.visitInsertStmt(self)
            else:
                return visitor.visitChildren(self)




    def insertStmt(self):

        localctx = MiniSQLParser.InsertStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_insertStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(MiniSQLParser.INSERT)
            self.state = 82
            self.match(MiniSQLParser.INTO)
            self.state = 83
            self.tableName()
            self.state = 84
            self.match(MiniSQLParser.T__3)
            self.state = 85
            self.columnName()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 86
                self.match(MiniSQLParser.T__2)
                self.state = 87
                self.columnName()
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 93
            self.match(MiniSQLParser.T__4)
            self.state = 94
            self.match(MiniSQLParser.VALUES)
            self.state = 95
            self.match(MiniSQLParser.T__3)
            self.state = 96
            self.literal()
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 97
                self.match(MiniSQLParser.T__2)
                self.state = 98
                self.literal()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(MiniSQLParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DELETE(self):
            return self.getToken(MiniSQLParser.DELETE, 0)

        def FROM(self):
            return self.getToken(MiniSQLParser.FROM, 0)

        def tableName(self):
            return self.getTypedRuleContext(MiniSQLParser.TableNameContext,0)


        def WHERE(self):
            return self.getToken(MiniSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_deleteStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteStmt" ):
                return visitor.visitDeleteStmt(self)
            else:
                return visitor.visitChildren(self)




    def deleteStmt(self):

        localctx = MiniSQLParser.DeleteStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_deleteStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(MiniSQLParser.DELETE)
            self.state = 107
            self.match(MiniSQLParser.FROM)
            self.state = 108
            self.tableName()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 109
                self.match(MiniSQLParser.WHERE)
                self.state = 110
                self.condition(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UPDATE(self):
            return self.getToken(MiniSQLParser.UPDATE, 0)

        def tableName(self):
            return self.getTypedRuleContext(MiniSQLParser.TableNameContext,0)


        def SET(self):
            return self.getToken(MiniSQLParser.SET, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.AssignmentContext,i)


        def WHERE(self):
            return self.getToken(MiniSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_updateStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateStmt" ):
                return visitor.visitUpdateStmt(self)
            else:
                return visitor.visitChildren(self)




    def updateStmt(self):

        localctx = MiniSQLParser.UpdateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_updateStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MiniSQLParser.UPDATE)
            self.state = 114
            self.tableName()
            self.state = 115
            self.match(MiniSQLParser.SET)
            self.state = 116
            self.assignment()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 117
                self.match(MiniSQLParser.T__2)
                self.state = 118
                self.assignment()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 124
                self.match(MiniSQLParser.WHERE)
                self.state = 125
                self.condition(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MiniSQLParser.ColumnNameContext,0)


        def literal(self):
            return self.getTypedRuleContext(MiniSQLParser.LiteralContext,0)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniSQLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.columnName()
            self.state = 129
            self.match(MiniSQLParser.T__5)
            self.state = 130
            self.literal()
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
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniSQLParser.SingleAndContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 133
            self.andCond(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniSQLParser.OrConditionContext(self, MiniSQLParser.ConditionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 135
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 136
                    self.match(MiniSQLParser.OR)
                    self.state = 137
                    self.andCond(0) 
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_andCond, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniSQLParser.SingleBaseContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 144
            self.baseCond()
            self._ctx.stop = self._input.LT(-1)
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniSQLParser.AndConditionContext(self, MiniSQLParser.AndCondContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andCond)
                    self.state = 146
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 147
                    self.match(MiniSQLParser.AND)
                    self.state = 148
                    self.baseCond() 
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 20, self.RULE_baseCond)
        try:
            localctx = MiniSQLParser.BaseConditionContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.expression()
            self.state = 155
            self.comparator()
            self.state = 156
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orderItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.OrderItemContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.OrderItemContext,i)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_orderList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderList" ):
                return visitor.visitOrderList(self)
            else:
                return visitor.visitChildren(self)




    def orderList(self):

        localctx = MiniSQLParser.OrderListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_orderList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.orderItem()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 159
                self.match(MiniSQLParser.T__2)
                self.state = 160
                self.orderItem()
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MiniSQLParser.ColumnNameContext,0)


        def ASC(self):
            return self.getToken(MiniSQLParser.ASC, 0)

        def DESC(self):
            return self.getToken(MiniSQLParser.DESC, 0)

        def getRuleIndex(self):
            return MiniSQLParser.RULE_orderItem

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderItem" ):
                return visitor.visitOrderItem(self)
            else:
                return visitor.visitChildren(self)




    def orderItem(self):

        localctx = MiniSQLParser.OrderItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_orderItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.columnName()
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25 or _la==26:
                self.state = 167
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
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
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 170
                self.columnName()
                pass
            elif token in [28, 29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
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
        self.enterRule(localctx, 28, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4032) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
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
        self.enterRule(localctx, 32, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
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
        self.enterRule(localctx, 34, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
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
        self._predicates[8] = self.condition_sempred
        self._predicates[9] = self.andCond_sempred
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
         




