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
        4,1,27,162,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,60,8,2,1,3,1,3,1,3,1,3,5,3,66,8,3,10,3,12,3,69,9,3,
        3,3,71,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,80,8,4,10,4,12,4,83,9,
        4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,91,8,4,10,4,12,4,94,9,4,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,3,5,103,8,5,1,6,1,6,1,6,1,6,1,6,1,6,5,6,111,8,
        6,10,6,12,6,114,9,6,1,6,1,6,3,6,118,8,6,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,5,8,130,8,8,10,8,12,8,133,9,8,1,9,1,9,1,9,1,9,1,
        9,1,9,5,9,141,8,9,10,9,12,9,144,9,9,1,10,1,10,1,10,1,10,1,11,1,11,
        3,11,152,8,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,15,0,2,16,
        18,16,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,0,2,1,0,6,11,1,
        0,24,25,160,0,33,1,0,0,0,2,51,1,0,0,0,4,53,1,0,0,0,6,70,1,0,0,0,
        8,72,1,0,0,0,10,97,1,0,0,0,12,104,1,0,0,0,14,119,1,0,0,0,16,123,
        1,0,0,0,18,134,1,0,0,0,20,145,1,0,0,0,22,151,1,0,0,0,24,153,1,0,
        0,0,26,155,1,0,0,0,28,157,1,0,0,0,30,159,1,0,0,0,32,34,3,2,1,0,33,
        32,1,0,0,0,34,35,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,
        0,37,38,5,0,0,1,38,1,1,0,0,0,39,40,3,4,2,0,40,41,5,1,0,0,41,52,1,
        0,0,0,42,43,3,8,4,0,43,44,5,1,0,0,44,52,1,0,0,0,45,46,3,10,5,0,46,
        47,5,1,0,0,47,52,1,0,0,0,48,49,3,12,6,0,49,50,5,1,0,0,50,52,1,0,
        0,0,51,39,1,0,0,0,51,42,1,0,0,0,51,45,1,0,0,0,51,48,1,0,0,0,52,3,
        1,0,0,0,53,54,5,12,0,0,54,55,3,6,3,0,55,56,5,17,0,0,56,59,3,28,14,
        0,57,58,5,18,0,0,58,60,3,16,8,0,59,57,1,0,0,0,59,60,1,0,0,0,60,5,
        1,0,0,0,61,71,5,2,0,0,62,67,3,26,13,0,63,64,5,3,0,0,64,66,3,26,13,
        0,65,63,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,71,
        1,0,0,0,69,67,1,0,0,0,70,61,1,0,0,0,70,62,1,0,0,0,71,7,1,0,0,0,72,
        73,5,13,0,0,73,74,5,14,0,0,74,75,3,28,14,0,75,76,5,4,0,0,76,81,3,
        26,13,0,77,78,5,3,0,0,78,80,3,26,13,0,79,77,1,0,0,0,80,83,1,0,0,
        0,81,79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,
        5,5,0,0,85,86,5,15,0,0,86,87,5,4,0,0,87,92,3,30,15,0,88,89,5,3,0,
        0,89,91,3,30,15,0,90,88,1,0,0,0,91,94,1,0,0,0,92,90,1,0,0,0,92,93,
        1,0,0,0,93,95,1,0,0,0,94,92,1,0,0,0,95,96,5,5,0,0,96,9,1,0,0,0,97,
        98,5,16,0,0,98,99,5,17,0,0,99,102,3,28,14,0,100,101,5,18,0,0,101,
        103,3,16,8,0,102,100,1,0,0,0,102,103,1,0,0,0,103,11,1,0,0,0,104,
        105,5,19,0,0,105,106,3,28,14,0,106,107,5,20,0,0,107,112,3,14,7,0,
        108,109,5,3,0,0,109,111,3,14,7,0,110,108,1,0,0,0,111,114,1,0,0,0,
        112,110,1,0,0,0,112,113,1,0,0,0,113,117,1,0,0,0,114,112,1,0,0,0,
        115,116,5,18,0,0,116,118,3,16,8,0,117,115,1,0,0,0,117,118,1,0,0,
        0,118,13,1,0,0,0,119,120,3,26,13,0,120,121,5,6,0,0,121,122,3,30,
        15,0,122,15,1,0,0,0,123,124,6,8,-1,0,124,125,3,18,9,0,125,131,1,
        0,0,0,126,127,10,2,0,0,127,128,5,22,0,0,128,130,3,18,9,0,129,126,
        1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,17,1,
        0,0,0,133,131,1,0,0,0,134,135,6,9,-1,0,135,136,3,20,10,0,136,142,
        1,0,0,0,137,138,10,2,0,0,138,139,5,21,0,0,139,141,3,20,10,0,140,
        137,1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,
        19,1,0,0,0,144,142,1,0,0,0,145,146,3,22,11,0,146,147,3,24,12,0,147,
        148,3,22,11,0,148,21,1,0,0,0,149,152,3,26,13,0,150,152,3,30,15,0,
        151,149,1,0,0,0,151,150,1,0,0,0,152,23,1,0,0,0,153,154,7,0,0,0,154,
        25,1,0,0,0,155,156,5,23,0,0,156,27,1,0,0,0,157,158,5,23,0,0,158,
        29,1,0,0,0,159,160,7,1,0,0,160,31,1,0,0,0,13,35,51,59,67,70,81,92,
        102,112,117,131,142,151
    ]

