# Generated from /home/ntr18/Documents/initial/src/main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u023a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\5")
        buf.write("\13\u0105\n\13\3\f\3\f\3\f\7\f\u010a\n\f\f\f\16\f\u010d")
        buf.write("\13\f\3\f\5\f\u0110\n\f\3\r\3\r\3\r\5\r\u0115\n\r\3\r")
        buf.write("\5\r\u0118\n\r\3\r\3\r\3\16\3\16\3\16\3\17\6\17\u0120")
        buf.write("\n\17\r\17\16\17\u0121\3\20\3\20\5\20\u0126\n\20\3\20")
        buf.write("\6\20\u0129\n\20\r\20\16\20\u012a\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\23\7\23\u0134\n\23\f\23\16\23\u0137\13\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)")
        buf.write("\3)\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3")
        buf.write("-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3")
        buf.write("\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\39\39\39\3:\3:\3:\3;\3;\3<\3<\3")
        buf.write("=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3")
        buf.write("F\3F\7F\u01fb\nF\fF\16F\u01fe\13F\3G\6G\u0201\nG\rG\16")
        buf.write("G\u0202\3G\3G\3H\3H\3H\3H\7H\u020b\nH\fH\16H\u020e\13")
        buf.write("H\3H\3H\3H\3H\3H\3I\3I\3I\3I\7I\u0219\nI\fI\16I\u021c")
        buf.write("\13I\3I\3I\3J\3J\3J\3K\3K\3K\7K\u0226\nK\fK\16K\u0229")
        buf.write("\13K\3K\3K\3K\3L\3L\3L\7L\u0231\nL\fL\16L\u0234\13L\3")
        buf.write("L\3L\3L\3M\3M\3\u020c\2N\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\2\35\2\37\2!\2#\2%\17\'")
        buf.write("\2)\2+\2-\20/\21\61\22\63\23\65\24\67\259\26;\27=\30?")
        buf.write("\31A\32C\33E\34G\35I\36K\37M O!Q\"S#U$W%Y&[\'](_)a*c+")
        buf.write("e,g-i.k/m\60o\61q\62s\63u\64w\65y\66{\67}8\1779\u0081")
        buf.write(":\u0083;\u0085<\u0087=\u0089>\u008b?\u008d@\u008fA\u0091")
        buf.write("B\u0093C\u0095D\u0097E\u0099\2\3\2\16\3\2\63;\4\2\62;")
        buf.write("aa\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$^^\n\2$$))^^ddhhp")
        buf.write("pttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\4\2")
        buf.write("\f\f\17\17\5\2$$))^^\2\u0242\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2%\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u009b")
        buf.write("\3\2\2\2\5\u00a5\3\2\2\2\7\u00ae\3\2\2\2\t\u00b9\3\2\2")
        buf.write("\2\13\u00c5\3\2\2\2\r\u00d2\3\2\2\2\17\u00df\3\2\2\2\21")
        buf.write("\u00eb\3\2\2\2\23\u00f1\3\2\2\2\25\u0104\3\2\2\2\27\u010f")
        buf.write("\3\2\2\2\31\u0111\3\2\2\2\33\u011b\3\2\2\2\35\u011f\3")
        buf.write("\2\2\2\37\u0123\3\2\2\2!\u012c\3\2\2\2#\u012e\3\2\2\2")
        buf.write("%\u0130\3\2\2\2\'\u013b\3\2\2\2)\u013d\3\2\2\2+\u013f")
        buf.write("\3\2\2\2-\u0142\3\2\2\2/\u0147\3\2\2\2\61\u014d\3\2\2")
        buf.write("\2\63\u0155\3\2\2\2\65\u0158\3\2\2\2\67\u015d\3\2\2\2")
        buf.write("9\u0163\3\2\2\2;\u0169\3\2\2\2=\u016d\3\2\2\2?\u0176\3")
        buf.write("\2\2\2A\u0179\3\2\2\2C\u0181\3\2\2\2E\u0188\3\2\2\2G\u018f")
        buf.write("\3\2\2\2I\u0194\3\2\2\2K\u0199\3\2\2\2M\u019f\3\2\2\2")
        buf.write("O\u01a3\3\2\2\2Q\u01ac\3\2\2\2S\u01af\3\2\2\2U\u01b7\3")
        buf.write("\2\2\2W\u01bd\3\2\2\2Y\u01bf\3\2\2\2[\u01c1\3\2\2\2]\u01c3")
        buf.write("\3\2\2\2_\u01c5\3\2\2\2a\u01c7\3\2\2\2c\u01c9\3\2\2\2")
        buf.write("e\u01cc\3\2\2\2g\u01cf\3\2\2\2i\u01d2\3\2\2\2k\u01d5\3")
        buf.write("\2\2\2m\u01d7\3\2\2\2o\u01da\3\2\2\2q\u01dc\3\2\2\2s\u01df")
        buf.write("\3\2\2\2u\u01e2\3\2\2\2w\u01e4\3\2\2\2y\u01e6\3\2\2\2")
        buf.write("{\u01e8\3\2\2\2}\u01ea\3\2\2\2\177\u01ec\3\2\2\2\u0081")
        buf.write("\u01ee\3\2\2\2\u0083\u01f0\3\2\2\2\u0085\u01f2\3\2\2\2")
        buf.write("\u0087\u01f4\3\2\2\2\u0089\u01f6\3\2\2\2\u008b\u01f8\3")
        buf.write("\2\2\2\u008d\u0200\3\2\2\2\u008f\u0206\3\2\2\2\u0091\u0214")
        buf.write("\3\2\2\2\u0093\u021f\3\2\2\2\u0095\u0222\3\2\2\2\u0097")
        buf.write("\u022d\3\2\2\2\u0099\u0238\3\2\2\2\u009b\u009c\7t\2\2")
        buf.write("\u009c\u009d\7g\2\2\u009d\u009e\7c\2\2\u009e\u009f\7f")
        buf.write("\2\2\u009f\u00a0\7K\2\2\u00a0\u00a1\7p\2\2\u00a1\u00a2")
        buf.write("\7v\2\2\u00a2\u00a3\7*\2\2\u00a3\u00a4\7+\2\2\u00a4\4")
        buf.write("\3\2\2\2\u00a5\u00a6\7r\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8")
        buf.write("\7k\2\2\u00a8\u00a9\7p\2\2\u00a9\u00aa\7v\2\2\u00aa\u00ab")
        buf.write("\7K\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad\7v\2\2\u00ad\6")
        buf.write("\3\2\2\2\u00ae\u00af\7y\2\2\u00af\u00b0\7t\2\2\u00b0\u00b1")
        buf.write("\7k\2\2\u00b1\u00b2\7v\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4")
        buf.write("\7H\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6\7q\2\2\u00b6\u00b7")
        buf.write("\7c\2\2\u00b7\u00b8\7v\2\2\u00b8\b\3\2\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7c\2\2\u00bc\u00bd")
        buf.write("\7f\2\2\u00bd\u00be\7H\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7c\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7*\2\2\u00c3\u00c4\7+\2\2\u00c4\n\3\2\2\2\u00c5\u00c6")
        buf.write("\7r\2\2\u00c6\u00c7\7t\2\2\u00c7\u00c8\7k\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\u00ca\7v\2\2\u00ca\u00cb\7D\2\2\u00cb\u00cc")
        buf.write("\7q\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7n\2\2\u00ce\u00cf")
        buf.write("\7g\2\2\u00cf\u00d0\7c\2\2\u00d0\u00d1\7p\2\2\u00d1\f")
        buf.write("\3\2\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7g\2\2\u00d4\u00d5")
        buf.write("\7c\2\2\u00d5\u00d6\7f\2\2\u00d6\u00d7\7U\2\2\u00d7\u00d8")
        buf.write("\7v\2\2\u00d8\u00d9\7t\2\2\u00d9\u00da\7k\2\2\u00da\u00db")
        buf.write("\7p\2\2\u00db\u00dc\7i\2\2\u00dc\u00dd\7*\2\2\u00dd\u00de")
        buf.write("\7+\2\2\u00de\16\3\2\2\2\u00df\u00e0\7r\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7k\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4")
        buf.write("\7v\2\2\u00e4\u00e5\7U\2\2\u00e5\u00e6\7v\2\2\u00e6\u00e7")
        buf.write("\7t\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7i\2\2\u00ea\20\3\2\2\2\u00eb\u00ec\7u\2\2\u00ec\u00ed")
        buf.write("\7w\2\2\u00ed\u00ee\7r\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0")
        buf.write("\7t\2\2\u00f0\22\3\2\2\2\u00f1\u00f2\7r\2\2\u00f2\u00f3")
        buf.write("\7t\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5\7x\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9")
        buf.write("\7F\2\2\u00f9\u00fa\7g\2\2\u00fa\u00fb\7h\2\2\u00fb\u00fc")
        buf.write("\7c\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7n\2\2\u00fe\u00ff")
        buf.write("\7v\2\2\u00ff\u0100\7*\2\2\u0100\u0101\7+\2\2\u0101\24")
        buf.write("\3\2\2\2\u0102\u0105\5G$\2\u0103\u0105\5\67\34\2\u0104")
        buf.write("\u0102\3\2\2\2\u0104\u0103\3\2\2\2\u0105\26\3\2\2\2\u0106")
        buf.write("\u0110\7\62\2\2\u0107\u010b\t\2\2\2\u0108\u010a\t\3\2")
        buf.write("\2\u0109\u0108\3\2\2\2\u010a\u010d\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010e\3\2\2\2\u010d")
        buf.write("\u010b\3\2\2\2\u010e\u0110\b\f\2\2\u010f\u0106\3\2\2\2")
        buf.write("\u010f\u0107\3\2\2\2\u0110\30\3\2\2\2\u0111\u0117\5\27")
        buf.write("\f\2\u0112\u0118\5\33\16\2\u0113\u0115\5\33\16\2\u0114")
        buf.write("\u0113\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\u0118\5\37\20\2\u0117\u0112\3\2\2\2\u0117\u0114")
        buf.write("\3\2\2\2\u0118\u0119\3\2\2\2\u0119\u011a\b\r\3\2\u011a")
        buf.write("\32\3\2\2\2\u011b\u011c\5\u0089E\2\u011c\u011d\5\35\17")
        buf.write("\2\u011d\34\3\2\2\2\u011e\u0120\t\4\2\2\u011f\u011e\3")
        buf.write("\2\2\2\u0120\u0121\3\2\2\2\u0121\u011f\3\2\2\2\u0121\u0122")
        buf.write("\3\2\2\2\u0122\36\3\2\2\2\u0123\u0125\5!\21\2\u0124\u0126")
        buf.write("\5#\22\2\u0125\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0128\3\2\2\2\u0127\u0129\5\35\17\2\u0128\u0127\3\2\2")
        buf.write("\2\u0129\u012a\3\2\2\2\u012a\u0128\3\2\2\2\u012a\u012b")
        buf.write("\3\2\2\2\u012b \3\2\2\2\u012c\u012d\t\5\2\2\u012d\"\3")
        buf.write("\2\2\2\u012e\u012f\t\6\2\2\u012f$\3\2\2\2\u0130\u0135")
        buf.write("\5)\25\2\u0131\u0134\5+\26\2\u0132\u0134\5\'\24\2\u0133")
        buf.write("\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134\u0137\3\2\2\2")
        buf.write("\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\u0138\3")
        buf.write("\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139\5)\25\2\u0139\u013a")
        buf.write("\b\23\4\2\u013a&\3\2\2\2\u013b\u013c\n\7\2\2\u013c(\3")
        buf.write("\2\2\2\u013d\u013e\7$\2\2\u013e*\3\2\2\2\u013f\u0140\7")
        buf.write("^\2\2\u0140\u0141\t\b\2\2\u0141,\3\2\2\2\u0142\u0143\7")
        buf.write("c\2\2\u0143\u0144\7w\2\2\u0144\u0145\7v\2\2\u0145\u0146")
        buf.write("\7q\2\2\u0146.\3\2\2\2\u0147\u0148\7d\2\2\u0148\u0149")
        buf.write("\7t\2\2\u0149\u014a\7g\2\2\u014a\u014b\7c\2\2\u014b\u014c")
        buf.write("\7m\2\2\u014c\60\3\2\2\2\u014d\u014e\7d\2\2\u014e\u014f")
        buf.write("\7q\2\2\u014f\u0150\7q\2\2\u0150\u0151\7n\2\2\u0151\u0152")
        buf.write("\7g\2\2\u0152\u0153\7c\2\2\u0153\u0154\7p\2\2\u0154\62")
        buf.write("\3\2\2\2\u0155\u0156\7f\2\2\u0156\u0157\7q\2\2\u0157\64")
        buf.write("\3\2\2\2\u0158\u0159\7g\2\2\u0159\u015a\7n\2\2\u015a\u015b")
        buf.write("\7u\2\2\u015b\u015c\7g\2\2\u015c\66\3\2\2\2\u015d\u015e")
        buf.write("\7h\2\2\u015e\u015f\7c\2\2\u015f\u0160\7n\2\2\u0160\u0161")
        buf.write("\7u\2\2\u0161\u0162\7g\2\2\u01628\3\2\2\2\u0163\u0164")
        buf.write("\7h\2\2\u0164\u0165\7n\2\2\u0165\u0166\7q\2\2\u0166\u0167")
        buf.write("\7c\2\2\u0167\u0168\7v\2\2\u0168:\3\2\2\2\u0169\u016a")
        buf.write("\7h\2\2\u016a\u016b\7q\2\2\u016b\u016c\7t\2\2\u016c<\3")
        buf.write("\2\2\2\u016d\u016e\7h\2\2\u016e\u016f\7w\2\2\u016f\u0170")
        buf.write("\7p\2\2\u0170\u0171\7e\2\2\u0171\u0172\7v\2\2\u0172\u0173")
        buf.write("\7k\2\2\u0173\u0174\7q\2\2\u0174\u0175\7p\2\2\u0175>\3")
        buf.write("\2\2\2\u0176\u0177\7k\2\2\u0177\u0178\7h\2\2\u0178@\3")
        buf.write("\2\2\2\u0179\u017a\7k\2\2\u017a\u017b\7p\2\2\u017b\u017c")
        buf.write("\7v\2\2\u017c\u017d\7g\2\2\u017d\u017e\7i\2\2\u017e\u017f")
        buf.write("\7g\2\2\u017f\u0180\7t\2\2\u0180B\3\2\2\2\u0181\u0182")
        buf.write("\7t\2\2\u0182\u0183\7g\2\2\u0183\u0184\7v\2\2\u0184\u0185")
        buf.write("\7w\2\2\u0185\u0186\7t\2\2\u0186\u0187\7p\2\2\u0187D\3")
        buf.write("\2\2\2\u0188\u0189\7u\2\2\u0189\u018a\7v\2\2\u018a\u018b")
        buf.write("\7t\2\2\u018b\u018c\7k\2\2\u018c\u018d\7p\2\2\u018d\u018e")
        buf.write("\7i\2\2\u018eF\3\2\2\2\u018f\u0190\7v\2\2\u0190\u0191")
        buf.write("\7t\2\2\u0191\u0192\7w\2\2\u0192\u0193\7g\2\2\u0193H\3")
        buf.write("\2\2\2\u0194\u0195\7x\2\2\u0195\u0196\7q\2\2\u0196\u0197")
        buf.write("\7k\2\2\u0197\u0198\7f\2\2\u0198J\3\2\2\2\u0199\u019a")
        buf.write("\7y\2\2\u019a\u019b\7j\2\2\u019b\u019c\7k\2\2\u019c\u019d")
        buf.write("\7n\2\2\u019d\u019e\7g\2\2\u019eL\3\2\2\2\u019f\u01a0")
        buf.write("\7q\2\2\u01a0\u01a1\7w\2\2\u01a1\u01a2\7v\2\2\u01a2N\3")
        buf.write("\2\2\2\u01a3\u01a4\7e\2\2\u01a4\u01a5\7q\2\2\u01a5\u01a6")
        buf.write("\7p\2\2\u01a6\u01a7\7v\2\2\u01a7\u01a8\7k\2\2\u01a8\u01a9")
        buf.write("\7p\2\2\u01a9\u01aa\7w\2\2\u01aa\u01ab\7g\2\2\u01abP\3")
        buf.write("\2\2\2\u01ac\u01ad\7q\2\2\u01ad\u01ae\7h\2\2\u01aeR\3")
        buf.write("\2\2\2\u01af\u01b0\7k\2\2\u01b0\u01b1\7p\2\2\u01b1\u01b2")
        buf.write("\7j\2\2\u01b2\u01b3\7g\2\2\u01b3\u01b4\7t\2\2\u01b4\u01b5")
        buf.write("\7k\2\2\u01b5\u01b6\7v\2\2\u01b6T\3\2\2\2\u01b7\u01b8")
        buf.write("\7c\2\2\u01b8\u01b9\7t\2\2\u01b9\u01ba\7t\2\2\u01ba\u01bb")
        buf.write("\7c\2\2\u01bb\u01bc\7{\2\2\u01bcV\3\2\2\2\u01bd\u01be")
        buf.write("\7-\2\2\u01beX\3\2\2\2\u01bf\u01c0\7/\2\2\u01c0Z\3\2\2")
        buf.write("\2\u01c1\u01c2\7,\2\2\u01c2\\\3\2\2\2\u01c3\u01c4\7\61")
        buf.write("\2\2\u01c4^\3\2\2\2\u01c5\u01c6\7\'\2\2\u01c6`\3\2\2\2")
        buf.write("\u01c7\u01c8\7#\2\2\u01c8b\3\2\2\2\u01c9\u01ca\7(\2\2")
        buf.write("\u01ca\u01cb\7(\2\2\u01cbd\3\2\2\2\u01cc\u01cd\7~\2\2")
        buf.write("\u01cd\u01ce\7~\2\2\u01cef\3\2\2\2\u01cf\u01d0\7?\2\2")
        buf.write("\u01d0\u01d1\7?\2\2\u01d1h\3\2\2\2\u01d2\u01d3\7#\2\2")
        buf.write("\u01d3\u01d4\7?\2\2\u01d4j\3\2\2\2\u01d5\u01d6\7>\2\2")
        buf.write("\u01d6l\3\2\2\2\u01d7\u01d8\7>\2\2\u01d8\u01d9\7?\2\2")
        buf.write("\u01d9n\3\2\2\2\u01da\u01db\7@\2\2\u01dbp\3\2\2\2\u01dc")
        buf.write("\u01dd\7@\2\2\u01dd\u01de\7?\2\2\u01der\3\2\2\2\u01df")
        buf.write("\u01e0\7<\2\2\u01e0\u01e1\7<\2\2\u01e1t\3\2\2\2\u01e2")
        buf.write("\u01e3\7*\2\2\u01e3v\3\2\2\2\u01e4\u01e5\7+\2\2\u01e5")
        buf.write("x\3\2\2\2\u01e6\u01e7\7]\2\2\u01e7z\3\2\2\2\u01e8\u01e9")
        buf.write("\7_\2\2\u01e9|\3\2\2\2\u01ea\u01eb\7.\2\2\u01eb~\3\2\2")
        buf.write("\2\u01ec\u01ed\7<\2\2\u01ed\u0080\3\2\2\2\u01ee\u01ef")
        buf.write("\7=\2\2\u01ef\u0082\3\2\2\2\u01f0\u01f1\7}\2\2\u01f1\u0084")
        buf.write("\3\2\2\2\u01f2\u01f3\7\177\2\2\u01f3\u0086\3\2\2\2\u01f4")
        buf.write("\u01f5\7?\2\2\u01f5\u0088\3\2\2\2\u01f6\u01f7\7\60\2\2")
        buf.write("\u01f7\u008a\3\2\2\2\u01f8\u01fc\t\t\2\2\u01f9\u01fb\t")
        buf.write("\n\2\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa")
        buf.write("\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u008c\3\2\2\2\u01fe")
        buf.write("\u01fc\3\2\2\2\u01ff\u0201\t\13\2\2\u0200\u01ff\3\2\2")
        buf.write("\2\u0201\u0202\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\bG\5\2\u0205")
        buf.write("\u008e\3\2\2\2\u0206\u0207\7\61\2\2\u0207\u0208\7,\2\2")
        buf.write("\u0208\u020c\3\2\2\2\u0209\u020b\13\2\2\2\u020a\u0209")
        buf.write("\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020d\3\2\2\2\u020c")
        buf.write("\u020a\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020c\3\2\2\2")
        buf.write("\u020f\u0210\7,\2\2\u0210\u0211\7\61\2\2\u0211\u0212\3")
        buf.write("\2\2\2\u0212\u0213\bH\5\2\u0213\u0090\3\2\2\2\u0214\u0215")
        buf.write("\7\61\2\2\u0215\u0216\7\61\2\2\u0216\u021a\3\2\2\2\u0217")
        buf.write("\u0219\n\f\2\2\u0218\u0217\3\2\2\2\u0219\u021c\3\2\2\2")
        buf.write("\u021a\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021d\3")
        buf.write("\2\2\2\u021c\u021a\3\2\2\2\u021d\u021e\bI\5\2\u021e\u0092")
        buf.write("\3\2\2\2\u021f\u0220\13\2\2\2\u0220\u0221\bJ\6\2\u0221")
        buf.write("\u0094\3\2\2\2\u0222\u0227\7$\2\2\u0223\u0226\5+\26\2")
        buf.write("\u0224\u0226\5\'\24\2\u0225\u0223\3\2\2\2\u0225\u0224")
        buf.write("\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2")
        buf.write("\u022a\u022b\7\2\2\3\u022b\u022c\bK\7\2\u022c\u0096\3")
        buf.write("\2\2\2\u022d\u0232\7$\2\2\u022e\u0231\5+\26\2\u022f\u0231")
        buf.write("\5\'\24\2\u0230\u022e\3\2\2\2\u0230\u022f\3\2\2\2\u0231")
        buf.write("\u0234\3\2\2\2\u0232\u0230\3\2\2\2\u0232\u0233\3\2\2\2")
        buf.write("\u0233\u0235\3\2\2\2\u0234\u0232\3\2\2\2\u0235\u0236\5")
        buf.write("\u0099M\2\u0236\u0237\bL\b\2\u0237\u0098\3\2\2\2\u0238")
        buf.write("\u0239\t\r\2\2\u0239\u009a\3\2\2\2\25\2\u0104\u010b\u010f")
        buf.write("\u0114\u0117\u0121\u0125\u012a\u0133\u0135\u01fc\u0202")
        buf.write("\u020c\u021a\u0225\u0227\u0230\u0232\t\3\f\2\3\r\3\3\23")
        buf.write("\4\b\2\2\3J\5\3K\6\3L\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

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
    BooleanLiteral = 10
    IntegerLiteral = 11
    FloatLiteral = 12
    StringLiteral = 13
    AUTO = 14
    BREAK = 15
    BOOLEAN = 16
    DO = 17
    ELSE = 18
    FALSE = 19
    FLOAT = 20
    FOR = 21
    FUNCTION = 22
    IF = 23
    INTEGER = 24
    RETURN = 25
    STRING = 26
    TRUE = 27
    VOID = 28
    WHILE = 29
    OUT = 30
    CONTINUE = 31
    OF = 32
    INHERIT = 33
    ARRAY = 34
    Plus = 35
    Minus = 36
    Multiple = 37
    Division = 38
    Remain = 39
    Negation = 40
    And = 41
    Or = 42
    Equal = 43
    NotEqual = 44
    Less = 45
    LessEqual = 46
    Greater = 47
    GreaterEqual = 48
    CONCATENATE = 49
    LP = 50
    RP = 51
    LSB = 52
    RSB = 53
    COMMA = 54
    COLON = 55
    SEMICOLON = 56
    LCB = 57
    RCB = 58
    ASSIGN = 59
    DOT = 60
    Identifier = 61
    WS = 62
    BlockComment = 63
    LineComment = 64
    ERROR_CHAR = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'readInt()'", "'printInt'", "'writeFloat'", "'readFloat()'", 
            "'printBoolean'", "'readString()'", "'printString'", "'super'", 
            "'preventDefault()'", "'auto'", "'break'", "'boolean'", "'do'", 
            "'else'", "'false'", "'float'", "'for'", "'function'", "'if'", 
            "'integer'", "'return'", "'string'", "'true'", "'void'", "'while'", 
            "'out'", "'continue'", "'of'", "'inherit'", "'array'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'<'", "'<='", "'>'", "'>='", "'::'", "'('", "')'", "'['", "']'", 
            "','", "':'", "';'", "'{'", "'}'", "'='", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BooleanLiteral", "IntegerLiteral", "FloatLiteral", "StringLiteral", 
            "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", "FLOAT", 
            "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", "STRING", "TRUE", 
            "VOID", "WHILE", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "Plus", "Minus", "Multiple", "Division", "Remain", "Negation", 
            "And", "Or", "Equal", "NotEqual", "Less", "LessEqual", "Greater", 
            "GreaterEqual", "CONCATENATE", "LP", "RP", "LSB", "RSB", "COMMA", 
            "COLON", "SEMICOLON", "LCB", "RCB", "ASSIGN", "DOT", "Identifier", 
            "WS", "BlockComment", "LineComment", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "BooleanLiteral", "IntegerLiteral", "FloatLiteral", 
                  "Decimal", "DIGIT", "Exponent", "EXPONENT", "SIGN", "StringLiteral", 
                  "Char", "DOUBLEQUOTE", "ESC", "AUTO", "BREAK", "BOOLEAN", 
                  "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", 
                  "INTEGER", "RETURN", "STRING", "TRUE", "VOID", "WHILE", 
                  "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", "Plus", "Minus", 
                  "Multiple", "Division", "Remain", "Negation", "And", "Or", 
                  "Equal", "NotEqual", "Less", "LessEqual", "Greater", "GreaterEqual", 
                  "CONCATENATE", "LP", "RP", "LSB", "RSB", "COMMA", "COLON", 
                  "SEMICOLON", "LCB", "RCB", "ASSIGN", "DOT", "Identifier", 
                  "WS", "BlockComment", "LineComment", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[10] = self.IntegerLiteral_action 
            actions[11] = self.FloatLiteral_action 
            actions[17] = self.StringLiteral_action 
            actions[72] = self.ERROR_CHAR_action 
            actions[73] = self.UNCLOSE_STRING_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def IntegerLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace('_','') 
     

    def FloatLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             self.text = self.text.replace('_','') 
     

    def StringLiteral_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            	
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     


