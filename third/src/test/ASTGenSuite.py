import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_short_vardecl(self):
        input = """x: integer;"""
        expect = str(Program([VarDecl("x", IntegerType())]))
        self.assertTrue(TestAST.test(input, expect, 300))

    def test_full_vardecl(self):
        input = """x, y, z: integer = 1, 2, 3;"""
        expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_vardecls(self):
        input = """x, y, z: integer = 1, 2, 3;
            a: float;
            b: auto = 1;
            c: array [3, 2] of integer;
            
            foo: function integer(a: integer){}
            fact: function float(b: float, inherit c: string) inherit foo{}
            main: function void(){
                super(a, b, c);
            }"""
        expect = """"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_simple_program(self):
        """Simple program"""
        input = """foo: function integer(a: integer){
                a: float;
            }
            
            main: function void(){
                a: float;
                if(1) x = 1;
                else x = 2;
            }"""
        expect = """"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_more_complex_program(self):
        """More complex program"""
        input = """foo: function integer(a: integer){
                if (a == 1) return 1;
                else return 0.5;
            }
            
            main: function void(){
                a: float;
                if(1) x = 1;
                else x = 2;
            }"""
        expect = """"""
        self.assertTrue(TestAST.test(input, expect, 304))
    
    def test_more_complex_program(self):
        """More complex program"""
        input = """            
            arr : array [3, 2] of integer = {{{1}, {2}}, {{2}, {3}}, {{3}, {3, 3}}} ;
            """
        expect = """"""
        self.assertTrue(TestAST.test(input, expect, 305))

