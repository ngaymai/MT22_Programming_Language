import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    # def test_lowercase_identifier(self):
    #     input = """
    #         x, y, z: integer = 2.3, 2, 3;
    #         a: float;
    #         b: auto = 1;
    #         c: array [3, 2] of integer;            
    #         foo: function integer(a: integer){
            
    #         }
    #         fact: function float(b: float, inherit c: string) inherit foo{  
                  
    #         }
    #         main: function void(){
    #             t: integer = "1";
    #             c = {
    #                 {1,2}, 3, {5,6}      
    #             };
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_lowercase_identifier(self):
    #     input = """
    #         x, y, z: integer = 1, 2, 3;
    #         a: float;
    #         b: auto = 1;
    #         c: array [3, 2] of integer;            
    #         foo: function integer(a: integer){
            
    #         }
    #         fact: function float(b: float, inherit c: string) inherit foo{  
                  
    #         }
    #         main: function void(){
    #             if(1) x = 1;
    #             else x = 2;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test_lowercase_identifier(self):
    #     input = """                        
    #         foo: function integer(a: integer){
    #             a: float;
    #         }
            
    #         main: function void(){
    #             a: float;
    #             if(1) x = 1;
    #             else x = 2;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test_lowercase_identifier(self):
    #     input = """                        
    #         foo: function integer(a: integer){
    #             if (a == 1) return 1;
    #             else return 0.5;
    #         }
            
    #         main: function void(){
    #             a: float;
    #             if(1) x = 1;
    #             else x = 2;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 404))
    
    # def test_lowercase_identifier(self):
    #     input = """                        
    #         foo: function auto(a: integer){
    #             if (a == 1) return 1;
    #             else return 0.5;
    #         }
            
    #         main: function void(){
    #             a: float;
    #             if(1) x = 1;
    #             else x = 2;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_lowercase_identifier(self):
    #     input = """         
    #         main: function void(){
    #             a: float = 1;
    #             a = a + 1;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 406))
    
    # def test_lowercase_identifier(self):
    #     input = """         
    #         main: function void(){
    #             a: float = 1;
    #             a = 1 + 2 * 3;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test_lowercase_identifier(self):
    #     input = """         
    #         main: function void(){
    #             a: float = 1;
    #             b: integer;

    #             a = b + 3;
    #             a = 1 + 2 * 3;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test_lowercase_identifier(self):
    #     input = """         
    #         main: function void(){
    #             a: float = 1;
    #             b: integer;

    #             a = b + 3;
    #             a = 1 + 2 * 3;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    
    # def test_lowercase_identifier(self):
    #     input = """         
    #         main: function void(){
    #             a: float = 1;
    #             b: integer;
                
    #             a = b + 3;
    #             a = 1 + 2 * 3;
    #             b = 2 + 3 * 4 / 5 - 5/3;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    
    # def test_lowercase_identifier(self):
    #     input = """         
    #         main: function void(){
    #             a: boolean = true;
    #             b: boolean = !a;
    #         }
    #             """
    #     expect = """"""
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    

    # def test1(self):
    #     input = """x : integer ; y : integer ; """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test2(self):
    #     input = """x : integer = y ; y : integer = 2 ;"""
    #     expect = "Undeclared Identifier: y"
    #     self.assertTrue(TestChecker.test(input, expect, 402))

    # def test3(self):
    #     input = """x : auto ;"""
    #     expect = "Invalid Variable: x"
    #     self.assertTrue(TestChecker.test(input, expect, 403))

    # def test4(self):
    #     input = """x, y, z : string = "abd", "eex", 5 ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(z, StringType, IntegerLit(5))"
    #     self.assertTrue(TestChecker.test(input, expect, 404))

    # def test5(self):
    #     input = """x, y : integer = 2, x ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test6(self):
    #     input = """x : string = 22 ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(x, StringType, IntegerLit(22))"
    #     self.assertTrue(TestChecker.test(input, expect, 406))

    # def test7(self):
    #     input = """x, y : string = "22", z ;"""
    #     expect = "Undeclared Identifier: z"
    #     self.assertTrue(TestChecker.test(input, expect, 407))

    # def test8(self):
    #     input = """a, b, c, d, e : integer = 2, a, b, c, d ; x, y, z : float = a, b, c ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 408))

    # def test9(self):
    #     input = """a : string ; b : string = a ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 409))

    # def test10(self):
    #     input = """a : integer = 1 + 1.2 ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, IntegerLit(1), FloatLit(1.2)))"
    #     self.assertTrue(TestChecker.test(input, expect, 410))

    # def test11(self):
    #     input = """a : float = 1 + 1.2 ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 411))

    # def test12(self):
    #     input = """a : integer = 1.93 + 1.2 ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, FloatLit(1.93), FloatLit(1.2)))"
    #     self.assertTrue(TestChecker.test(input, expect, 412))

    # def test13(self):
    #     input = """a : integer = 1 + 2 + 3 ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 413))

    # def test14(self):
    #     input = """a : integer = 1 + 2 + 3.3 ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, BinExpr(+, IntegerLit(1), IntegerLit(2)), FloatLit(3.3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 414))

    # def test15(self):
    #     input = """a : integer = 1 + 2.2 + 3 ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, BinExpr(+, IntegerLit(1), FloatLit(2.2)), IntegerLit(3)))"
    #     self.assertTrue(TestChecker.test(input, expect, 415))

    # # def test16(self):
    # #     input = """a : integer = 1 + true ;"""
    # #     expect = "Type mismatch in expression: BooleanLit(True)"
    # #     self.assertTrue(TestChecker.test(input, expect, 416))

    # def test17(self):
    #     input = """a : integer = 1 + 0.9 ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(+, IntegerLit(1), FloatLit(0.9)))"
    #     self.assertTrue(TestChecker.test(input, expect, 417))

    # def test18(self):
    #     input = """a : integer = 8 % 3 ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 418))

    # # def test19(self):
    # #     input = """a : integer = 8 % 2.3 ;"""
    # #     expect = "Type mismatch in expression: FloatLit(2.3)"
    # #     self.assertTrue(TestChecker.test(input, expect, 419))

    # # def test21(self):
    # #     input = """a : boolean = true || false || 2 ;"""
    # #     expect = "Type mismatch in expression: IntegerLit(2)"
    # #     self.assertTrue(TestChecker.test(input, expect, 421))

    # def test22(self):
    #     input = """a : string = true || false || true ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, BinExpr(||, BinExpr(||, BooleanLit(True), BooleanLit(False)), BooleanLit(True)))"
    #     self.assertTrue(TestChecker.test(input, expect, 422))

    # def test24(self):
    #     input = """a, b, c : integer ; d : float = a + b + c ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 424))

    # # def test25(self):
    # #     input = """a, b : integer ; c : string ; d : float = a + b + c ;"""
    # #     expect = "Type mismatch in expression: Id(c)"
    # #     self.assertTrue(TestChecker.test(input, expect, 425))

    # # def test26(self):
    # #     input = """c, b : float ; a : boolean = c == b ;"""
    # #     expect = "Type mismatch in expression: BinExpr(==, Id(c), Id(b))"
    # #     self.assertTrue(TestChecker.test(input, expect, 426))

    # def test27(self):
    #     input = """ a : integer = 2 == 6 ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(==, IntegerLit(2), IntegerLit(6)))"
    #     self.assertTrue(TestChecker.test(input, expect, 427))

    # def test28(self):
    #     input = """ a : boolean = 2 != false ;"""
    #     expect = "Type mismatch in expression: BinExpr(!=, IntegerLit(2), BooleanLit(False))"
    #     self.assertTrue(TestChecker.test(input, expect, 428))

    # def test29(self):
    #     input = """ a : boolean = 3 >= 3.4 ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 429))

    # def test30(self):
    #     input = """ b : float ; a : boolean = 3 >= b ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 430))

    # # def test31(self):
    # #     input = """ b : string ; a : boolean = 3 >= b ;"""
    # #     expect = "Type mismatch in expression: Id(b)"
    # #     self.assertTrue(TestChecker.test(input, expect, 431))

    # def test32(self):
    #     input = """ a : string = "2" :: "33" ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 432))

    # def test33(self):
    #     input = """ x : string = "223232" ; a : string = "2" :: x ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 433))

    # def test34(self):
    #     input = """ x : float = -2.5554 ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 434))

    # def test35(self):
    #     input = """ x : float = -2.5554 + 3 + -4.2 ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 435))

    # def test36(self):
    #     input = """ x : boolean = !true ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 436))

    # def test37(self):
    #     input = """ a : boolean = false ; x : boolean = !a ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # # def test38(self):
    # #     input = """ a : string = "false" ; x : boolean = !a ;"""
    # #     expect = "Type mismatch in expression: Id(a)"
    # #     self.assertTrue(TestChecker.test(input, expect, 438))

    # def test39(self):
    #     input = """ x : integer ; a : array [3,1] of integer = {{1}, {2}, {x}} ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 439))

    # # def test40(self):
    # #     input = """ x : float ; a : array [1,2] of integer = {1, 2, x} ;"""
    # #     expect = "Illegal array literal: Id(x)"
    # #     self.assertTrue(TestChecker.test(input, expect, 440))

    # def test41(self):
    #     input = """ a : array [1,2] of integer = {1, 2, x} ;"""
    #     expect = "Undeclared Identifier: x"
    #     self.assertTrue(TestChecker.test(input, expect, 441))

    # def test42(self):
    #     input = """ a : array [2,1] of integer = {{1 + 2}, {3 + 4}} ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 442))

    # # def test43(self):
    # #     input = """ a : array [1,2] of integer = {true, 1} ;"""
    # #     expect = "Illegal array literal: IntegerLit(1)"
    # #     self.assertTrue(TestChecker.test(input, expect, 443))

    # def test44(self):
    #     input = """ x, y : integer ; a : array [2] of integer = {1 + x, 2 * y} ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 444))

    # # def test45(self):
    # #     input = """ x, y : integer ; b : array [2, 3] of integer ; a : array [1,2] of integer = {1 + x, 2 * b} ;"""
    # #     expect = "Type mismatch in expression: Id(b)"
    # #     self.assertTrue(TestChecker.test(input, expect, 445))

    # # def test46(self):
    # #     input = """ a : array [1,2] of integer = {true, true, false} ;"""
    # #     expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2], IntegerType), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False)]))"
    # #     self.assertTrue(TestChecker.test(input, expect, 446))

    # def test47(self):
    #     input = """ a : array [2, 2] of integer = {{1, 2}, {3, 4}} ; b : integer = a[0] ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(0)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 447))

    # def test48(self):
    #     input = """ b : integer = a[2] ;"""
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input, expect, 448))

    # def test49(self):
    #     input = """ a : integer ; b : integer = a[2] ;"""
    #     expect = "Type mismatch in expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input, expect, 449))

    # def test50(self):
    #     input = """ a : array [1,2] of integer ; b : integer = a[2, 3, 5] ;"""
    #     expect = "Type mismatch in expression: IntegerLit(5)"
    #     self.assertTrue(TestChecker.test(input, expect, 450))

    # def test51(self):
    #     input = """ a : array [1,2] of integer ; b : integer = a[2.2] ;"""
    #     expect = "Type mismatch in expression: FloatLit(2.2)"
    #     self.assertTrue(TestChecker.test(input, expect, 451))

    # def test52(self):
    #     input = """ a : array [1,2] of integer ; b : integer = a[1 + 2] ;"""
    #     expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), IntegerLit(2))"
    #     self.assertTrue(TestChecker.test(input, expect, 452))

    # def test53(self):
    #     input = """ a : auto = "false" ; b : auto = a :: "true" ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 453))

    # def test55(self):
    #     input = """ x : auto = {{1.0, 2.2}, {3.9, 2.5}, {3.7, 9.0}} ; """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 455))

    # def test56(self):
    #     input = """ x : auto = 1 + {1, 2, 3}; """
    #     expect = "Type mismatch in expression: ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 456))

    # def test59(self):
    #     input = """ arr : array [3, 2] of integer = {{{1}, {2}}, {{2}, {3}}, {{3}, {3, 3}}} ; """
    #     expect = "Type mismatch in expression: ArrayLit([IntegerLit(3), IntegerLit(3)])"
    #     self.assertTrue(TestChecker.test(input, expect, 459))

    # def test60(self):
    #     input = """ arr : array [3, 2] of integer = {{1, 2}, {2, 3}, {3, 3, 4}} ; """
    #     expect = "Type mismatch in expression: ArrayLit([IntegerLit(3), IntegerLit(3), IntegerLit(4)])"
    #     self.assertTrue(TestChecker.test(input, expect, 460))

    # def test61(self):
    #     input = """ arr : array [3, 2] of integer = {{1, 2}, {2, 3}, {1.2, 1}} ; """
    #     expect = "Illegal array literal: IntegerLit(1)"
    #     self.assertTrue(TestChecker.test(input, expect, 461))

    # def test62(self):
    #     input = """ arr : array [3, 2] of float = {{1.0, 2.0}, {2.0, 3.0}, {1.2, 1.0}} ; """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 462))

    # def test63(self):
    #     input = """ arr : array [3, 2] of float = {{1.0, 2.0}, {2.0, 3.0}, {1.2, 1.0}} ; a : integer = arr[-1] ;  """
    #     expect = "Type mismatch in expression: UnExpr(-, IntegerLit(1))"
    #     self.assertTrue(TestChecker.test(input, expect, 463))

    # def test64(self):
    #     input = """ arr : array [3, 2] of float = {{1.0, 2.0}, {2.0, 3.0}, {1.2, 1.0}} ; a : integer = arr[a + 2 + c] ;  """
    #     expect = "Type mismatch in expression: BinExpr(+, BinExpr(+, Id(a), IntegerLit(2)), Id(c))"
    #     self.assertTrue(TestChecker.test(input, expect, 464))

    # def test65(self):
    #     input = """ a : array [1,2] of integer ; b : integer = a[2, 3, 5] ;"""
    #     expect = "Type mismatch in expression: IntegerLit(5)"
    #     self.assertTrue(TestChecker.test(input, expect, 474))

    # def test66(self):
    #     input = """ a : array [3,2] of float = {{2.0, 3.0}, {3.0, 4.0}, {5.0, 6.6}} ; b : float = a[0, 1] ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 476))

    # def test67(self):
    #     input = """ a : array [3,2] of float = {{2.0, 3.0}, {3.0, 4.0}, {5.0, 6.6}} ; b : integer = a[2, 1] ;"""
    #     expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(2), IntegerLit(1)]))"
    #     self.assertTrue(TestChecker.test(input, expect, 477))

    # def test68(self):
    #     input = """ a : array [3] of float = {1.0, 2.0, 6.6} ; b : float = a[2] ;"""
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 478))

    # def test69(self):
    #     input = """ x, y, z : float ; main1 : function integer (a : integer, b : float) {} main2 : function integer (c : integer, d : float) {} main3 : function integer (e : integer, f : float) {} """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 469))

    # def test70(self):
    #     input = """  
    #     a : array [2, 2] of float = {{2.0, 3.6}, {5.0, 9.9}} ;
    #     main : function void () {
    #         x : float = a[0, 0] ;
    #         y : float = a[1, 1] ;
    #         return ;
    #     } """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 470))

    # def test71(self):
    #     input = """
    #     a : array [2, 2] of float = {{1.0, 2.0}, {3.0, 4.4}} ;  
    #     func : function integer (a : integer, b : float) {
    #         a = 2 ;
    #         c : float ;
    #         c = a[1, 0] ;
    #         return ;
    #     } """
    #     expect = "Type mismatch in expression: Id(a)"
    #     self.assertTrue(TestChecker.test(input, expect, 471))

    # def test72(self):
    #     input = """ 
    #     func : function integer (a : auto, b : string) {
    #         a = {2, 3} ;
    #         b = func1(1, 2) ;
    #         return ;
    #     } 
    #     func1 : function auto (x : auto, y : auto) {}
    #     """
    #     expect = "Type mismatch in statement: ReturnStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 472))

    # def test73(self):
    #     input = """ 
    #     func : function integer (a : auto, b : string) {
    #         a = {2, 3} ;
    #         c : string = func1(2, 3) ;
    #         return ;
    #     } 
    #     func1 : function auto (x : auto, y : auto) {}
    #     """
    #     expect = "Type mismatch in statement: ReturnStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 473))

    # def test74(self):
    #     input = """
    #     x : array [2, 2] of float = {{1.0, 2.0}, {3.0, 4.4}} ;  
    #     b : float = x[0, 0] ;
    #     func : function auto (a : auto, b : string) {
    #         c : float ;
    #         return ;
    #         }
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 474))

    # def test75(self):
    #     input = """
    #     x : array [2, 2] of float = {{1.0, 2.0}, {3.0, 4.4}} ;  
    #     b : float = x[0, 0] ;
    #     func : function auto (a : auto, b : string) {
    #         c : float ;
    #         return ;
    #         }
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 475))

    # def test76(self):
    #     input = """
    #     func : function integer (a : integer, b : integer) {
    #         a = 2 ;
    #         b = 5 ;
    #         if (a > b) break ;
    #         else continue ;
    #         }
    #     """
    #     expect = "Must in loop: BreakStmt()"
    #     self.assertTrue(TestChecker.test(input, expect, 476))

    # def test77(self):
    #     input = """
    #     func : function float (a : integer, b : integer) {
    #             x : integer ;
    #             return func1(1 ,2) ;
    #         }
    #     func1 : function auto (x : integer, y : integer) {}
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 477))

    # def test79(self):
    #     input = """
    #     func : function float (a : integer, b : integer) {
    #             func1(1, 2) ;
    #         }
    #     func1 : function auto (x : auto, y : auto) {}
    #     """
    #     expect = "No entry point"
    #     self.assertTrue(TestChecker.test(input, expect, 479))
    def testVardecl0(self):
        input = "x, y, z: integer = 1, 2, 3;"
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 400))
    def testVardecl1(self):
        input = """a: array[10,1] of integer = {1,2,3};
            a: auto = 10 ;
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([10, 1], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 401))
    def testVardecl2(self):
        input = "x, y, z: integer = 1, 2, 3; k:auto;"
        expect = "Invalid Variable: k"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def testEntryPoint3(self):
        input = """
        foo1: function integer(z: auto, y: string) {
            return 1;
        }
        foo: function auto(b: integer, c: string) inherit foo1 {
        preventDefault();
    d: string = "abc";
        }
