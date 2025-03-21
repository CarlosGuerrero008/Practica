# Generated from MiGramatica.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24")
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\7\21N\n\21\f\21\16\21Q\13\21\3\22\6\22T\n\22\r\22")
        buf.write("\16\22U\3\23\6\23Y\n\23\r\23\16\23Z\3\23\3\23\2\2\24\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\3\2\6\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2`\2\3\3\2\2\2\2\5")
        buf.write("\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2")
        buf.write("\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2")
        buf.write("\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2")
        buf.write("\2\2\5)\3\2\2\2\7/\3\2\2\2\t\61\3\2\2\2\13\63\3\2\2\2")
        buf.write("\r\65\3\2\2\2\17\67\3\2\2\2\219\3\2\2\2\23;\3\2\2\2\25")
        buf.write(">\3\2\2\2\27A\3\2\2\2\31C\3\2\2\2\33E\3\2\2\2\35G\3\2")
        buf.write("\2\2\37I\3\2\2\2!K\3\2\2\2#S\3\2\2\2%X\3\2\2\2\'(\7=\2")
        buf.write("\2(\4\3\2\2\2)*\7y\2\2*+\7j\2\2+,\7k\2\2,-\7n\2\2-.\7")
        buf.write("g\2\2.\6\3\2\2\2/\60\7*\2\2\60\b\3\2\2\2\61\62\7+\2\2")
        buf.write("\62\n\3\2\2\2\63\64\7}\2\2\64\f\3\2\2\2\65\66\7\177\2")
        buf.write("\2\66\16\3\2\2\2\678\7@\2\28\20\3\2\2\29:\7>\2\2:\22\3")
        buf.write("\2\2\2;<\7?\2\2<=\7?\2\2=\24\3\2\2\2>?\7#\2\2?@\7?\2\2")
        buf.write("@\26\3\2\2\2AB\7?\2\2B\30\3\2\2\2CD\7,\2\2D\32\3\2\2\2")
        buf.write("EF\7\61\2\2F\34\3\2\2\2GH\7-\2\2H\36\3\2\2\2IJ\7/\2\2")
        buf.write("J \3\2\2\2KO\t\2\2\2LN\t\3\2\2ML\3\2\2\2NQ\3\2\2\2OM\3")
        buf.write("\2\2\2OP\3\2\2\2P\"\3\2\2\2QO\3\2\2\2RT\t\4\2\2SR\3\2")
        buf.write("\2\2TU\3\2\2\2US\3\2\2\2UV\3\2\2\2V$\3\2\2\2WY\t\5\2\2")
        buf.write("XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\\\3\2\2\2\\")
        buf.write("]\b\23\2\2]&\3\2\2\2\6\2OUZ\3\b\2\2")
        return buf.getvalue()


class MiGramaticaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    ID = 16
    INT = 17
    WS = 18

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'while'", "'('", "')'", "'{'", "'}'", "'>'", "'<'", 
            "'=='", "'!='", "'='", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "ID", "INT", "WS" ]

    grammarFileName = "MiGramatica.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


