# Generated from Sample.g4 by ANTLR 4.13.1
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
        4,1,17,70,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,1,1,1,3,1,27,8,1,1,
        2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,38,8,3,1,4,1,4,1,4,1,4,3,4,
        44,8,4,1,5,1,5,3,5,48,8,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,1,
        8,3,8,60,8,8,1,9,1,9,1,9,1,9,3,9,66,8,9,1,10,1,10,1,10,0,0,11,0,
        2,4,6,8,10,12,14,16,18,20,0,1,1,0,11,13,66,0,22,1,0,0,0,2,26,1,0,
        0,0,4,28,1,0,0,0,6,37,1,0,0,0,8,43,1,0,0,0,10,45,1,0,0,0,12,51,1,
        0,0,0,14,54,1,0,0,0,16,57,1,0,0,0,18,65,1,0,0,0,20,67,1,0,0,0,22,
        23,3,2,1,0,23,1,1,0,0,0,24,27,3,4,2,0,25,27,3,8,4,0,26,24,1,0,0,
        0,26,25,1,0,0,0,27,3,1,0,0,0,28,29,5,1,0,0,29,30,3,6,3,0,30,31,5,
        2,0,0,31,32,3,8,4,0,32,5,1,0,0,0,33,34,5,3,0,0,34,38,5,15,0,0,35,
        36,5,4,0,0,36,38,5,15,0,0,37,33,1,0,0,0,37,35,1,0,0,0,38,7,1,0,0,
        0,39,44,3,10,5,0,40,44,3,12,6,0,41,44,3,14,7,0,42,44,3,16,8,0,43,
        39,1,0,0,0,43,40,1,0,0,0,43,41,1,0,0,0,43,42,1,0,0,0,44,9,1,0,0,
        0,45,47,5,5,0,0,46,48,3,18,9,0,47,46,1,0,0,0,47,48,1,0,0,0,48,49,
        1,0,0,0,49,50,3,20,10,0,50,11,1,0,0,0,51,52,5,6,0,0,52,53,5,16,0,
        0,53,13,1,0,0,0,54,55,5,7,0,0,55,56,5,16,0,0,56,15,1,0,0,0,57,59,
        5,8,0,0,58,60,3,18,9,0,59,58,1,0,0,0,59,60,1,0,0,0,60,17,1,0,0,0,
        61,62,5,9,0,0,62,66,5,14,0,0,63,64,5,10,0,0,64,66,5,14,0,0,65,61,
        1,0,0,0,65,63,1,0,0,0,66,19,1,0,0,0,67,68,7,0,0,0,68,21,1,0,0,0,
        6,26,37,43,47,59,65
    ]

class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'If'", "'then'", "'the time is after'", 
                     "'the time is before'", "'Turn on the'", "'Set the temperature to'", 
                     "'Increase brightness by'", "'Play music'", "'in the'", 
                     "'the'", "'light'", "'fan'", "'AC'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ROOM", "TIME", "NUMBER", 
                      "WS" ]

    RULE_program = 0
    RULE_command = 1
    RULE_conditionalCommand = 2
    RULE_condition = 3
    RULE_simpleCommand = 4
    RULE_turnOnCommand = 5
    RULE_setTemperatureCommand = 6
    RULE_increaseBrightnessCommand = 7
    RULE_playMusicCommand = 8
    RULE_location = 9
    RULE_device = 10

    ruleNames =  [ "program", "command", "conditionalCommand", "condition", 
                   "simpleCommand", "turnOnCommand", "setTemperatureCommand", 
                   "increaseBrightnessCommand", "playMusicCommand", "location", 
                   "device" ]

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
    ROOM=14
    TIME=15
    NUMBER=16
    WS=17

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

        def command(self):
            return self.getTypedRuleContext(SampleParser.CommandContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_program




    def program(self):

        localctx = SampleParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.command()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionalCommand(self):
            return self.getTypedRuleContext(SampleParser.ConditionalCommandContext,0)


        def simpleCommand(self):
            return self.getTypedRuleContext(SampleParser.SimpleCommandContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_command




    def command(self):

        localctx = SampleParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.conditionalCommand()
                pass
            elif token in [5, 6, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.simpleCommand()
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


    class ConditionalCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(SampleParser.ConditionContext,0)


        def simpleCommand(self):
            return self.getTypedRuleContext(SampleParser.SimpleCommandContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_conditionalCommand




    def conditionalCommand(self):

        localctx = SampleParser.ConditionalCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditionalCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(SampleParser.T__0)
            self.state = 29
            self.condition()
            self.state = 30
            self.match(SampleParser.T__1)
            self.state = 31
            self.simpleCommand()
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

        def TIME(self):
            return self.getToken(SampleParser.TIME, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_condition




    def condition(self):

        localctx = SampleParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condition)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(SampleParser.T__2)
                self.state = 34
                self.match(SampleParser.TIME)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(SampleParser.T__3)
                self.state = 36
                self.match(SampleParser.TIME)
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


    class SimpleCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def turnOnCommand(self):
            return self.getTypedRuleContext(SampleParser.TurnOnCommandContext,0)


        def setTemperatureCommand(self):
            return self.getTypedRuleContext(SampleParser.SetTemperatureCommandContext,0)


        def increaseBrightnessCommand(self):
            return self.getTypedRuleContext(SampleParser.IncreaseBrightnessCommandContext,0)


        def playMusicCommand(self):
            return self.getTypedRuleContext(SampleParser.PlayMusicCommandContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_simpleCommand




    def simpleCommand(self):

        localctx = SampleParser.SimpleCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simpleCommand)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.turnOnCommand()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.setTemperatureCommand()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.increaseBrightnessCommand()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.playMusicCommand()
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


    class TurnOnCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def device(self):
            return self.getTypedRuleContext(SampleParser.DeviceContext,0)


        def location(self):
            return self.getTypedRuleContext(SampleParser.LocationContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_turnOnCommand




    def turnOnCommand(self):

        localctx = SampleParser.TurnOnCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_turnOnCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(SampleParser.T__4)
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 46
                self.location()


            self.state = 49
            self.device()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetTemperatureCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SampleParser.NUMBER, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_setTemperatureCommand




    def setTemperatureCommand(self):

        localctx = SampleParser.SetTemperatureCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_setTemperatureCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(SampleParser.T__5)
            self.state = 52
            self.match(SampleParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncreaseBrightnessCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SampleParser.NUMBER, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_increaseBrightnessCommand




    def increaseBrightnessCommand(self):

        localctx = SampleParser.IncreaseBrightnessCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_increaseBrightnessCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(SampleParser.T__6)
            self.state = 55
            self.match(SampleParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlayMusicCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def location(self):
            return self.getTypedRuleContext(SampleParser.LocationContext,0)


        def getRuleIndex(self):
            return SampleParser.RULE_playMusicCommand




    def playMusicCommand(self):

        localctx = SampleParser.PlayMusicCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_playMusicCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(SampleParser.T__7)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 58
                self.location()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ROOM(self):
            return self.getToken(SampleParser.ROOM, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_location




    def location(self):

        localctx = SampleParser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_location)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(SampleParser.T__8)
                self.state = 62
                self.match(SampleParser.ROOM)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(SampleParser.T__9)
                self.state = 64
                self.match(SampleParser.ROOM)
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


    class DeviceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SampleParser.RULE_device




    def device(self):

        localctx = SampleParser.DeviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_device)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14336) != 0)):
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





