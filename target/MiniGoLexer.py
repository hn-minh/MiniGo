# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u01f0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\7\2\u0092\n\2\f\2")
        buf.write("\16\2\u0095\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\7\3\u009e")
        buf.write("\n\3\f\3\16\3\u00a1\13\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\5\33")
        buf.write("\u00e4\n\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3")
        buf.write("\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3")
        buf.write("$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\7\60\u015d")
        buf.write("\n\60\f\60\16\60\u0160\13\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3:\7:\u0177\n:\f:\16:\u017a\13:\5:\u017c\n")
        buf.write(":\3;\3;\3;\3;\5;\u0182\n;\3;\6;\u0185\n;\r;\16;\u0186")
        buf.write("\3<\3<\3<\3<\5<\u018d\n<\3<\6<\u0190\n<\r<\16<\u0191\3")
        buf.write("=\3=\3=\3=\5=\u0198\n=\3=\6=\u019b\n=\r=\16=\u019c\3>")
        buf.write("\3>\3>\3>\5>\u01a3\n>\3?\6?\u01a6\n?\r?\16?\u01a7\3?\3")
        buf.write("?\7?\u01ac\n?\f?\16?\u01af\13?\3?\3?\5?\u01b3\n?\3?\6")
        buf.write("?\u01b6\n?\r?\16?\u01b7\7?\u01ba\n?\f?\16?\u01bd\13?\3")
        buf.write("@\3@\3@\3A\3A\3A\7A\u01c5\nA\fA\16A\u01c8\13A\3A\3A\3")
        buf.write("B\3B\3C\6C\u01cf\nC\rC\16C\u01d0\3C\3C\3D\3D\3D\7D\u01d8")
        buf.write("\nD\fD\16D\u01db\13D\3D\3D\3D\3E\3E\3E\7E\u01e3\nE\fE")
        buf.write("\16E\u01e6\13E\3E\5E\u01e9\nE\3E\3E\5E\u01ed\nE\3F\3F")
        buf.write("\3\u009f\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s\2u\2w\2y\2{;}<\177\2\u0081=\u0083>\u0085?\u0087")
        buf.write("@\u0089A\u008bB\3\2\21\4\2\f\f\17\17\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\3\2\62\62\3\2\63;\3\2\62;\3\2\62\63\3\2\629\5")
        buf.write("\2\62;CHch\4\2GGgg\4\2--//\7\2$$^^ppttvv\4\2$$^^\5\2\13")
        buf.write("\13\16\17\"\"\6\2\f\f\17\17$$^^\2\u0208\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2{\3\2")
        buf.write("\2\2\2}\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\3\u008d\3\2\2\2\5\u0098\3\2\2\2\7\u00a7\3\2\2\2\t\u00a9")
        buf.write("\3\2\2\2\13\u00ab\3\2\2\2\r\u00ad\3\2\2\2\17\u00af\3\2")
        buf.write("\2\2\21\u00b1\3\2\2\2\23\u00b4\3\2\2\2\25\u00b7\3\2\2")
        buf.write("\2\27\u00b9\3\2\2\2\31\u00bc\3\2\2\2\33\u00be\3\2\2\2")
        buf.write("\35\u00c1\3\2\2\2\37\u00c4\3\2\2\2!\u00c7\3\2\2\2#\u00c9")
        buf.write("\3\2\2\2%\u00cc\3\2\2\2\'\u00cf\3\2\2\2)\u00d2\3\2\2\2")
        buf.write("+\u00d5\3\2\2\2-\u00d8\3\2\2\2/\u00db\3\2\2\2\61\u00dd")
        buf.write("\3\2\2\2\63\u00df\3\2\2\2\65\u00e3\3\2\2\2\67\u00e5\3")
        buf.write("\2\2\29\u00e8\3\2\2\2;\u00ed\3\2\2\2=\u00f1\3\2\2\2?\u00f8")
        buf.write("\3\2\2\2A\u0102\3\2\2\2C\u0109\3\2\2\2E\u010f\3\2\2\2")
        buf.write("G\u0113\3\2\2\2I\u011a\3\2\2\2K\u011f\3\2\2\2M\u0123\3")
        buf.write("\2\2\2O\u0128\3\2\2\2Q\u012e\3\2\2\2S\u0136\3\2\2\2U\u013f")
        buf.write("\3\2\2\2W\u0145\3\2\2\2Y\u014b\3\2\2\2[\u0150\3\2\2\2")
        buf.write("]\u0156\3\2\2\2_\u015a\3\2\2\2a\u0161\3\2\2\2c\u0163\3")
        buf.write("\2\2\2e\u0165\3\2\2\2g\u0167\3\2\2\2i\u0169\3\2\2\2k\u016b")
        buf.write("\3\2\2\2m\u016d\3\2\2\2o\u016f\3\2\2\2q\u0171\3\2\2\2")
        buf.write("s\u017b\3\2\2\2u\u0181\3\2\2\2w\u018c\3\2\2\2y\u0197\3")
        buf.write("\2\2\2{\u01a2\3\2\2\2}\u01a5\3\2\2\2\177\u01be\3\2\2\2")
        buf.write("\u0081\u01c1\3\2\2\2\u0083\u01cb\3\2\2\2\u0085\u01ce\3")
        buf.write("\2\2\2\u0087\u01d4\3\2\2\2\u0089\u01df\3\2\2\2\u008b\u01ee")
        buf.write("\3\2\2\2\u008d\u008e\7\61\2\2\u008e\u008f\7\61\2\2\u008f")
        buf.write("\u0093\3\2\2\2\u0090\u0092\n\2\2\2\u0091\u0090\3\2\2\2")
        buf.write("\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0094\3")
        buf.write("\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093\3\2\2\2\u0096\u0097")
        buf.write("\b\2\2\2\u0097\4\3\2\2\2\u0098\u0099\7\61\2\2\u0099\u009a")
        buf.write("\7,\2\2\u009a\u009f\3\2\2\2\u009b\u009e\5\5\3\2\u009c")
        buf.write("\u009e\13\2\2\2\u009d\u009b\3\2\2\2\u009d\u009c\3\2\2")
        buf.write("\2\u009e\u00a1\3\2\2\2\u009f\u00a0\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u00a0\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2")
        buf.write("\u00a3\7,\2\2\u00a3\u00a4\7\61\2\2\u00a4\u00a5\3\2\2\2")
        buf.write("\u00a5\u00a6\b\3\2\2\u00a6\6\3\2\2\2\u00a7\u00a8\7-\2")
        buf.write("\2\u00a8\b\3\2\2\2\u00a9\u00aa\7/\2\2\u00aa\n\3\2\2\2")
        buf.write("\u00ab\u00ac\7,\2\2\u00ac\f\3\2\2\2\u00ad\u00ae\7\61\2")
        buf.write("\2\u00ae\16\3\2\2\2\u00af\u00b0\7\'\2\2\u00b0\20\3\2\2")
        buf.write("\2\u00b1\u00b2\7?\2\2\u00b2\u00b3\7?\2\2\u00b3\22\3\2")
        buf.write("\2\2\u00b4\u00b5\7#\2\2\u00b5\u00b6\7?\2\2\u00b6\24\3")
        buf.write("\2\2\2\u00b7\u00b8\7>\2\2\u00b8\26\3\2\2\2\u00b9\u00ba")
        buf.write("\7>\2\2\u00ba\u00bb\7?\2\2\u00bb\30\3\2\2\2\u00bc\u00bd")
        buf.write("\7@\2\2\u00bd\32\3\2\2\2\u00be\u00bf\7@\2\2\u00bf\u00c0")
        buf.write("\7?\2\2\u00c0\34\3\2\2\2\u00c1\u00c2\7(\2\2\u00c2\u00c3")
        buf.write("\7(\2\2\u00c3\36\3\2\2\2\u00c4\u00c5\7~\2\2\u00c5\u00c6")
        buf.write("\7~\2\2\u00c6 \3\2\2\2\u00c7\u00c8\7#\2\2\u00c8\"\3\2")
        buf.write("\2\2\u00c9\u00ca\7<\2\2\u00ca\u00cb\7?\2\2\u00cb$\3\2")
        buf.write("\2\2\u00cc\u00cd\7-\2\2\u00cd\u00ce\7?\2\2\u00ce&\3\2")
        buf.write("\2\2\u00cf\u00d0\7/\2\2\u00d0\u00d1\7?\2\2\u00d1(\3\2")
        buf.write("\2\2\u00d2\u00d3\7,\2\2\u00d3\u00d4\7?\2\2\u00d4*\3\2")
        buf.write("\2\2\u00d5\u00d6\7\61\2\2\u00d6\u00d7\7?\2\2\u00d7,\3")
        buf.write("\2\2\2\u00d8\u00d9\7\'\2\2\u00d9\u00da\7?\2\2\u00da.\3")
        buf.write("\2\2\2\u00db\u00dc\7?\2\2\u00dc\60\3\2\2\2\u00dd\u00de")
        buf.write("\7<\2\2\u00de\62\3\2\2\2\u00df\u00e0\7=\2\2\u00e0\64\3")
        buf.write("\2\2\2\u00e1\u00e4\5Y-\2\u00e2\u00e4\5[.\2\u00e3\u00e1")
        buf.write("\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\66\3\2\2\2\u00e5\u00e6")
        buf.write("\7k\2\2\u00e6\u00e7\7h\2\2\u00e78\3\2\2\2\u00e8\u00e9")
        buf.write("\7g\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7u\2\2\u00eb\u00ec")
        buf.write("\7g\2\2\u00ec:\3\2\2\2\u00ed\u00ee\7h\2\2\u00ee\u00ef")
        buf.write("\7q\2\2\u00ef\u00f0\7t\2\2\u00f0<\3\2\2\2\u00f1\u00f2")
        buf.write("\7u\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4\7t\2\2\u00f4\u00f5")
        buf.write("\7w\2\2\u00f5\u00f6\7e\2\2\u00f6\u00f7\7v\2\2\u00f7>\3")
        buf.write("\2\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa\u00fb")
        buf.write("\7v\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7t\2\2\u00fd\u00fe")
        buf.write("\7h\2\2\u00fe\u00ff\7c\2\2\u00ff\u0100\7e\2\2\u0100\u0101")
        buf.write("\7g\2\2\u0101@\3\2\2\2\u0102\u0103\7u\2\2\u0103\u0104")
        buf.write("\7v\2\2\u0104\u0105\7t\2\2\u0105\u0106\7k\2\2\u0106\u0107")
        buf.write("\7p\2\2\u0107\u0108\7i\2\2\u0108B\3\2\2\2\u0109\u010a")
        buf.write("\7e\2\2\u010a\u010b\7q\2\2\u010b\u010c\7p\2\2\u010c\u010d")
        buf.write("\7u\2\2\u010d\u010e\7v\2\2\u010eD\3\2\2\2\u010f\u0110")
        buf.write("\7x\2\2\u0110\u0111\7c\2\2\u0111\u0112\7t\2\2\u0112F\3")
        buf.write("\2\2\2\u0113\u0114\7t\2\2\u0114\u0115\7g\2\2\u0115\u0116")
        buf.write("\7v\2\2\u0116\u0117\7w\2\2\u0117\u0118\7t\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119H\3\2\2\2\u011a\u011b\7h\2\2\u011b\u011c")
        buf.write("\7w\2\2\u011c\u011d\7p\2\2\u011d\u011e\7e\2\2\u011eJ\3")
        buf.write("\2\2\2\u011f\u0120\7k\2\2\u0120\u0121\7p\2\2\u0121\u0122")
        buf.write("\7v\2\2\u0122L\3\2\2\2\u0123\u0124\7v\2\2\u0124\u0125")
        buf.write("\7{\2\2\u0125\u0126\7r\2\2\u0126\u0127\7g\2\2\u0127N\3")
        buf.write("\2\2\2\u0128\u0129\7h\2\2\u0129\u012a\7n\2\2\u012a\u012b")
        buf.write("\7q\2\2\u012b\u012c\7c\2\2\u012c\u012d\7v\2\2\u012dP\3")
        buf.write("\2\2\2\u012e\u012f\7d\2\2\u012f\u0130\7q\2\2\u0130\u0131")
        buf.write("\7q\2\2\u0131\u0132\7n\2\2\u0132\u0133\7g\2\2\u0133\u0134")
        buf.write("\7c\2\2\u0134\u0135\7p\2\2\u0135R\3\2\2\2\u0136\u0137")
        buf.write("\7e\2\2\u0137\u0138\7q\2\2\u0138\u0139\7p\2\2\u0139\u013a")
        buf.write("\7v\2\2\u013a\u013b\7k\2\2\u013b\u013c\7p\2\2\u013c\u013d")
        buf.write("\7w\2\2\u013d\u013e\7g\2\2\u013eT\3\2\2\2\u013f\u0140")
        buf.write("\7d\2\2\u0140\u0141\7t\2\2\u0141\u0142\7g\2\2\u0142\u0143")
        buf.write("\7c\2\2\u0143\u0144\7m\2\2\u0144V\3\2\2\2\u0145\u0146")
        buf.write("\7t\2\2\u0146\u0147\7c\2\2\u0147\u0148\7p\2\2\u0148\u0149")
        buf.write("\7i\2\2\u0149\u014a\7g\2\2\u014aX\3\2\2\2\u014b\u014c")
        buf.write("\7v\2\2\u014c\u014d\7t\2\2\u014d\u014e\7w\2\2\u014e\u014f")
        buf.write("\7g\2\2\u014fZ\3\2\2\2\u0150\u0151\7h\2\2\u0151\u0152")
        buf.write("\7c\2\2\u0152\u0153\7n\2\2\u0153\u0154\7u\2\2\u0154\u0155")
        buf.write("\7g\2\2\u0155\\\3\2\2\2\u0156\u0157\7p\2\2\u0157\u0158")
        buf.write("\7k\2\2\u0158\u0159\7n\2\2\u0159^\3\2\2\2\u015a\u015e")
        buf.write("\t\3\2\2\u015b\u015d\t\4\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write("\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f`\3\2\2\2\u0160\u015e\3\2\2\2\u0161\u0162\7*\2\2")
        buf.write("\u0162b\3\2\2\2\u0163\u0164\7+\2\2\u0164d\3\2\2\2\u0165")
        buf.write("\u0166\7}\2\2\u0166f\3\2\2\2\u0167\u0168\7\177\2\2\u0168")
        buf.write("h\3\2\2\2\u0169\u016a\7]\2\2\u016aj\3\2\2\2\u016b\u016c")
        buf.write("\7_\2\2\u016cl\3\2\2\2\u016d\u016e\7.\2\2\u016en\3\2\2")
        buf.write("\2\u016f\u0170\7\60\2\2\u0170p\3\2\2\2\u0171\u0172\7a")
        buf.write("\2\2\u0172r\3\2\2\2\u0173\u017c\t\5\2\2\u0174\u0178\t")
        buf.write("\6\2\2\u0175\u0177\t\7\2\2\u0176\u0175\3\2\2\2\u0177\u017a")
        buf.write("\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179")
        buf.write("\u017c\3\2\2\2\u017a\u0178\3\2\2\2\u017b\u0173\3\2\2\2")
        buf.write("\u017b\u0174\3\2\2\2\u017ct\3\2\2\2\u017d\u017e\7\62\2")
        buf.write("\2\u017e\u0182\7d\2\2\u017f\u0180\7\62\2\2\u0180\u0182")
        buf.write("\7D\2\2\u0181\u017d\3\2\2\2\u0181\u017f\3\2\2\2\u0182")
        buf.write("\u0184\3\2\2\2\u0183\u0185\t\b\2\2\u0184\u0183\3\2\2\2")
        buf.write("\u0185\u0186\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187\3")
        buf.write("\2\2\2\u0187v\3\2\2\2\u0188\u0189\7\62\2\2\u0189\u018d")
        buf.write("\7q\2\2\u018a\u018b\7\62\2\2\u018b\u018d\7Q\2\2\u018c")
        buf.write("\u0188\3\2\2\2\u018c\u018a\3\2\2\2\u018d\u018f\3\2\2\2")
        buf.write("\u018e\u0190\t\t\2\2\u018f\u018e\3\2\2\2\u0190\u0191\3")
        buf.write("\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192x")
        buf.write("\3\2\2\2\u0193\u0194\7\62\2\2\u0194\u0198\7z\2\2\u0195")
        buf.write("\u0196\7\62\2\2\u0196\u0198\7Z\2\2\u0197\u0193\3\2\2\2")
        buf.write("\u0197\u0195\3\2\2\2\u0198\u019a\3\2\2\2\u0199\u019b\t")
        buf.write("\n\2\2\u019a\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019dz\3\2\2\2\u019e\u01a3")
        buf.write("\5s:\2\u019f\u01a3\5u;\2\u01a0\u01a3\5w<\2\u01a1\u01a3")
        buf.write("\5y=\2\u01a2\u019e\3\2\2\2\u01a2\u019f\3\2\2\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3|\3\2\2\2\u01a4\u01a6")
        buf.write("\t\7\2\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9\u01ad\7\60\2\2\u01aa\u01ac\t\7\2\2\u01ab\u01aa")
        buf.write("\3\2\2\2\u01ac\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad")
        buf.write("\u01ae\3\2\2\2\u01ae\u01bb\3\2\2\2\u01af\u01ad\3\2\2\2")
        buf.write("\u01b0\u01b2\t\13\2\2\u01b1\u01b3\t\f\2\2\u01b2\u01b1")
        buf.write("\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b5\3\2\2\2\u01b4")
        buf.write("\u01b6\t\7\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01ba\3")
        buf.write("\2\2\2\u01b9\u01b0\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01b9")
        buf.write("\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc~\3\2\2\2\u01bd\u01bb")
        buf.write("\3\2\2\2\u01be\u01bf\7^\2\2\u01bf\u01c0\t\r\2\2\u01c0")
        buf.write("\u0080\3\2\2\2\u01c1\u01c6\7$\2\2\u01c2\u01c5\5\177@\2")
        buf.write("\u01c3\u01c5\n\16\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c8\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c7\3\2\2\2\u01c7\u01c9\3\2\2\2\u01c8\u01c6\3\2\2\2")
        buf.write("\u01c9\u01ca\7$\2\2\u01ca\u0082\3\2\2\2\u01cb\u01cc\7")
        buf.write("\f\2\2\u01cc\u0084\3\2\2\2\u01cd\u01cf\t\17\2\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\b")
        buf.write("C\2\2\u01d3\u0086\3\2\2\2\u01d4\u01d9\7$\2\2\u01d5\u01d8")
        buf.write("\n\20\2\2\u01d6\u01d8\5\177@\2\u01d7\u01d5\3\2\2\2\u01d7")
        buf.write("\u01d6\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2")
        buf.write("\u01d9\u01da\3\2\2\2\u01da\u01dc\3\2\2\2\u01db\u01d9\3")
        buf.write("\2\2\2\u01dc\u01dd\7^\2\2\u01dd\u01de\13\2\2\2\u01de\u0088")
        buf.write("\3\2\2\2\u01df\u01e4\7$\2\2\u01e0\u01e3\n\20\2\2\u01e1")
        buf.write("\u01e3\5\177@\2\u01e2\u01e0\3\2\2\2\u01e2\u01e1\3\2\2")
        buf.write("\2\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5")
        buf.write("\3\2\2\2\u01e5\u01ec\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7")
        buf.write("\u01e9\7\17\2\2\u01e8\u01e7\3\2\2\2\u01e8\u01e9\3\2\2")
        buf.write("\2\u01e9\u01ea\3\2\2\2\u01ea\u01ed\7\f\2\2\u01eb\u01ed")
        buf.write("\7\2\2\3\u01ec\u01e8\3\2\2\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("\u008a\3\2\2\2\u01ee\u01ef\13\2\2\2\u01ef\u008c\3\2\2")
        buf.write("\2 \2\u0093\u009d\u009f\u00e3\u015e\u0178\u017b\u0181")
        buf.write("\u0186\u018c\u0191\u0197\u019a\u019c\u01a2\u01a7\u01ad")
        buf.write("\u01b2\u01b7\u01bb\u01c4\u01c6\u01d0\u01d7\u01d9\u01e2")
        buf.write("\u01e4\u01e8\u01ec\3\b\2\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SINGLE_COMMENT = 1
    MULTI_COMMENT = 2
    PLUS = 3
    MINUS = 4
    MUL = 5
    DIV = 6
    MOD = 7
    EQ = 8
    NEQ = 9
    LT = 10
    LE = 11
    GT = 12
    GE = 13
    AND = 14
    OR = 15
    NOT = 16
    ASSIGN = 17
    ADD_ASSIGN = 18
    SUB_ASSIGN = 19
    MUL_ASSIGN = 20
    DIV_ASSIGN = 21
    MOD_ASSIGN = 22
    EQUAL = 23
    COLON = 24
    SEMICOLON = 25
    BOOLEAN_LIT = 26
    KW_IF = 27
    KW_ELSE = 28
    KW_FOR = 29
    KW_STRUCT = 30
    KW_INTERFACE = 31
    KW_STRING = 32
    KW_CONST = 33
    KW_VAR = 34
    KW_RETURN = 35
    KW_FUNC = 36
    KW_INT = 37
    KW_TYPE = 38
    KW_FLOAT = 39
    KW_BOOL = 40
    KW_CONTINUE = 41
    KW_BREAK = 42
    KW_RANGE = 43
    KW_TRUE = 44
    KW_FALSE = 45
    KW_NIL = 46
    IDENTIFIER = 47
    LPAREN = 48
    RPAREN = 49
    LBRACE = 50
    RBRACE = 51
    LBRACK = 52
    RBRACK = 53
    COMMA = 54
    DOT = 55
    UNDERLINE = 56
    INTEGER_LIT = 57
    FLOAT_LIT = 58
    STRING_LIT = 59
    NL = 60
    WS = 61
    ILLEGAL_ESCAPE = 62
    UNCLOSE_STRING = 63
    ERROR_CHAR = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'&&'", "'||'", "'!'", "':='", "'+='", "'-='", 
            "'*='", "'/='", "'%='", "'='", "':'", "';'", "'if'", "'else'", 
            "'for'", "'struct'", "'interface'", "'string'", "'const'", "'var'", 
            "'return'", "'func'", "'int'", "'type'", "'float'", "'boolean'", 
            "'continue'", "'break'", "'range'", "'true'", "'false'", "'nil'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "'.'", "'_'", 
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "SINGLE_COMMENT", "MULTI_COMMENT", "PLUS", "MINUS", "MUL", "DIV", 
            "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR", "NOT", 
            "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", 
            "MOD_ASSIGN", "EQUAL", "COLON", "SEMICOLON", "BOOLEAN_LIT", 
            "KW_IF", "KW_ELSE", "KW_FOR", "KW_STRUCT", "KW_INTERFACE", "KW_STRING", 
            "KW_CONST", "KW_VAR", "KW_RETURN", "KW_FUNC", "KW_INT", "KW_TYPE", 
            "KW_FLOAT", "KW_BOOL", "KW_CONTINUE", "KW_BREAK", "KW_RANGE", 
            "KW_TRUE", "KW_FALSE", "KW_NIL", "IDENTIFIER", "LPAREN", "RPAREN", 
            "LBRACE", "RBRACE", "LBRACK", "RBRACK", "COMMA", "DOT", "UNDERLINE", 
            "INTEGER_LIT", "FLOAT_LIT", "STRING_LIT", "NL", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "SINGLE_COMMENT", "MULTI_COMMENT", "PLUS", "MINUS", "MUL", 
                  "DIV", "MOD", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", 
                  "OR", "NOT", "ASSIGN", "ADD_ASSIGN", "SUB_ASSIGN", "MUL_ASSIGN", 
                  "DIV_ASSIGN", "MOD_ASSIGN", "EQUAL", "COLON", "SEMICOLON", 
                  "BOOLEAN_LIT", "KW_IF", "KW_ELSE", "KW_FOR", "KW_STRUCT", 
                  "KW_INTERFACE", "KW_STRING", "KW_CONST", "KW_VAR", "KW_RETURN", 
                  "KW_FUNC", "KW_INT", "KW_TYPE", "KW_FLOAT", "KW_BOOL", 
                  "KW_CONTINUE", "KW_BREAK", "KW_RANGE", "KW_TRUE", "KW_FALSE", 
                  "KW_NIL", "IDENTIFIER", "LPAREN", "RPAREN", "LBRACE", 
                  "RBRACE", "LBRACK", "RBRACK", "COMMA", "DOT", "UNDERLINE", 
                  "DEC_INT", "BIN_INT", "OCT_INT", "HEX_INT", "INTEGER_LIT", 
                  "FLOAT_LIT", "ESC_SEQ", "STRING_LIT", "NL", "WS", "ILLEGAL_ESCAPE", 
                  "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



    last_token = None

    def emitSemicolon(self):
        self.type = self.SEMICOLON ;
        self.text = ";";
        return super().emit();

    def emit(self):
        global last_token
        
        tk = self.type

        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            unclosed_text = result.text.rstrip("\r\n");
            raise UncloseString(unclosed_text);

        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            illegal_text = result.text;
            raise IllegalEscape(illegal_text);

        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 

        elif tk == self.NL: 
            if last_token is not None and (
                last_token.type in [
                    self.IDENTIFIER, self.INTEGER_LIT, self.FLOAT_LIT,
                    self.BOOLEAN_LIT, self.STRING_LIT, self.KW_INT,
                    self.KW_FLOAT, self.KW_BOOL, self.KW_STRING, self.KW_RETURN,
                    self.KW_CONTINUE, self.KW_BREAK, self.RPAREN, self.RBRACK, self.RBRACE
                ]):
                semicolon_token = self.emitSemicolon()
                last_token = semicolon_token
                return semicolon_token
            else: 
                return self.nextToken()

        else:
            last_token = super().emit()
            return last_token


