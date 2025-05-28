# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u02b1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u00b2\n\4\3\5\3\5")
        buf.write("\5\5\u00b6\n\5\3\5\3\5\3\6\3\6\5\6\u00bc\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\t\5\t\u00c7\n\t\3\t\3\t\3\t\3")
        buf.write("\t\5\t\u00cd\n\t\7\t\u00cf\n\t\f\t\16\t\u00d2\13\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\5\f\u00de\n\f")
        buf.write("\3\r\3\r\3\r\3\r\5\r\u00e4\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u00ef\n\16\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\3\21\3\21\3\21\5\21\u00fa\n\21\3\22\3\22")
        buf.write("\3\22\5\22\u00ff\n\22\3\23\3\23\5\23\u0103\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\5\24\u010b\n\24\3\24\3\24\3\25")
        buf.write("\3\25\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u0119")
        buf.write("\n\27\f\27\16\27\u011c\13\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\7\30\u0124\n\30\f\30\16\30\u0127\13\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\7\31\u012f\n\31\f\31\16\31\u0132")
        buf.write("\13\31\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u013a\n\32\f")
        buf.write("\32\16\32\u013d\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7")
        buf.write("\33\u0145\n\33\f\33\16\33\u0148\13\33\3\34\3\34\3\34\3")
        buf.write("\34\3\34\5\34\u014f\n\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\7\35\u0160")
        buf.write("\n\35\f\35\16\35\u0163\13\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u016e\n\36\3\37\3\37\5\37\u0172")
        buf.write("\n\37\3 \3 \3 \3 \5 \u0178\n \3 \3 \3 \3!\3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\5#\u018d\n#\3#\3")
        buf.write("#\3#\3#\3$\3$\5$\u0195\n$\3%\3%\3%\3%\3%\5%\u019c\n%\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3\'\5\'\u01a5\n\'\3(\3(\3(\3(\5(\u01ab")
        buf.write("\n(\3)\3)\3)\3)\5)\u01b1\n)\3*\3*\3*\3*\3+\3+\3+\3+\3")
        buf.write(",\3,\3,\3,\3-\3-\3-\3-\3-\3-\5-\u01c5\n-\3.\3.\3.\3.\3")
        buf.write(".\5.\u01cc\n.\3/\3/\3/\3/\5/\u01d2\n/\5/\u01d4\n/\3\60")
        buf.write("\3\60\5\60\u01d8\n\60\3\61\3\61\3\61\3\61\3\61\5\61\u01df")
        buf.write("\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\5\63")
        buf.write("\u01ea\n\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01f2\n")
        buf.write("\63\3\63\3\63\5\63\u01f6\n\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\66\3\66\5\66\u0202\n\66\3\67\3\67\3")
        buf.write("\67\3\67\3\67\5\67\u0209\n\67\38\38\38\38\39\39\39\39")
        buf.write("\39\39\39\39\39\39\39\59\u021a\n9\39\39\39\39\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3;\3;\5;\u0229\n;\3<\3<\3<\3<\5<\u022f\n")
        buf.write("<\3=\3=\3=\3=\3=\3=\5=\u0237\n=\3=\3=\3>\3>\5>\u023d\n")
        buf.write(">\3?\3?\3?\3?\3?\5?\u0244\n?\3@\3@\3@\3A\3A\3A\3A\5A\u024d")
        buf.write("\nA\3B\3B\3B\3B\3B\3B\5B\u0255\nB\3C\3C\3C\3C\3D\3D\3")
        buf.write("D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3E\3F\3F\3F\5F\u026b\nF\3")
        buf.write("G\3G\3G\3G\5G\u0271\nG\3H\3H\3H\3H\3H\3H\3H\3H\3H\3I\3")
        buf.write("I\3I\3I\3I\3J\3J\3J\5J\u0284\nJ\3K\3K\3K\3K\3K\3K\3L\3")
        buf.write("L\3L\5L\u028f\nL\3L\3L\3L\3L\3L\3L\3L\3L\3M\3M\3M\3M\3")
        buf.write("M\3M\3M\3M\3M\3M\3M\3N\3N\3O\3O\3P\3P\5P\u02aa\nP\3Q\3")
        buf.write("Q\3Q\5Q\u02af\nQ\3Q\2\t\20,.\60\62\648R\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098")
        buf.write("\u009a\u009c\u009e\u00a0\2\n\5\2\34\34\60\60;=\5\2\"\"")
        buf.write("\'\')*\3\2\23\30\3\2\n\17\3\2\5\6\3\2\7\t\4\2\61\61;;")
        buf.write("\4\2\61\61::\2\u02ac\2\u00a2\3\2\2\2\4\u00a7\3\2\2\2\6")
        buf.write("\u00b1\3\2\2\2\b\u00b5\3\2\2\2\n\u00bb\3\2\2\2\f\u00bd")
        buf.write("\3\2\2\2\16\u00c1\3\2\2\2\20\u00c3\3\2\2\2\22\u00d3\3")
        buf.write("\2\2\2\24\u00d6\3\2\2\2\26\u00dd\3\2\2\2\30\u00e3\3\2")
        buf.write("\2\2\32\u00ee\3\2\2\2\34\u00f2\3\2\2\2\36\u00f4\3\2\2")
        buf.write("\2 \u00f6\3\2\2\2\"\u00fe\3\2\2\2$\u0102\3\2\2\2&\u010a")
        buf.write("\3\2\2\2(\u010e\3\2\2\2*\u0110\3\2\2\2,\u0112\3\2\2\2")
        buf.write(".\u011d\3\2\2\2\60\u0128\3\2\2\2\62\u0133\3\2\2\2\64\u013e")
        buf.write("\3\2\2\2\66\u014e\3\2\2\28\u0150\3\2\2\2:\u016d\3\2\2")
        buf.write("\2<\u0171\3\2\2\2>\u0173\3\2\2\2@\u017c\3\2\2\2B\u0180")
        buf.write("\3\2\2\2D\u0185\3\2\2\2F\u0194\3\2\2\2H\u019b\3\2\2\2")
        buf.write("J\u019d\3\2\2\2L\u01a4\3\2\2\2N\u01aa\3\2\2\2P\u01b0\3")
        buf.write("\2\2\2R\u01b2\3\2\2\2T\u01b6\3\2\2\2V\u01ba\3\2\2\2X\u01c4")
        buf.write("\3\2\2\2Z\u01cb\3\2\2\2\\\u01d3\3\2\2\2^\u01d7\3\2\2\2")
        buf.write("`\u01de\3\2\2\2b\u01e0\3\2\2\2d\u01f5\3\2\2\2f\u01f7\3")
        buf.write("\2\2\2h\u01fa\3\2\2\2j\u0201\3\2\2\2l\u0208\3\2\2\2n\u020a")
        buf.write("\3\2\2\2p\u020e\3\2\2\2r\u021f\3\2\2\2t\u0228\3\2\2\2")
        buf.write("v\u022e\3\2\2\2x\u0230\3\2\2\2z\u023c\3\2\2\2|\u0243\3")
        buf.write("\2\2\2~\u0245\3\2\2\2\u0080\u024c\3\2\2\2\u0082\u0254")
        buf.write("\3\2\2\2\u0084\u0256\3\2\2\2\u0086\u025a\3\2\2\2\u0088")
        buf.write("\u025e\3\2\2\2\u008a\u0267\3\2\2\2\u008c\u0270\3\2\2\2")
        buf.write("\u008e\u0272\3\2\2\2\u0090\u027b\3\2\2\2\u0092\u0283\3")
        buf.write("\2\2\2\u0094\u0285\3\2\2\2\u0096\u028b\3\2\2\2\u0098\u0298")
        buf.write("\3\2\2\2\u009a\u02a3\3\2\2\2\u009c\u02a5\3\2\2\2\u009e")
        buf.write("\u02a9\3\2\2\2\u00a0\u02ae\3\2\2\2\u00a2\u00a3\7\61\2")
        buf.write("\2\u00a3\u00a4\7\62\2\2\u00a4\u00a5\5^\60\2\u00a5\u00a6")
        buf.write("\7\63\2\2\u00a6\3\3\2\2\2\u00a7\u00a8\79\2\2\u00a8\u00a9")
        buf.write("\7\61\2\2\u00a9\u00aa\7\62\2\2\u00aa\u00ab\5^\60\2\u00ab")
        buf.write("\u00ac\7\63\2\2\u00ac\5\3\2\2\2\u00ad\u00ae\5\4\3\2\u00ae")
        buf.write("\u00af\5\6\4\2\u00af\u00b2\3\2\2\2\u00b0\u00b2\5\4\3\2")
        buf.write("\u00b1\u00ad\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\7\3\2\2")
        buf.write("\2\u00b3\u00b6\7\61\2\2\u00b4\u00b6\5\n\6\2\u00b5\u00b3")
        buf.write("\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7")
        buf.write("\u00b8\5\6\4\2\u00b8\t\3\2\2\2\u00b9\u00bc\5\f\7\2\u00ba")
        buf.write("\u00bc\5\16\b\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2")
        buf.write("\2\u00bc\13\3\2\2\2\u00bd\u00be\5\20\t\2\u00be\u00bf\7")
        buf.write("9\2\2\u00bf\u00c0\7\61\2\2\u00c0\r\3\2\2\2\u00c1\u00c2")
        buf.write("\5\20\t\2\u00c2\17\3\2\2\2\u00c3\u00c6\b\t\1\2\u00c4\u00c7")
        buf.write("\5\22\n\2\u00c5\u00c7\7\61\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c5\3\2\2\2\u00c7\u00d0\3\2\2\2\u00c8\u00c9\f\4\2\2")
        buf.write("\u00c9\u00cc\79\2\2\u00ca\u00cd\5\22\n\2\u00cb\u00cd\7")
        buf.write("\61\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\u00cf\3\2\2\2\u00ce\u00c8\3\2\2\2\u00cf\u00d2\3\2\2\2")
        buf.write("\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\21\3\2")
        buf.write("\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\7\61\2\2\u00d4\u00d5")
        buf.write("\5P)\2\u00d5\23\3\2\2\2\u00d6\u00d7\5\26\f\2\u00d7\u00d8")
        buf.write("\7\2\2\3\u00d8\25\3\2\2\2\u00d9\u00da\5&\24\2\u00da\u00db")
        buf.write("\5\26\f\2\u00db\u00de\3\2\2\2\u00dc\u00de\5&\24\2\u00dd")
        buf.write("\u00d9\3\2\2\2\u00dd\u00dc\3\2\2\2\u00de\27\3\2\2\2\u00df")
        buf.write("\u00e0\5\32\16\2\u00e0\u00e1\5\30\r\2\u00e1\u00e4\3\2")
        buf.write("\2\2\u00e2\u00e4\5\32\16\2\u00e3\u00df\3\2\2\2\u00e3\u00e2")
        buf.write("\3\2\2\2\u00e4\31\3\2\2\2\u00e5\u00ef\5<\37\2\u00e6\u00ef")
        buf.write("\5B\"\2\u00e7\u00ef\5\u0082B\2\u00e8\u00ef\5\u0088E\2")
        buf.write("\u00e9\u00ef\5\u0092J\2\u00ea\u00ef\5\u009aN\2\u00eb\u00ef")
        buf.write("\5\u009cO\2\u00ec\u00ef\5\u009eP\2\u00ed\u00ef\5\u00a0")
        buf.write("Q\2\u00ee\u00e5\3\2\2\2\u00ee\u00e6\3\2\2\2\u00ee\u00e7")
        buf.write("\3\2\2\2\u00ee\u00e8\3\2\2\2\u00ee\u00e9\3\2\2\2\u00ee")
        buf.write("\u00ea\3\2\2\2\u00ee\u00eb\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\7")
        buf.write("\33\2\2\u00f1\33\3\2\2\2\u00f2\u00f3\t\2\2\2\u00f3\35")
        buf.write("\3\2\2\2\u00f4\u00f5\t\3\2\2\u00f5\37\3\2\2\2\u00f6\u00f9")
        buf.write("\5N(\2\u00f7\u00fa\5\36\20\2\u00f8\u00fa\7\61\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa!\3\2\2\2\u00fb")
        buf.write("\u00ff\5\36\20\2\u00fc\u00ff\7\61\2\2\u00fd\u00ff\5 \21")
        buf.write("\2\u00fe\u00fb\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd")
        buf.write("\3\2\2\2\u00ff#\3\2\2\2\u0100\u0103\7\61\2\2\u0101\u0103")
        buf.write("\5\n\6\2\u0102\u0100\3\2\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("%\3\2\2\2\u0104\u010b\5<\37\2\u0105\u010b\5B\"\2\u0106")
        buf.write("\u010b\5b\62\2\u0107\u010b\5p9\2\u0108\u010b\5D#\2\u0109")
        buf.write("\u010b\5r:\2\u010a\u0104\3\2\2\2\u010a\u0105\3\2\2\2\u010a")
        buf.write("\u0106\3\2\2\2\u010a\u0107\3\2\2\2\u010a\u0108\3\2\2\2")
        buf.write("\u010a\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\7")
        buf.write("\33\2\2\u010d\'\3\2\2\2\u010e\u010f\t\4\2\2\u010f)\3\2")
        buf.write("\2\2\u0110\u0111\5,\27\2\u0111+\3\2\2\2\u0112\u0113\b")
        buf.write("\27\1\2\u0113\u0114\5.\30\2\u0114\u011a\3\2\2\2\u0115")
        buf.write("\u0116\f\4\2\2\u0116\u0117\7\21\2\2\u0117\u0119\5.\30")
        buf.write("\2\u0118\u0115\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b-\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011d\u011e\b\30\1\2\u011e\u011f\5\60\31\2\u011f")
        buf.write("\u0125\3\2\2\2\u0120\u0121\f\4\2\2\u0121\u0122\7\20\2")
        buf.write("\2\u0122\u0124\5\60\31\2\u0123\u0120\3\2\2\2\u0124\u0127")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("/\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\b\31\1\2\u0129")
        buf.write("\u012a\5\62\32\2\u012a\u0130\3\2\2\2\u012b\u012c\f\4\2")
        buf.write("\2\u012c\u012d\t\5\2\2\u012d\u012f\5\62\32\2\u012e\u012b")
        buf.write("\3\2\2\2\u012f\u0132\3\2\2\2\u0130\u012e\3\2\2\2\u0130")
        buf.write("\u0131\3\2\2\2\u0131\61\3\2\2\2\u0132\u0130\3\2\2\2\u0133")
        buf.write("\u0134\b\32\1\2\u0134\u0135\5\64\33\2\u0135\u013b\3\2")
        buf.write("\2\2\u0136\u0137\f\4\2\2\u0137\u0138\t\6\2\2\u0138\u013a")
        buf.write("\5\64\33\2\u0139\u0136\3\2\2\2\u013a\u013d\3\2\2\2\u013b")
        buf.write("\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c\63\3\2\2\2\u013d")
        buf.write("\u013b\3\2\2\2\u013e\u013f\b\33\1\2\u013f\u0140\5\66\34")
        buf.write("\2\u0140\u0146\3\2\2\2\u0141\u0142\f\4\2\2\u0142\u0143")
        buf.write("\t\7\2\2\u0143\u0145\5\66\34\2\u0144\u0141\3\2\2\2\u0145")
        buf.write("\u0148\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2")
        buf.write("\u0147\65\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a\7\22")
        buf.write("\2\2\u014a\u014f\5\66\34\2\u014b\u014c\7\6\2\2\u014c\u014f")
        buf.write("\5\66\34\2\u014d\u014f\58\35\2\u014e\u0149\3\2\2\2\u014e")
        buf.write("\u014b\3\2\2\2\u014e\u014d\3\2\2\2\u014f\67\3\2\2\2\u0150")
        buf.write("\u0151\b\35\1\2\u0151\u0152\5:\36\2\u0152\u0161\3\2\2")
        buf.write("\2\u0153\u0154\f\5\2\2\u0154\u0155\79\2\2\u0155\u0160")
        buf.write("\7\61\2\2\u0156\u0157\f\4\2\2\u0157\u0160\5P)\2\u0158")
        buf.write("\u0159\f\3\2\2\u0159\u015a\79\2\2\u015a\u015b\7\61\2\2")
        buf.write("\u015b\u015c\7\62\2\2\u015c\u015d\5^\60\2\u015d\u015e")
        buf.write("\7\63\2\2\u015e\u0160\3\2\2\2\u015f\u0153\3\2\2\2\u015f")
        buf.write("\u0156\3\2\2\2\u015f\u0158\3\2\2\2\u0160\u0163\3\2\2\2")
        buf.write("\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u01629\3\2\2")
        buf.write("\2\u0163\u0161\3\2\2\2\u0164\u016e\5\34\17\2\u0165\u016e")
        buf.write("\7\61\2\2\u0166\u016e\5\2\2\2\u0167\u016e\5V,\2\u0168")
        buf.write("\u016e\5h\65\2\u0169\u016a\7\62\2\2\u016a\u016b\5*\26")
        buf.write("\2\u016b\u016c\7\63\2\2\u016c\u016e\3\2\2\2\u016d\u0164")
        buf.write("\3\2\2\2\u016d\u0165\3\2\2\2\u016d\u0166\3\2\2\2\u016d")
        buf.write("\u0167\3\2\2\2\u016d\u0168\3\2\2\2\u016d\u0169\3\2\2\2")
        buf.write("\u016e;\3\2\2\2\u016f\u0172\5> \2\u0170\u0172\5@!\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172=\3\2\2\2\u0173")
        buf.write("\u0174\7$\2\2\u0174\u0177\7\61\2\2\u0175\u0178\5\"\22")
        buf.write("\2\u0176\u0178\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017a\7\31\2\2\u017a")
        buf.write("\u017b\5*\26\2\u017b?\3\2\2\2\u017c\u017d\7$\2\2\u017d")
        buf.write("\u017e\7\61\2\2\u017e\u017f\5\"\22\2\u017fA\3\2\2\2\u0180")
        buf.write("\u0181\7#\2\2\u0181\u0182\7\61\2\2\u0182\u0183\7\31\2")
        buf.write("\2\u0183\u0184\5*\26\2\u0184C\3\2\2\2\u0185\u0186\7&\2")
        buf.write("\2\u0186\u0187\7\61\2\2\u0187\u0188\7\62\2\2\u0188\u0189")
        buf.write("\5F$\2\u0189\u018c\7\63\2\2\u018a\u018d\5\"\22\2\u018b")
        buf.write("\u018d\3\2\2\2\u018c\u018a\3\2\2\2\u018c\u018b\3\2\2\2")
        buf.write("\u018d\u018e\3\2\2\2\u018e\u018f\7\64\2\2\u018f\u0190")
        buf.write("\5\30\r\2\u0190\u0191\7\65\2\2\u0191E\3\2\2\2\u0192\u0195")
        buf.write("\5H%\2\u0193\u0195\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0193")
        buf.write("\3\2\2\2\u0195G\3\2\2\2\u0196\u0197\5J&\2\u0197\u0198")
        buf.write("\78\2\2\u0198\u0199\5H%\2\u0199\u019c\3\2\2\2\u019a\u019c")
        buf.write("\5J&\2\u019b\u0196\3\2\2\2\u019b\u019a\3\2\2\2\u019cI")
        buf.write("\3\2\2\2\u019d\u019e\5L\'\2\u019e\u019f\5\"\22\2\u019f")
        buf.write("K\3\2\2\2\u01a0\u01a1\7\61\2\2\u01a1\u01a2\78\2\2\u01a2")
        buf.write("\u01a5\5L\'\2\u01a3\u01a5\7\61\2\2\u01a4\u01a0\3\2\2\2")
        buf.write("\u01a4\u01a3\3\2\2\2\u01a5M\3\2\2\2\u01a6\u01a7\5R*\2")
        buf.write("\u01a7\u01a8\5N(\2\u01a8\u01ab\3\2\2\2\u01a9\u01ab\5R")
        buf.write("*\2\u01aa\u01a6\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abO\3\2")
        buf.write("\2\2\u01ac\u01ad\5T+\2\u01ad\u01ae\5P)\2\u01ae\u01b1\3")
        buf.write("\2\2\2\u01af\u01b1\5T+\2\u01b0\u01ac\3\2\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1Q\3\2\2\2\u01b2\u01b3\7\66\2\2\u01b3\u01b4")
        buf.write("\t\b\2\2\u01b4\u01b5\7\67\2\2\u01b5S\3\2\2\2\u01b6\u01b7")
        buf.write("\7\66\2\2\u01b7\u01b8\5*\26\2\u01b8\u01b9\7\67\2\2\u01b9")
        buf.write("U\3\2\2\2\u01ba\u01bb\5N(\2\u01bb\u01bc\5\"\22\2\u01bc")
        buf.write("\u01bd\5X-\2\u01bdW\3\2\2\2\u01be\u01bf\7\64\2\2\u01bf")
        buf.write("\u01c0\5Z.\2\u01c0\u01c1\7\65\2\2\u01c1\u01c5\3\2\2\2")
        buf.write("\u01c2\u01c3\7\64\2\2\u01c3\u01c5\7\65\2\2\u01c4\u01be")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5Y\3\2\2\2\u01c6\u01c7")
        buf.write("\5\\/\2\u01c7\u01c8\78\2\2\u01c8\u01c9\5Z.\2\u01c9\u01cc")
        buf.write("\3\2\2\2\u01ca\u01cc\5\\/\2\u01cb\u01c6\3\2\2\2\u01cb")
        buf.write("\u01ca\3\2\2\2\u01cc[\3\2\2\2\u01cd\u01d4\5X-\2\u01ce")
        buf.write("\u01d2\5\34\17\2\u01cf\u01d2\5h\65\2\u01d0\u01d2\7\61")
        buf.write("\2\2\u01d1\u01ce\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d0")
        buf.write("\3\2\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01cd\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d4]\3\2\2\2\u01d5\u01d8\5`\61\2\u01d6")
        buf.write("\u01d8\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6\3\2\2\2")
        buf.write("\u01d8_\3\2\2\2\u01d9\u01da\5*\26\2\u01da\u01db\78\2\2")
        buf.write("\u01db\u01dc\5`\61\2\u01dc\u01df\3\2\2\2\u01dd\u01df\5")
        buf.write("*\26\2\u01de\u01d9\3\2\2\2\u01de\u01dd\3\2\2\2\u01dfa")
        buf.write("\3\2\2\2\u01e0\u01e1\7(\2\2\u01e1\u01e2\7\61\2\2\u01e2")
        buf.write("\u01e3\7 \2\2\u01e3\u01e4\7\64\2\2\u01e4\u01e5\5d\63\2")
        buf.write("\u01e5\u01e6\7\65\2\2\u01e6c\3\2\2\2\u01e7\u01ea\5f\64")
        buf.write("\2\u01e8\u01ea\5p9\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8\3")
        buf.write("\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\7\33\2\2\u01ec")
        buf.write("\u01ed\3\2\2\2\u01ed\u01ee\5d\63\2\u01ee\u01f6\3\2\2\2")
        buf.write("\u01ef\u01f2\5f\64\2\u01f0\u01f2\5p9\2\u01f1\u01ef\3\2")
        buf.write("\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4")
        buf.write("\7\33\2\2\u01f4\u01f6\3\2\2\2\u01f5\u01e9\3\2\2\2\u01f5")
        buf.write("\u01f1\3\2\2\2\u01f6e\3\2\2\2\u01f7\u01f8\7\61\2\2\u01f8")
        buf.write("\u01f9\5\"\22\2\u01f9g\3\2\2\2\u01fa\u01fb\7\61\2\2\u01fb")
        buf.write("\u01fc\7\64\2\2\u01fc\u01fd\5j\66\2\u01fd\u01fe\7\65\2")
        buf.write("\2\u01fei\3\2\2\2\u01ff\u0202\5l\67\2\u0200\u0202\3\2")
        buf.write("\2\2\u0201\u01ff\3\2\2\2\u0201\u0200\3\2\2\2\u0202k\3")
        buf.write("\2\2\2\u0203\u0204\5n8\2\u0204\u0205\78\2\2\u0205\u0206")
        buf.write("\5l\67\2\u0206\u0209\3\2\2\2\u0207\u0209\5n8\2\u0208\u0203")
        buf.write("\3\2\2\2\u0208\u0207\3\2\2\2\u0209m\3\2\2\2\u020a\u020b")
        buf.write("\7\61\2\2\u020b\u020c\7\32\2\2\u020c\u020d\5*\26\2\u020d")
        buf.write("o\3\2\2\2\u020e\u020f\7&\2\2\u020f\u0210\7\62\2\2\u0210")
        buf.write("\u0211\7\61\2\2\u0211\u0212\7\61\2\2\u0212\u0213\7\63")
        buf.write("\2\2\u0213\u0214\7\61\2\2\u0214\u0215\7\62\2\2\u0215\u0216")
        buf.write("\5F$\2\u0216\u0219\7\63\2\2\u0217\u021a\5\"\22\2\u0218")
        buf.write("\u021a\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u0218\3\2\2\2")
        buf.write("\u021a\u021b\3\2\2\2\u021b\u021c\7\64\2\2\u021c\u021d")
        buf.write("\5\30\r\2\u021d\u021e\7\65\2\2\u021eq\3\2\2\2\u021f\u0220")
        buf.write("\7(\2\2\u0220\u0221\7\61\2\2\u0221\u0222\7!\2\2\u0222")
        buf.write("\u0223\7\64\2\2\u0223\u0224\5t;\2\u0224\u0225\7\65\2\2")
        buf.write("\u0225s\3\2\2\2\u0226\u0229\5v<\2\u0227\u0229\3\2\2\2")
        buf.write("\u0228\u0226\3\2\2\2\u0228\u0227\3\2\2\2\u0229u\3\2\2")
        buf.write("\2\u022a\u022b\5x=\2\u022b\u022c\5v<\2\u022c\u022f\3\2")
        buf.write("\2\2\u022d\u022f\5x=\2\u022e\u022a\3\2\2\2\u022e\u022d")
        buf.write("\3\2\2\2\u022fw\3\2\2\2\u0230\u0231\7\61\2\2\u0231\u0232")
        buf.write("\7\62\2\2\u0232\u0233\5z>\2\u0233\u0236\7\63\2\2\u0234")
        buf.write("\u0237\5\"\22\2\u0235\u0237\3\2\2\2\u0236\u0234\3\2\2")
        buf.write("\2\u0236\u0235\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239")
        buf.write("\7\33\2\2\u0239y\3\2\2\2\u023a\u023d\5|?\2\u023b\u023d")
        buf.write("\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023b\3\2\2\2\u023d")
        buf.write("{\3\2\2\2\u023e\u023f\5~@\2\u023f\u0240\78\2\2\u0240\u0241")
        buf.write("\5|?\2\u0241\u0244\3\2\2\2\u0242\u0244\5~@\2\u0243\u023e")
        buf.write("\3\2\2\2\u0243\u0242\3\2\2\2\u0244}\3\2\2\2\u0245\u0246")
        buf.write("\5\u0080A\2\u0246\u0247\5\"\22\2\u0247\177\3\2\2\2\u0248")
        buf.write("\u0249\7\61\2\2\u0249\u024a\78\2\2\u024a\u024d\5\u0080")
        buf.write("A\2\u024b\u024d\7\61\2\2\u024c\u0248\3\2\2\2\u024c\u024b")
        buf.write("\3\2\2\2\u024d\u0081\3\2\2\2\u024e\u024f\5$\23\2\u024f")
        buf.write("\u0250\5(\25\2\u0250\u0251\5*\26\2\u0251\u0255\3\2\2\2")
        buf.write("\u0252\u0255\5\u0084C\2\u0253\u0255\5\u0086D\2\u0254\u024e")
        buf.write("\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0253\3\2\2\2\u0255")
        buf.write("\u0083\3\2\2\2\u0256\u0257\5$\23\2\u0257\u0258\7\23\2")
        buf.write("\2\u0258\u0259\5V,\2\u0259\u0085\3\2\2\2\u025a\u025b\5")
        buf.write("$\23\2\u025b\u025c\7\23\2\2\u025c\u025d\5h\65\2\u025d")
        buf.write("\u0087\3\2\2\2\u025e\u025f\7\35\2\2\u025f\u0260\7\62\2")
        buf.write("\2\u0260\u0261\5*\26\2\u0261\u0262\7\63\2\2\u0262\u0263")
        buf.write("\7\64\2\2\u0263\u0264\5\30\r\2\u0264\u0265\7\65\2\2\u0265")
        buf.write("\u0266\5\u008aF\2\u0266\u0089\3\2\2\2\u0267\u026a\5\u008c")
        buf.write("G\2\u0268\u026b\5\u0090I\2\u0269\u026b\3\2\2\2\u026a\u0268")
        buf.write("\3\2\2\2\u026a\u0269\3\2\2\2\u026b\u008b\3\2\2\2\u026c")
        buf.write("\u026d\5\u008eH\2\u026d\u026e\5\u008cG\2\u026e\u0271\3")
        buf.write("\2\2\2\u026f\u0271\3\2\2\2\u0270\u026c\3\2\2\2\u0270\u026f")
        buf.write("\3\2\2\2\u0271\u008d\3\2\2\2\u0272\u0273\7\36\2\2\u0273")
        buf.write("\u0274\7\35\2\2\u0274\u0275\7\62\2\2\u0275\u0276\5*\26")
        buf.write("\2\u0276\u0277\7\63\2\2\u0277\u0278\7\64\2\2\u0278\u0279")
        buf.write("\5\30\r\2\u0279\u027a\7\65\2\2\u027a\u008f\3\2\2\2\u027b")
        buf.write("\u027c\7\36\2\2\u027c\u027d\7\64\2\2\u027d\u027e\5\30")
        buf.write("\r\2\u027e\u027f\7\65\2\2\u027f\u0091\3\2\2\2\u0280\u0284")
        buf.write("\5\u0094K\2\u0281\u0284\5\u0096L\2\u0282\u0284\5\u0098")
        buf.write("M\2\u0283\u0280\3\2\2\2\u0283\u0281\3\2\2\2\u0283\u0282")
        buf.write("\3\2\2\2\u0284\u0093\3\2\2\2\u0285\u0286\7\37\2\2\u0286")
        buf.write("\u0287\5*\26\2\u0287\u0288\7\64\2\2\u0288\u0289\5\30\r")
        buf.write("\2\u0289\u028a\7\65\2\2\u028a\u0095\3\2\2\2\u028b\u028e")
        buf.write("\7\37\2\2\u028c\u028f\5\u0082B\2\u028d\u028f\5> \2\u028e")
        buf.write("\u028c\3\2\2\2\u028e\u028d\3\2\2\2\u028f\u0290\3\2\2\2")
        buf.write("\u0290\u0291\7\33\2\2\u0291\u0292\5*\26\2\u0292\u0293")
        buf.write("\7\33\2\2\u0293\u0294\5\u0082B\2\u0294\u0295\7\64\2\2")
        buf.write("\u0295\u0296\5\30\r\2\u0296\u0297\7\65\2\2\u0297\u0097")
        buf.write("\3\2\2\2\u0298\u0299\7\37\2\2\u0299\u029a\t\t\2\2\u029a")
        buf.write("\u029b\78\2\2\u029b\u029c\7\61\2\2\u029c\u029d\7\23\2")
        buf.write("\2\u029d\u029e\7-\2\2\u029e\u029f\5*\26\2\u029f\u02a0")
        buf.write("\7\64\2\2\u02a0\u02a1\5\30\r\2\u02a1\u02a2\7\65\2\2\u02a2")
        buf.write("\u0099\3\2\2\2\u02a3\u02a4\7,\2\2\u02a4\u009b\3\2\2\2")
        buf.write("\u02a5\u02a6\7+\2\2\u02a6\u009d\3\2\2\2\u02a7\u02aa\5")
        buf.write("\2\2\2\u02a8\u02aa\5\b\5\2\u02a9\u02a7\3\2\2\2\u02a9\u02a8")
        buf.write("\3\2\2\2\u02aa\u009f\3\2\2\2\u02ab\u02ac\7%\2\2\u02ac")
        buf.write("\u02af\5*\26\2\u02ad\u02af\7%\2\2\u02ae\u02ab\3\2\2\2")
        buf.write("\u02ae\u02ad\3\2\2\2\u02af\u00a1\3\2\2\29\u00b1\u00b5")
        buf.write("\u00bb\u00c6\u00cc\u00d0\u00dd\u00e3\u00ee\u00f9\u00fe")
        buf.write("\u0102\u010a\u011a\u0125\u0130\u013b\u0146\u014e\u015f")
        buf.write("\u0161\u016d\u0171\u0177\u018c\u0194\u019b\u01a4\u01aa")
        buf.write("\u01b0\u01c4\u01cb\u01d1\u01d3\u01d7\u01de\u01e9\u01f1")
        buf.write("\u01f5\u0201\u0208\u0219\u0228\u022e\u0236\u023c\u0243")
        buf.write("\u024c\u0254\u026a\u0270\u0283\u028e\u02a9\u02ae")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "':='", "'+='", 
                     "'-='", "'*='", "'/='", "'%='", "'='", "':'", "';'", 
                     "<INVALID>", "'if'", "'else'", "'for'", "'struct'", 
                     "'interface'", "'string'", "'const'", "'var'", "'return'", 
                     "'func'", "'int'", "'type'", "'float'", "'boolean'", 
                     "'continue'", "'break'", "'range'", "'true'", "'false'", 
                     "'nil'", "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "'.'", "'_'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "SINGLE_COMMENT", "MULTI_COMMENT", "PLUS", 
                      "MINUS", "MUL", "DIV", "MOD", "EQ", "NEQ", "LT", "LE", 
                      "GT", "GE", "AND", "OR", "NOT", "ASSIGN", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "MOD_ASSIGN", 
                      "EQUAL", "COLON", "SEMICOLON", "BOOLEAN_LIT", "KW_IF", 
                      "KW_ELSE", "KW_FOR", "KW_STRUCT", "KW_INTERFACE", 
                      "KW_STRING", "KW_CONST", "KW_VAR", "KW_RETURN", "KW_FUNC", 
                      "KW_INT", "KW_TYPE", "KW_FLOAT", "KW_BOOL", "KW_CONTINUE", 
                      "KW_BREAK", "KW_RANGE", "KW_TRUE", "KW_FALSE", "KW_NIL", 
                      "IDENTIFIER", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACK", "RBRACK", "COMMA", "DOT", "UNDERLINE", "INTEGER_LIT", 
                      "FLOAT_LIT", "STRING_LIT", "NL", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_func_call = 0
    RULE_single_method_call = 1
    RULE_list_method_call = 2
    RULE_method_call = 3
    RULE_struct_arr_access = 4
    RULE_struct_access = 5
    RULE_arr_access = 6
    RULE_struct_arr_access_prime = 7
    RULE_arr_ele = 8
    RULE_program = 9
    RULE_list_declr = 10
    RULE_list_statement = 11
    RULE_stmt = 12
    RULE_primitive_values = 13
    RULE_primitive_types = 14
    RULE_arr_type = 15
    RULE_all_types = 16
    RULE_all_var = 17
    RULE_declr_all = 18
    RULE_assign_opp = 19
    RULE_expression = 20
    RULE_logicalOrExpr = 21
    RULE_logicalAndExpr = 22
    RULE_equalityExpr = 23
    RULE_additiveExpr = 24
    RULE_multiplicativeExpr = 25
    RULE_unaryExpr = 26
    RULE_postfixExpr = 27
    RULE_primaryExpr = 28
    RULE_var_dec = 29
    RULE_var_dec_init = 30
    RULE_var_dec_no_init = 31
    RULE_const_dec = 32
    RULE_func_dec = 33
    RULE_list_arguments = 34
    RULE_list_arg_prime = 35
    RULE_arg = 36
    RULE_arg_prime = 37
    RULE_dimension_list_in_lit = 38
    RULE_dimension_list_in_var = 39
    RULE_dimension_in_lit = 40
    RULE_dimension_in_var = 41
    RULE_arr_lit = 42
    RULE_nested_list = 43
    RULE_element_list = 44
    RULE_element = 45
    RULE_list_val = 46
    RULE_expression_prime = 47
    RULE_struct_def = 48
    RULE_list_field = 49
    RULE_field_dec = 50
    RULE_struct_lit = 51
    RULE_list_field_init = 52
    RULE_list_field_prime = 53
    RULE_field_init = 54
    RULE_struct_method_def = 55
    RULE_interface_dec = 56
    RULE_list_method = 57
    RULE_list_method_prime = 58
    RULE_method_dec = 59
    RULE_list_prototypes = 60
    RULE_list_prototypes_prime = 61
    RULE_prototype = 62
    RULE_prototype_prime = 63
    RULE_assignment = 64
    RULE_arr_assign = 65
    RULE_struct_assign = 66
    RULE_if_stmt = 67
    RULE_list_else_if_stmt = 68
    RULE_list_else_if_stmt_prime = 69
    RULE_one_esle_if_stmt = 70
    RULE_else_stmt = 71
    RULE_for_stmt = 72
    RULE_basic_for_stmt = 73
    RULE_init_for_stmt = 74
    RULE_range_for_stmt = 75
    RULE_break_stmt = 76
    RULE_continue_stmt = 77
    RULE_call_stmt = 78
    RULE_return_stmt = 79

    ruleNames =  [ "func_call", "single_method_call", "list_method_call", 
                   "method_call", "struct_arr_access", "struct_access", 
                   "arr_access", "struct_arr_access_prime", "arr_ele", "program", 
                   "list_declr", "list_statement", "stmt", "primitive_values", 
                   "primitive_types", "arr_type", "all_types", "all_var", 
                   "declr_all", "assign_opp", "expression", "logicalOrExpr", 
                   "logicalAndExpr", "equalityExpr", "additiveExpr", "multiplicativeExpr", 
                   "unaryExpr", "postfixExpr", "primaryExpr", "var_dec", 
                   "var_dec_init", "var_dec_no_init", "const_dec", "func_dec", 
                   "list_arguments", "list_arg_prime", "arg", "arg_prime", 
                   "dimension_list_in_lit", "dimension_list_in_var", "dimension_in_lit", 
                   "dimension_in_var", "arr_lit", "nested_list", "element_list", 
                   "element", "list_val", "expression_prime", "struct_def", 
                   "list_field", "field_dec", "struct_lit", "list_field_init", 
                   "list_field_prime", "field_init", "struct_method_def", 
                   "interface_dec", "list_method", "list_method_prime", 
                   "method_dec", "list_prototypes", "list_prototypes_prime", 
                   "prototype", "prototype_prime", "assignment", "arr_assign", 
                   "struct_assign", "if_stmt", "list_else_if_stmt", "list_else_if_stmt_prime", 
                   "one_esle_if_stmt", "else_stmt", "for_stmt", "basic_for_stmt", 
                   "init_for_stmt", "range_for_stmt", "break_stmt", "continue_stmt", 
                   "call_stmt", "return_stmt" ]

    EOF = Token.EOF
    SINGLE_COMMENT=1
    MULTI_COMMENT=2
    PLUS=3
    MINUS=4
    MUL=5
    DIV=6
    MOD=7
    EQ=8
    NEQ=9
    LT=10
    LE=11
    GT=12
    GE=13
    AND=14
    OR=15
    NOT=16
    ASSIGN=17
    ADD_ASSIGN=18
    SUB_ASSIGN=19
    MUL_ASSIGN=20
    DIV_ASSIGN=21
    MOD_ASSIGN=22
    EQUAL=23
    COLON=24
    SEMICOLON=25
    BOOLEAN_LIT=26
    KW_IF=27
    KW_ELSE=28
    KW_FOR=29
    KW_STRUCT=30
    KW_INTERFACE=31
    KW_STRING=32
    KW_CONST=33
    KW_VAR=34
    KW_RETURN=35
    KW_FUNC=36
    KW_INT=37
    KW_TYPE=38
    KW_FLOAT=39
    KW_BOOL=40
    KW_CONTINUE=41
    KW_BREAK=42
    KW_RANGE=43
    KW_TRUE=44
    KW_FALSE=45
    KW_NIL=46
    IDENTIFIER=47
    LPAREN=48
    RPAREN=49
    LBRACE=50
    RBRACE=51
    LBRACK=52
    RBRACK=53
    COMMA=54
    DOT=55
    UNDERLINE=56
    INTEGER_LIT=57
    FLOAT_LIT=58
    STRING_LIT=59
    NL=60
    WS=61
    ILLEGAL_ESCAPE=62
    UNCLOSE_STRING=63
    ERROR_CHAR=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_val(self):
            return self.getTypedRuleContext(MiniGoParser.List_valContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = MiniGoParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_func_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 161
            self.match(MiniGoParser.LPAREN)
            self.state = 162
            self.list_val()
            self.state = 163
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Single_method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_val(self):
            return self.getTypedRuleContext(MiniGoParser.List_valContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_single_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingle_method_call" ):
                return visitor.visitSingle_method_call(self)
            else:
                return visitor.visitChildren(self)




    def single_method_call(self):

        localctx = MiniGoParser.Single_method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_single_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MiniGoParser.DOT)
            self.state = 166
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 167
            self.match(MiniGoParser.LPAREN)
            self.state = 168
            self.list_val()
            self.state = 169
            self.match(MiniGoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def single_method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Single_method_callContext,0)


        def list_method_call(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_method_call" ):
                return visitor.visitList_method_call(self)
            else:
                return visitor.visitChildren(self)




    def list_method_call(self):

        localctx = MiniGoParser.List_method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_list_method_call)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.single_method_call()
                self.state = 172
                self.list_method_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.single_method_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_method_call(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_callContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_arr_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_arr_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_call" ):
                return visitor.visitMethod_call(self)
            else:
                return visitor.visitChildren(self)




    def method_call(self):

        localctx = MiniGoParser.Method_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_method_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 177
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 178
                self.struct_arr_access()
                pass


            self.state = 181
            self.list_method_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_arr_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def arr_access(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_arr_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_arr_access" ):
                return visitor.visitStruct_arr_access(self)
            else:
                return visitor.visitChildren(self)




    def struct_arr_access(self):

        localctx = MiniGoParser.Struct_arr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_struct_arr_access)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.struct_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.arr_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_arr_access_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_arr_access_primeContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_access" ):
                return visitor.visitStruct_access(self)
            else:
                return visitor.visitChildren(self)




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.struct_arr_access_prime(0)
            self.state = 188
            self.match(MiniGoParser.DOT)
            self.state = 189
            self.match(MiniGoParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_arr_access_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_arr_access_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_access" ):
                return visitor.visitArr_access(self)
            else:
                return visitor.visitChildren(self)




    def arr_access(self):

        localctx = MiniGoParser.Arr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.struct_arr_access_prime(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_arr_access_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arr_ele(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_eleContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_arr_access_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_arr_access_primeContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_arr_access_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_arr_access_prime" ):
                return visitor.visitStruct_arr_access_prime(self)
            else:
                return visitor.visitChildren(self)



    def struct_arr_access_prime(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Struct_arr_access_primeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_struct_arr_access_prime, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 194
                self.arr_ele()
                pass

            elif la_ == 2:
                self.state = 195
                self.match(MiniGoParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 206
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Struct_arr_access_primeContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_struct_arr_access_prime)
                    self.state = 198
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 199
                    self.match(MiniGoParser.DOT)
                    self.state = 202
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        self.state = 200
                        self.arr_ele()
                        pass

                    elif la_ == 2:
                        self.state = 201
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

             
                self.state = 208
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Arr_eleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def dimension_list_in_var(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_list_in_varContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_ele

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_ele" ):
                return visitor.visitArr_ele(self)
            else:
                return visitor.visitChildren(self)




    def arr_ele(self):

        localctx = MiniGoParser.Arr_eleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arr_ele)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 210
            self.dimension_list_in_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_declr(self):
            return self.getTypedRuleContext(MiniGoParser.List_declrContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.list_declr()
            self.state = 213
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_declrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declr_all(self):
            return self.getTypedRuleContext(MiniGoParser.Declr_allContext,0)


        def list_declr(self):
            return self.getTypedRuleContext(MiniGoParser.List_declrContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_declr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_declr" ):
                return visitor.visitList_declr(self)
            else:
                return visitor.visitChildren(self)




    def list_declr(self):

        localctx = MiniGoParser.List_declrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_list_declr)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.declr_all()
                self.state = 216
                self.list_declr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.declr_all()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = MiniGoParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_statement)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.stmt()
                self.state = 222
                self.list_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def var_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decContext,0)


        def const_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Const_decContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.For_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 227
                self.var_dec()
                pass

            elif la_ == 2:
                self.state = 228
                self.const_dec()
                pass

            elif la_ == 3:
                self.state = 229
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 230
                self.if_stmt()
                pass

            elif la_ == 5:
                self.state = 231
                self.for_stmt()
                pass

            elif la_ == 6:
                self.state = 232
                self.break_stmt()
                pass

            elif la_ == 7:
                self.state = 233
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.state = 234
                self.call_stmt()
                pass

            elif la_ == 9:
                self.state = 235
                self.return_stmt()
                pass


            self.state = 238
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_valuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LIT(self):
            return self.getToken(MiniGoParser.INTEGER_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(MiniGoParser.BOOLEAN_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def KW_NIL(self):
            return self.getToken(MiniGoParser.KW_NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_values

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_values" ):
                return visitor.visitPrimitive_values(self)
            else:
                return visitor.visitChildren(self)




    def primitive_values(self):

        localctx = MiniGoParser.Primitive_valuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_primitive_values)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BOOLEAN_LIT) | (1 << MiniGoParser.KW_NIL) | (1 << MiniGoParser.INTEGER_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
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


    class Primitive_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INT(self):
            return self.getToken(MiniGoParser.KW_INT, 0)

        def KW_BOOL(self):
            return self.getToken(MiniGoParser.KW_BOOL, 0)

        def KW_STRING(self):
            return self.getToken(MiniGoParser.KW_STRING, 0)

        def KW_FLOAT(self):
            return self.getToken(MiniGoParser.KW_FLOAT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primitive_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_types" ):
                return visitor.visitPrimitive_types(self)
            else:
                return visitor.visitChildren(self)




    def primitive_types(self):

        localctx = MiniGoParser.Primitive_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.KW_STRING) | (1 << MiniGoParser.KW_INT) | (1 << MiniGoParser.KW_FLOAT) | (1 << MiniGoParser.KW_BOOL))) != 0)):
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


    class Arr_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list_in_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_list_in_litContext,0)


        def primitive_types(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typesContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_type" ):
                return visitor.visitArr_type(self)
            else:
                return visitor.visitChildren(self)




    def arr_type(self):

        localctx = MiniGoParser.Arr_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arr_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.dimension_list_in_lit()
            self.state = 247
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOL]:
                self.state = 245
                self.primitive_types()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.state = 246
                self.match(MiniGoParser.IDENTIFIER)
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


    class All_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_types(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_typesContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def arr_type(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_typeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_all_types

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_types" ):
                return visitor.visitAll_types(self)
            else:
                return visitor.visitChildren(self)




    def all_types(self):

        localctx = MiniGoParser.All_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_all_types)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.primitive_types()
                pass
            elif token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self.match(MiniGoParser.IDENTIFIER)
                pass
            elif token in [MiniGoParser.LBRACK]:
                self.enterOuterAlt(localctx, 3)
                self.state = 251
                self.arr_type()
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


    class All_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def struct_arr_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_arr_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_all_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_var" ):
                return visitor.visitAll_var(self)
            else:
                return visitor.visitChildren(self)




    def all_var(self):

        localctx = MiniGoParser.All_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_all_var)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.struct_arr_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declr_allContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def var_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Var_decContext,0)


        def const_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Const_decContext,0)


        def struct_def(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_defContext,0)


        def struct_method_def(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_method_defContext,0)


        def func_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Func_decContext,0)


        def interface_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Interface_decContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_declr_all

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclr_all" ):
                return visitor.visitDeclr_all(self)
            else:
                return visitor.visitChildren(self)




    def declr_all(self):

        localctx = MiniGoParser.Declr_allContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_declr_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 258
                self.var_dec()
                pass

            elif la_ == 2:
                self.state = 259
                self.const_dec()
                pass

            elif la_ == 3:
                self.state = 260
                self.struct_def()
                pass

            elif la_ == 4:
                self.state = 261
                self.struct_method_def()
                pass

            elif la_ == 5:
                self.state = 262
                self.func_dec()
                pass

            elif la_ == 6:
                self.state = 263
                self.interface_dec()
                pass


            self.state = 266
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_oppContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def ADD_ASSIGN(self):
            return self.getToken(MiniGoParser.ADD_ASSIGN, 0)

        def SUB_ASSIGN(self):
            return self.getToken(MiniGoParser.SUB_ASSIGN, 0)

        def MUL_ASSIGN(self):
            return self.getToken(MiniGoParser.MUL_ASSIGN, 0)

        def DIV_ASSIGN(self):
            return self.getToken(MiniGoParser.DIV_ASSIGN, 0)

        def MOD_ASSIGN(self):
            return self.getToken(MiniGoParser.MOD_ASSIGN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assign_opp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_opp" ):
                return visitor.visitAssign_opp(self)
            else:
                return visitor.visitChildren(self)




    def assign_opp(self):

        localctx = MiniGoParser.Assign_oppContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assign_opp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN) | (1 << MiniGoParser.ADD_ASSIGN) | (1 << MiniGoParser.SUB_ASSIGN) | (1 << MiniGoParser.MUL_ASSIGN) | (1 << MiniGoParser.DIV_ASSIGN) | (1 << MiniGoParser.MOD_ASSIGN))) != 0)):
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

        def logicalOrExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalOrExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = MiniGoParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.logicalOrExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalAndExprContext,0)


        def logicalOrExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalOrExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logicalOrExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpr" ):
                return visitor.visitLogicalOrExpr(self)
            else:
                return visitor.visitChildren(self)



    def logicalOrExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LogicalOrExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_logicalOrExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.logicalAndExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicalOrExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalOrExpr)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    self.match(MiniGoParser.OR)
                    self.state = 277
                    self.logicalAndExpr(0) 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LogicalAndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpr(self):
            return self.getTypedRuleContext(MiniGoParser.EqualityExprContext,0)


        def logicalAndExpr(self):
            return self.getTypedRuleContext(MiniGoParser.LogicalAndExprContext,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_logicalAndExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpr" ):
                return visitor.visitLogicalAndExpr(self)
            else:
                return visitor.visitChildren(self)



    def logicalAndExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LogicalAndExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_logicalAndExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.equalityExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.LogicalAndExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_logicalAndExpr)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    self.match(MiniGoParser.AND)
                    self.state = 288
                    self.equalityExpr(0) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class EqualityExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AdditiveExprContext,0)


        def equalityExpr(self):
            return self.getTypedRuleContext(MiniGoParser.EqualityExprContext,0)


        def EQ(self):
            return self.getToken(MiniGoParser.EQ, 0)

        def NEQ(self):
            return self.getToken(MiniGoParser.NEQ, 0)

        def LT(self):
            return self.getToken(MiniGoParser.LT, 0)

        def LE(self):
            return self.getToken(MiniGoParser.LE, 0)

        def GT(self):
            return self.getToken(MiniGoParser.GT, 0)

        def GE(self):
            return self.getToken(MiniGoParser.GE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_equalityExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpr" ):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)



    def equalityExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.EqualityExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_equalityExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.additiveExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.EqualityExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_equalityExpr)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQ) | (1 << MiniGoParser.NEQ) | (1 << MiniGoParser.LT) | (1 << MiniGoParser.LE) | (1 << MiniGoParser.GT) | (1 << MiniGoParser.GE))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 299
                    self.additiveExpr(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AdditiveExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MultiplicativeExprContext,0)


        def additiveExpr(self):
            return self.getTypedRuleContext(MiniGoParser.AdditiveExprContext,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_additiveExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpr" ):
                return visitor.visitAdditiveExpr(self)
            else:
                return visitor.visitChildren(self)



    def additiveExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.AdditiveExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_additiveExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.multiplicativeExpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.AdditiveExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_additiveExpr)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.multiplicativeExpr(0) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultiplicativeExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExprContext,0)


        def multiplicativeExpr(self):
            return self.getTypedRuleContext(MiniGoParser.MultiplicativeExprContext,0)


        def MUL(self):
            return self.getToken(MiniGoParser.MUL, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MOD(self):
            return self.getToken(MiniGoParser.MOD, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_multiplicativeExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpr" ):
                return visitor.visitMultiplicativeExpr(self)
            else:
                return visitor.visitChildren(self)



    def multiplicativeExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.MultiplicativeExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_multiplicativeExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.unaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.MultiplicativeExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_multiplicativeExpr)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MUL) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 321
                    self.unaryExpr() 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def unaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExprContext,0)


        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def postfixExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PostfixExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = MiniGoParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_unaryExpr)
        try:
            self.state = 332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.match(MiniGoParser.NOT)
                self.state = 328
                self.unaryExpr()
                pass
            elif token in [MiniGoParser.MINUS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 329
                self.match(MiniGoParser.MINUS)
                self.state = 330
                self.unaryExpr()
                pass
            elif token in [MiniGoParser.BOOLEAN_LIT, MiniGoParser.KW_NIL, MiniGoParser.IDENTIFIER, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.INTEGER_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 331
                self.postfixExpr(0)
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


    class PostfixExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def postfixExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PostfixExprContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def dimension_list_in_var(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_list_in_varContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_val(self):
            return self.getTypedRuleContext(MiniGoParser.List_valContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_postfixExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPostfixExpr" ):
                return visitor.visitPostfixExpr(self)
            else:
                return visitor.visitChildren(self)



    def postfixExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.PostfixExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_postfixExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.primaryExpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 349
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.PostfixExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpr)
                        self.state = 337
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 338
                        self.match(MiniGoParser.DOT)
                        self.state = 339
                        self.match(MiniGoParser.IDENTIFIER)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.PostfixExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpr)
                        self.state = 340
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 341
                        self.dimension_list_in_var()
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.PostfixExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_postfixExpr)
                        self.state = 342
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 343
                        self.match(MiniGoParser.DOT)
                        self.state = 344
                        self.match(MiniGoParser.IDENTIFIER)
                        self.state = 345
                        self.match(MiniGoParser.LPAREN)
                        self.state = 346
                        self.list_val()
                        self.state = 347
                        self.match(MiniGoParser.RPAREN)
                        pass

             
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_values(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_valuesContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def arr_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_litContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpr(self):

        localctx = MiniGoParser.PrimaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_primaryExpr)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.primitive_values()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.match(MiniGoParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.func_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
                self.arr_lit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 358
                self.struct_lit()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 359
                self.match(MiniGoParser.LPAREN)
                self.state = 360
                self.expression()
                self.state = 361
                self.match(MiniGoParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_dec_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_dec_initContext,0)


        def var_dec_no_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_dec_no_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec" ):
                return visitor.visitVar_dec(self)
            else:
                return visitor.visitChildren(self)




    def var_dec(self):

        localctx = MiniGoParser.Var_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_var_dec)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.var_dec_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.var_dec_no_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dec_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(MiniGoParser.KW_VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_dec_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec_init" ):
                return visitor.visitVar_dec_init(self)
            else:
                return visitor.visitChildren(self)




    def var_dec_init(self):

        localctx = MiniGoParser.Var_dec_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_var_dec_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.match(MiniGoParser.KW_VAR)
            self.state = 370
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOL, MiniGoParser.IDENTIFIER, MiniGoParser.LBRACK]:
                self.state = 371
                self.all_types()
                pass
            elif token in [MiniGoParser.EQUAL]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 375
            self.match(MiniGoParser.EQUAL)
            self.state = 376
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_dec_no_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(MiniGoParser.KW_VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_var_dec_no_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_dec_no_init" ):
                return visitor.visitVar_dec_no_init(self)
            else:
                return visitor.visitChildren(self)




    def var_dec_no_init(self):

        localctx = MiniGoParser.Var_dec_no_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_dec_no_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(MiniGoParser.KW_VAR)
            self.state = 379
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 380
            self.all_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Const_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONST(self):
            return self.getToken(MiniGoParser.KW_CONST, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_const_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst_dec" ):
                return visitor.visitConst_dec(self)
            else:
                return visitor.visitChildren(self)




    def const_dec(self):

        localctx = MiniGoParser.Const_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_const_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(MiniGoParser.KW_CONST)
            self.state = 383
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 384
            self.match(MiniGoParser.EQUAL)
            self.state = 385
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(MiniGoParser.KW_FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_arguments(self):
            return self.getTypedRuleContext(MiniGoParser.List_argumentsContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_func_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_dec" ):
                return visitor.visitFunc_dec(self)
            else:
                return visitor.visitChildren(self)




    def func_dec(self):

        localctx = MiniGoParser.Func_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_func_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(MiniGoParser.KW_FUNC)
            self.state = 388
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 389
            self.match(MiniGoParser.LPAREN)
            self.state = 390
            self.list_arguments()
            self.state = 391
            self.match(MiniGoParser.RPAREN)
            self.state = 394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOL, MiniGoParser.IDENTIFIER, MiniGoParser.LBRACK]:
                self.state = 392
                self.all_types()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 396
            self.match(MiniGoParser.LBRACE)
            self.state = 397
            self.list_statement()
            self.state = 398
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_argumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_arg_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_arg_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_arguments

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_arguments" ):
                return visitor.visitList_arguments(self)
            else:
                return visitor.visitChildren(self)




    def list_arguments(self):

        localctx = MiniGoParser.List_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_list_arguments)
        try:
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.list_arg_prime()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

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


    class List_arg_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self):
            return self.getTypedRuleContext(MiniGoParser.ArgContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_arg_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_arg_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_arg_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_arg_prime" ):
                return visitor.visitList_arg_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_arg_prime(self):

        localctx = MiniGoParser.List_arg_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_list_arg_prime)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.arg()
                self.state = 405
                self.match(MiniGoParser.COMMA)
                self.state = 406
                self.list_arg_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.arg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Arg_primeContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arg

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg" ):
                return visitor.visitArg(self)
            else:
                return visitor.visitChildren(self)




    def arg(self):

        localctx = MiniGoParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.arg_prime()
            self.state = 412
            self.all_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def arg_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Arg_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arg_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArg_prime" ):
                return visitor.visitArg_prime(self)
            else:
                return visitor.visitChildren(self)




    def arg_prime(self):

        localctx = MiniGoParser.Arg_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_arg_prime)
        try:
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 414
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 415
                self.match(MiniGoParser.COMMA)
                self.state = 416
                self.arg_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(MiniGoParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_list_in_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_in_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_in_litContext,0)


        def dimension_list_in_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_list_in_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_list_in_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list_in_lit" ):
                return visitor.visitDimension_list_in_lit(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list_in_lit(self):

        localctx = MiniGoParser.Dimension_list_in_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_dimension_list_in_lit)
        try:
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.dimension_in_lit()
                self.state = 421
                self.dimension_list_in_lit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
                self.dimension_in_lit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_list_in_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_in_var(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_in_varContext,0)


        def dimension_list_in_var(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_list_in_varContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_list_in_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_list_in_var" ):
                return visitor.visitDimension_list_in_var(self)
            else:
                return visitor.visitChildren(self)




    def dimension_list_in_var(self):

        localctx = MiniGoParser.Dimension_list_in_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_dimension_list_in_var)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.dimension_in_var()
                self.state = 427
                self.dimension_list_in_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self.dimension_in_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_in_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def INTEGER_LIT(self):
            return self.getToken(MiniGoParser.INTEGER_LIT, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_in_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_in_lit" ):
                return visitor.visitDimension_in_lit(self)
            else:
                return visitor.visitChildren(self)




    def dimension_in_lit(self):

        localctx = MiniGoParser.Dimension_in_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_dimension_in_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(MiniGoParser.LBRACK)
            self.state = 433
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.INTEGER_LIT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 434
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dimension_in_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACK(self):
            return self.getToken(MiniGoParser.LBRACK, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RBRACK(self):
            return self.getToken(MiniGoParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimension_in_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension_in_var" ):
                return visitor.visitDimension_in_var(self)
            else:
                return visitor.visitChildren(self)




    def dimension_in_var(self):

        localctx = MiniGoParser.Dimension_in_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_dimension_in_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(MiniGoParser.LBRACK)
            self.state = 437
            self.expression()
            self.state = 438
            self.match(MiniGoParser.RBRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimension_list_in_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Dimension_list_in_litContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def nested_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nested_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_lit" ):
                return visitor.visitArr_lit(self)
            else:
                return visitor.visitChildren(self)




    def arr_lit(self):

        localctx = MiniGoParser.Arr_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_arr_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.dimension_list_in_lit()
            self.state = 441
            self.all_types()
            self.state = 442
            self.nested_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nested_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Element_listContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_nested_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNested_list" ):
                return visitor.visitNested_list(self)
            else:
                return visitor.visitChildren(self)




    def nested_list(self):

        localctx = MiniGoParser.Nested_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_nested_list)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.match(MiniGoParser.LBRACE)
                self.state = 445
                self.element_list()
                self.state = 446
                self.match(MiniGoParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.match(MiniGoParser.LBRACE)
                self.state = 449
                self.match(MiniGoParser.RBRACE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def element_list(self):
            return self.getTypedRuleContext(MiniGoParser.Element_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_list" ):
                return visitor.visitElement_list(self)
            else:
                return visitor.visitChildren(self)




    def element_list(self):

        localctx = MiniGoParser.Element_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_element_list)
        try:
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.element()
                self.state = 453
                self.match(MiniGoParser.COMMA)
                self.state = 454
                self.element_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nested_list(self):
            return self.getTypedRuleContext(MiniGoParser.Nested_listContext,0)


        def primitive_values(self):
            return self.getTypedRuleContext(MiniGoParser.Primitive_valuesContext,0)


        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_element)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.LBRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.nested_list()
                pass
            elif token in [MiniGoParser.BOOLEAN_LIT, MiniGoParser.KW_NIL, MiniGoParser.IDENTIFIER, MiniGoParser.INTEGER_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                if la_ == 1:
                    self.state = 460
                    self.primitive_values()
                    pass

                elif la_ == 2:
                    self.state = 461
                    self.struct_lit()
                    pass

                elif la_ == 3:
                    self.state = 462
                    self.match(MiniGoParser.IDENTIFIER)
                    pass


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


    class List_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_val" ):
                return visitor.visitList_val(self)
            else:
                return visitor.visitChildren(self)




    def list_val(self):

        localctx = MiniGoParser.List_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_list_val)
        try:
            self.state = 469
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.BOOLEAN_LIT, MiniGoParser.KW_NIL, MiniGoParser.IDENTIFIER, MiniGoParser.LPAREN, MiniGoParser.LBRACK, MiniGoParser.INTEGER_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.expression_prime()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

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


    class Expression_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def expression_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Expression_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expression_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_prime" ):
                return visitor.visitExpression_prime(self)
            else:
                return visitor.visitChildren(self)




    def expression_prime(self):

        localctx = MiniGoParser.Expression_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expression_prime)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                self.expression()
                self.state = 472
                self.match(MiniGoParser.COMMA)
                self.state = 473
                self.expression_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TYPE(self):
            return self.getToken(MiniGoParser.KW_TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def KW_STRUCT(self):
            return self.getToken(MiniGoParser.KW_STRUCT, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_field(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_def" ):
                return visitor.visitStruct_def(self)
            else:
                return visitor.visitChildren(self)




    def struct_def(self):

        localctx = MiniGoParser.Struct_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_struct_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(MiniGoParser.KW_TYPE)
            self.state = 479
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 480
            self.match(MiniGoParser.KW_STRUCT)
            self.state = 481
            self.match(MiniGoParser.LBRACE)
            self.state = 482
            self.list_field()
            self.state = 483
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_field(self):
            return self.getTypedRuleContext(MiniGoParser.List_fieldContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def field_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Field_decContext,0)


        def struct_method_def(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_method_defContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_field" ):
                return visitor.visitList_field(self)
            else:
                return visitor.visitChildren(self)




    def list_field(self):

        localctx = MiniGoParser.List_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_list_field)
        try:
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IDENTIFIER]:
                    self.state = 485
                    self.field_dec()
                    pass
                elif token in [MiniGoParser.KW_FUNC]:
                    self.state = 486
                    self.struct_method_def()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 489
                self.match(MiniGoParser.SEMICOLON)
                self.state = 491
                self.list_field()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.IDENTIFIER]:
                    self.state = 493
                    self.field_dec()
                    pass
                elif token in [MiniGoParser.KW_FUNC]:
                    self.state = 494
                    self.struct_method_def()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 497
                self.match(MiniGoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_dec" ):
                return visitor.visitField_dec(self)
            else:
                return visitor.visitChildren(self)




    def field_dec(self):

        localctx = MiniGoParser.Field_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_field_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 502
            self.all_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_field_init(self):
            return self.getTypedRuleContext(MiniGoParser.List_field_initContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_lit" ):
                return visitor.visitStruct_lit(self)
            else:
                return visitor.visitChildren(self)




    def struct_lit(self):

        localctx = MiniGoParser.Struct_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_struct_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 505
            self.match(MiniGoParser.LBRACE)
            self.state = 506
            self.list_field_init()
            self.state = 507
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_field_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_field_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_field_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_field_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_field_init" ):
                return visitor.visitList_field_init(self)
            else:
                return visitor.visitChildren(self)




    def list_field_init(self):

        localctx = MiniGoParser.List_field_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_list_field_init)
        try:
            self.state = 511
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.list_field_prime()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

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


    class List_field_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_init(self):
            return self.getTypedRuleContext(MiniGoParser.Field_initContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_field_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_field_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_field_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_field_prime" ):
                return visitor.visitList_field_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_field_prime(self):

        localctx = MiniGoParser.List_field_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_list_field_prime)
        try:
            self.state = 518
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
                self.field_init()
                self.state = 514
                self.match(MiniGoParser.COMMA)
                self.state = 515
                self.list_field_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.field_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_field_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField_init" ):
                return visitor.visitField_init(self)
            else:
                return visitor.visitChildren(self)




    def field_init(self):

        localctx = MiniGoParser.Field_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_field_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 521
            self.match(MiniGoParser.COLON)
            self.state = 522
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_method_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(MiniGoParser.KW_FUNC, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.LPAREN)
            else:
                return self.getToken(MiniGoParser.LPAREN, i)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.RPAREN)
            else:
                return self.getToken(MiniGoParser.RPAREN, i)

        def list_arguments(self):
            return self.getTypedRuleContext(MiniGoParser.List_argumentsContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_method_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_method_def" ):
                return visitor.visitStruct_method_def(self)
            else:
                return visitor.visitChildren(self)




    def struct_method_def(self):

        localctx = MiniGoParser.Struct_method_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_struct_method_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
            self.match(MiniGoParser.KW_FUNC)
            self.state = 525
            self.match(MiniGoParser.LPAREN)
            self.state = 526
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 527
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 528
            self.match(MiniGoParser.RPAREN)
            self.state = 529
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 530
            self.match(MiniGoParser.LPAREN)
            self.state = 531
            self.list_arguments()
            self.state = 532
            self.match(MiniGoParser.RPAREN)
            self.state = 535
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOL, MiniGoParser.IDENTIFIER, MiniGoParser.LBRACK]:
                self.state = 533
                self.all_types()
                pass
            elif token in [MiniGoParser.LBRACE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 537
            self.match(MiniGoParser.LBRACE)
            self.state = 538
            self.list_statement()
            self.state = 539
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interface_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TYPE(self):
            return self.getToken(MiniGoParser.KW_TYPE, 0)

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def KW_INTERFACE(self):
            return self.getToken(MiniGoParser.KW_INTERFACE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_method(self):
            return self.getTypedRuleContext(MiniGoParser.List_methodContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interface_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterface_dec" ):
                return visitor.visitInterface_dec(self)
            else:
                return visitor.visitChildren(self)




    def interface_dec(self):

        localctx = MiniGoParser.Interface_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_interface_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(MiniGoParser.KW_TYPE)
            self.state = 542
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 543
            self.match(MiniGoParser.KW_INTERFACE)
            self.state = 544
            self.match(MiniGoParser.LBRACE)
            self.state = 545
            self.list_method()
            self.state = 546
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_methodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_method_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_method" ):
                return visitor.visitList_method(self)
            else:
                return visitor.visitChildren(self)




    def list_method(self):

        localctx = MiniGoParser.List_methodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_list_method)
        try:
            self.state = 550
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.list_method_prime()
                pass
            elif token in [MiniGoParser.RBRACE]:
                self.enterOuterAlt(localctx, 2)

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


    class List_method_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_dec(self):
            return self.getTypedRuleContext(MiniGoParser.Method_decContext,0)


        def list_method_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_method_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_method_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_method_prime" ):
                return visitor.visitList_method_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_method_prime(self):

        localctx = MiniGoParser.List_method_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_list_method_prime)
        try:
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.method_dec()
                self.state = 553
                self.list_method_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
                self.method_dec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_decContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def list_prototypes(self):
            return self.getTypedRuleContext(MiniGoParser.List_prototypesContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_dec" ):
                return visitor.visitMethod_dec(self)
            else:
                return visitor.visitChildren(self)




    def method_dec(self):

        localctx = MiniGoParser.Method_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_method_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 559
            self.match(MiniGoParser.LPAREN)
            self.state = 560
            self.list_prototypes()
            self.state = 561
            self.match(MiniGoParser.RPAREN)
            self.state = 564
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.KW_STRING, MiniGoParser.KW_INT, MiniGoParser.KW_FLOAT, MiniGoParser.KW_BOOL, MiniGoParser.IDENTIFIER, MiniGoParser.LBRACK]:
                self.state = 562
                self.all_types()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 566
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_prototypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_prototypes_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_prototypes_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_prototypes

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_prototypes" ):
                return visitor.visitList_prototypes(self)
            else:
                return visitor.visitChildren(self)




    def list_prototypes(self):

        localctx = MiniGoParser.List_prototypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_list_prototypes)
        try:
            self.state = 570
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 568
                self.list_prototypes_prime()
                pass
            elif token in [MiniGoParser.RPAREN]:
                self.enterOuterAlt(localctx, 2)

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


    class List_prototypes_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prototype(self):
            return self.getTypedRuleContext(MiniGoParser.PrototypeContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def list_prototypes_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_prototypes_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_prototypes_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_prototypes_prime" ):
                return visitor.visitList_prototypes_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_prototypes_prime(self):

        localctx = MiniGoParser.List_prototypes_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_list_prototypes_prime)
        try:
            self.state = 577
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 572
                self.prototype()
                self.state = 573
                self.match(MiniGoParser.COMMA)
                self.state = 574
                self.list_prototypes_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 576
                self.prototype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrototypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prototype_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Prototype_primeContext,0)


        def all_types(self):
            return self.getTypedRuleContext(MiniGoParser.All_typesContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_prototype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototype" ):
                return visitor.visitPrototype(self)
            else:
                return visitor.visitChildren(self)




    def prototype(self):

        localctx = MiniGoParser.PrototypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_prototype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.prototype_prime()
            self.state = 580
            self.all_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prototype_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MiniGoParser.IDENTIFIER, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def prototype_prime(self):
            return self.getTypedRuleContext(MiniGoParser.Prototype_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_prototype_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrototype_prime" ):
                return visitor.visitPrototype_prime(self)
            else:
                return visitor.visitChildren(self)




    def prototype_prime(self):

        localctx = MiniGoParser.Prototype_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_prototype_prime)
        try:
            self.state = 586
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 582
                self.match(MiniGoParser.IDENTIFIER)
                self.state = 583
                self.match(MiniGoParser.COMMA)
                self.state = 584
                self.prototype_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 585
                self.match(MiniGoParser.IDENTIFIER)
                pass


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

        def all_var(self):
            return self.getTypedRuleContext(MiniGoParser.All_varContext,0)


        def assign_opp(self):
            return self.getTypedRuleContext(MiniGoParser.Assign_oppContext,0)


        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def arr_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_assignContext,0)


        def struct_assign(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_assignContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_assignment)
        try:
            self.state = 594
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 588
                self.all_var()
                self.state = 589
                self.assign_opp()
                self.state = 590
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 592
                self.arr_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 593
                self.struct_assign()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arr_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_var(self):
            return self.getTypedRuleContext(MiniGoParser.All_varContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def arr_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Arr_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arr_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArr_assign" ):
                return visitor.visitArr_assign(self)
            else:
                return visitor.visitChildren(self)




    def arr_assign(self):

        localctx = MiniGoParser.Arr_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_arr_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.all_var()
            self.state = 597
            self.match(MiniGoParser.ASSIGN)
            self.state = 598
            self.arr_lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def all_var(self):
            return self.getTypedRuleContext(MiniGoParser.All_varContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def struct_lit(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_litContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_assign" ):
                return visitor.visitStruct_assign(self)
            else:
                return visitor.visitChildren(self)




    def struct_assign(self):

        localctx = MiniGoParser.Struct_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_struct_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.all_var()
            self.state = 601
            self.match(MiniGoParser.ASSIGN)
            self.state = 602
            self.struct_lit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IF(self):
            return self.getToken(MiniGoParser.KW_IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def list_else_if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.List_else_if_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = MiniGoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.match(MiniGoParser.KW_IF)
            self.state = 605
            self.match(MiniGoParser.LPAREN)
            self.state = 606
            self.expression()
            self.state = 607
            self.match(MiniGoParser.RPAREN)
            self.state = 608
            self.match(MiniGoParser.LBRACE)
            self.state = 609
            self.list_statement()
            self.state = 610
            self.match(MiniGoParser.RBRACE)
            self.state = 611
            self.list_else_if_stmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_else_if_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_else_if_stmt_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_else_if_stmt_primeContext,0)


        def else_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_else_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_else_if_stmt" ):
                return visitor.visitList_else_if_stmt(self)
            else:
                return visitor.visitChildren(self)




    def list_else_if_stmt(self):

        localctx = MiniGoParser.List_else_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_list_else_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 613
            self.list_else_if_stmt_prime()
            self.state = 616
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.KW_ELSE]:
                self.state = 614
                self.else_stmt()
                pass
            elif token in [MiniGoParser.SEMICOLON]:
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


    class List_else_if_stmt_primeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def one_esle_if_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.One_esle_if_stmtContext,0)


        def list_else_if_stmt_prime(self):
            return self.getTypedRuleContext(MiniGoParser.List_else_if_stmt_primeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_list_else_if_stmt_prime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_else_if_stmt_prime" ):
                return visitor.visitList_else_if_stmt_prime(self)
            else:
                return visitor.visitChildren(self)




    def list_else_if_stmt_prime(self):

        localctx = MiniGoParser.List_else_if_stmt_primeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_list_else_if_stmt_prime)
        try:
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                self.one_esle_if_stmt()
                self.state = 619
                self.list_else_if_stmt_prime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class One_esle_if_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELSE(self):
            return self.getToken(MiniGoParser.KW_ELSE, 0)

        def KW_IF(self):
            return self.getToken(MiniGoParser.KW_IF, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_one_esle_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOne_esle_if_stmt" ):
                return visitor.visitOne_esle_if_stmt(self)
            else:
                return visitor.visitChildren(self)




    def one_esle_if_stmt(self):

        localctx = MiniGoParser.One_esle_if_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_one_esle_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 624
            self.match(MiniGoParser.KW_ELSE)
            self.state = 625
            self.match(MiniGoParser.KW_IF)
            self.state = 626
            self.match(MiniGoParser.LPAREN)
            self.state = 627
            self.expression()
            self.state = 628
            self.match(MiniGoParser.RPAREN)
            self.state = 629
            self.match(MiniGoParser.LBRACE)
            self.state = 630
            self.list_statement()
            self.state = 631
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ELSE(self):
            return self.getToken(MiniGoParser.KW_ELSE, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = MiniGoParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_else_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.match(MiniGoParser.KW_ELSE)
            self.state = 634
            self.match(MiniGoParser.LBRACE)
            self.state = 635
            self.list_statement()
            self.state = 636
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basic_for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Basic_for_stmtContext,0)


        def init_for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Init_for_stmtContext,0)


        def range_for_stmt(self):
            return self.getTypedRuleContext(MiniGoParser.Range_for_stmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = MiniGoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_for_stmt)
        try:
            self.state = 641
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 638
                self.basic_for_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 639
                self.init_for_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 640
                self.range_for_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Basic_for_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FOR(self):
            return self.getToken(MiniGoParser.KW_FOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basic_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasic_for_stmt" ):
                return visitor.visitBasic_for_stmt(self)
            else:
                return visitor.visitChildren(self)




    def basic_for_stmt(self):

        localctx = MiniGoParser.Basic_for_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_basic_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.match(MiniGoParser.KW_FOR)
            self.state = 644
            self.expression()
            self.state = 645
            self.match(MiniGoParser.LBRACE)
            self.state = 646
            self.list_statement()
            self.state = 647
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_for_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FOR(self):
            return self.getToken(MiniGoParser.KW_FOR, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.AssignmentContext,i)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def var_dec_init(self):
            return self.getTypedRuleContext(MiniGoParser.Var_dec_initContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_init_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_for_stmt" ):
                return visitor.visitInit_for_stmt(self)
            else:
                return visitor.visitChildren(self)




    def init_for_stmt(self):

        localctx = MiniGoParser.Init_for_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_init_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 649
            self.match(MiniGoParser.KW_FOR)
            self.state = 652
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IDENTIFIER]:
                self.state = 650
                self.assignment()
                pass
            elif token in [MiniGoParser.KW_VAR]:
                self.state = 651
                self.var_dec_init()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 654
            self.match(MiniGoParser.SEMICOLON)
            self.state = 655
            self.expression()
            self.state = 656
            self.match(MiniGoParser.SEMICOLON)
            self.state = 657
            self.assignment()
            self.state = 658
            self.match(MiniGoParser.LBRACE)
            self.state = 659
            self.list_statement()
            self.state = 660
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Range_for_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FOR(self):
            return self.getToken(MiniGoParser.KW_FOR, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.IDENTIFIER)
            else:
                return self.getToken(MiniGoParser.IDENTIFIER, i)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def KW_RANGE(self):
            return self.getToken(MiniGoParser.KW_RANGE, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def list_statement(self):
            return self.getTypedRuleContext(MiniGoParser.List_statementContext,0)


        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def UNDERLINE(self):
            return self.getToken(MiniGoParser.UNDERLINE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_range_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRange_for_stmt" ):
                return visitor.visitRange_for_stmt(self)
            else:
                return visitor.visitChildren(self)




    def range_for_stmt(self):

        localctx = MiniGoParser.Range_for_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_range_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 662
            self.match(MiniGoParser.KW_FOR)
            self.state = 663
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.IDENTIFIER or _la==MiniGoParser.UNDERLINE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 664
            self.match(MiniGoParser.COMMA)
            self.state = 665
            self.match(MiniGoParser.IDENTIFIER)
            self.state = 666
            self.match(MiniGoParser.ASSIGN)
            self.state = 667
            self.match(MiniGoParser.KW_RANGE)
            self.state = 668
            self.expression()
            self.state = 669
            self.match(MiniGoParser.LBRACE)
            self.state = 670
            self.list_statement()
            self.state = 671
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BREAK(self):
            return self.getToken(MiniGoParser.KW_BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = MiniGoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 673
            self.match(MiniGoParser.KW_BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONTINUE(self):
            return self.getToken(MiniGoParser.KW_CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = MiniGoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
            self.match(MiniGoParser.KW_CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(MiniGoParser.Func_callContext,0)


        def method_call(self):
            return self.getTypedRuleContext(MiniGoParser.Method_callContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = MiniGoParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_call_stmt)
        try:
            self.state = 679
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 677
                self.func_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 678
                self.method_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_RETURN(self):
            return self.getToken(MiniGoParser.KW_RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniGoParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = MiniGoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_return_stmt)
        try:
            self.state = 684
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 681
                self.match(MiniGoParser.KW_RETURN)
                self.state = 682
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 683
                self.match(MiniGoParser.KW_RETURN)
                pass


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
        self._predicates[7] = self.struct_arr_access_prime_sempred
        self._predicates[21] = self.logicalOrExpr_sempred
        self._predicates[22] = self.logicalAndExpr_sempred
        self._predicates[23] = self.equalityExpr_sempred
        self._predicates[24] = self.additiveExpr_sempred
        self._predicates[25] = self.multiplicativeExpr_sempred
        self._predicates[27] = self.postfixExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def struct_arr_access_prime_sempred(self, localctx:Struct_arr_access_primeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def logicalOrExpr_sempred(self, localctx:LogicalOrExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def logicalAndExpr_sempred(self, localctx:LogicalAndExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def equalityExpr_sempred(self, localctx:EqualityExprContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def additiveExpr_sempred(self, localctx:AdditiveExprContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def multiplicativeExpr_sempred(self, localctx:MultiplicativeExprContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def postfixExpr_sempred(self, localctx:PostfixExprContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 1)
         




