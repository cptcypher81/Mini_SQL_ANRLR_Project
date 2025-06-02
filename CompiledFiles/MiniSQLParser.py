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
        4,1,41,232,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,4,0,46,8,0,11,0,12,0,47,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,64,8,1,1,2,1,2,3,2,68,8,2,
        1,2,1,2,1,2,1,2,1,2,3,2,75,8,2,1,2,3,2,78,8,2,1,2,1,2,1,2,3,2,83,
        8,2,1,2,1,2,3,2,87,8,2,1,3,1,3,1,3,1,3,5,3,93,8,3,10,3,12,3,96,9,
        3,3,3,98,8,3,1,4,1,4,3,4,102,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,5,6,116,8,6,10,6,12,6,119,9,6,1,6,1,6,1,6,1,6,1,
        6,1,6,5,6,127,8,6,10,6,12,6,130,9,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,
        3,7,139,8,7,1,8,1,8,1,8,1,8,1,8,1,8,5,8,147,8,8,10,8,12,8,150,9,
        8,1,8,1,8,3,8,154,8,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,
        10,5,10,166,8,10,10,10,12,10,169,9,10,1,11,1,11,1,11,1,11,1,11,1,
        11,5,11,177,8,11,10,11,12,11,180,9,11,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,194,8,12,1,13,1,13,1,13,5,
        13,199,8,13,10,13,12,13,202,9,13,1,14,1,14,3,14,206,8,14,1,15,1,
        15,1,16,1,16,1,16,1,16,1,16,5,16,215,8,16,10,16,12,16,218,9,16,1,
        17,1,17,3,17,222,8,17,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,
        21,0,2,20,22,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,0,4,2,0,4,6,35,36,1,0,29,30,1,0,9,14,1,0,38,39,234,0,
        45,1,0,0,0,2,63,1,0,0,0,4,65,1,0,0,0,6,97,1,0,0,0,8,101,1,0,0,0,
        10,103,1,0,0,0,12,108,1,0,0,0,14,133,1,0,0,0,16,140,1,0,0,0,18,155,
        1,0,0,0,20,159,1,0,0,0,22,170,1,0,0,0,24,193,1,0,0,0,26,195,1,0,
        0,0,28,203,1,0,0,0,30,207,1,0,0,0,32,209,1,0,0,0,34,221,1,0,0,0,
        36,223,1,0,0,0,38,225,1,0,0,0,40,227,1,0,0,0,42,229,1,0,0,0,44,46,
        3,2,1,0,45,44,1,0,0,0,46,47,1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,
        48,49,1,0,0,0,49,50,5,0,0,1,50,1,1,0,0,0,51,52,3,4,2,0,52,53,5,1,
        0,0,53,64,1,0,0,0,54,55,3,12,6,0,55,56,5,1,0,0,56,64,1,0,0,0,57,
        58,3,14,7,0,58,59,5,1,0,0,59,64,1,0,0,0,60,61,3,16,8,0,61,62,5,1,
        0,0,62,64,1,0,0,0,63,51,1,0,0,0,63,54,1,0,0,0,63,57,1,0,0,0,63,60,
        1,0,0,0,64,3,1,0,0,0,65,67,5,15,0,0,66,68,3,30,15,0,67,66,1,0,0,
        0,67,68,1,0,0,0,68,69,1,0,0,0,69,70,3,6,3,0,70,71,5,20,0,0,71,74,
        3,40,20,0,72,73,5,21,0,0,73,75,3,20,10,0,74,72,1,0,0,0,74,75,1,0,
        0,0,75,77,1,0,0,0,76,78,3,32,16,0,77,76,1,0,0,0,77,78,1,0,0,0,78,
        82,1,0,0,0,79,80,5,26,0,0,80,81,5,28,0,0,81,83,3,26,13,0,82,79,1,
        0,0,0,82,83,1,0,0,0,83,86,1,0,0,0,84,85,5,31,0,0,85,87,5,38,0,0,
        86,84,1,0,0,0,86,87,1,0,0,0,87,5,1,0,0,0,88,98,5,2,0,0,89,94,3,8,
        4,0,90,91,5,3,0,0,91,93,3,8,4,0,92,90,1,0,0,0,93,96,1,0,0,0,94,92,
        1,0,0,0,94,95,1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,97,88,1,0,0,0,
        97,89,1,0,0,0,98,7,1,0,0,0,99,102,3,10,5,0,100,102,3,38,19,0,101,
        99,1,0,0,0,101,100,1,0,0,0,102,9,1,0,0,0,103,104,7,0,0,0,104,105,
        5,7,0,0,105,106,3,38,19,0,106,107,5,8,0,0,107,11,1,0,0,0,108,109,
        5,16,0,0,109,110,5,17,0,0,110,111,3,40,20,0,111,112,5,7,0,0,112,
        117,3,38,19,0,113,114,5,3,0,0,114,116,3,38,19,0,115,113,1,0,0,0,
        116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,120,1,0,0,0,
        119,117,1,0,0,0,120,121,5,8,0,0,121,122,5,18,0,0,122,123,5,7,0,0,
        123,128,3,42,21,0,124,125,5,3,0,0,125,127,3,42,21,0,126,124,1,0,
        0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,131,1,0,
        0,0,130,128,1,0,0,0,131,132,5,8,0,0,132,13,1,0,0,0,133,134,5,19,
        0,0,134,135,5,20,0,0,135,138,3,40,20,0,136,137,5,21,0,0,137,139,
        3,20,10,0,138,136,1,0,0,0,138,139,1,0,0,0,139,15,1,0,0,0,140,141,
        5,22,0,0,141,142,3,40,20,0,142,143,5,23,0,0,143,148,3,18,9,0,144,
        145,5,3,0,0,145,147,3,18,9,0,146,144,1,0,0,0,147,150,1,0,0,0,148,
        146,1,0,0,0,148,149,1,0,0,0,149,153,1,0,0,0,150,148,1,0,0,0,151,
        152,5,21,0,0,152,154,3,20,10,0,153,151,1,0,0,0,153,154,1,0,0,0,154,
        17,1,0,0,0,155,156,3,38,19,0,156,157,5,9,0,0,157,158,3,42,21,0,158,
        19,1,0,0,0,159,160,6,10,-1,0,160,161,3,22,11,0,161,167,1,0,0,0,162,
        163,10,2,0,0,163,164,5,25,0,0,164,166,3,22,11,0,165,162,1,0,0,0,
        166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,21,1,0,0,0,169,
        167,1,0,0,0,170,171,6,11,-1,0,171,172,3,24,12,0,172,178,1,0,0,0,
        173,174,10,2,0,0,174,175,5,24,0,0,175,177,3,24,12,0,176,173,1,0,
        0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,23,1,0,0,
        0,180,178,1,0,0,0,181,182,5,34,0,0,182,194,3,24,12,0,183,184,3,34,
        17,0,184,185,3,36,18,0,185,186,3,34,17,0,186,194,1,0,0,0,187,188,
        3,34,17,0,188,189,5,33,0,0,189,190,3,34,17,0,190,191,5,24,0,0,191,
        192,3,34,17,0,192,194,1,0,0,0,193,181,1,0,0,0,193,183,1,0,0,0,193,
        187,1,0,0,0,194,25,1,0,0,0,195,200,3,28,14,0,196,197,5,3,0,0,197,
        199,3,28,14,0,198,196,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,
        201,1,0,0,0,201,27,1,0,0,0,202,200,1,0,0,0,203,205,3,38,19,0,204,
        206,7,1,0,0,205,204,1,0,0,0,205,206,1,0,0,0,206,29,1,0,0,0,207,208,
        5,32,0,0,208,31,1,0,0,0,209,210,5,27,0,0,210,211,5,28,0,0,211,216,
        3,38,19,0,212,213,5,3,0,0,213,215,3,38,19,0,214,212,1,0,0,0,215,
        218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,33,1,0,0,0,218,216,
        1,0,0,0,219,222,3,38,19,0,220,222,3,42,21,0,221,219,1,0,0,0,221,
        220,1,0,0,0,222,35,1,0,0,0,223,224,7,2,0,0,224,37,1,0,0,0,225,226,
        5,37,0,0,226,39,1,0,0,0,227,228,5,37,0,0,228,41,1,0,0,0,229,230,
        7,3,0,0,230,43,1,0,0,0,22,47,63,67,74,77,82,86,94,97,101,117,128,
        138,148,153,167,178,193,200,205,216,221
    ]