class MiniSQLParser ( Parser ):

    grammarFileName = "MiniSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "','", "'('", "')'", "'='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'SELECT'", "'INSERT'", 
                     "'INTO'", "'VALUES'", "'DELETE'", "'FROM'", "'WHERE'", 
                     "'UPDATE'", "'SET'", "'AND'", "'OR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SELECT", "INSERT", "INTO", "VALUES", "DELETE", "FROM", 
                      "WHERE", "UPDATE", "SET", "AND", "OR", "IDENTIFIER", 
                      "NUMBER", "STRING", "WS", "COMMENT" ]

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
    RULE_expression = 11
    RULE_comparator = 12
    RULE_columnName = 13
    RULE_tableName = 14
    RULE_literal = 15

    ruleNames =  [ "program", "statement", "selectStmt", "columnList", "insertStmt", 
                   "deleteStmt", "updateStmt", "assignment", "condition", 
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
    IDENTIFIER=23
    NUMBER=24
    STRING=25
    WS=26
    COMMENT=27

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
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.statement()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 602112) != 0)):
                    break

            self.state = 37
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
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.selectStmt()
                self.state = 40
                self.match(MiniSQLParser.T__0)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.insertStmt()
                self.state = 43
                self.match(MiniSQLParser.T__0)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.deleteStmt()
                self.state = 46
                self.match(MiniSQLParser.T__0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.updateStmt()
                self.state = 49
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
            self.state = 53
            self.match(MiniSQLParser.SELECT)
            self.state = 54
            self.columnList()
            self.state = 55
            self.match(MiniSQLParser.FROM)
            self.state = 56
            self.tableName()
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 57
                self.match(MiniSQLParser.WHERE)
                self.state = 58
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
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MiniSQLParser.AllColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(MiniSQLParser.T__1)
                pass
            elif token in [23]:
                localctx = MiniSQLParser.SpecificColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.columnName()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 63
                    self.match(MiniSQLParser.T__2)
                    self.state = 64
                    self.columnName()
                    self.state = 69
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
            self.state = 72
            self.match(MiniSQLParser.INSERT)
            self.state = 73
            self.match(MiniSQLParser.INTO)
            self.state = 74
            self.tableName()
            self.state = 75
            self.match(MiniSQLParser.T__3)
            self.state = 76
            self.columnName()
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 77
                self.match(MiniSQLParser.T__2)
                self.state = 78
                self.columnName()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(MiniSQLParser.T__4)
            self.state = 85
            self.match(MiniSQLParser.VALUES)
            self.state = 86
            self.match(MiniSQLParser.T__3)
            self.state = 87
            self.literal()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 88
                self.match(MiniSQLParser.T__2)
                self.state = 89
                self.literal()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 95
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
            self.state = 97
            self.match(MiniSQLParser.DELETE)
            self.state = 98
            self.match(MiniSQLParser.FROM)
            self.state = 99
            self.tableName()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 100
                self.match(MiniSQLParser.WHERE)
                self.state = 101
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
            self.state = 104
            self.match(MiniSQLParser.UPDATE)
            self.state = 105
            self.tableName()
            self.state = 106
            self.match(MiniSQLParser.SET)
            self.state = 107
            self.assignment()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 108
                self.match(MiniSQLParser.T__2)
                self.state = 109
                self.assignment()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 115
                self.match(MiniSQLParser.WHERE)
                self.state = 116
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
            self.state = 119
            self.columnName()
            self.state = 120
            self.match(MiniSQLParser.T__5)
            self.state = 121
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

            self.state = 124
            self.andCond(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniSQLParser.OrConditionContext(self, MiniSQLParser.ConditionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 126
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 127
                    self.match(MiniSQLParser.OR)
                    self.state = 128
                    self.andCond(0) 
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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

            self.state = 135
            self.baseCond()
            self._ctx.stop = self._input.LT(-1)
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniSQLParser.AndConditionContext(self, MiniSQLParser.AndCondContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andCond)
                    self.state = 137
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 138
                    self.match(MiniSQLParser.AND)
                    self.state = 139
                    self.baseCond() 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
            self.state = 145
            self.expression()
            self.state = 146
            self.comparator()
            self.state = 147
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
        self.enterRule(localctx, 22, self.RULE_expression)
        try:
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.columnName()
                pass
            elif token in [24, 25]:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
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
        self.enterRule(localctx, 24, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
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
        self.enterRule(localctx, 26, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
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
        self.enterRule(localctx, 28, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
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
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not(_la==24 or _la==25):
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
         