main:function void() {
  return 0;
}
        """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(0))"
        self.assertTrue(TestChecker.test(input,expect, 403))

    def testFuncCall4(self):
        input = """
        foo: function auto(b: integer, c: string) {
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            a = c;
            c = 1000;
            
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(c), IntegerLit(1000))"

        self.assertTrue(TestChecker.test(input,expect, 404))

    def testFuncCall5(self):
        input = """
        foo: function auto(b: integer, c: string) {
        a: string = "abc";
        }
        main:function void() {
            x, y: integer = 1, foo(1, "abc");
            a: integer;
            main: integer;
            for(a=1, a<10, a+1) {
            a: integer = 1;
             a: string = "abc";
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect, 405))

    def testExpression6(self):
        input = """
        foo: function auto(b: integer, c: string) {
        a: string = "abc";
        return 0;
        }
        main:function void() {
            a: integer;
            main: integer;
            for(a=1, a<10, a+1) {
             a = 1*2+true/3.3;
            }
        }
        """
        expect = "Type mismatch in expression: BinExpr(/, BooleanLit(True), FloatLit(3.3))"
        self.assertTrue(TestChecker.test(input,expect, 406))

    def testExpression7(self):
        input = """
        foo: function auto(b: integer, c: string) {
        a: string = "abc";
        return a;
        }
        main:function void(c: float) {
            a: integer;
            b: float;
            e,e1: boolean;
            d: string;
            // integer
            // a = foo(a, d);
            a =  1+2-2*3/4%5;
            // float
            b = 1.1+2.2+3*9-2.2*3.3/4.4;
            b=1*2.2+3/23+10+b+10;
            // string
            d = "abc"::("def"::d);

            // boolean
            e= true||false&&true;
            e = !e;
            e = e&&e1;

            e = ((((((1==true)!=(e!=1000))<10.1)>20)<=30)>=2010.123121)+2;
        }
        """
        expect = "Type mismatch in expression: BinExpr(<, BinExpr(!=, BinExpr(==, IntegerLit(1), BooleanLit(True)), BinExpr(!=, Id(e), IntegerLit(1000))), FloatLit(10.1))"
        self.assertTrue(TestChecker.test(input,expect, 407))

    def testExpression8(self):
        input="""
        foo: function auto(b: integer, c: string) {
            a: string = "abc";
        return a;
        }
        main:function void(c: float) {
        a: integer;
        b: float;
        e,e1: boolean;
        d: string;
        // integer
        a = foo(a, d);
    }
    """
        expect = "Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo, [Id(a), Id(d)]))"
        self.assertTrue(TestChecker.test(input,expect, 408))

    def testExpression9(self):
        input = """
        foo: function auto(b: integer, c: string) {
        a: string = "abc";
         return a;
        }
        main:function void(c: float) {
            a: integer;
            b: float;
            e,e1: boolean;
            d: string;
            // integer
            a = foo(a, d);
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo, [Id(a), Id(d)]))"
        self.assertTrue(TestChecker.test(input,expect, 409))

    def testExpression10(self):
        input = """
        foo: function void(b: integer, c: string) {
        a: string = "abc";
        }
        main:function void(c: float) {
            a: integer;
            b: float;
            e,e1: boolean;
            d: string;
            // integer
            a = foo(a, d);
        }
        """
        expect = "Type mismatch in expression: FuncCall(foo, [Id(a), Id(d)])"
        self.assertTrue(TestChecker.test(input,expect, 410))

    def test11(self):
        input = """
        foo: function auto(b: integer, c: auto) {
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo(1, 2);
            a = c;
            c = 1000;
            
}
        """
        expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(1), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input,expect, 411))

    def test12(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 412))

    def test13(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 413))


    def test14(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 414))

    def test15(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 415))


    def test16(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 416))


    def test17(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 417))

    def test18(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
            x: integer = 1;
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
        
        }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect, 418))

    def test19(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
            x: integer= 1;
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 419))

    def testArray20(self):

        input = """
        main:function void() {

        b: array[3,2,1] of integer = {{{1},{2}},{{3},{4}},{{5},{6}}};
        // d: array[1,2,3] of integer = {{{1},{2}}, };

        a: array[2] of integer = { {1,2},{21,21},{12,13} }; // type mismatch var decl

        // x: integer = b[1];  // b[1] type: ArrayType([2,3] IntegerType)
        }
        """
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(21), IntegerLit(21)]), ArrayLit([IntegerLit(12), IntegerLit(13)])]))"
        self.assertTrue(TestChecker.test(input,expect, 420))

    def testArray21(self):

        input = """
        main:function void() {
        a: string;
        b: array[3,2,1] of integer = {{{"fasdfs", a},{2}},{{3},{4}},{{5},{6}}}; // Type mismatch
        // d: array[1,2,3] of integer = {{{1},{2}}};

        a: array[2] of integer = { {1,2},{21,21},{12,13} }; // type mismatch var decl

        // x: integer = b[1];  // b[1] type: ArrayType([2,3] IntegerType)
        }
        """
        expect = "Illegal array literal: ArrayLit([ArrayLit([StringLit(fasdfs), Id(a)]), ArrayLit([IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input,expect, 421))

    def test22(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
            x: integer= 1;
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 422))


    def test23(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
            x: integer= 1;
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 423))

    def test24(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
            x: integer= 1;
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 424))


    def test25(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
            x: integer= 1;
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 425))


    def test26(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
            x: integer= 1;
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 426))

    def test27(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
            x: integer= 1;
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 427))

    def test28(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
            x: integer= 1;
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 428))

    def test29(self):
        input = """
        foo: function auto(b: integer, c: auto) inherit foo1 {
            super(1,2);
        }

        main:function void() {
            b: integer = 1;
            a:auto = b<100;
            d: auto = "abc" :: "def";
            c:auto = foo(1, d);
            foo1(1,2);
            foo(1, "3123");
            foo1(1, 1.2);
            foo(1, 2);
            a = c;
            c = 1000;
        }
        
        foo1: function auto(inherit x: auto, y: auto) {
            x: integer= 1;
        
        }
        """
        expect = "Type mismatch in statement: CallStmt(foo1, IntegerLit(1), FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input,expect, 429))


    def testScope30(self):

        input = """
        main:function void() {
        a: integer;
        if (a==1) {
            a: integer = 1;
            b: float = 2.3;
            if (b>2) {
                a: float = 1.1;
                a: string ;
            }
        }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect, 430))

    def testScope31(self):

        input = """
        main:function void() {
        a: integer;
        if (a==1) {
            a: string = "dads";
            b: float = 2.3;
            if (b>2) {
                a = "fasfd";
            }
                a= "ffdfssfsfdffs";
        }
        a = "3jiojiojoij";
        }
        """
        expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(3jiojiojoij))"
        self.assertTrue(TestChecker.test(input,expect, 431))

    def testScope32(self):

            input = """
            main:function void() {
            a: integer;
            if (a==1) {
                a: string = "dads";
                b: float = 2.3;
                if (b>2) {
                    a = "fasfd";
                }
                    a= "ffdfssfsfdffs";
            }
            a = "3jiojiojoij";
            }
            """
            expect = "Type mismatch in statement: AssignStmt(Id(a), StringLit(3jiojiojoij))"
            self.assertTrue(TestChecker.test(input,expect, 432))

    def test33(self):
        input = """
        foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
            return a+b;
        }

        foo: function integer(x: string, y: integer) inherit foo1 {
            preventDefault();
            a: integer = 1;
            b: integer = 2;
            d: float = 3.4;            
            return 1;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect, 433))

    def test34(self):
        input = """
        foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
            return a+b;
        }

        foo: function integer(x: string, y: integer) inherit foo1 {
            preventDefault();
            a: integer = 1;
            b: integer = 2;
            d: float = 3.4;
            
            return 1;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect, 434))

    def test35(self):
        input = """
        foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
            return a+b;
        }

        foo: function integer(x: string, y: integer) inherit foo1 {
            preventDefault();
            a: integer = 1;
            b: integer = 2;
            d: float = 3.4;
            
            return 1;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect, 435))

    def test36(self):
        input = """
        foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
            return a+b;
        }

        foo: function integer(x: string, y: integer) inherit foo1 {
            preventDefault();
            a: integer = 1;
            b: integer = 2;
            d: float = 3.4;
            
            return 1;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect, 436))

    def test37(self):
        input = """
        foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
            return a+b;
        }

        foo: function integer(x: string, x: integer) inherit foo1 {
            preventDefault();
            a: integer = 1;
            b: integer = 2;
            d: float = 3.4;
            
            return 1;
        }
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input,expect, 437))

    def test38(self):
        input = """
        foo1: function integer(inherit a: integer, a: integer, inherit out c: string, d: float) {
            return a+b;
        }

        foo: function integer(x: string, y: integer) inherit foo1 {
            preventDefault();
            a: integer = 1;
            b: integer = 2;
            d: float = 3.4;
            
            return 1;
        }
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect, 438))

    def test39(self):
        input = """
        foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
            return a+b;
        }

        foo: function integer(x: string, y: integer) inherit foo1 {
            preventDefault();
            a: integer = 1;
            b: integer = 2;
            d: float = 3.4;
            
            return 1;
        }
        """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect, 439))

    def testInherit40(self):
        input = """
        foo1: function integer(inherit a: integer, b: integer, inherit out c: string, d: float) {
            return a+b;
        }

        foo: function integer(x: string, y: integer) inherit foo1 {
            super(123123, "strText");
            return 1;
        }
        """
        expect = "Type mismatch in expression: StringLit(strText)"
        self.assertTrue(TestChecker.test(input,expect, 440))


    def testInherit41(self):
        input = """
        foo1: function integer(inherit a: integer, b: integer,inherit out c: string, d: float) {
            return a+b;
        }

        foo: function integer(a: string, y: integer) inherit foo1 {
            super(123123, "fadfsfdff");
            return 1;
        }
        """
        expect = "Type mismatch in expression: StringLit(fadfsfdff)"
        self.assertTrue(TestChecker.test(input,expect, 441))

    def testInherit42(self):
        input = """
           foo1: function integer(a: integer, inherit b: integer, out c: string, d: float) {
               return a+b;
           }

           foo: function integer(a: string, y: integer) inherit foo1 {
               super(10,20, "arwerwwer", 10.1);
                b: float; // redeclared b from foo1
               return 1;
           }
           """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 442))


    def testInherit43(self):
        input = """
           foo1: function integer(a: integer, inherit b: integer, out c: string, d: float) {
               return a+b;
           }

           foo: function integer(a: string, y: integer) inherit foo1 {
               super(10,20, "arwerwwer");
                b: float; // redeclared b from foo1
               return 1;
           }
           """
        expect = "Type mismatch in expression: "
        self.assertTrue(TestChecker.test(input, expect, 443))

    def testInherit44(self):
        input = """
           foo1: function integer(a: integer, inherit b: integer, out c: string, d: float) {
               return a+b;
           }

           foo: function integer(a: string, y: integer) inherit foo1 {
               super(10,20, "arwerwwer", 13.312, true,a,y);
                b: float; // redeclared b from foo1
               return 1;
           }
           """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def testInherit45(self):
        input = """
           foo1: function integer(a: integer, inherit b: integer, out c: string, d: float) {
               return a+b;
           }

           foo: function integer(a: string, y: integer) inherit foo1 {
               super(10,20, "arwerwwer", 10.1);
                b: float; // redeclared b from foo1
               return 1;
           }
           """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def testDecl446(self):
        input = """
    main: function void() {
        x:auto = foo(1);
       foo2();
       arr:array[2,2] of integer = {{1,2}, {1,2}};
       foo(1);
        b[2] = 9;
        a[1,2] = {1,2,3,4,5,6,7,8};
      c: array [2,2] of integer = {{21,2},{12,212}};
      
        // a: integer = bar(10);
       // b: array [2] of integer = {1,2};
      // d: array [2] of integer = { x({2}, 2), bar(10) };
    // a: array [1] of integer = {1};
     // bar(1);
    // a: integer = x(b);

    }

            foo:function float(x:integer){
                return x + 1.2;
            }
            foo2: function void(){}
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test447(self):
        input = """
        foo1: function integer(inherit a: integer, b: integer) {
        printString("hello");
            a = printInteger("fadsf");
            c: integer;
            c = foo("fdadf",b);
            a = 10;
        }
        foo: function array[4] of integer(a: string, y: integer) inherit foo1 {
//             super(a, a);
            preventDefault();
            a: integer;
            return {1,2,3,4};
        }

        main: function void() {
        // a = b;
        }
        """

        expect = "Type mismatch in expression: FuncCall(printInteger, [StringLit(fadsf)])"

        self.assertTrue(TestChecker.test(input, expect, 447))

    def test448(self): # TODO: fix raise index Op arr[1,2,3]
        intput = """
       main:function void() inherit foo{
                super(12);
                x:auto = foo(1);
                foo2();
                arr:array[2,2] of integer = {{1,2}, {1,2}};
                arr[1,2,3] = 1;
            }
            foo:function float(x:float){
                return x + 1.2;
            }
            foo2: function void(){}
        """
        expect = "Type mismatch in expression: IntegerLit(3)"
        self.assertTrue(TestChecker.test(intput, expect, 448))

    def test449(self):
        input = """
        foo: function auto() {}
        inc : function void (out b : integer, d: float) inherit foo{
              super();
              foo();
              a: integer = 1 % foo();
              c: integer = 124;
        }
        foo : function void (inherit n: float, f: integer){}

               foo: function void (b: auto, c: auto){
            d: string;
            a: string = b + d;

        }
        b: integer = foo();
        main: function void() {

        }
        """
        expect = "Redeclared Function: foo"

        self.assertTrue(TestChecker.test(input, expect, 449))

    def test50(self):
        input = """
        foo: function auto() {}
        
        inc : function void (out b : integer, d: float){
            i: integer;
            for (i = 0, i < 10, 1) {
                if (b > 1) {
                    b = b + 1;
                    break;
                }
                continue;
            }   
            continue;
        }
            
        """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test51(self):
        input = """
        foo: function auto() {}
        
        inc : function void (out b : integer, d: float){
            i,j: integer;
            a: float;
            for (i = 0, i < 10, 1) {
                if (b > 1) {
                    b = b + 1;
                    for (i = "fsdf", i < 10, a) {
                    break;
                        while(true) {
                        break; 
                        }
                    }
                    break;
                }
                continue;
            }   
            continue;
        }
        """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), StringLit(fsdf)), BinExpr(<, Id(i), IntegerLit(10)), Id(a), BlockStmt([BreakStmt(), WhileStmt(BooleanLit(True), BlockStmt([BreakStmt()]))]))"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test52(self):
        input = """ a : string = "2" :: "33" ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test53(self):
        input = """ x : string = "223232" ; a : string = "2" :: x ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test54(self):
        input = """ x : float = -2.5554 ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test55(self):
        input = """ x : float = -2.5554 + 3 + -4.2 ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test56(self):
        input = """ x : boolean = !true ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test57(self):
        input = """ a : boolean = false ; x : boolean = !a ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test58(self):
        input = """ a : string = "false" ; x : boolean = !a ;"""
        expect = "Type mismatch in expression: UnExpr(!, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test59(self):
        input = """ x : integer ; a : array [3,1] of integer = {{1}, {2}, {x}} ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test60(self):
        input = """ x : float ; a : array [1,2] of integer = {1, 2, x} ;"""
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), Id(x)])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test61(self):
        input = """ a : array [1,2] of integer = {1, 2, x} ;"""
        expect = "Undeclared Identifier: x"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test62(self):
        input = """ a : array [2,1] of integer = {{1 + 2}, {3 + 4}} ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test63(self):
        input = """ a : array [1,2] of integer = {true, 1} ;"""
        expect = "Illegal array literal: ArrayLit([BooleanLit(True), IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test64(self):
        input = """ x, y : integer ; a : array [2] of integer = {1 + x, 2 * y} ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test65(self):
        input = """ x, y : integer ; b : array [2, 3] of integer ; a : array [1,2] of integer = {1 + x, 2 * b} ;"""
        expect = "Type mismatch in expression: BinExpr(*, IntegerLit(2), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test66(self):
        input = """ a : array [1,2] of integer = {true, true, false} ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([1, 2], IntegerType), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False)]))"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test67(self):
        input = """ a : array [2, 2] of integer = {{1, 2}, {3, 4}} ; b : integer = a[0] ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(0)]))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test68(self):
        input = """ b : integer = a[2] ;"""
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test69(self):
        input = """ a : integer ; b : integer = a[2] ;"""
        expect = "Type mismatch in expression: Id(a)"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test70(self):
        input = """ a : array [1,2] of integer ; b : integer = a[2, 3, 5] ;"""
        expect = "Type mismatch in expression: IntegerLit(5)"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test71(self):
        input = """ a : array [1,2] of integer ; b : integer = a[2.2] ;"""
        expect = "Type mismatch in expression: FloatLit(2.2)"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test72(self):
        input = """ a : array [1,2] of integer ; b : integer = a[1 + 2] ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [BinExpr(+, IntegerLit(1), IntegerLit(2))]))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test73(self):
        input = """ a : auto = "false" ; b : auto = a :: "true" ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test74(self):
        input = """ x : auto = {1, 2, 3} ; b : auto = x :: {4, 5, 6} ;"""
        expect = "Type mismatch in expression: BinExpr(::, Id(x), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]))"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test75(self):
        input = """ x : auto = {{1.0, 2.2}, {3.9, 2.5}, {3.7, 9.0}} ; """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test76(self):
        input = """ x : auto = 1 + {1, 2, 3}; """
        expect = "Type mismatch in expression: BinExpr(+, IntegerLit(1), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test77(self):
        input = """ a : array [3,2] of float = {{2.0, 3.0}, {3.0, 4.0}, {5.0, 6.6}} ; b : integer = a[2, 1] ;"""
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, ArrayCell(a, [IntegerLit(2), IntegerLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test78(self):
        input = """ a : array [3] of float = {1.0, 2.0, 6.6} ; b : float = a[2] ;"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test79(self):
        input = """ arr : array [3, 2] of integer = {{{1}, {2}}, {{2}, {3}}, {{3}, {3, 3}}} ; """
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(3)])])"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_80(self):
        input = """
        x: float = 3.0;
        a : array [2] of integer;
        foo: function auto(){}
        fact : function integer (n : integer) {
            b: float;
            n = b + 1;
        }
        main: function void(){}
    """

        expect = "Type mismatch in statement: AssignStmt(Id(n), BinExpr(+, Id(b), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input = """
        a : array [2] of integer;
        foo: function auto(x: integer){}
        fact : function integer (n : integer) {
            foo: float = 3.0;
            b: integer;
            n1: boolean = -foo(1) == true;
        }
        main: function void(){}
    """

        expect = "Type mismatch in expression: BinExpr(==, UnExpr(-, FuncCall(foo, [IntegerLit(1)])), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_82(self):
        input = """
        foo: function auto(x: integer){}
        foo1: function auto(x: float){}
        fact : function integer (n : integer) {
            a : array [2] of integer;
            a[1] = (foo1(foo(1900)) + 1);
        }
        main: function integer(){}
    """

        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_83(self):
        input = """
        // foo: function auto(){}
        foo1: function auto(y: boolean){}
        foo2: function boolean(){}
        fact : function integer (n : integer) {
            a : array [2] of integer;
            i: float = 3;
            for (i = 123, 9 > 8, i + 1){}
        }
        main: function void(){}
    """

        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(123)), BinExpr(>, IntegerLit(9), IntegerLit(8)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([]))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_84(self):
        input = """
        foo2: function boolean(i: integer){}
        main: function void(){
            for (i = 123, i > 8, foo2(1)){}
        }
    """

        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_85(self):
        input = """
        foo2: function auto(i: integer){
            return 1;
        }
        main: function void(){
            foo1(213);
        }
    """

        expect = "Undeclared Function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_86(self):
        input = """
        foo1: function integer(){}
        foo2: function float(inherit x: boolean){
            return 1;
        }
        foo3: function float() inherit foo1{
            printInteger(1);
            preventDefault();
            return 1.123;
        }
        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Invalid statement in function: foo3"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_87(self):
        input = """
        x: integer;
        foo1: function integer(inherit x: float){}
        foo2: function float(inherit y: float) inherit foo1{
            super(10);
            z: float = 10.1;
            return 1;
        }
        foo3: function float(out z: float) inherit foo2{
            preventDefault();
            y: integer = 10;
            printInteger(1);
            return 1.123;
        }
        main: function void(){
            x: integer = readInteger();
            break;
        }
    """

        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_88(self):
        input = """
        x: integer;
        foo1: function integer(inherit x: float){}
        foo2: function float(inherit y: float){
            super(10);
            z: float = 10.1;
            return 1;
        }
        main: function void(){
            x: integer = readInteger();
        }
    """

        expect = "Invalid statement in function: foo2"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_89(self):
        input = """
        x: integer;
        foo1: function integer(){}
        foo2: function float(inherit y: float) inherit foo1{
            super();
            z: float = 10.1;
            return 1;
        }
        main: function void(){
            x: integer = readInteger();
            return 1;
        }
    """

        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_90(self): # TODO: fix index op
        input = """
        isPalindrome: function boolean(strs: array[100] of string, strSize: integer) {
            i: integer;
          for (i = 0, i < strSize / 2, i+1) {
            if (strs[i] != strs[strSize-i-1]) {
          return 10;
              return false;
            }
          }
          return true;
        }
        main: function void() {
            strs   : array [5] of string = {"hello", "world", "!!!", "", "test\\n"};
            if(isPalindrome(strs, 5)) printString("Correct!!!");
            else printString("Wrong!!!");
        }
    """

        expect = "Type mismatch in expression: BinExpr(!=, ArrayCell(strs, [Id(i)]), ArrayCell(strs, [BinExpr(-, BinExpr(-, Id(strSize), Id(i)), IntegerLit(1))]))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_91(self):
        input = """
        inc: function auto(a: integer, b: float)
        {
            a = -1 + -2 + -3;
            b = a + a / b + a;
            while (a!=0)
                a = a - 1;
            do
            {
                return b;
            }
            while (a==true);
            return a;
        }
        main: function void() {
        return 1;
        }
    """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = r"""
        count: function boolean(n: integer)
        {
            i: integer;
            c: integer = 0;
            for (i=1,i<n,i+1)
                if (n%i==0)
                    c = c + 1;
            if (c == 2)
                return true;
            else
                return false;
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            readInteger(n);
            if (count(n) == true)
                print("n is prime number");
            else
                print("n is not prime number");
        }
    """
        expect = "Type mismatch in statement: CallStmt(readInteger, Id(n))"
        self.assertTrue(TestChecker.test(input, expect, 492))

    def test_93(self):
        input = r"""
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + readString();
            return s;
        }
        main: function void() {}
    """
        expect = "Type mismatch in expression: BinExpr(+, Id(s), FuncCall(readString, []))"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_94(self):
        input = """
        foo3: function auto(inherit i: integer, a: float) {}
        foo2: function auto(inherit b: float, a: float) inherit foo3 {
            super(1, 1.0);
            c: integer = 1;
        }
        foo1: function integer(inherit c: float) inherit foo2 {
            super(1, 1.0);
            i: integer = 2;
            
            b: string;
            return 1;
        }
        main: function void(){
            foo2(foo1(1.0), 1);
        }
            """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_95(self):
        input = r"""
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + randomChar();
            return s;
        }
        main: function void() {}
    """
        expect = "Undeclared Function: randomChar"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input = r"""
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s + readString();
            return s;
        }
        main: function void() {}
    """
        expect = "Type mismatch in expression: BinExpr(+, Id(s), FuncCall(readString, []))"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_97(self):
        input = r"""
        s : string;
        random: function string(n: integer)
        {
            i: integer;
            s = "";
            for (i = 0,i < n,i+1)
                s = s::readString();
            return s;
        }
        main: function void() {
            n : integer;
            printString("Input n:");
            n = readInteger();
            printString("The random string length n is "::random(n));
            return 1;
        }
    """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_98(self): # TODO: fix index op
        input = r"""
        a,b: array[10] of integer;
        swap: function void(out a: array[10] of integer, out b: array[10] of integer, n: integer)
        {
            if (n>10)
                return;
            else
            {
                temp,i : integer;
                for (i=0,i<n,i+1)
                {
                    temp=a[i];
                    a[i]=b[i];
                    b[i]=temp;
                }
            }
        }
        main: function void() {
            return 1;
        }
    """
        expect = "Type mismatch in statement: ReturnStmt(IntegerLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_99(self):
        input = """
            foo3: function auto(inherit i: integer, a: float) {}
            foo2: function auto(inherit b: float, a: float) inherit foo3 {
                super(true, 1.0);
            }
            main: function void(){
                foo2(foo1(1.0), 1);
            }
            """
        expect = "Type mismatch in expression: BooleanLit(True)"
        self.assertTrue(TestChecker.test(input, expect, 499))