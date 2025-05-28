import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/minigo/parser/' in sys.path:
    sys.path.append('./main/minigo/parser/')
if not './main/minigo/astgen/' in sys.path:
    sys.path.append('./main/minigo/astgen/')
if not './main/minigo/checker/' in sys.path:
    sys.path.append('./main/minigo/checker/')
if not './main/minigo/codegen/' in sys.path:
    sys.path.append('./main/minigo/codegen/')
if os.path.isdir('../target/main/minigo/parser') and not '../target/main/minigo/parser/' in sys.path:
    sys.path.append('../target/main/minigo/parser/')
from MiniGoLexer import MiniGoLexer
from MiniGoParser import MiniGoParser
from lexererr import *
from ASTGeneration import ASTGeneration
from StaticCheck import StaticChecker
from StaticError import *
from CodeGenerator import CodeGenerator
import subprocess
import glob

JASMIN_JAR = "./external/jasmin.jar"
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
Lexer = MiniGoLexer
Parser = MiniGoParser


class TestCodeGen():
    @staticmethod
    def check(input_file):
        lexer = Lexer(FileStream(input_file))
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        checker = StaticChecker(asttree)
        try:
            checker.check()
        except StaticError as e:
            print("ERROR:", str(e))
            return
        
        codeGen = CodeGenerator()
        path = './bytecode'

        try:
            codeGen.gen(asttree, path)
            subprocess.call("java  -jar "+ JASMIN_JAR + " " + path + "/*.j",shell=True,stderr=subprocess.STDOUT)
            subprocess.run("java -cp .;lib MiniGoClass",shell=True, timeout=10)
        except StaticError as e:
            print(str(e))
        except subprocess.TimeoutExpired:
            print("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        finally:
            for jfile in glob.glob(os.path.join(path, "*.j")):
                try:
                    os.remove(jfile)
                except Exception as e:
                    print(f"Error deleting {jfile}: {e}")

            for class_file in glob.glob("*.class"):
                try:
                    os.remove(class_file)
                except Exception as e:
                    print(f"Error deleting {class_file}: {e}")
                        
            
    