class MiniSQLParser ( Parser ):

    grammarFileName = "MiniSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "','", "'SUM'", "'MIN'", 
                     "'MAX'", "'('", "')'", "'='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'SELECT'", "'INSERT'", "'INTO'", "'VALUES'", 
                     "'DELETE'", "'FROM'", "'WHERE'", "'UPDATE'", "'SET'", 
                     "'AND'", "'OR'", "'ORDER'", "'GROUP'", "'BY'", "'ASC'", 
                     "'DESC'", "'LIMIT'", "'DISTINCT'", "'BETWEEN'", "'NOT'", 
                     "'COUNT'", "'AVG'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "SELECT", "INSERT", 
                      "INTO", "VALUES", "DELETE", "FROM", "WHERE", "UPDATE", 
                      "SET", "AND", "OR", "ORDER", "GROUP", "BY", "ASC", 
                      "DESC", "LIMIT", "DISTINCT", "BETWEEN", "NOT", "COUNT", 
                      "AVG", "IDENTIFIER", "NUMBER", "STRING", "WS", "COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_selectStmt = 2
    RULE_columnList = 3
    RULE_columnExpr = 4
    RULE_aggregateFunction = 5
    RULE_insertStmt = 6
    RULE_deleteStmt = 7
    RULE_updateStmt = 8
    RULE_assignment = 9
    RULE_condition = 10
    RULE_andCond = 11
    RULE_baseCond = 12
    RULE_orderList = 13
    RULE_orderItem = 14
    RULE_distinctModifier = 15
    RULE_groupByClause = 16
    RULE_expression = 17
    RULE_comparator = 18
    RULE_columnName = 19
    RULE_tableName = 20
    RULE_literal = 21

    ruleNames =  [ "program", "statement", "selectStmt", "columnList", "columnExpr", 
                   "aggregateFunction", "insertStmt", "deleteStmt", "updateStmt", 
                   "assignment", "condition", "andCond", "baseCond", "orderList", 
                   "orderItem", "distinctModifier", "groupByClause", "expression", 
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
    T__11=12
    T__12=13
    T__13=14
    SELECT=15
    INSERT=16
    INTO=17
    VALUES=18
    DELETE=19
    FROM=20
    WHERE=21
    UPDATE=22
    SET=23
    AND=24
    OR=25
    ORDER=26
    GROUP=27
    BY=28
    ASC=29
    DESC=30
    LIMIT=31
    DISTINCT=32
    BETWEEN=33
    NOT=34
    COUNT=35
    AVG=36
    IDENTIFIER=37
    NUMBER=38
    STRING=39
    WS=40
    COMMENT=41

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
            self.state = 45 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 44
                self.statement()
                self.state = 47 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4816896) != 0)):
                    break

            self.state = 49
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
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 51
                self.selectStmt()
                self.state = 52
                self.match(MiniSQLParser.T__0)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.insertStmt()
                self.state = 55
                self.match(MiniSQLParser.T__0)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.deleteStmt()
                self.state = 58
                self.match(MiniSQLParser.T__0)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.updateStmt()
                self.state = 61
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


        def distinctModifier(self):
            return self.getTypedRuleContext(MiniSQLParser.DistinctModifierContext,0)


        def WHERE(self):
            return self.getToken(MiniSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(MiniSQLParser.ConditionContext,0)


        def groupByClause(self):
            return self.getTypedRuleContext(MiniSQLParser.GroupByClauseContext,0)


        def ORDER(self):
            return self.getToken(MiniSQLParser.ORDER, 0)

        def BY(self):
            return self.getToken(MiniSQLParser.BY, 0)

        def orderList(self):
            return self.getTypedRuleContext(MiniSQLParser.OrderListContext,0)


        def LIMIT(self):
            return self.getToken(MiniSQLParser.LIMIT, 0)

        def NUMBER(self):
            return self.getToken(MiniSQLParser.NUMBER, 0)

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
            self.state = 65
            self.match(MiniSQLParser.SELECT)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 66
                self.distinctModifier()


            self.state = 69
            self.columnList()
            self.state = 70
            self.match(MiniSQLParser.FROM)
            self.state = 71
            self.tableName()
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 72
                self.match(MiniSQLParser.WHERE)
                self.state = 73
                self.condition(0)


            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 76
                self.groupByClause()


            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 79
                self.match(MiniSQLParser.ORDER)
                self.state = 80
                self.match(MiniSQLParser.BY)
                self.state = 81
                self.orderList()


            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 84
                self.match(MiniSQLParser.LIMIT)
                self.state = 85
                self.match(MiniSQLParser.NUMBER)


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

        def columnExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.ColumnExprContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.ColumnExprContext,i)


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
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                localctx = MiniSQLParser.AllColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(MiniSQLParser.T__1)
                pass
            elif token in [4, 5, 6, 35, 36, 37]:
                localctx = MiniSQLParser.SpecificColumnsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.columnExpr()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==3:
                    self.state = 90
                    self.match(MiniSQLParser.T__2)
                    self.state = 91
                    self.columnExpr()
                    self.state = 96
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


    class ColumnExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniSQLParser.RULE_columnExpr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SimpleColumnContext(ColumnExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.ColumnExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def columnName(self):
            return self.getTypedRuleContext(MiniSQLParser.ColumnNameContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleColumn" ):
                return visitor.visitSimpleColumn(self)
            else:
                return visitor.visitChildren(self)


    class AggFuncExprContext(ColumnExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.ColumnExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def aggregateFunction(self):
            return self.getTypedRuleContext(MiniSQLParser.AggregateFunctionContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggFuncExpr" ):
                return visitor.visitAggFuncExpr(self)
            else:
                return visitor.visitChildren(self)



    def columnExpr(self):

        localctx = MiniSQLParser.ColumnExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_columnExpr)
        try:
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 35, 36]:
                localctx = MiniSQLParser.AggFuncExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.aggregateFunction()
                pass
            elif token in [37]:
                localctx = MiniSQLParser.SimpleColumnContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                self.columnName()
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


    class AggregateFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MiniSQLParser.ColumnNameContext,0)


        def COUNT(self):
            return self.getToken(MiniSQLParser.COUNT, 0)

        def AVG(self):
            return self.getToken(MiniSQLParser.AVG, 0)

        def getRuleIndex(self):
            return MiniSQLParser.RULE_aggregateFunction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateFunction" ):
                return visitor.visitAggregateFunction(self)
            else:
                return visitor.visitChildren(self)




    def aggregateFunction(self):

        localctx = MiniSQLParser.AggregateFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_aggregateFunction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 103079215216) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 104
            self.match(MiniSQLParser.T__6)
            self.state = 105
            self.columnName()
            self.state = 106
            self.match(MiniSQLParser.T__7)
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
        self.enterRule(localctx, 12, self.RULE_insertStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(MiniSQLParser.INSERT)
            self.state = 109
            self.match(MiniSQLParser.INTO)
            self.state = 110
            self.tableName()
            self.state = 111
            self.match(MiniSQLParser.T__6)
            self.state = 112
            self.columnName()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 113
                self.match(MiniSQLParser.T__2)
                self.state = 114
                self.columnName()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 120
            self.match(MiniSQLParser.T__7)
            self.state = 121
            self.match(MiniSQLParser.VALUES)
            self.state = 122
            self.match(MiniSQLParser.T__6)
            self.state = 123
            self.literal()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 124
                self.match(MiniSQLParser.T__2)
                self.state = 125
                self.literal()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 131
            self.match(MiniSQLParser.T__7)
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
        self.enterRule(localctx, 14, self.RULE_deleteStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(MiniSQLParser.DELETE)
            self.state = 134
            self.match(MiniSQLParser.FROM)
            self.state = 135
            self.tableName()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 136
                self.match(MiniSQLParser.WHERE)
                self.state = 137
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
        self.enterRule(localctx, 16, self.RULE_updateStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(MiniSQLParser.UPDATE)
            self.state = 141
            self.tableName()
            self.state = 142
            self.match(MiniSQLParser.SET)
            self.state = 143
            self.assignment()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 144
                self.match(MiniSQLParser.T__2)
                self.state = 145
                self.assignment()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 151
                self.match(MiniSQLParser.WHERE)
                self.state = 152
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
        self.enterRule(localctx, 18, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.columnName()
            self.state = 156
            self.match(MiniSQLParser.T__8)
            self.state = 157
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_condition, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniSQLParser.SingleAndContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 160
            self.andCond(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniSQLParser.OrConditionContext(self, MiniSQLParser.ConditionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 162
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 163
                    self.match(MiniSQLParser.OR)
                    self.state = 164
                    self.andCond(0) 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

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
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_andCond, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = MiniSQLParser.SingleBaseContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 171
            self.baseCond()
            self._ctx.stop = self._input.LT(-1)
            self.state = 178
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniSQLParser.AndConditionContext(self, MiniSQLParser.AndCondContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_andCond)
                    self.state = 173
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 174
                    self.match(MiniSQLParser.AND)
                    self.state = 175
                    self.baseCond() 
                self.state = 180
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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


    class NotConditionContext(BaseCondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.BaseCondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MiniSQLParser.NOT, 0)
        def baseCond(self):
            return self.getTypedRuleContext(MiniSQLParser.BaseCondContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotCondition" ):
                return visitor.visitNotCondition(self)
            else:
                return visitor.visitChildren(self)


    class BetweenConditionContext(BaseCondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniSQLParser.BaseCondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.ExpressionContext,i)

        def BETWEEN(self):
            return self.getToken(MiniSQLParser.BETWEEN, 0)
        def AND(self):
            return self.getToken(MiniSQLParser.AND, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBetweenCondition" ):
                return visitor.visitBetweenCondition(self)
            else:
                return visitor.visitChildren(self)



    def baseCond(self):

        localctx = MiniSQLParser.BaseCondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_baseCond)
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = MiniSQLParser.NotConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(MiniSQLParser.NOT)
                self.state = 182
                self.baseCond()
                pass

            elif la_ == 2:
                localctx = MiniSQLParser.BaseConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 183
                self.expression()
                self.state = 184
                self.comparator()
                self.state = 185
                self.expression()
                pass

            elif la_ == 3:
                localctx = MiniSQLParser.BetweenConditionContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.expression()
                self.state = 188
                self.match(MiniSQLParser.BETWEEN)
                self.state = 189
                self.expression()
                self.state = 190
                self.match(MiniSQLParser.AND)
                self.state = 191
                self.expression()
                pass


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
        self.enterRule(localctx, 26, self.RULE_orderList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.orderItem()
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 196
                self.match(MiniSQLParser.T__2)
                self.state = 197
                self.orderItem()
                self.state = 202
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
        self.enterRule(localctx, 28, self.RULE_orderItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.columnName()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29 or _la==30:
                self.state = 204
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
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


    class DistinctModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISTINCT(self):
            return self.getToken(MiniSQLParser.DISTINCT, 0)

        def getRuleIndex(self):
            return MiniSQLParser.RULE_distinctModifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDistinctModifier" ):
                return visitor.visitDistinctModifier(self)
            else:
                return visitor.visitChildren(self)




    def distinctModifier(self):

        localctx = MiniSQLParser.DistinctModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_distinctModifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(MiniSQLParser.DISTINCT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GroupByClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(MiniSQLParser.GROUP, 0)

        def BY(self):
            return self.getToken(MiniSQLParser.BY, 0)

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniSQLParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(MiniSQLParser.ColumnNameContext,i)


        def getRuleIndex(self):
            return MiniSQLParser.RULE_groupByClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGroupByClause" ):
                return visitor.visitGroupByClause(self)
            else:
                return visitor.visitChildren(self)




    def groupByClause(self):

        localctx = MiniSQLParser.GroupByClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_groupByClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniSQLParser.GROUP)
            self.state = 210
            self.match(MiniSQLParser.BY)
            self.state = 211
            self.columnName()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 212
                self.match(MiniSQLParser.T__2)
                self.state = 213
                self.columnName()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 34, self.RULE_expression)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.columnName()
                pass
            elif token in [38, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 220
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
        self.enterRule(localctx, 36, self.RULE_comparator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 32256) != 0)):
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
        self.enterRule(localctx, 38, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
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
        self.enterRule(localctx, 40, self.RULE_tableName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
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
        self.enterRule(localctx, 42, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
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
        self._predicates[10] = self.condition_sempred
        self._predicates[11] = self.andCond_sempred
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
         




