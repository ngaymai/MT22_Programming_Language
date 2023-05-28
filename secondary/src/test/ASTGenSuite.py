import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
        def test_program_0(self):
            input = """x, y: integer;"""
            expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
])"""
            self.assertTrue(TestAST.test(input, expect, 300))

        def test_program_1(self):
            input = """x, y, z: integer = 1, 2, 3;"""
            expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
])"""
            self.assertTrue(TestAST.test(input, expect, 301))

        def test_program_2(self):
            input = """x, y, z: integer = 1, 2, 3;
            a, b: float;"""
            expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(1))
	VarDecl(y, IntegerType, IntegerLit(2))
	VarDecl(z, IntegerType, IntegerLit(3))
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
])"""
            self.assertTrue(TestAST.test(input, expect, 302))

        def test_program_3(self):
            input = """
                    main: function void () { }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
            self.assertTrue(TestAST.test(input, expect, 303))

        def test_program_4(self):
            
            input = """
                    main: function void ()
                    {
                        printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printinteger, IntegerLit(4))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 304))

        def test_program_5(self):
            input = """
                    main: function void ()
                    {
                        printinteger(4);
                        foo(1,2);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printinteger, IntegerLit(4)), CallStmt(foo, IntegerLit(1), IntegerLit(2))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 305))

        def test_program_6(self):
            input = """
                    main: function void ()
                    {
                        printinteger(4);
                        foo();
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printinteger, IntegerLit(4)), CallStmt(foo, )]))
])"""
            self.assertTrue(TestAST.test(input, expect, 306))

        def test_program_7(self):
            input = """
                    fact: function integer (n: integer)
                    {
                        if (n==0) return 1;
                        else return n*fact(n-1);
                    }
                    main: function void ()
                    {
                        printinteger(4);
                        fact(3);
                    }
                    """
            expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printinteger, IntegerLit(4)), CallStmt(fact, IntegerLit(3))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 307))

        def test_program_8(self):
            """More complex program"""
            input = """
                    main: function void () {
                        for( i = 1, i < 10, i+1)
                            if (i == 5)
                                printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), IntegerLit(5)), CallStmt(printinteger, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 308))

        def test_program_9(self):
            input = """
                    main: function void () {
                        for( i = 1, i < 10, i+1)
                            if (!i)
                                printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(UnExpr(!, Id(i)), CallStmt(printinteger, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 309))

        def test_program_10(self):
            input = """
                    main: function void () {
                        i: integer;
                        for( i = 1, i < 10, i+1)
                            if (!i)
                                printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(UnExpr(!, Id(i)), CallStmt(printinteger, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 310))

        def test_program_11(self):
            """More complex program"""
            input = """
                    main: function void () {
                        i: integer;
                        a: array [5] of integer;
                        a = {1,2,3,4,5};
                        for( i = 1, i < 10, i+1)
                            if (!i)
                                printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(a, ArrayType([5], IntegerType)), AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(UnExpr(!, Id(i)), CallStmt(printinteger, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 311))

        def test_program_12(self):
            input = """
                    main: function void () {
                        i: integer;
                        j: float;
                        j = i + 1;
                        for( i = 1, i < 10, i+1)
                            if (!i)
                                printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, FloatType), AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(UnExpr(!, Id(i)), CallStmt(printinteger, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 312))

        def test_program_13(self):
            input = """
                    main: function void () {
                        i,j,t: integer;
                        f: boolean;
                        j = i + 1 + t*4;
                        for( i = 1, i < 10, i+1)
                            if (!i)
                                printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(t, IntegerType), VarDecl(f, BooleanType), AssignStmt(Id(j), BinExpr(+, BinExpr(+, Id(i), IntegerLit(1)), BinExpr(*, Id(t), IntegerLit(4)))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(UnExpr(!, Id(i)), CallStmt(printinteger, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 313))

        def test_program_14(self):
            input = """
                    main: function void () {
                        i,j,t: integer = 1,2,3;
                        j = i + 1 + t*4;
                        for( i = 1, i < 10, i+1)
                            if (!i)
                                printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(1)), VarDecl(j, IntegerType, IntegerLit(2)), VarDecl(t, IntegerType, IntegerLit(3)), AssignStmt(Id(j), BinExpr(+, BinExpr(+, Id(i), IntegerLit(1)), BinExpr(*, Id(t), IntegerLit(4)))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(UnExpr(!, Id(i)), CallStmt(printinteger, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 314))

        def test_program_15(self):
            input = """
                    main: function void () {
                        i: integer;
                        a: array [3,3] of integer;
                        for( i = 1, i < 10, i+1)
                            if (!i)
                                printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(a, ArrayType([3, 3], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(UnExpr(!, Id(i)), CallStmt(printinteger, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 315))

        def test_program_16(self):
            input = """
                    main: function void () {
                    i: integer;
                    a,b,c: array [5,3] of integer;
                    for( i = 1, i < 10, i+1)
                        if (!i)
                            printinteger(4);
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(a, ArrayType([5, 3], IntegerType)), VarDecl(b, ArrayType([5, 3], IntegerType)), VarDecl(c, ArrayType([5, 3], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(UnExpr(!, Id(i)), CallStmt(printinteger, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 316))

        def test_program_17(self):
            input = """
                    main: function void () {
                        i: float = 0.6;
                        a: array [5] of float;
                        b: array [3] of integer;
                        a = {1,2,3,4,5};
                        b= {1,3,4};
                        i = a[2];
                        b[1] = a[3] * 5;
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, FloatType, FloatLit(0.6)), VarDecl(a, ArrayType([5], FloatType)), VarDecl(b, ArrayType([3], IntegerType)), AssignStmt(Id(a), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(b), ArrayLit([IntegerLit(1), IntegerLit(3), IntegerLit(4)])), AssignStmt(Id(i), ArrayCell(a, [IntegerLit(2)])), AssignStmt(ArrayCell(b, [IntegerLit(1)]), BinExpr(*, ArrayCell(a, [IntegerLit(3)]), IntegerLit(5)))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 317))

        def test_program_18(self):
            """More complex program"""
            input = """
                    main: function void ()
                    {
                        a: array [3,3] of integer;
                        a = {
                            {1,2,3},{4,5,6},{7,8,9}
                        };

                        i = a[0,0] + a[0,1] * a[2,2];
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 3], IntegerType)), AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(7), IntegerLit(8), IntegerLit(9)])])), AssignStmt(Id(i), BinExpr(+, ArrayCell(a, [IntegerLit(0), IntegerLit(0)]), BinExpr(*, ArrayCell(a, [IntegerLit(0), IntegerLit(1)]), ArrayCell(a, [IntegerLit(2), IntegerLit(2)]))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 318))

        def test_program_19(self):
            input = """
                    main: function void ()
                    {
                        a: array [3,3] of integer;
                        b: float = -1.5;
                        c: integer = -18;
                        a = {
                            {-1,-2,-3},{-4,-5,-6},{-7,-8,-9}
                        };

                        a[0,0] = b + c * a[2,2];
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([3, 3], IntegerType)), VarDecl(b, FloatType, UnExpr(-, FloatLit(1.5))), VarDecl(c, IntegerType, UnExpr(-, IntegerLit(18))), AssignStmt(Id(a), ArrayLit([ArrayLit([UnExpr(-, IntegerLit(1)), UnExpr(-, IntegerLit(2)), UnExpr(-, IntegerLit(3))]), ArrayLit([UnExpr(-, IntegerLit(4)), UnExpr(-, IntegerLit(5)), UnExpr(-, IntegerLit(6))]), ArrayLit([UnExpr(-, IntegerLit(7)), UnExpr(-, IntegerLit(8)), UnExpr(-, IntegerLit(9))])])), AssignStmt(ArrayCell(a, [IntegerLit(0), IntegerLit(0)]), BinExpr(+, Id(b), BinExpr(*, Id(c), ArrayCell(a, [IntegerLit(2), IntegerLit(2)]))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 319))

        def test_program_20(self):
            input = """
                    main: function void ()
                    {
                        a, b : integer = -1, -2;
                        a = b + -4;
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, UnExpr(-, IntegerLit(1))), VarDecl(b, IntegerType, UnExpr(-, IntegerLit(2))), AssignStmt(Id(a), BinExpr(+, Id(b), UnExpr(-, IntegerLit(4))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 320))

        def test_program_21(self):
            input = """
                        x,y,z:integer;
                        g, h , i , k: string;
                        q,t: float;
                    """
            expect = """Program([
	VarDecl(x, IntegerType)
	VarDecl(y, IntegerType)
	VarDecl(z, IntegerType)
	VarDecl(g, StringType)
	VarDecl(h, StringType)
	VarDecl(i, StringType)
	VarDecl(k, StringType)
	VarDecl(q, FloatType)
	VarDecl(t, FloatType)
])"""
            self.assertTrue(TestAST.test(input, expect, 321))

        def test_program_22(self):
            input = """
                        x: integer = 10;
                        y: float = 10.5;
                        z: string = "hello";
                    foo: function string (a:string, out b:string)
                    {
                        b = a;
                        return b;
                    }
                    main: function void()
                    {
                        foo(z);
                    }
                    """
            expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, FloatType, FloatLit(10.5))
	VarDecl(z, StringType, StringLit(hello))
	FuncDecl(foo, StringType, [Param(a, StringType), OutParam(b, StringType)], None, BlockStmt([AssignStmt(Id(b), Id(a)), ReturnStmt(Id(b))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, Id(z))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 322))

        def test_program_23(self):
            input = """
                        x: integer = 10;
                        y: float = 10.5;
                        z, t: string = "hello", "world";
                    foo: function string (a:string, out b:string){
                        b = a;
                        return b;
                    }
                    main: function void(){
                        w: string;
                        w = foo(z)::(z::t);
                    }
                    """
            expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	VarDecl(y, FloatType, FloatLit(10.5))
	VarDecl(z, StringType, StringLit(hello))
	VarDecl(t, StringType, StringLit(world))
	FuncDecl(foo, StringType, [Param(a, StringType), OutParam(b, StringType)], None, BlockStmt([AssignStmt(Id(b), Id(a)), ReturnStmt(Id(b))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(w, StringType), AssignStmt(Id(w), BinExpr(::, FuncCall(foo, [Id(z)]), BinExpr(::, Id(z), Id(t))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 323))

        def test_program_24(self):
            input = """
                        x: integer = 10;

                    foo: function string (a:integer, b: integer){
                        return a + b;
                    }
                    main: function void(){
                        w: integer;
                        w = x + foo(10,20);
                    }
                    """
            expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	FuncDecl(foo, StringType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(w, IntegerType), AssignStmt(Id(w), BinExpr(+, Id(x), FuncCall(foo, [IntegerLit(10), IntegerLit(20)])))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 324))

        def test_program_25(self):
            input = """
                        x: integer = 10;

                    foo: function string (a:integer, b: integer){
                        return a + b;
                    }
                    main: function void(){
                        w: integer;
                        c, t, f: auto = 1, 2, 3;
                        w = x + foo(c + t, t + f);
                    }
                    """
            expect = """Program([
	VarDecl(x, IntegerType, IntegerLit(10))
	FuncDecl(foo, StringType, [Param(a, IntegerType), Param(b, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(+, Id(a), Id(b)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(w, IntegerType), VarDecl(c, AutoType, IntegerLit(1)), VarDecl(t, AutoType, IntegerLit(2)), VarDecl(f, AutoType, IntegerLit(3)), AssignStmt(Id(w), BinExpr(+, Id(x), FuncCall(foo, [BinExpr(+, Id(c), Id(t)), BinExpr(+, Id(t), Id(f))])))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 325))

        def test_program_26(self):
            input = """
                        x: boolean = true;

                    foo: function string (a:boolean, b: boolean){
                        if (a) return b;
                        else return a;
                    }
                    main: function void(){
                        y: boolean = !x;

                         foo(!x, y);
                    }
                    """
            expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	FuncDecl(foo, StringType, [Param(a, BooleanType), Param(b, BooleanType)], None, BlockStmt([IfStmt(Id(a), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(y, BooleanType, UnExpr(!, Id(x))), CallStmt(foo, UnExpr(!, Id(x)), Id(y))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 326))

        def test_program_27(self):
            input = """
                        x,y,z: boolean = true, false, true;

                    foo: function boolean (a:boolean, b: boolean){
                        if (a) return b;
                        else return a;
                    }
                    main: function void(){
                       c, t, f : boolean = !x, !y, !z;
                       foo(c && t, t || f);

                    }
                    """
            expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(z, BooleanType, BooleanLit(True))
	FuncDecl(foo, BooleanType, [Param(a, BooleanType), Param(b, BooleanType)], None, BlockStmt([IfStmt(Id(a), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(c, BooleanType, UnExpr(!, Id(x))), VarDecl(t, BooleanType, UnExpr(!, Id(y))), VarDecl(f, BooleanType, UnExpr(!, Id(z))), CallStmt(foo, BinExpr(&&, Id(c), Id(t)), BinExpr(||, Id(t), Id(f)))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 327))

        def test_program_28(self):
            input = """
                        x,y,z: boolean = true, false, true;

                    foo: function boolean (a:boolean, b: boolean, c: boolean){
                        if (a && b || c) return b;
                        else return a;
                    }
                    main: function void(){
                       c : boolean = foo(c && t, t || f, f && c);

                    }
                    """
            expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(z, BooleanType, BooleanLit(True))
	FuncDecl(foo, BooleanType, [Param(a, BooleanType), Param(b, BooleanType), Param(c, BooleanType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(c, BooleanType, FuncCall(foo, [BinExpr(&&, Id(c), Id(t)), BinExpr(||, Id(t), Id(f)), BinExpr(&&, Id(f), Id(c))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 328))

        def test_program_29(self):
            input = """
                        x,y,z, t: float = 1.234, 2.345, 0.12345, 2.345;

                    f1: function boolean (f: boolean){
                        if (a && b || c) return b;
                        else return a;
                    }
                    f2: function float (a: float, b: float){
                        if(a == b)
                            return f1(z != t);
                        else
                            return f1(z == t);
                    }
                    main: function void(){

                    }
                    """
            expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.234))
	VarDecl(y, FloatType, FloatLit(2.345))
	VarDecl(z, FloatType, FloatLit(0.12345))
	VarDecl(t, FloatType, FloatLit(2.345))
	FuncDecl(f1, BooleanType, [Param(f, BooleanType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(f2, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), ReturnStmt(FuncCall(f1, [BinExpr(!=, Id(z), Id(t))])), ReturnStmt(FuncCall(f1, [BinExpr(==, Id(z), Id(t))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
            self.assertTrue(TestAST.test(input, expect, 329))

        def test_program_30(self):
            input = """
                        x,y,z, t: float = 1.234, 2.345, 0.12345, 2.345;

                    f1: function boolean (f: boolean){
                        if (a && b || c) return b;
                        else return a;
                    }
                    f2: function float (a: float, b: float){
                        if(a == b)
                            return f1(z != t);
                        else
                            return f1(z == t);
                    }
                    main: function void(){
                        if (f1()){
                            t1: string;
                        }

                    }
                    """
            expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.234))
	VarDecl(y, FloatType, FloatLit(2.345))
	VarDecl(z, FloatType, FloatLit(0.12345))
	VarDecl(t, FloatType, FloatLit(2.345))
	FuncDecl(f1, BooleanType, [Param(f, BooleanType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(f2, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), ReturnStmt(FuncCall(f1, [BinExpr(!=, Id(z), Id(t))])), ReturnStmt(FuncCall(f1, [BinExpr(==, Id(z), Id(t))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(FuncCall(f1, []), BlockStmt([VarDecl(t1, StringType)]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 330))

        def test_program_31(self):
            input = """
                        x,y,z, t: float = 1.234, 2.345, 0.12345, 2.345;

                    f1: function boolean (f: boolean){
                        if (a && b || c) return b;
                        else return a;
                    }
                    f2: function float (a: float, b: float){
                        if(a == b)
                            return f1(z != t);
                        else
                            return f1(z == t);
                    }
                    main: function void(){
                        if (f1()){
                            t1, t2, t3: string;
                            f1, f2: integer = 123, 432;
                        }
                        else{

                        }
                    }
                    """
            expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.234))
	VarDecl(y, FloatType, FloatLit(2.345))
	VarDecl(z, FloatType, FloatLit(0.12345))
	VarDecl(t, FloatType, FloatLit(2.345))
	FuncDecl(f1, BooleanType, [Param(f, BooleanType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(f2, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), ReturnStmt(FuncCall(f1, [BinExpr(!=, Id(z), Id(t))])), ReturnStmt(FuncCall(f1, [BinExpr(==, Id(z), Id(t))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(FuncCall(f1, []), BlockStmt([VarDecl(t1, StringType), VarDecl(t2, StringType), VarDecl(t3, StringType), VarDecl(f1, IntegerType, IntegerLit(123)), VarDecl(f2, IntegerType, IntegerLit(432))]), BlockStmt([]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 331))

        def test_program_32(self):
            input = """
                        x,y,z, t: float = 1.234, 2.345, 0.12345, 2.345;

                    f1: function boolean (f: boolean){
                        if (a && b || c) return b;
                        else return a;
                    }
                    f2: function float (a: float, b: float){
                        if(a == b)
                            return f1(z != t);
                        else
                            return f1(z == t);
                    }
                    main: function void(){
                        f1(x || y);
                        f2(x*y, z+t);
                    }
                    """
            expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.234))
	VarDecl(y, FloatType, FloatLit(2.345))
	VarDecl(z, FloatType, FloatLit(0.12345))
	VarDecl(t, FloatType, FloatLit(2.345))
	FuncDecl(f1, BooleanType, [Param(f, BooleanType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(f2, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), ReturnStmt(FuncCall(f1, [BinExpr(!=, Id(z), Id(t))])), ReturnStmt(FuncCall(f1, [BinExpr(==, Id(z), Id(t))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(f1, BinExpr(||, Id(x), Id(y))), CallStmt(f2, BinExpr(*, Id(x), Id(y)), BinExpr(+, Id(z), Id(t)))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 332))

        def test_program_33(self):
            input = """
                        x,y,z, t: float = 1.234, 2.345, 0.12345, 2.345;

                    f1: function boolean (f: boolean){
                        if (a && b || c) return b;
                        else return a;
                    }
                    f2: function float (a: float, b: float){
                        if(a == b)
                            return f1(z != t);
                        else
                            return f1(z == t);
                    }
                    main: function void(){
                        if(f1())
                            for ( i = 1, i < 10 , i + 1)
                                f1(x||y);
                                f2(x && y, z || t);
                    }
                    """
            expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.234))
	VarDecl(y, FloatType, FloatLit(2.345))
	VarDecl(z, FloatType, FloatLit(0.12345))
	VarDecl(t, FloatType, FloatLit(2.345))
	FuncDecl(f1, BooleanType, [Param(f, BooleanType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(f2, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), ReturnStmt(FuncCall(f1, [BinExpr(!=, Id(z), Id(t))])), ReturnStmt(FuncCall(f1, [BinExpr(==, Id(z), Id(t))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(FuncCall(f1, []), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(f1, BinExpr(||, Id(x), Id(y))))), CallStmt(f2, BinExpr(&&, Id(x), Id(y)), BinExpr(||, Id(z), Id(t)))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 333))

        def test_program_34(self):
            input = """
                        x,y,z, t: float = 1.234, 2.345, 0.12345, 2.345;

                    f1: function boolean (f: boolean){
                        if (a && b || c) return b;
                        else return a;
                    }
                    f2: function float (a: float, b: float){
                        if(a == b)
                            return f1(z != t);
                        else
                            return f1(z == t);
                    }
                    main: function void(){
                        while(true || false)
                            if(true)
                                f1(x * y + z - t);
                    }
                    """
            expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.234))
	VarDecl(y, FloatType, FloatLit(2.345))
	VarDecl(z, FloatType, FloatLit(0.12345))
	VarDecl(t, FloatType, FloatLit(2.345))
	FuncDecl(f1, BooleanType, [Param(f, BooleanType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(f2, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), ReturnStmt(FuncCall(f1, [BinExpr(!=, Id(z), Id(t))])), ReturnStmt(FuncCall(f1, [BinExpr(==, Id(z), Id(t))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(||, BooleanLit(True), BooleanLit(False)), IfStmt(BooleanLit(True), CallStmt(f1, BinExpr(-, BinExpr(+, BinExpr(*, Id(x), Id(y)), Id(z)), Id(t)))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 334))

        def test_program_35(self):
            input = """
                        x,y,z, t: float = 1.234, 2.345, 0.12345, 2.345;

                    f1: function boolean (f: boolean){
                        if (a && b || c) return b;
                        else return a;
                    }
                    f2: function float (a: float, b: float){
                        if(a == b)
                            return f1(z != t);
                        else
                            return f1(z == t);
                    }
                    main: function void(){
                        while(f1(true))
                            if(true)
                                f1(x * y + z - t);
                            if(false)
                                f2(1.342);
                            else
                                f1(!f2());
                    }
                    """
            expect = """Program([
	VarDecl(x, FloatType, FloatLit(1.234))
	VarDecl(y, FloatType, FloatLit(2.345))
	VarDecl(z, FloatType, FloatLit(0.12345))
	VarDecl(t, FloatType, FloatLit(2.345))
	FuncDecl(f1, BooleanType, [Param(f, BooleanType)], None, BlockStmt([IfStmt(BinExpr(||, BinExpr(&&, Id(a), Id(b)), Id(c)), ReturnStmt(Id(b)), ReturnStmt(Id(a)))]))
	FuncDecl(f2, FloatType, [Param(a, FloatType), Param(b, FloatType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), Id(b)), ReturnStmt(FuncCall(f1, [BinExpr(!=, Id(z), Id(t))])), ReturnStmt(FuncCall(f1, [BinExpr(==, Id(z), Id(t))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(FuncCall(f1, [BooleanLit(True)]), IfStmt(BooleanLit(True), CallStmt(f1, BinExpr(-, BinExpr(+, BinExpr(*, Id(x), Id(y)), Id(z)), Id(t))))), IfStmt(BooleanLit(False), CallStmt(f2, FloatLit(1.342)), CallStmt(f1, UnExpr(!, FuncCall(f2, []))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 335))

        def test_program_36(self):
            input = """
                    x, y, z: array [5] of integer  ;

                    main: function void(){
                        a, b, c: array [2,2] of float ;
                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 336))

        def test_program_37(self):
            input = """
                    x, y, z: array [5] of integer;
                    f1: function array [5] of integer (f: integer){

                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;
                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(f, IntegerType)], None, BlockStmt([]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 337))

        def test_program_38(self):
            input = """
                        x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        return n;
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;
                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(Id(n))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 338))

        def test_program_39(self):
            input = """
                        x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + 1;
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;
                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), IntegerLit(1))))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 339))

        def test_program_40(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;
                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 340))

        def test_program_41(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        for ( i = 0, i< 2, i + 1)
                            for(j = 0, j< 2, j + 1)
                                a[i, j] = a[j, i];
                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(2)), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(ArrayCell(a, [Id(i), Id(j)]), ArrayCell(a, [Id(j), Id(i)]))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 341))

        def test_program_42(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        i, j: integer = 0, 0;
                        for ( i = 0, i< 2, i + 1)
                        {
                            k: integer = 10;
                            a[i] = a[i + 2] * 10;
                            for(j = 0, j< 2, j + 1)
                                a[i, j] = a[j, i];
                        }

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(k, IntegerType, IntegerLit(10)), AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(*, ArrayCell(a, [BinExpr(+, Id(i), IntegerLit(2))]), IntegerLit(10))), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(2)), BinExpr(+, Id(j), IntegerLit(1)), AssignStmt(ArrayCell(a, [Id(i), Id(j)]), ArrayCell(a, [Id(j), Id(i)])))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 342))

        def test_program_43(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        i, j: integer = 0, 0;
                        for ( i = 0, i< 2, i + 1)
                        {
                            k: integer = 10;
                            a[i] = a[i + 2] * 10;
                            for(j = 0, j< 2, j + 1)
                            {
                                t: float = 1.4;
                                a[i, j] = a[j, i] % t;
                            }

                        }

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(j, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(k, IntegerType, IntegerLit(10)), AssignStmt(ArrayCell(a, [Id(i)]), BinExpr(*, ArrayCell(a, [BinExpr(+, Id(i), IntegerLit(2))]), IntegerLit(10))), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(2)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([VarDecl(t, FloatType, FloatLit(1.4)), AssignStmt(ArrayCell(a, [Id(i), Id(j)]), BinExpr(%, ArrayCell(a, [Id(j), Id(i)]), Id(t)))]))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 343))

        def test_program_44(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        f1(x);

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), CallStmt(f1, Id(x))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 344))

        def test_program_45(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        y = {2,3,4,5,6};
                        z = {x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3], x[4] + y[4] };
                        f1(z);

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(y), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(z), ArrayLit([BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(y, [IntegerLit(0)])), BinExpr(+, ArrayCell(x, [IntegerLit(1)]), ArrayCell(y, [IntegerLit(1)])), BinExpr(+, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(2)])), BinExpr(+, ArrayCell(x, [IntegerLit(3)]), ArrayCell(y, [IntegerLit(3)])), BinExpr(+, ArrayCell(x, [IntegerLit(4)]), ArrayCell(y, [IntegerLit(4)]))])), CallStmt(f1, Id(z))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 345))

        def test_program_46(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        y = {2,3,4,5,6};
                        z = {x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3], x[4] + y[4] };
                        z[0] = x[index(y)];

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(y), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(z), ArrayLit([BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(y, [IntegerLit(0)])), BinExpr(+, ArrayCell(x, [IntegerLit(1)]), ArrayCell(y, [IntegerLit(1)])), BinExpr(+, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(2)])), BinExpr(+, ArrayCell(x, [IntegerLit(3)]), ArrayCell(y, [IntegerLit(3)])), BinExpr(+, ArrayCell(x, [IntegerLit(4)]), ArrayCell(y, [IntegerLit(4)]))])), AssignStmt(ArrayCell(z, [IntegerLit(0)]), ArrayCell(x, [FuncCall(index, [Id(y)])]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 346))

        def test_program_47(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        y = {2,3,4,5,6};
                        z = {x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3], x[4] + y[4] };
                        z[0] = x[index(y)];
                        do{
                        i: integer = 0;
                        i = i + z[i];
                        }
                        while(z[1+4*5] == y[2+2-4]);

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(y), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(z), ArrayLit([BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(y, [IntegerLit(0)])), BinExpr(+, ArrayCell(x, [IntegerLit(1)]), ArrayCell(y, [IntegerLit(1)])), BinExpr(+, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(2)])), BinExpr(+, ArrayCell(x, [IntegerLit(3)]), ArrayCell(y, [IntegerLit(3)])), BinExpr(+, ArrayCell(x, [IntegerLit(4)]), ArrayCell(y, [IntegerLit(4)]))])), AssignStmt(ArrayCell(z, [IntegerLit(0)]), ArrayCell(x, [FuncCall(index, [Id(y)])])), DoWhileStmt(BinExpr(==, ArrayCell(z, [BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(4), IntegerLit(5)))]), ArrayCell(y, [BinExpr(-, BinExpr(+, IntegerLit(2), IntegerLit(2)), IntegerLit(4))])), BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), ArrayCell(z, [Id(i)])))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 347))

        def test_program_48(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        y = {2,3,4,5,6};
                        z = {x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3], x[4] + y[4] };
                        z[0] = x[index(y)];
                        do{
                        i: integer = 0;
                        i = i + z[i];
                        while(i == 0)
                            f1(y);
                        }
                        while(z[1+4*5] == y[2+2-4]);

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(y), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(z), ArrayLit([BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(y, [IntegerLit(0)])), BinExpr(+, ArrayCell(x, [IntegerLit(1)]), ArrayCell(y, [IntegerLit(1)])), BinExpr(+, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(2)])), BinExpr(+, ArrayCell(x, [IntegerLit(3)]), ArrayCell(y, [IntegerLit(3)])), BinExpr(+, ArrayCell(x, [IntegerLit(4)]), ArrayCell(y, [IntegerLit(4)]))])), AssignStmt(ArrayCell(z, [IntegerLit(0)]), ArrayCell(x, [FuncCall(index, [Id(y)])])), DoWhileStmt(BinExpr(==, ArrayCell(z, [BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(4), IntegerLit(5)))]), ArrayCell(y, [BinExpr(-, BinExpr(+, IntegerLit(2), IntegerLit(2)), IntegerLit(4))])), BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), ArrayCell(z, [Id(i)]))), WhileStmt(BinExpr(==, Id(i), IntegerLit(0)), CallStmt(f1, Id(y)))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 348))

        def test_program_49(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        y = {2,3,4,5,6};
                        z = {x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3], x[4] + y[4] };
                        z[0] = x[index(y)];
                        do{
                        i: integer = 0;
                        i = i + z[i];
                        while(i == 0)
                            {
                                f1(y);
                                j: integer = 1;
                                continue;
                            }
                        }
                        while(z[1+4*5] == y[2+2-4]);

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(y), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(z), ArrayLit([BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(y, [IntegerLit(0)])), BinExpr(+, ArrayCell(x, [IntegerLit(1)]), ArrayCell(y, [IntegerLit(1)])), BinExpr(+, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(2)])), BinExpr(+, ArrayCell(x, [IntegerLit(3)]), ArrayCell(y, [IntegerLit(3)])), BinExpr(+, ArrayCell(x, [IntegerLit(4)]), ArrayCell(y, [IntegerLit(4)]))])), AssignStmt(ArrayCell(z, [IntegerLit(0)]), ArrayCell(x, [FuncCall(index, [Id(y)])])), DoWhileStmt(BinExpr(==, ArrayCell(z, [BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(4), IntegerLit(5)))]), ArrayCell(y, [BinExpr(-, BinExpr(+, IntegerLit(2), IntegerLit(2)), IntegerLit(4))])), BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), ArrayCell(z, [Id(i)]))), WhileStmt(BinExpr(==, Id(i), IntegerLit(0)), BlockStmt([CallStmt(f1, Id(y)), VarDecl(j, IntegerType, IntegerLit(1)), ContinueStmt()]))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 349))

        def test_program_50(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        y = {2,3,4,5,6};
                        z = {x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3], x[4] + y[4] };
                        z[0] = x[index(y)];
                        do{
                        i: integer = 0;
                        i = i + z[i];
                        while(i == 0)
                            {
                                f1(y);
                                j: integer = 1;
                                if(i == j)
                                    continue;
                                else
                                    break;
                            }
                        }
                        while(z[1+4*5] == y[2+2-4]);

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(y), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(z), ArrayLit([BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(y, [IntegerLit(0)])), BinExpr(+, ArrayCell(x, [IntegerLit(1)]), ArrayCell(y, [IntegerLit(1)])), BinExpr(+, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(2)])), BinExpr(+, ArrayCell(x, [IntegerLit(3)]), ArrayCell(y, [IntegerLit(3)])), BinExpr(+, ArrayCell(x, [IntegerLit(4)]), ArrayCell(y, [IntegerLit(4)]))])), AssignStmt(ArrayCell(z, [IntegerLit(0)]), ArrayCell(x, [FuncCall(index, [Id(y)])])), DoWhileStmt(BinExpr(==, ArrayCell(z, [BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(4), IntegerLit(5)))]), ArrayCell(y, [BinExpr(-, BinExpr(+, IntegerLit(2), IntegerLit(2)), IntegerLit(4))])), BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), ArrayCell(z, [Id(i)]))), WhileStmt(BinExpr(==, Id(i), IntegerLit(0)), BlockStmt([CallStmt(f1, Id(y)), VarDecl(j, IntegerType, IntegerLit(1)), IfStmt(BinExpr(==, Id(i), Id(j)), ContinueStmt(), BreakStmt())]))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 350))

        def test_program_51(self):
            input = """
                       x, y, z: array [5] of integer;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        y = {2,3,4,5,6};
                        z = {x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3], x[4] + y[4] };
                        z[0] = x[index(y)];
                        do{
                        i: integer = 0;
                        i = i + z[i];
                        while(i == 0)
                            {
                                f1(y);
                                j: integer = 1;
                                if(i == j)
                                    for(i = j, i<10, i+ 1)
                                        {
                                            k: integer = 9;
                                            x [k] = f1(k) + f2(b);
                                        }
                                else
                                    break;
                            }
                        }
                        while(z[1+4*5] == y[2+2-4]);

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(y), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(z), ArrayLit([BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(y, [IntegerLit(0)])), BinExpr(+, ArrayCell(x, [IntegerLit(1)]), ArrayCell(y, [IntegerLit(1)])), BinExpr(+, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(2)])), BinExpr(+, ArrayCell(x, [IntegerLit(3)]), ArrayCell(y, [IntegerLit(3)])), BinExpr(+, ArrayCell(x, [IntegerLit(4)]), ArrayCell(y, [IntegerLit(4)]))])), AssignStmt(ArrayCell(z, [IntegerLit(0)]), ArrayCell(x, [FuncCall(index, [Id(y)])])), DoWhileStmt(BinExpr(==, ArrayCell(z, [BinExpr(+, IntegerLit(1), BinExpr(*, IntegerLit(4), IntegerLit(5)))]), ArrayCell(y, [BinExpr(-, BinExpr(+, IntegerLit(2), IntegerLit(2)), IntegerLit(4))])), BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(Id(i), BinExpr(+, Id(i), ArrayCell(z, [Id(i)]))), WhileStmt(BinExpr(==, Id(i), IntegerLit(0)), BlockStmt([CallStmt(f1, Id(y)), VarDecl(j, IntegerType, IntegerLit(1)), IfStmt(BinExpr(==, Id(i), Id(j)), ForStmt(AssignStmt(Id(i), Id(j)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([VarDecl(k, IntegerType, IntegerLit(9)), AssignStmt(ArrayCell(x, [Id(k)]), BinExpr(+, FuncCall(f1, [Id(k)]), FuncCall(f2, [Id(b)])))])), BreakStmt())]))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 351))

        def test_program_52(self):
            input = """
                       x, y, z: array [5] of integer;
                       a,b,c: integer = 1,2,3;
                    f1: function array [5] of integer (n: array [5] of integer){
                        i: integer;
                        t,y,e: boolean = true, false, true;
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        y = {2,3,4,5,6};
                        z = {x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3], x[4] + y[4] };
                        z[0] = x[index(y)];

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], IntegerType))], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(t, BooleanType, BooleanLit(True)), VarDecl(y, BooleanType, BooleanLit(False)), VarDecl(e, BooleanType, BooleanLit(True)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(y), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(z), ArrayLit([BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(y, [IntegerLit(0)])), BinExpr(+, ArrayCell(x, [IntegerLit(1)]), ArrayCell(y, [IntegerLit(1)])), BinExpr(+, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(2)])), BinExpr(+, ArrayCell(x, [IntegerLit(3)]), ArrayCell(y, [IntegerLit(3)])), BinExpr(+, ArrayCell(x, [IntegerLit(4)]), ArrayCell(y, [IntegerLit(4)]))])), AssignStmt(ArrayCell(z, [IntegerLit(0)]), ArrayCell(x, [FuncCall(index, [Id(y)])]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 352))

        def test_program_53(self):
            input = """
                       x, y, z: array [5] of integer;
                       a,b,c: integer = 1,2,3;
                       s,g,r : boolean = true, true, false;
                    f1: function array [5] of integer (n: array [5] of boolean){
                        i: integer;
                        t,y,e: boolean = true, false, true;
                        if((n[1]==n[2]) && (n[3]==n[4]))
                            return f1(x);
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                        a, b, c: array [2,2] of float;

                        a = {
                            {1.2, 2.3}, {2.3, 4.5}
                        } ;
                        x = {1,2,3,4,5};
                        y = {2,3,4,5,6};
                        z = {x[0] + y[0], x[1] + y[1], x[2] + y[2], x[3] + y[3], x[4] + y[4] };
                        z[0] = x[index(y)];

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(s, BooleanType, BooleanLit(True))
	VarDecl(g, BooleanType, BooleanLit(True))
	VarDecl(r, BooleanType, BooleanLit(False))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], BooleanType))], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(t, BooleanType, BooleanLit(True)), VarDecl(y, BooleanType, BooleanLit(False)), VarDecl(e, BooleanType, BooleanLit(True)), IfStmt(BinExpr(&&, BinExpr(==, ArrayCell(n, [IntegerLit(1)]), ArrayCell(n, [IntegerLit(2)])), BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)]))), ReturnStmt(FuncCall(f1, [Id(x)]))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([2, 2], FloatType)), VarDecl(b, ArrayType([2, 2], FloatType)), VarDecl(c, ArrayType([2, 2], FloatType)), AssignStmt(Id(a), ArrayLit([ArrayLit([FloatLit(1.2), FloatLit(2.3)]), ArrayLit([FloatLit(2.3), FloatLit(4.5)])])), AssignStmt(Id(x), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), AssignStmt(Id(y), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)])), AssignStmt(Id(z), ArrayLit([BinExpr(+, ArrayCell(x, [IntegerLit(0)]), ArrayCell(y, [IntegerLit(0)])), BinExpr(+, ArrayCell(x, [IntegerLit(1)]), ArrayCell(y, [IntegerLit(1)])), BinExpr(+, ArrayCell(x, [IntegerLit(2)]), ArrayCell(y, [IntegerLit(2)])), BinExpr(+, ArrayCell(x, [IntegerLit(3)]), ArrayCell(y, [IntegerLit(3)])), BinExpr(+, ArrayCell(x, [IntegerLit(4)]), ArrayCell(y, [IntegerLit(4)]))])), AssignStmt(ArrayCell(z, [IntegerLit(0)]), ArrayCell(x, [FuncCall(index, [Id(y)])]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 353))

        def test_program_54(self):
            input = """
                       x, y, z: array [5] of integer;
                       a,b,c: integer = 1,2,3;
                       s,g,r : boolean = true, true, false;
                    f1: function array [5] of integer (n: array [5] of boolean){
                        i: integer;
                        t,y,e: boolean = true, false, true;
                        if((n[1]==n[2]) && (n[3]==n[4]))
                            return f1(x);
                        else
                            {
                                do{
                                    i = i + 1;
                                    while((i ==j) || (j!=i))
                                        break;
                                }while(a[i] == a[i+1]);
                            }
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(s, BooleanType, BooleanLit(True))
	VarDecl(g, BooleanType, BooleanLit(True))
	VarDecl(r, BooleanType, BooleanLit(False))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], BooleanType))], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(t, BooleanType, BooleanLit(True)), VarDecl(y, BooleanType, BooleanLit(False)), VarDecl(e, BooleanType, BooleanLit(True)), IfStmt(BinExpr(&&, BinExpr(==, ArrayCell(n, [IntegerLit(1)]), ArrayCell(n, [IntegerLit(2)])), BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)]))), ReturnStmt(FuncCall(f1, [Id(x)])), BlockStmt([DoWhileStmt(BinExpr(==, ArrayCell(a, [Id(i)]), ArrayCell(a, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), WhileStmt(BinExpr(||, BinExpr(==, Id(i), Id(j)), BinExpr(!=, Id(j), Id(i))), BreakStmt())]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
            self.assertTrue(TestAST.test(input, expect, 354))

        def test_program_55(self):
            input = """
                       x, y, z: array [5] of integer;
                       a,b,c: integer = 1,2,3;
                       s,g,r : array [4] of boolean ;

                    f1: function array [5] of integer (n: array [5] of boolean){
                        i: integer;
                        t,y,e: boolean = true, false, true;

                        if((n[1]==n[2]) && (n[3]==n[4]))
                            return f1(x);
                        else
                            {
                                do{
                                    i = i + 1;
                                    while((i ==j) || (j!=i))
                                        for(i=1, i< j+1, i*5)
                                            return index(x[5] + y[4] - -z[7]);
                                }while(a[i] == a[i+1]);
                            }
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                         s = {true, true, false, true};
                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(s, ArrayType([4], BooleanType))
	VarDecl(g, ArrayType([4], BooleanType))
	VarDecl(r, ArrayType([4], BooleanType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], BooleanType))], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(t, BooleanType, BooleanLit(True)), VarDecl(y, BooleanType, BooleanLit(False)), VarDecl(e, BooleanType, BooleanLit(True)), IfStmt(BinExpr(&&, BinExpr(==, ArrayCell(n, [IntegerLit(1)]), ArrayCell(n, [IntegerLit(2)])), BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)]))), ReturnStmt(FuncCall(f1, [Id(x)])), BlockStmt([DoWhileStmt(BinExpr(==, ArrayCell(a, [Id(i)]), ArrayCell(a, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), WhileStmt(BinExpr(||, BinExpr(==, Id(i), Id(j)), BinExpr(!=, Id(j), Id(i))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), BinExpr(+, Id(j), IntegerLit(1))), BinExpr(*, Id(i), IntegerLit(5)), ReturnStmt(FuncCall(index, [BinExpr(-, BinExpr(+, ArrayCell(x, [IntegerLit(5)]), ArrayCell(y, [IntegerLit(4)])), UnExpr(-, ArrayCell(z, [IntegerLit(7)])))]))))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False), BooleanLit(True)]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 355))

        def test_program_56(self):
            input = """
                    age : integer;
                       x, y, z: array [5] of integer;
                       a,b,c: integer = 1,2,3;
                       s,g,r : array [4] of boolean ;

                    f1: function array [5] of integer (n: array [5] of boolean){
                        i: integer;
                        t,y,e: boolean = true, false, true;

                        if((n[1]==n[2]) && (n[3]==n[4]))
                            return f1(x);
                        else
                            {
                                do{
                                    i = i + 1;
                                    while((i ==j) || (j!=i))
                                        for(i=1, i< j+1, i*5)
                                            return index(x[5] + y[4] - -z[7]);
                                }while(a[i] == a[i+1]);
                            }
                        for (i = 0, i < 5, i + 1)
                            n[i] = n[i] + n[i + 1];
                        if(n[3] == n[4])
                            return n;
                    }
                    index: function integer(a: array [5] of integer ){
                        return a[2];
                    }
                    main: function void(){
                         s = {true, true, false, true};
                         while ((age > 0) && (age <= 100)) {
                            Write("Enter age (1 - 100): ");
    		                Readln(age);
    		                if (age < 1)
    			                Writeln("Age cannot be less than 1...");
    		                if (age > 100)
    			                Writeln("Age cannot be greater than 100...");
                         }
                    }
                    """
            expect = """Program([
	VarDecl(age, IntegerType)
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	VarDecl(a, IntegerType, IntegerLit(1))
	VarDecl(b, IntegerType, IntegerLit(2))
	VarDecl(c, IntegerType, IntegerLit(3))
	VarDecl(s, ArrayType([4], BooleanType))
	VarDecl(g, ArrayType([4], BooleanType))
	VarDecl(r, ArrayType([4], BooleanType))
	FuncDecl(f1, ArrayType([5], IntegerType), [Param(n, ArrayType([5], BooleanType))], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(t, BooleanType, BooleanLit(True)), VarDecl(y, BooleanType, BooleanLit(False)), VarDecl(e, BooleanType, BooleanLit(True)), IfStmt(BinExpr(&&, BinExpr(==, ArrayCell(n, [IntegerLit(1)]), ArrayCell(n, [IntegerLit(2)])), BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)]))), ReturnStmt(FuncCall(f1, [Id(x)])), BlockStmt([DoWhileStmt(BinExpr(==, ArrayCell(a, [Id(i)]), ArrayCell(a, [BinExpr(+, Id(i), IntegerLit(1))])), BlockStmt([AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))), WhileStmt(BinExpr(||, BinExpr(==, Id(i), Id(j)), BinExpr(!=, Id(j), Id(i))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), BinExpr(+, Id(j), IntegerLit(1))), BinExpr(*, Id(i), IntegerLit(5)), ReturnStmt(FuncCall(index, [BinExpr(-, BinExpr(+, ArrayCell(x, [IntegerLit(5)]), ArrayCell(y, [IntegerLit(4)])), UnExpr(-, ArrayCell(z, [IntegerLit(7)])))]))))]))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(ArrayCell(n, [Id(i)]), BinExpr(+, ArrayCell(n, [Id(i)]), ArrayCell(n, [BinExpr(+, Id(i), IntegerLit(1))])))), IfStmt(BinExpr(==, ArrayCell(n, [IntegerLit(3)]), ArrayCell(n, [IntegerLit(4)])), ReturnStmt(Id(n)))]))
	FuncDecl(index, IntegerType, [Param(a, ArrayType([5], IntegerType))], None, BlockStmt([ReturnStmt(ArrayCell(a, [IntegerLit(2)]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False), BooleanLit(True)])), WhileStmt(BinExpr(&&, BinExpr(>, Id(age), IntegerLit(0)), BinExpr(<=, Id(age), IntegerLit(100))), BlockStmt([CallStmt(Write, StringLit(Enter age (1 - 100): )), CallStmt(Readln, Id(age)), IfStmt(BinExpr(<, Id(age), IntegerLit(1)), CallStmt(Writeln, StringLit(Age cannot be less than 1...))), IfStmt(BinExpr(>, Id(age), IntegerLit(100)), CallStmt(Writeln, StringLit(Age cannot be greater than 100...)))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 356))

        def test_program_57(self):
            input = """
                       x, y, z: array [5] of integer;
                       a,b,c: auto = 1,2.3,true;
                       s,g,r : auto = x, y, z;

                    main: function void(){

                    }
                    """
            expect = """Program([
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, FloatLit(2.3))
	VarDecl(c, AutoType, BooleanLit(True))
	VarDecl(s, AutoType, Id(x))
	VarDecl(g, AutoType, Id(y))
	VarDecl(r, AutoType, Id(z))
	FuncDecl(main, VoidType, [], None, BlockStmt([]))
])"""
            self.assertTrue(TestAST.test(input, expect, 357))

        def test_program_58(self):
            input = """
                    main: function void(){
                         s = {true, true, false, true};
                         i: integer = 0;
                         for(i = 0, i<10, i+1)
                         {
                            while(s[i] == true)
                                {
                                    j: integer;
                                    for(j = 0, j<10, j + 1)
                                        {
                                            do{
                                                s[i] = s[j] + j * i;
                                                if(true)
                                                    print("absdlfasdf");
                                                else
                                                    break;
                                            } while(s[i + j] == !true);
                                        }
                                }
                         }
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False), BooleanLit(True)])), VarDecl(i, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(==, ArrayCell(s, [Id(i)]), BooleanLit(True)), BlockStmt([VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(10)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(==, ArrayCell(s, [BinExpr(+, Id(i), Id(j))]), UnExpr(!, BooleanLit(True))), BlockStmt([AssignStmt(ArrayCell(s, [Id(i)]), BinExpr(+, ArrayCell(s, [Id(j)]), BinExpr(*, Id(j), Id(i)))), IfStmt(BooleanLit(True), CallStmt(print, StringLit(absdlfasdf)), BreakStmt())]))]))]))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 358))

        def test_program_59(self):
            input = """
                    age : integer;
                    x, y, z: array [5] of integer;
                       a,b,c: auto = 1,2.3,true;
                       s,g,r : auto = x + age, y - age, z*foo(age);
                    main: function void(){
                         s = {true, true, false, true};
                         while ((age > 0) && (age <= 100)) {
                            Write("Enter age (1 - 100): ");
    		                Readln(age);
    		                if (age < 1)
    			                Writeln("Age cannot be less than 1...");
    		                if (age > 100)
    			                Writeln("Age cannot be greater than 100...");
                         }
               }
                    """
            expect = """Program([
	VarDecl(age, IntegerType)
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, FloatLit(2.3))
	VarDecl(c, AutoType, BooleanLit(True))
	VarDecl(s, AutoType, BinExpr(+, Id(x), Id(age)))
	VarDecl(g, AutoType, BinExpr(-, Id(y), Id(age)))
	VarDecl(r, AutoType, BinExpr(*, Id(z), FuncCall(foo, [Id(age)])))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False), BooleanLit(True)])), WhileStmt(BinExpr(&&, BinExpr(>, Id(age), IntegerLit(0)), BinExpr(<=, Id(age), IntegerLit(100))), BlockStmt([CallStmt(Write, StringLit(Enter age (1 - 100): )), CallStmt(Readln, Id(age)), IfStmt(BinExpr(<, Id(age), IntegerLit(1)), CallStmt(Writeln, StringLit(Age cannot be less than 1...))), IfStmt(BinExpr(>, Id(age), IntegerLit(100)), CallStmt(Writeln, StringLit(Age cannot be greater than 100...)))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 359))

        def test_program_60(self):
            input = """
                    age : integer;
                    x, y, z: array [5] of integer;
                       a,b,c: auto = 1,2.3,true;
                       s,g,r : auto = x + age, y - age, z*foo(age);
                    main: function void(){
                         s = {true, true, false, true};
                         s = {s == g, a > b, s[0] || s[1]};
                         while ((age > 0) && (age <= 100)) {
                            Write("Enter age (1 - 100): ");
    		                Readln(age);
    		                if (age < 1)
    			                Writeln("Age cannot be less than 1...");
    		                if (age > 100)
    			                Writeln("Age cannot be greater than 100...");
                         }
               }
                    """
            expect = """Program([
	VarDecl(age, IntegerType)
	VarDecl(x, ArrayType([5], IntegerType))
	VarDecl(y, ArrayType([5], IntegerType))
	VarDecl(z, ArrayType([5], IntegerType))
	VarDecl(a, AutoType, IntegerLit(1))
	VarDecl(b, AutoType, FloatLit(2.3))
	VarDecl(c, AutoType, BooleanLit(True))
	VarDecl(s, AutoType, BinExpr(+, Id(x), Id(age)))
	VarDecl(g, AutoType, BinExpr(-, Id(y), Id(age)))
	VarDecl(r, AutoType, BinExpr(*, Id(z), FuncCall(foo, [Id(age)])))
	FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(s), ArrayLit([BooleanLit(True), BooleanLit(True), BooleanLit(False), BooleanLit(True)])), AssignStmt(Id(s), ArrayLit([BinExpr(==, Id(s), Id(g)), BinExpr(>, Id(a), Id(b)), BinExpr(||, ArrayCell(s, [IntegerLit(0)]), ArrayCell(s, [IntegerLit(1)]))])), WhileStmt(BinExpr(&&, BinExpr(>, Id(age), IntegerLit(0)), BinExpr(<=, Id(age), IntegerLit(100))), BlockStmt([CallStmt(Write, StringLit(Enter age (1 - 100): )), CallStmt(Readln, Id(age)), IfStmt(BinExpr(<, Id(age), IntegerLit(1)), CallStmt(Writeln, StringLit(Age cannot be less than 1...))), IfStmt(BinExpr(>, Id(age), IntegerLit(100)), CallStmt(Writeln, StringLit(Age cannot be greater than 100...)))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 360))

            # /////////////////////////////////////////////////////////////#

        def test_program_61(self):
            input = """
            foo: function void (x: integer, a_123: string) {
                i: integer = 150;
                {
                    {
                        while (true) {
                            return -1;
                            for (i = 150, i > 0, i-1) {
                                writeln("as;djfs;ghsdjfewofj");
                            }
                        }
                    }
                }
            }
            """
            expect = """Program([
	FuncDecl(foo, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(150)), BlockStmt([BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([ReturnStmt(UnExpr(-, IntegerLit(1))), ForStmt(AssignStmt(Id(i), IntegerLit(150)), BinExpr(>, Id(i), IntegerLit(0)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeln, StringLit(as;djfs;ghsdjfewofj))]))]))])])]))
])"""
            self.assertTrue(TestAST.test(input, expect, 361))

        def test_program_62(self):
            input = """
            main: function void (x: integer, a_123: string) {
                i: integer =0;
                {
                    {
                        a[1+foo(2)] = 5 + 3 + 2 * 2;
                    }
                }
            }
            """
            expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2))))])])]))
])"""
            self.assertTrue(TestAST.test(input, expect, 362))

        def test_program_63(self):
            input = """
            main: function void (x: integer, a_123: string) {
                i: integer =0;
                {
                    {
                        a[1+foo(2)] = 5 + 3 + 2 * 2;
                    }
                }
            }
            """
            expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2))))])])]))
])"""
            self.assertTrue(TestAST.test(input, expect, 363))

        def test_program_64(self):
            input = """
            main: function void (x: integer, a_123: string) {
                i: integer =0;
                {
                    {
                        a[1+foo(2)] = f1();
                    }
                }
            }
            """
            expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), FuncCall(f1, []))])])]))
])"""
            self.assertTrue(TestAST.test(input, expect, 364))

        def test_program_65(self):
            input = """
            main: function void (x: integer, a_123: string) {
                i: integer =0;

                        a[1+foo(2)] = 5 + 3 + 2 * 2;
                        while (x > 1) {
                            do {
                                while (n < 1) {
                                    for (i = 3.20, i < 10, i+2) {
                                        return;
                                    }
                                }
                            } while(true);
                            i = i + 1;
                        }

            }
            """
            expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BooleanLit(True), BlockStmt([WhileStmt(BinExpr(<, Id(n), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), FloatLit(3.2)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ReturnStmt()]))]))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 365))

        def test_program_66(self):
            input = """
            main: function void (x: integer, a_123: string) {
                i: integer =0;
                    a[1+foo(2)] = 5 + 3 + 2 * 2;
                        while (x > 1) {
                            do {
                                while (n < 1) {
                                    for (i = 3.202, i < 10, i+2) {
                                        return;
                                    }
                                }
                            }while(false);
                            i = i + 1;
                        }

            }
            """
            expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BooleanLit(False), BlockStmt([WhileStmt(BinExpr(<, Id(n), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), FloatLit(3.202)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ReturnStmt()]))]))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 366))

        def test_program_67(self):
            input = """
            main: function void (x: integer, a_123: string) {
                i: integer =0;
                {
                    {
                        a[1+foo(2)] = 5 + 3 + 2 * 2;
                         while (x > 1) {
                            if (x == 1)
                            i = i + 1;
                            break;
                            for (i = 0, i <= 10, i + (1_000_1.03)) {
                                writeln();
                            }
                        }
                    }
                }
            }
            """
            expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(x), IntegerLit(1)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))), BreakStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<=, Id(i), IntegerLit(10)), BinExpr(+, Id(i), FloatLit(10001.03)), BlockStmt([CallStmt(writeln, )]))]))])])]))
])"""
            self.assertTrue(TestAST.test(input, expect, 367))

        def test_program_268(self):
            input = """
            main: function void (x: integer, a_123: string) {
                i: integer =0;
                {
                    {
                        a[1+foo(2)] = 5 + 3 + 2 * 2;
                        while (x > 1) {
                            do {
                                while (n < 1) {
                                    for (i = 3.202, i < 10, i+2) {
                                        return;
                                    }
                                }
                            }
                            while (x > 1);
                            i = i + 1;
                        }
                    }
                }
            }
            """
            expect = """Program([
	FuncDecl(main, VoidType, [Param(x, IntegerType), Param(a_123, StringType)], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(0)), BlockStmt([BlockStmt([AssignStmt(ArrayCell(a, [BinExpr(+, IntegerLit(1), FuncCall(foo, [IntegerLit(2)]))]), BinExpr(+, BinExpr(+, IntegerLit(5), IntegerLit(3)), BinExpr(*, IntegerLit(2), IntegerLit(2)))), WhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([DoWhileStmt(BinExpr(>, Id(x), IntegerLit(1)), BlockStmt([WhileStmt(BinExpr(<, Id(n), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), FloatLit(3.202)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([ReturnStmt()]))]))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))])])]))
])"""
            self.assertTrue(TestAST.test(input, expect, 368))

        def test_program_269(self):
            input = """
            main: function void(){
        a, b, c, delta, x1, x2 : float = readFloat(), readFloat(), readFloat(), readFloat(), readFloat(), readFloat();
        delta = b * b - 4 * a * c;
        if (delta < 0) {
            printString("The equation has no real roots.\\n");
        } else  {
            x1 = -b / (2 * a);
            printString("The only solution is: \\n");
        }
    }
            """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FuncCall(readFloat, [])), VarDecl(b, FloatType, FuncCall(readFloat, [])), VarDecl(c, FloatType, FuncCall(readFloat, [])), VarDecl(delta, FloatType, FuncCall(readFloat, [])), VarDecl(x1, FloatType, FuncCall(readFloat, [])), VarDecl(x2, FloatType, FuncCall(readFloat, [])), AssignStmt(Id(delta), BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), IfStmt(BinExpr(<, Id(delta), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(The equation has no real roots.\\n))]), BlockStmt([AssignStmt(Id(x1), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printString, StringLit(The only solution is: \\n))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 369))

        def test_program_270(self):
            input = """
            main: function void () {
                for (i[0] = 1, i[0] < 10, i[0]+1)
                    print(":");
            }
            """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(ArrayCell(i, [IntegerLit(0)]), IntegerLit(1)), BinExpr(<, ArrayCell(i, [IntegerLit(0)]), IntegerLit(10)), BinExpr(+, ArrayCell(i, [IntegerLit(0)]), IntegerLit(1)), CallStmt(print, StringLit(:)))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 370))

        def test_program_271(self):
            input = """
            fact: function integer (n: integer) {
                while ((n == 10) || (n == 20) && (n == 30)) {
                        delta: integer = fact(3);
                        inc(x, delta, alpha);
                        do {printHello();}
                        while (1 + 4 == 2);
                    }
                }
            main: function void () {
                a, b,c: integer = 4,3,55;
                fact(c+10);
            }
            """
            expect = """Program([
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(||, BinExpr(==, Id(n), IntegerLit(10)), BinExpr(==, Id(n), IntegerLit(20))), BinExpr(==, Id(n), IntegerLit(30))), BlockStmt([VarDecl(delta, IntegerType, FuncCall(fact, [IntegerLit(3)])), CallStmt(inc, Id(x), Id(delta), Id(alpha)), DoWhileStmt(BinExpr(==, BinExpr(+, IntegerLit(1), IntegerLit(4)), IntegerLit(2)), BlockStmt([CallStmt(printHello, )]))]))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(4)), VarDecl(b, IntegerType, IntegerLit(3)), VarDecl(c, IntegerType, IntegerLit(55)), CallStmt(fact, BinExpr(+, Id(c), IntegerLit(10)))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 371))

        def test_program_72(self):
            input = """
                    main: function void(){
                             x: array [3,3] of string;
                        x = {
                        {"aaa","bbb","ccc"}, {"eee","edc","esae"},{"ewq","eew","erwd"}
                        };
                        x[0,0] = x [1,2] :: ((x[2,2] :: x[1,0]) :: x[1,1]);
                        }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3, 3], StringType)), AssignStmt(Id(x), ArrayLit([ArrayLit([StringLit(aaa), StringLit(bbb), StringLit(ccc)]), ArrayLit([StringLit(eee), StringLit(edc), StringLit(esae)]), ArrayLit([StringLit(ewq), StringLit(eew), StringLit(erwd)])])), AssignStmt(ArrayCell(x, [IntegerLit(0), IntegerLit(0)]), BinExpr(::, ArrayCell(x, [IntegerLit(1), IntegerLit(2)]), BinExpr(::, BinExpr(::, ArrayCell(x, [IntegerLit(2), IntegerLit(2)]), ArrayCell(x, [IntegerLit(1), IntegerLit(0)])), ArrayCell(x, [IntegerLit(1), IntegerLit(1)]))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 372))

        def test_program_73(self):
            input = """
                    main: function void(){
                        i, j: integer;

                        for (i = 1, i <= 5, i+1) {
                            continue;
                        }

                    // sdffefg
                    j = 1;
                    while (j <= 5) {
                        j = j+2;
                    }

                    a,b : integer =10, 20;
                    if (a > b) {
                        printString("a lon hon b\t");
                    } else {
                        printString("a nho hon hoac bang b\t");
                    }
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ContinueStmt()])), AssignStmt(Id(j), IntegerLit(1)), WhileStmt(BinExpr(<=, Id(j), IntegerLit(5)), BlockStmt([AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(2)))])), VarDecl(a, IntegerType, IntegerLit(10)), VarDecl(b, IntegerType, IntegerLit(20)), IfStmt(BinExpr(>, Id(a), Id(b)), BlockStmt([CallStmt(printString, StringLit(a lon hon b	))]), BlockStmt([CallStmt(printString, StringLit(a nho hon hoac bang b	))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 373))

        def test_Program_74(self):

            input = """
                   main: function integer () {
                     n: integer;
                     n=readinteger();
                       if (n == 0) return 1;
                       else
                           return n * fact(n - 1);
                   }
                   inc: function void( n: integer, delta: integer) {
                       n = n + delta;
                       check: boolean = false;
                       if ((n>3)&&(delta<3))
                           check=true;
                       else check = false;
                       while ((n>3)&&(delta<3)){
                           printinteger(n);

                           delta=delta+4;
                           if (n==5) printNum(delta);
                       }
                   }"""
            expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readinteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), VarDecl(check, BooleanType, BooleanLit(False)), IfStmt(BinExpr(&&, BinExpr(>, Id(n), IntegerLit(3)), BinExpr(<, Id(delta), IntegerLit(3))), AssignStmt(Id(check), BooleanLit(True)), AssignStmt(Id(check), BooleanLit(False))), WhileStmt(BinExpr(&&, BinExpr(>, Id(n), IntegerLit(3)), BinExpr(<, Id(delta), IntegerLit(3))), BlockStmt([CallStmt(printinteger, Id(n)), AssignStmt(Id(delta), BinExpr(+, Id(delta), IntegerLit(4))), IfStmt(BinExpr(==, Id(n), IntegerLit(5)), CallStmt(printNum, Id(delta)))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 374))

        def test_Program_75(self):
            input = """
                    main: function integer () {
                        n: integer;
                        n=readInteger();
                        if (n == 0) return 1;
                        else return n * fact(n - 1);
                    }
                    inc: function void( n: integer, delta: integer) {
                        n = n + delta;
                        for (i = 1, i < 10, i + 1) {
                            writeInt(i);
                            if (i>3) { // if()
                            break; }
                            else continue; // add ()
                        }
                    }
                    """
            expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), BlockStmt([BreakStmt()]), ContinueStmt())]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 375))

        def test_program_76(self):
            input = """
                    main: function integer () {
                        n: integer;
                        n=readInteger();
               // if (n == 0) return 1;
               /*else return n * fact(n - 1); */
                    }
                    """
            expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, []))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 376))
    # ==============================================================

        def test_program_77(self):
            input = """
                    main: function void() {
                    arr: array [2] of boolean;
                    arr = {true, false};
                         if(true || arr[1])
                         {
                         x : integer;
                         }

                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([2], BooleanType)), AssignStmt(Id(arr), ArrayLit([BooleanLit(True), BooleanLit(False)])), IfStmt(BinExpr(||, BooleanLit(True), ArrayCell(arr, [IntegerLit(1)])), BlockStmt([VarDecl(x, IntegerType)]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 377))

        def test_Program_78(self):

            input = """
                   main: function void() {
                         if(true || 1+2 > 0)
                         {
                         x : integer;
                         }
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(>, BinExpr(||, BooleanLit(True), BinExpr(+, IntegerLit(1), IntegerLit(2))), IntegerLit(0)), BlockStmt([VarDecl(x, IntegerType)]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 378))

        def test_Program_79(self):
            input = """
                    main: function void() {
                            y: float;
                        y = 1 + 3.2 / 2;
                    }
                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(y, FloatType), AssignStmt(Id(y), BinExpr(+, IntegerLit(1), BinExpr(/, FloatLit(3.2), IntegerLit(2))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 379))

        def test_program_80(self):

            input = """
                    main: function integer () {
                     n: integer;
                     n=readInteger();
                       if (n == 0) return 1;
                       else
                           return n * fact(n - 1);
                   }
                   inc: function void( n: integer, delta: integer) {
                       n = n + delta;
                       check: boolean = false;
                       if ((n>3)&&(delta<3))
                           check=true;
                       else check = false;
                       do {
                           printInteger(n);

                           delta=delta+4;
                           if (n==5) printNum(delta);
                       }
                       while (n>3);
                   }
                    """
            expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), VarDecl(check, BooleanType, BooleanLit(False)), IfStmt(BinExpr(&&, BinExpr(>, Id(n), IntegerLit(3)), BinExpr(<, Id(delta), IntegerLit(3))), AssignStmt(Id(check), BooleanLit(True)), AssignStmt(Id(check), BooleanLit(False))), DoWhileStmt(BinExpr(>, Id(n), IntegerLit(3)), BlockStmt([CallStmt(printInteger, Id(n)), AssignStmt(Id(delta), BinExpr(+, Id(delta), IntegerLit(4))), IfStmt(BinExpr(==, Id(n), IntegerLit(5)), CallStmt(printNum, Id(delta)))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 380))

        def test_program_81(self):
            input = """
                    a: float;
                    main: function integer () {
                        foo();
                        bar(1);
                        nty(1,2,3);
                        pty(hyy, dyf(), ily(123, 456, fay), jtq(gyh())) ;
                    }

                    """
            expect = """Program([
	VarDecl(a, FloatType)
	FuncDecl(main, IntegerType, [], None, BlockStmt([CallStmt(foo, ), CallStmt(bar, IntegerLit(1)), CallStmt(nty, IntegerLit(1), IntegerLit(2), IntegerLit(3)), CallStmt(pty, Id(hyy), FuncCall(dyf, []), FuncCall(ily, [IntegerLit(123), IntegerLit(456), Id(fay)]), FuncCall(jtq, [FuncCall(gyh, [])]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 381))

        def test_program_82(self):

            input = """
                    a,b,c: float;
                    x,y,z: boolean;
                    g,h,y: integer;
                    nty: function boolean(){
                        x,y,z: integer;
                        readLine();
                        //this is readLine()
                        fs = readDtdin();
                        do{
                        for(i = 4, i>6, i - 1)
                            if (i >6) return 0;
                        } while(true && false);
                        return 1;
                    }
                    main: function integer () {
                        /*
                        nty();
                        a;sdf
                        */
                    }

                    """
            expect = """Program([
	VarDecl(a, FloatType)
	VarDecl(b, FloatType)
	VarDecl(c, FloatType)
	VarDecl(x, BooleanType)
	VarDecl(y, BooleanType)
	VarDecl(z, BooleanType)
	VarDecl(g, IntegerType)
	VarDecl(h, IntegerType)
	VarDecl(y, IntegerType)
	FuncDecl(nty, BooleanType, [], None, BlockStmt([VarDecl(x, IntegerType), VarDecl(y, IntegerType), VarDecl(z, IntegerType), CallStmt(readLine, ), AssignStmt(Id(fs), FuncCall(readDtdin, [])), DoWhileStmt(BinExpr(&&, BooleanLit(True), BooleanLit(False)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(4)), BinExpr(>, Id(i), IntegerLit(6)), BinExpr(-, Id(i), IntegerLit(1)), IfStmt(BinExpr(>, Id(i), IntegerLit(6)), ReturnStmt(IntegerLit(0))))])), ReturnStmt(IntegerLit(1))]))
	FuncDecl(main, IntegerType, [], None, BlockStmt([]))
])"""
            self.assertTrue(TestAST.test(input, expect, 382))

        def test_program_83(self):

            input = """

                    main: function integer () {
                        i = f(g(h[5*t]));
                    }

                    """
            expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(i), FuncCall(f, [FuncCall(g, [ArrayCell(h, [BinExpr(*, IntegerLit(5), Id(t))])])]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 383))

        def test_program_84(self):

            input = """

                    main: function integer () {
                        i = f(g(h[5*t(9,1)]));
                    }

                    """
            expect = """Program([
	FuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(i), FuncCall(f, [FuncCall(g, [ArrayCell(h, [BinExpr(*, IntegerLit(5), FuncCall(t, [IntegerLit(9), IntegerLit(1)]))])])]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 384))

        def test_program_85(self):

            input = """
                    nty: function float(){
                    c,y,t: integer;
                    // this is readlinee

                    htg(/*etsd*/);
                    }
                    main: function integer () {
                        i = f(g(h[5*t(9,1)]));
                        // nty(i)
                    }

                    """
            expect = """Program([
	FuncDecl(nty, FloatType, [], None, BlockStmt([VarDecl(c, IntegerType), VarDecl(y, IntegerType), VarDecl(t, IntegerType), CallStmt(htg, )]))
	FuncDecl(main, IntegerType, [], None, BlockStmt([AssignStmt(Id(i), FuncCall(f, [FuncCall(g, [ArrayCell(h, [BinExpr(*, IntegerLit(5), FuncCall(t, [IntegerLit(9), IntegerLit(1)]))])])]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 385))

        def test_program_86(self):

            input = """
                    main: function void () {
                        {
                            {
                                ok();
                            }
                        }
                    }

                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([BlockStmt([CallStmt(ok, )])])]))
])"""
            self.assertTrue(TestAST.test(input, expect, 386))

        def test_program_87(self):

            input = """
                    main: function void() {
                        r, c: integer;
                        // a[10,10], transpose[10,10]

                        a, transpose: array [10,10] of integer;

                    printf("Enter rows and columns: ");
                    scanf("%d %d", r, c);

                    // asssigning elements to the matrix
                    printf("\nEnter matrix elements:\n");
                    for (i = 0, i < r, i+1)
                    for (j = 0, j < c, j+1) {
                        printf("Enter element a%d%d: ", i + 1, j + 1);
                        scanf("%d", a[i,j]);
                    }

                    // printing the matrix a[][]
                    printf("\nEntered matrix: \n");
                    for (i= 0, i < r, i+1)
                    for (j = 0, j < c, j+1) {
                        printf("%d  ", a[i,j]);
                        if (j == c - 1)
                        printf("\n");
                    }

                    // computing the transpose
                    for (i = 0, i < r, i+1)
                    for (j = 0, j < c, j+1) {
                        transpose[j,i] = a[i,j];
                    }
                }

                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(c, IntegerType), VarDecl(a, ArrayType([10, 10], IntegerType)), VarDecl(transpose, ArrayType([10, 10], IntegerType)), CallStmt(printf, StringLit(Enter rows and columns: )), CallStmt(scanf, StringLit(%d %d), Id(r), Id(c)), CallStmt(printf, StringLit(
Enter matrix elements:
)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(Enter element a%d%d: ), BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(j), IntegerLit(1))), CallStmt(scanf, StringLit(%d), ArrayCell(a, [Id(i), Id(j)]))]))), CallStmt(printf, StringLit(
Entered matrix: 
)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(%d  ), ArrayCell(a, [Id(i), Id(j)])), IfStmt(BinExpr(==, Id(j), BinExpr(-, Id(c), IntegerLit(1))), CallStmt(printf, StringLit(
)))]))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(transpose, [Id(j), Id(i)]), ArrayCell(a, [Id(i), Id(j)]))])))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 387))

        def test_program_88(self):

            input = """
                    main: function void() {
                        n: integer;
                        printf("\nNhap n = ");
                        scanf("%d", n);
                        if(n < 2){
                            printf("\n%d khong phai so nguyen to", n);
                            return 0;
                        }
                        count: integer = 0;
                        for(i = 2, i <= sqrt(n), i+1){
                            if(n % i == 0){
                            count = count + 1;
                            }
                        }
                        if(count == 0){
                            printf("\n%d la so nguyen to", n);
                        }else{
                            printf("\n%d khong phai so nguyen to", n);
                        }
                    }

                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(n, IntegerType), CallStmt(printf, StringLit(
Nhap n = )), CallStmt(scanf, StringLit(%d), Id(n)), IfStmt(BinExpr(<, Id(n), IntegerLit(2)), BlockStmt([CallStmt(printf, StringLit(
%d khong phai so nguyen to), Id(n)), ReturnStmt(IntegerLit(0))])), VarDecl(count, IntegerType, IntegerLit(0)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), FuncCall(sqrt, [Id(n)])), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), BlockStmt([AssignStmt(Id(count), BinExpr(+, Id(count), IntegerLit(1)))]))])), IfStmt(BinExpr(==, Id(count), IntegerLit(0)), BlockStmt([CallStmt(printf, StringLit(
%d la so nguyen to), Id(n))]), BlockStmt([CallStmt(printf, StringLit(
%d khong phai so nguyen to), Id(n))]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 388))

        def test_program_89(self):

            input = """
                    main: function void() {
                        a: float = 10.21e2;
                        b: float = 0.21e2;
                        c: float = 10_123_32e3;
                        d: float = 2.e2;
                        e: float = .e3;
                        r, s: integer;
                        a, b: array [10] of integer;
                        r = 4.0;
                        s = r * myPI;
                        a[0] = s;
                    }

                    """
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(1021.0)), VarDecl(b, FloatType, FloatLit(21.0)), VarDecl(c, FloatType, FloatLit(1012332000.0)), VarDecl(d, FloatType, FloatLit(200.0)), VarDecl(e, FloatType, FloatLit(0.0)), VarDecl(r, IntegerType), VarDecl(s, IntegerType), VarDecl(a, ArrayType([10], IntegerType)), VarDecl(b, ArrayType([10], IntegerType)), AssignStmt(Id(r), FloatLit(4.0)), AssignStmt(Id(s), BinExpr(*, Id(r), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 389))

        def test_program_90(self):

            input = """
                    giaiPT: function integer(a: float, b: float, c: float ,out x1: float,out x2: float){
                        delta: float = b*b - 4*a*c;
                        if(delta<0){
                            x1= 0.0;
                            x2= x1;
                            return 0;
                        }
                        else if(delta==0){
                            x1 = -b/(2*a);
                            x2 = -b/(2*a);
                            return 1;
                            }
                            else{
                                delta = sqrt(delta);
                                x1 = (-b + delta) / (2*a);
                                x2 = (-b - delta) / (2*a);
                                return 2;
                            }
                    }
                    main: function void(){
                        a,b,c: float;
                        x1,x2: float;
                        do{
                            printf("Nhap a (a!=0): ");
                            scanf("%f",a);
                            printf("Nhap b: ");
                            scanf("%f",b);
                            printf("Nhap c: ");
                            scanf("%f",c);
                        }
                        while(!a);// Neu a=0 the nhap lai
                        numNo:integer = giaiPT(a,b,c,x1,x2);
                        if(numNo == 0) {
                            printf("Phuong trinh da cho vo nghiem");
                        }
                        else if(numNo == 1){
                            printf("Phuong trinh da cho co nghiem kep x=%.4f",x1);
                            }
                            else{
                            printf("Phuong trinh da cho co hai nghiem phan biet\nx1=%.4f \nx2=%.4f",x1,x2);
                            }
                    }
                    """
            expect = """Program([
	FuncDecl(giaiPT, IntegerType, [Param(a, FloatType), Param(b, FloatType), Param(c, FloatType), OutParam(x1, FloatType), OutParam(x2, FloatType)], None, BlockStmt([VarDecl(delta, FloatType, BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), IfStmt(BinExpr(<, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x1), FloatLit(0.0)), AssignStmt(Id(x2), Id(x1)), ReturnStmt(IntegerLit(0))]), IfStmt(BinExpr(==, Id(delta), IntegerLit(0)), BlockStmt([AssignStmt(Id(x1), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, UnExpr(-, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), ReturnStmt(IntegerLit(1))]), BlockStmt([AssignStmt(Id(delta), FuncCall(sqrt, [Id(delta)])), AssignStmt(Id(x1), BinExpr(/, BinExpr(+, UnExpr(-, Id(b)), Id(delta)), BinExpr(*, IntegerLit(2), Id(a)))), AssignStmt(Id(x2), BinExpr(/, BinExpr(-, UnExpr(-, Id(b)), Id(delta)), BinExpr(*, IntegerLit(2), Id(a)))), ReturnStmt(IntegerLit(2))])))]))
	FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(c, FloatType), VarDecl(x1, FloatType), VarDecl(x2, FloatType), DoWhileStmt(UnExpr(!, Id(a)), BlockStmt([CallStmt(printf, StringLit(Nhap a (a!=0): )), CallStmt(scanf, StringLit(%f), Id(a)), CallStmt(printf, StringLit(Nhap b: )), CallStmt(scanf, StringLit(%f), Id(b)), CallStmt(printf, StringLit(Nhap c: )), CallStmt(scanf, StringLit(%f), Id(c))])), VarDecl(numNo, IntegerType, FuncCall(giaiPT, [Id(a), Id(b), Id(c), Id(x1), Id(x2)])), IfStmt(BinExpr(==, Id(numNo), IntegerLit(0)), BlockStmt([CallStmt(printf, StringLit(Phuong trinh da cho vo nghiem))]), IfStmt(BinExpr(==, Id(numNo), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(Phuong trinh da cho co nghiem kep x=%.4f), Id(x1))]), BlockStmt([CallStmt(printf, StringLit(Phuong trinh da cho co hai nghiem phan biet
x1=%.4f 
x2=%.4f), Id(x1), Id(x2))])))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 390))
        def test_program_91(self):
            input = """main1 : function string () {
                bool = "abc\\t" != "abc\t" ;
                return ;
                }"""
            expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(!=, StringLit(abc\\t), StringLit(abc	))), ReturnStmt()]))
])"""
            self.assertTrue(TestAST.test(input, expect, 391))

        def test_program_92(self):
            """More complex program"""
            input = """main1 : function string () {
                bool = ((1 < 2) < 3) < 4 ;
                return ;
                }"""
            expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(<, BinExpr(<, BinExpr(<, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4))), ReturnStmt()]))
])"""
            self.assertTrue(TestAST.test(input, expect, 392))

        def test_program_93(self):
            """More complex program"""
            input = """main1 : function string () {
                str = (("abc" :: "cde") :: "123") :: "456" ;
                return ;
                }"""
            expect = """Program([
	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(::, BinExpr(::, BinExpr(::, StringLit(abc), StringLit(cde)), StringLit(123)), StringLit(456))), ReturnStmt()]))
])"""
            self.assertTrue(TestAST.test(input, expect, 393))

        def test_progaram_94(self):

            input = """
            a : string = "213123213\\'" ;
            str : string = "\ttoo(;_;)many(;_;)test(;_;)cases(;_;)\t" ;

                """
            expect = """Program([
	VarDecl(a, StringType, StringLit(213123213\\'))
	VarDecl(str, StringType, StringLit(	too(;_;)many(;_;)test(;_;)cases(;_;)	))
])"""
            self.assertTrue(TestAST.test(input, expect, 394))

        def test_program_95(self):
            """More complex program"""
            input = """main1 : function array [2,2] of string (inherit a : array [2,3] of string, out b : array [3,3] of boolean) {
                while(a < 23)
                do {a = a / 9 ;}
                while (a > 100) ;
                }"""
            expect = """Program([
	FuncDecl(main1, ArrayType([2, 2], StringType), [InheritParam(a, ArrayType([2, 3], StringType)), OutParam(b, ArrayType([3, 3], BooleanType))], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))])))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 395))

        def test_program_96(self):
            """Simple program"""
            input = """main: function void () {
                    if (a == 9) b = 7 ;
                    else if (c == 9) b = 5 ;
                    else b = 20 ;
            }"""
            expect = """Program([
	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(7)), IfStmt(BinExpr(==, Id(c), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(5)), AssignStmt(Id(b), IntegerLit(20))))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 396))

        def test_program_97(self):
            """More complex program"""
            input = """func1 : function auto (out a : array [3,8] of integer, inherit b : float) {
                randfloat : float = 1_332.33e-23 ;
                randarr : array [7] of string ;
                return 2233;
                }
            func2 : function void (c : string, out d : array [2,3] of boolean) inherit func1 {
                if(a == 5) c = a % 7 ;
                else d = a / 8 ;
                randarr = arr1[1+1,3_3/3,5%4] + 332 - arr2[9/3]  ;
                return;
                }"""
            expect = """Program([
	FuncDecl(func1, AutoType, [OutParam(a, ArrayType([3, 8], IntegerType)), InheritParam(b, FloatType)], None, BlockStmt([VarDecl(randfloat, FloatType, FloatLit(1.33233e-20)), VarDecl(randarr, ArrayType([7], StringType)), ReturnStmt(IntegerLit(2233))]))
	FuncDecl(func2, VoidType, [Param(c, StringType), OutParam(d, ArrayType([2, 3], BooleanType))], func1, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), AssignStmt(Id(d), BinExpr(/, Id(a), IntegerLit(8)))), AssignStmt(Id(randarr), BinExpr(-, BinExpr(+, ArrayCell(arr1, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(/, IntegerLit(33), IntegerLit(3)), BinExpr(%, IntegerLit(5), IntegerLit(4))]), IntegerLit(332)), ArrayCell(arr2, [BinExpr(/, IntegerLit(9), IntegerLit(3))]))), ReturnStmt()]))
])"""
            self.assertTrue(TestAST.test(input, expect, 397))

        def test_program_98(self):
            """More complex program"""
            input = """func1 : function float (c : string, out d : boolean) {
                if(a == 5) c = a % 7 ;
                else if (a == 4) for (i = 8, i < 20, i / 2) { c = c + 1 ; }
                return 1.223e20 ;
                }"""
            expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), IfStmt(BinExpr(==, Id(a), IntegerLit(4)), ForStmt(AssignStmt(Id(i), IntegerLit(8)), BinExpr(<, Id(i), IntegerLit(20)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))])))), ReturnStmt(FloatLit(1.223e+20))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 398))

        def test_program_99(self):
            """More complex program"""
            input = """func1 : function float (c : string, out d : boolean) {
                if(a == 7) c = a % 7 ;
                else while (i < 20) { c = c + 1 ; }
                }"""
            expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(7)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), WhileStmt(BinExpr(<, Id(i), IntegerLit(20)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))])))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 399))

        def test_program_100(self):
            """More complex program"""
            input = """func1 : function float (c : string, out d : boolean) {
                    arr1, arr2, arr3 : array [2,2,2_3] of boolean = {}, {{},{}}, {{{{{}}}}} ;
                }"""
            expect = """Program([
	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(arr1, ArrayType([2, 2, 23], BooleanType), ArrayLit([])), VarDecl(arr2, ArrayType([2, 2, 23], BooleanType), ArrayLit([ArrayLit([]), ArrayLit([])])), VarDecl(arr3, ArrayType([2, 2, 23], BooleanType), ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([])])])])]))]))
])"""
            self.assertTrue(TestAST.test(input, expect, 400))

    # =====================================================================
    #     def test1(self):
    #         input = """x,y,z,a,b,c: array [1,2,3] of integer; a,b,c: array [4,6,7] of float;"""
    #         expect = """Program([
    # 	VarDecl(x, ArrayType([1, 2, 3], IntegerType))
    # 	VarDecl(y, ArrayType([1, 2, 3], IntegerType))
    # 	VarDecl(z, ArrayType([1, 2, 3], IntegerType))
    # 	VarDecl(a, ArrayType([1, 2, 3], IntegerType))
    # 	VarDecl(b, ArrayType([1, 2, 3], IntegerType))
    # 	VarDecl(c, ArrayType([1, 2, 3], IntegerType))
    # 	VarDecl(a, ArrayType([4, 6, 7], FloatType))
    # 	VarDecl(b, ArrayType([4, 6, 7], FloatType))
    # 	VarDecl(c, ArrayType([4, 6, 7], FloatType))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 301))

    #     def test2(self):
    #         input = """a, b, c: array[3,4] of integer = {1,2,3}, {}, {};"""
    #         expect = """Program([
    # 	VarDecl(a, ArrayType([3, 4], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
    # 	VarDecl(b, ArrayType([3, 4], IntegerType), ArrayLit([]))
    # 	VarDecl(c, ArrayType([3, 4], IntegerType), ArrayLit([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 302))

    #     def test3(self):
    #         input = """x, y, z: float = 1.2, 3e12, 1_33.33e-23;"""
    #         expect = """Program([
    # 	VarDecl(x, FloatType, FloatLit(1.2))
    # 	VarDecl(y, FloatType, FloatLit(3e12))
    # 	VarDecl(z, FloatType, FloatLit(133.33e-23))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 303))

    #     def test4(self):
    #         input = """x, y, z: boolean = true, false, true;"""
    #         expect = """Program([
    # 	VarDecl(x, BooleanType, BooleanLit(True))
    # 	VarDecl(y, BooleanType, BooleanLit(False))
    # 	VarDecl(z, BooleanType, BooleanLit(True))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 304))

    #     def test5(self):
    #         input = """x, y : integer = func(1,2,3), func1() ;"""
    #         expect = """Program([
    # 	VarDecl(x, IntegerType, FuncCall(func, [IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
    # 	VarDecl(y, IntegerType, FuncCall(func1, []))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 305))

    #     def test6(self):
    #         input = """x, y : integer = arr[0, 1, 2], arr1[4, 5, 6] ;"""
    #         expect = """Program([
    # 	VarDecl(x, IntegerType, ArrayCell(arr, [IntegerLit(0), IntegerLit(1), IntegerLit(2)]))
    # 	VarDecl(y, IntegerType, ArrayCell(arr1, [IntegerLit(4), IntegerLit(5), IntegerLit(6)]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 306))

    #     def test7(self):
    #         input = """x, y : integer = a, b ;"""
    #         expect = """Program([
    # 	VarDecl(x, IntegerType, Id(a))
    # 	VarDecl(y, IntegerType, Id(b))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 307))

    #     def test8(self):
    #         input = """x : string = "abc" ;"""
    #         expect = """Program([
    # 	VarDecl(x, StringType, StringLit(abc))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 308))

    #     def test9(self):
    #         input = """x : string = ("abc"::"cde")::"xyz" ;"""
    #         expect = """Program([
    # 	VarDecl(x, StringType, BinExpr(::, BinExpr(::, StringLit(abc), StringLit(cde)), StringLit(xyz)))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 309))

    #     def test10(self):
    #         input = """x : boolean = (a == 9) > (5 == 8) ;"""
    #         expect = """Program([
    # 	VarDecl(x, BooleanType, BinExpr(>, BinExpr(==, Id(a), IntegerLit(9)), BinExpr(==, IntegerLit(5), IntegerLit(8))))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 310))

    #     def test11(self):
    #         input = """x : boolean = a || b || c || d && e ;"""
    #         expect = """Program([
    # 	VarDecl(x, BooleanType, BinExpr(&&, BinExpr(||, BinExpr(||, BinExpr(||, Id(a), Id(b)), Id(c)), Id(d)), Id(e)))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 311))

    #     def test12(self):
    #         input = """x : float = 1 * a - 2.33e-32 / 33 + b % 33;"""
    #         expect = """Program([
    # 	VarDecl(x, FloatType, BinExpr(+, BinExpr(-, BinExpr(*, IntegerLit(1), Id(a)), BinExpr(/, FloatLit(2.33e-32), IntegerLit(33))), BinExpr(%, Id(b), IntegerLit(33))))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 312))

    #     def test13(self):
    #         input = """a,b,c: array[3,4,5] of integer = {},{{},{}}, {{{},{}},{}};"""
    #         expect = """Program([
    # 	VarDecl(a, ArrayType([3, 4, 5], IntegerType), ArrayLit([]))
    # 	VarDecl(b, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([]), ArrayLit([])]))
    # 	VarDecl(c, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([ArrayLit([]), ArrayLit([])]), ArrayLit([])]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 313))

    #     def test14(self):
    #         input = """a,b,c: array[3,4,5] of integer = {1,2,3},{{1,2},{3,4}}, {{{1,22},{33,4}},{77,88}};"""
    #         expect = """Program([
    # 	VarDecl(a, ArrayType([3, 4, 5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]))
    # 	VarDecl(b, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(3), IntegerLit(4)])]))
    # 	VarDecl(c, ArrayType([3, 4, 5], IntegerType), ArrayLit([ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(22)]), ArrayLit([IntegerLit(33), IntegerLit(4)])]), ArrayLit([IntegerLit(77), IntegerLit(88)])]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 314))

    #     def test15(self):
    #         """Simple program"""
    #         input = """main: function void () {

    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 315))

    #     def test16(self):
    #         """Simple program"""
    #         input = """main: function void (inherit a : integer, out b : float, inherit out c : boolean) {
    #                 int1: integer = a + b / c;
    #                 int2: integer = 1 + 3 - 8 ;
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [InheritParam(a, IntegerType), OutParam(b, FloatType), InheritOutParam(c, BooleanType)], None, BlockStmt([VarDecl(int1, IntegerType, BinExpr(+, Id(a), BinExpr(/, Id(b), Id(c)))), VarDecl(int2, IntegerType, BinExpr(-, BinExpr(+, IntegerLit(1), IntegerLit(3)), IntegerLit(8)))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 316))

    #     def test17(self):
    #         """Simple program"""
    #         input = """main: function void () {
    #                 if (a == 9) b = 7 ;
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(7)))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 317))

    #     def test18(self):
    #         """Simple program"""
    #         input = """main: function void () {
    #                 if (a == 9) b = 7 ;
    #                 else if (c == 9) b = 5 ;
    #                 else b = 20 ;
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(7)), IfStmt(BinExpr(==, Id(c), IntegerLit(9)), AssignStmt(Id(b), IntegerLit(5)), AssignStmt(Id(b), IntegerLit(20))))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 318))

    #     def test19(self):
    #         """Simple program"""
    #         input = """foo: function void (inherit a: integer, inherit out b: float) inherit bar {}
    #         main: function void () {
    #         {
    #         }
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(foo, VoidType, [InheritParam(a, IntegerType), InheritOutParam(b, FloatType)], bar, BlockStmt([]))
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([BlockStmt([])]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 319))

    #     def test20(self):
    #         """Simple program"""
    #         input = """main: function void () {
    #                 if (a == 9)
    #                 {
    #                         for (i = 5, i < 10, i + 1) a = a + i;
    #                 }
    #                 else if (c == 9)
    #                 {
    #                         i : integer = 23 ;
    #                         while (i < 5) i = i + 1 ;
    #                 }
    #                 else b = 20 ;
    #                 return ;
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(9)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(5)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(+, Id(a), Id(i))))]), IfStmt(BinExpr(==, Id(c), IntegerLit(9)), BlockStmt([VarDecl(i, IntegerType, IntegerLit(23)), WhileStmt(BinExpr(<, Id(i), IntegerLit(5)), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1))))]), AssignStmt(Id(b), IntegerLit(20)))), ReturnStmt()]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 320))

    #     def test21(self):
    #         """More complex program"""
    #         input = """main: function void (a : array [1,2] of integer, b : string) {
    #             printInteger(4);
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, VoidType, [Param(a, ArrayType([1, 2], IntegerType)), Param(b, StringType)], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 321))

    #     def test22(self):
    #         """More complex program"""
    #         input = """main: function array [2,3] of string () {
    #             printInteger(4);
    #         }"""
    #         expect = """Program([
    # 	FuncDecl(main, ArrayType([2, 3], StringType), [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 322))

    #     def test23(self):
    #         """More complex program"""
    #         input = """func1 : function auto (out a : array [3,8] of integer, inherit b : float) {
    #             randfloat : float = 1_332.33e-23 ;
    #             randarr : array [7] of string ;
    #             return 2233;
    #             }
    #         func2 : function void (c : string, out d : array [2,3] of boolean) inherit func1 {
    #             if(a == 5) c = a % 7 ;
    #             else d = a / 8 ;
    #             randarr = arr1[1+1,3_3/3,5%4] + 332 - arr2[9/3]  ;
    #             return;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(func1, AutoType, [OutParam(a, ArrayType([3, 8], IntegerType)), InheritParam(b, FloatType)], None, BlockStmt([VarDecl(randfloat, FloatType, FloatLit(1332.33e-23)), VarDecl(randarr, ArrayType([7], StringType)), ReturnStmt(IntegerLit(2233))]))
    # 	FuncDecl(func2, VoidType, [Param(c, StringType), OutParam(d, ArrayType([2, 3], BooleanType))], func1, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), AssignStmt(Id(d), BinExpr(/, Id(a), IntegerLit(8)))), AssignStmt(Id(randarr), BinExpr(-, BinExpr(+, ArrayCell(arr1, [BinExpr(+, IntegerLit(1), IntegerLit(1)), BinExpr(/, IntegerLit(33), IntegerLit(3)), BinExpr(%, IntegerLit(5), IntegerLit(4))]), IntegerLit(332)), ArrayCell(arr2, [BinExpr(/, IntegerLit(9), IntegerLit(3))]))), ReturnStmt()]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 323))

    #     def test24(self):
    #         """More complex program"""
    #         input = """func1 : function float (c : string, out d : boolean) {
    #             if(a == 5) c = a % 7 ;
    #             else if (a == 4) for (i = 8, i < 20, i / 2) { c = c + 1 ; }
    #             return 1.223e20 ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(5)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), IfStmt(BinExpr(==, Id(a), IntegerLit(4)), ForStmt(AssignStmt(Id(i), IntegerLit(8)), BinExpr(<, Id(i), IntegerLit(20)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))])))), ReturnStmt(FloatLit(1.223e20))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 324))

    #     def test25(self):
    #         """More complex program"""
    #         input = """func1 : function float (c : string, out d : boolean) {
    #             if(a == 7) c = a % 7 ;
    #             else while (i < 20) { c = c + 1 ; }
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(7)), AssignStmt(Id(c), BinExpr(%, Id(a), IntegerLit(7))), WhileStmt(BinExpr(<, Id(i), IntegerLit(20)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))])))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 325))

    #     def test26(self):
    #         """More complex program"""
    #         input = """func1 : function float (c : string, out d : boolean) {
    #                 arr1, arr2, arr3 : array [2,2,2_3] of boolean = {}, {{},{}}, {{{{{}}}}} ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(arr1, ArrayType([2, 2, 23], BooleanType), ArrayLit([])), VarDecl(arr2, ArrayType([2, 2, 23], BooleanType), ArrayLit([ArrayLit([]), ArrayLit([])])), VarDecl(arr3, ArrayType([2, 2, 23], BooleanType), ArrayLit([ArrayLit([ArrayLit([ArrayLit([ArrayLit([])])])])]))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 326))

    #     def test27(self):
    #         """More complex program"""
    #         input = """res : float = sin(a,b) / cos(c,d) ;"""
    #         expect = """Program([
    # 	VarDecl(res, FloatType, BinExpr(/, FuncCall(sin, [Id(a), Id(b)]), FuncCall(cos, [Id(c), Id(d)])))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 327))

    #     def test28(self):
    #         """More complex program"""
    #         input = """main1 : function string () {
    #             do {a = a / 9 ;}
    #             while (a > 100) ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))]))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 328))

    #     def test29(self):
    #         """More complex program"""
    #         input = """main1 : function string () {
    #             bool = "abc\\t" != "abc\t" ;
    #             return ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(!=, StringLit(abc\\t), StringLit(abc	))), ReturnStmt()]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 329))

    #     def test30(self):
    #         """More complex program"""
    #         input = """main1 : function string () {
    #             while(a < 23)
    #             do {a = a / 9 ;}
    #             while (a > 100) ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))])))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 330))

    #     def test31(self):
    #         """More complex program"""
    #         input = """main1 : function string () {
    #             bool = 7 - 9 < 4 - 6 ;
    #             return ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(<, BinExpr(-, IntegerLit(7), IntegerLit(9)), BinExpr(-, IntegerLit(4), IntegerLit(6)))), ReturnStmt()]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 331))

    #     def test32(self):
    #         """More complex program"""
    #         input = """main1 : function string () {
    #             str = 7 - 9 * 4 - 6 ;
    #             return ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(-, BinExpr(-, IntegerLit(7), BinExpr(*, IntegerLit(9), IntegerLit(4))), IntegerLit(6))), ReturnStmt()]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 332))

    #     def test33(self):
    #         """More complex program"""
    #         input = """main1 : function string () {
    #             str = (8 < 9) || (4 > 6) ;
    #             return ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(||, BinExpr(<, IntegerLit(8), IntegerLit(9)), BinExpr(>, IntegerLit(4), IntegerLit(6)))), ReturnStmt()]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 333))

    #     def test34(self):
    #         """More complex program"""
    #         input = """main1 : function string () {
    #             bool = ((1 < 2) < 3) < 4 ;
    #             return ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(bool), BinExpr(<, BinExpr(<, BinExpr(<, IntegerLit(1), IntegerLit(2)), IntegerLit(3)), IntegerLit(4))), ReturnStmt()]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 334))

    #     def test35(self):
    #         """More complex program"""
    #         input = """main1 : function string () {
    #             str = (("abc" :: "cde") :: "123") :: "456" ;
    #             return ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([AssignStmt(Id(str), BinExpr(::, BinExpr(::, BinExpr(::, StringLit(abc), StringLit(cde)), StringLit(123)), StringLit(456))), ReturnStmt()]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 335))

    #     def test36(self):
    #         """More complex program"""
    #         input = """ a : string = "213123213\\'" ;  """
    #         expect = """Program([
    # 	VarDecl(a, StringType, StringLit(213123213\\'))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 336))

    #     def test37(self):
    #         """More complex program"""
    #         input = """_A330xr : integer ;"""
    #         expect = """Program([
    # 	VarDecl(_A330xr, IntegerType)
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 337))

    #     def test38(self):
    #         """More complex program"""
    #         input = """str : string = "\ttoo(;_;)many(;_;)test(;_;)cases(;_;)\t" ;"""
    #         expect = """Program([
    # 	VarDecl(str, StringType, StringLit(	too(;_;)many(;_;)test(;_;)cases(;_;)	))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 338))

    #     def test39(self):
    #         """More complex program"""
    #         input = """main1 : function array [2,2] of string (inherit a : array [2,3] of string, out b : array [3,3] of boolean) {
    #             while(a < 23)
    #             do {a = a / 9 ;}
    #             while (a > 100) ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, ArrayType([2, 2], StringType), [InheritParam(a, ArrayType([2, 3], StringType)), OutParam(b, ArrayType([3, 3], BooleanType))], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), DoWhileStmt(BinExpr(>, Id(a), IntegerLit(100)), BlockStmt([AssignStmt(Id(a), BinExpr(/, Id(a), IntegerLit(9)))])))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 339))

    #     def test40(self):
    #         """More complex program"""
    #         input = """main1 : function array [2,2] of string () {
    #                 if(a < 4)
    #                 {
    #                         while(a < 23)
    #                         {
    #                                 for (i = 8, i < 20, i / 2) {c = c + 1 ; }
    #                         }
    #                 }
    #                 return;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, ArrayType([2, 2], StringType), [], None, BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(4)), BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(23)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(8)), BinExpr(<, Id(i), IntegerLit(20)), BinExpr(/, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(c), BinExpr(+, Id(c), IntegerLit(1)))]))]))])), ReturnStmt()]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 340))

    #     def test41(self):
    #         """More complex program"""
    #         input = """main1 : function array [2,2] of string () {
    #                 return 0;
    #                 return;
    #                 return 1;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(main1, ArrayType([2, 2], StringType), [], None, BlockStmt([ReturnStmt(IntegerLit(0)), ReturnStmt(), ReturnStmt(IntegerLit(1))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 341))

    #     def test42(self):
    #         """More complex program"""
    #         input = """func1 : function void (c : string, out d : boolean) {
    #                 printInteger(a);
    #                 readInteger();
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([CallStmt(printInteger, Id(a)), CallStmt(readInteger, )]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 342))

    #     def test43(self):
    #         """More complex program"""
    #         input = """func1 : function void (c : string, out d : boolean) {
    #                 writeFloat(a);
    #                 readFloat();
    #                 printBoolean(a);
    #                 readBoolean();
    #                 printString(a);
    #                 readString();
    #                 preventDefault();
    #                 super(b);
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([CallStmt(writeFloat, Id(a)), CallStmt(readFloat, ), CallStmt(printBoolean, Id(a)), CallStmt(readBoolean, ), CallStmt(printString, Id(a)), CallStmt(readString, ), CallStmt(preventDefault, ), CallStmt(super, Id(b))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 343))

    #     def test44(self):
    #         """More complex program"""
    #         input = """func1 : function void (c : string, out d : boolean) {
    #             do { for (i = 7, i < 13, i + 1) printInteger(i) ; }
    #             while (True) ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(func1, VoidType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([DoWhileStmt(Id(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(7)), BinExpr(<, Id(i), IntegerLit(13)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printInteger, Id(i)))]))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 344))

    #     def test45(self):
    #         """More complex program"""
    #         input = """func1 : function float (c : string, out d : boolean) {
    #             a,b,c : integer = 1,2,3 ;
    #             }"""
    #         expect = """Program([
    # 	FuncDecl(func1, FloatType, [Param(c, StringType), OutParam(d, BooleanType)], None, BlockStmt([VarDecl(a, IntegerType, IntegerLit(1)), VarDecl(b, IntegerType, IntegerLit(2)), VarDecl(c, IntegerType, IntegerLit(3))]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 345))

    #     def test46(self):
    #         """More complex program"""
    #         input = """a,b,c : array [2_7,3] of float = 1,2,3 ;"""
    #         expect = """Program([
    # 	VarDecl(a, ArrayType([27, 3], FloatType), IntegerLit(1))
    # 	VarDecl(b, ArrayType([27, 3], FloatType), IntegerLit(2))
    # 	VarDecl(c, ArrayType([27, 3], FloatType), IntegerLit(3))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 346))

    #     def test47(self):
    #         """More complex program"""
    #         input = """randfloat,b : float = 1_332.33e-23,.332e3 ;"""
    #         expect = """Program([
    # 	VarDecl(randfloat, FloatType, FloatLit(1332.33e-23))
    # 	VarDecl(b, FloatType, FloatLit(.332e3))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 347))

    #     def test48(self):
    #         """More complex program"""
    #         input = """abc : string = "ddxxdw"::"eerxxz" ; """
    #         expect = """Program([
    # 	VarDecl(abc, StringType, BinExpr(::, StringLit(ddxxdw), StringLit(eerxxz)))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 348))

    #     def test49(self):
    #         """More complex program"""
    #         input = """abc : float = a[22,3] / b[8-8,9/3] % c[8%2, 1*7] ; """
    #         expect = """Program([
    # 	VarDecl(abc, FloatType, BinExpr(%, BinExpr(/, ArrayCell(a, [IntegerLit(22), IntegerLit(3)]), ArrayCell(b, [BinExpr(-, IntegerLit(8), IntegerLit(8)), BinExpr(/, IntegerLit(9), IntegerLit(3))])), ArrayCell(c, [BinExpr(%, IntegerLit(8), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(7))])))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 349))

    #     def test50(self):
    #         """More complex program"""
    #         input = """abc, cde : float = a[22,3] / b[8-8,9/3] % c[8%2, 1*7], abc ; """
    #         expect = """Program([
    # 	VarDecl(abc, FloatType, BinExpr(%, BinExpr(/, ArrayCell(a, [IntegerLit(22), IntegerLit(3)]), ArrayCell(b, [BinExpr(-, IntegerLit(8), IntegerLit(8)), BinExpr(/, IntegerLit(9), IntegerLit(3))])), ArrayCell(c, [BinExpr(%, IntegerLit(8), IntegerLit(2)), BinExpr(*, IntegerLit(1), IntegerLit(7))])))
    # 	VarDecl(cde, FloatType, Id(abc))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 350))

    #     def test51(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 351))

    #     def test52(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 352))

    #     def test53(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 353))

    #     def test54(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 354))

    #     def test55(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 355))

    #     def test56(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 356))

    #     def test57(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 357))

    #     def test58(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 358))

    #     def test59(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 359))

    #     def test60(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 360))

    #     def test61(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 361))

    #     def test62(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 362))

    #     def test63(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 363))

    #     def test64(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 364))

    #     def test65(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 365))

    #     def test66(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 366))

    #     def test67(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 367))

    #     def test68(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 368))

    #     def test69(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 369))

    #     def test70(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 370))

    #     def test71(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 371))

    #     def test72(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 372))

    #     def test73(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 373))

    #     def test74(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 374))

    #     def test75(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 375))

    #     def test76(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 376))

    #     def test77(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 377))

    #     def test78(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 378))

    #     def test79(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 379))

    #     def test80(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 380))

    #     def test81(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 381))

    #     def test82(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 382))

    #     def test83(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 383))

    #     def test84(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 384))

    #     def test85(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 385))

    #     def test86(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 386))

    #     def test87(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 387))

    #     def test88(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 388))

    #     def test89(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 389))

    #     def test90(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 390))

    #     def test91(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 391))

    #     def test92(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 392))

    #     def test93(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 393))

    #     def test94(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 394))

    #     def test95(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 395))

    #     def test96(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 396))

    #     def test97(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 397))

    #     def test98(self):
    #         """More complex program"""
    #         input = """main1 : function string () {}"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 398))

    #     def test99(self):
    #         """More complex program"""
    #         input = """a,b,c: boolean = false, true, true;"""
    #         expect = """Program([
    # 	FuncDecl(main1, StringType, [], None, BlockStmt([]))
    # ])"""
    #         self.assertTrue(TestAST.test(input, expect, 399))



    
