
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
        def test_short_vardecl(self):
            input = """x,b: integer;"""
            expect = str(Program([VarDecl("x", IntegerType()), VarDecl('b', IntegerType())]))
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
            a, b: float;"""
            expect = """Program([
        VarDecl(x, IntegerType, IntegerLit(1))
        VarDecl(y, IntegerType, IntegerLit(2))
        VarDecl(z, IntegerType, IntegerLit(3))
        VarDecl(a, FloatType)
        VarDecl(b, FloatType)
    ])"""
            self.assertTrue(TestAST.test(input, expect, 302))

        def test_simple_program(self):
            """Simple program"""
            input = """main: function void () {
            
            }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 303))

        def test_more_complex_program(self):
            """More complex program"""
            input = """main: function void () {
                printInteger(4,4);
            }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInteger, IntegerLit(4), IntegerLit(4))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 304))

        def test_more_complex_program1(self):
            """More complex program"""
            input = """main: function void() {
                        dividend, divisor, quotient, remainder: integer;
                        quotient = dividend / divisor;
                        remainder = dividend % divisor;
                    printf("Quotient = %d\n", quotient);
                    }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(dividend, IntegerType), VarDecl(divisor, IntegerType), VarDecl(quotient, IntegerType), VarDecl(remainder, IntegerType), AssignStmt(Id(quotient), BinExpr(/, Id(dividend), Id(divisor))), AssignStmt(Id(remainder), BinExpr(%, Id(dividend), Id(divisor))), CallStmt(printf, StringLit(Quotient = %d

    ), Id(quotient))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 305))

        def test_simple_program6(self):
            input = """main: function void() {
                            i: integer = 10; 	// declaration and initialization at the same time
                            do // do contains the actual code and the updation
                            {
                                printf("i = %d\n",i);
                                i = i-1;	// updation
                            }
                            // while loop doesn't contain any code but just the condition
                            while(i > 0);
                            return 0;
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType, IntegerLit(10)), DoWhileStmt(BinExpr(>, Id(i), IntegerLit(0)), BlockStmt([CallStmt(printf, StringLit(i = %d

    ), Id(i)), AssignStmt(Id(i), BinExpr(-, Id(i), IntegerLit(1)))])), ReturnStmt(IntegerLit(0))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 306))

        def test_simple_program7(self):
            input = """main: function void() {
                        a = data[i,1];
                        a = a+b*c+d/2-10%2;
                        sum , mean, SD: float;
                            i: integer;
                            for (i = 0, i < 10, i+1) {
                                sum = sum + data[i];
                            }
                            mean = sum / 10;
                            for (i = 0, i < 10, i+1) {
                                SD = SD + pow(data[i] - mean, 2);
                            }
                            return sqrt(SD / 10);
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([AssignStmt(Id(a), ArrayCell(data, [Id(i), IntegerLit(1)])), AssignStmt(Id(a), BinExpr(-, BinExpr(+, BinExpr(+, Id(a), BinExpr(*, Id(b), Id(c))), BinExpr(/, Id(d), IntegerLit(2))), BinExpr(%, IntegerLit(10), IntegerLit(2)))), VarDecl(sum, FloatType), VarDecl(mean, FloatType), VarDecl(SD, FloatType), VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(data, [Id(i)])))])), AssignStmt(Id(mean), BinExpr(/, Id(sum), IntegerLit(10))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(SD), BinExpr(+, Id(SD), FuncCall(pow, [BinExpr(-, ArrayCell(data, [Id(i)]), Id(mean)), IntegerLit(2)])))])), ReturnStmt(FuncCall(sqrt, [BinExpr(/, Id(SD), IntegerLit(10))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 307))

        def test_simple_program8(self):
            input = """main: function void() {
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
                }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(c, IntegerType), VarDecl(a, ArrayType([10, 10], IntegerType)), VarDecl(transpose, ArrayType([10, 10], IntegerType)), CallStmt(printf, StringLit(Enter rows and columns: )), CallStmt(scanf, StringLit(%d %d), Id(r), Id(c)), CallStmt(printf, StringLit(

    Enter matrix elements:

    )), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(Enter element a%d%d: ), BinExpr(+, Id(i), IntegerLit(1)), BinExpr(+, Id(j), IntegerLit(1))), CallStmt(scanf, StringLit(%d), ArrayCell(a, [Id(i), Id(j)]))]))), CallStmt(printf, StringLit(

    Entered matrix:

    )), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(%d  ), ArrayCell(a, [Id(i), Id(j)])), IfStmt(BinExpr(==, Id(j), BinExpr(-, Id(c), IntegerLit(1))), CallStmt(printf, StringLit(

    )))]))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(r)), BinExpr(+, Id(i), IntegerLit(1)), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(c)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(transpose, [Id(j), Id(i)]), ArrayCell(a, [Id(i), Id(j)]))])))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 308))

        def test_simple_program9(self):
            input = """main: function void() {
                    i,j,k: integer;
                    for(i = 0, i < 5, i+1)
                    {
                        printf("\t\t\t\t");
                        for(j = 0, j < 5, j+1)
                        printf("* ");

                        printf("\n");
                    }
                }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(k, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(   			 )), ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(printf, StringLit(* ))), CallStmt(printf, StringLit(

    ))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 309))

        def test_simple_program10(self):
            input = """main: function void() {
            number: integer;
            if(number < 100)
                printf("Number is less than 100!\n");
            else if(number == 100)
                printf("Number is 100!\n");
            else
                printf("Number is greater than 100!\n");


        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(number, IntegerType), IfStmt(BinExpr(<, Id(number), IntegerLit(100)), CallStmt(printf, StringLit(Number is less than 100!

    )), IfStmt(BinExpr(==, Id(number), IntegerLit(100)), CallStmt(printf, StringLit(Number is 100!

    )), CallStmt(printf, StringLit(Number is greater than 100!

    ))))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 310))

        def test_simple_program11(self):
            input = """printDivisors: function void(n: integer)
                        {
                            i: integer;
                            for (i = 1, i <= n, i+1)
                                if (n % i == 0)
                                    printf("%d ", i);
                        }

                        main: function void() {

                        printDivisors(100);
                        }"""
            expect = """Program([
        FuncDecl(printDivisors, VoidType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), CallStmt(printf, StringLit(%d ), Id(i))))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printDivisors, IntegerLit(100))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 311))

        def test_simple_program12(self):
            input = """primenumber: function void(number: integer)
                        {
                            i: integer;

                            // condition for checking the
                            // given number is prime or
                            // not
                            for (i = 2, i <= number / 2, i+1) {
                                if (number % i != 0)
                                    continue;
                                else
                                    return 1;
                            }
                            return 0;
                        }

                        main: function void() {
                            primenumber(100);
                        }"""
            expect = """Program([
        FuncDecl(primenumber, VoidType, [Param(number, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), BinExpr(/, Id(number), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, BinExpr(%, Id(number), Id(i)), IntegerLit(0)), ContinueStmt(), ReturnStmt(IntegerLit(1)))])), ReturnStmt(IntegerLit(0))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(primenumber, IntegerLit(100))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 312))

        def test_simple_program13(self):
            input = """primenumber: function void(number: integer)
                        {
                            i: integer;

                            a : boolean = false;
                            return a;
                        }

                        main: function void() {
                            primenumber(100);
                        }"""
            expect = """Program([
        FuncDecl(primenumber, VoidType, [Param(number, IntegerType)], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(a, BooleanType, BooleanLit(True)), ReturnStmt(Id(a))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(primenumber, IntegerLit(100))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 313))

        def test_simple_program14(self):
            input = """main: function void() {
                            data: array [5] of integer;
                            for (i = 0, i < 5, i+1)
                                scanf("%d", data + i);
                            for (i = 0, i < 5, i+1)
                                printf("%d\n", (data + i));
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(data, ArrayType([5], IntegerType)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(scanf, StringLit(%d), BinExpr(+, Id(data), Id(i)))), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printf, StringLit(%d

    ), BinExpr(+, Id(data), Id(i))))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 314))

        def test_simple_program15(self):
            input = """main: function void() {
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
                    }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(1021.0)), VarDecl(b, FloatType, FloatLit(21.0)), VarDecl(c, FloatType, FloatLit(1012332000.0)), VarDecl(d, FloatType, FloatLit(200.0)), VarDecl(e, FloatType, FloatLit(0.0)), VarDecl(r, IntegerType), VarDecl(s, IntegerType), VarDecl(a, ArrayType([10], IntegerType)), VarDecl(b, ArrayType([10], IntegerType)), AssignStmt(Id(r), FloatLit(4.0)), AssignStmt(Id(s), BinExpr(*, Id(r), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 315))

        def test_simple_program16(self):
            input = """main: function void() {
                            foo(123*321,"12323");
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(*, IntegerLit(123), IntegerLit(321)), StringLit(12323))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 316))

        def test_simple_program17(self):
            input = """main: function void() {
                            foo(123*321,"12323");
                            while (true) {
                            if (a < 1) break;
                            }
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(*, IntegerLit(123), IntegerLit(321)), StringLit(12323)), WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(1)), BreakStmt())]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 317))

        def test_simple_program18(self):
            input = """main: function void() {
                            foo(123*321,"12323");
                            while (true) {
                            if (a < 1) break;
                            else continue;
                            }
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(*, IntegerLit(123), IntegerLit(321)), StringLit(12323)), WhileStmt(BooleanLit(True), BlockStmt([IfStmt(BinExpr(<, Id(a), IntegerLit(1)), BreakStmt(), ContinueStmt())]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 318))

        def test_simple_program19(self):
            input = """main: function void() {
                            foo(123*321,"12323");
                            while (true)
                            if (a < 1) break;
                            else continue;

                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(*, IntegerLit(123), IntegerLit(321)), StringLit(12323)), WhileStmt(BooleanLit(True), IfStmt(BinExpr(<, Id(a), IntegerLit(1)), BreakStmt(), ContinueStmt()))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 319))

        def test_simple_program20(self):
            input = """
                            main: function void() {
                            while (a < 100*3) {
                                writeInt(i);
                            }
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(*, IntegerLit(100), IntegerLit(3))), BlockStmt([CallStmt(writeInt, Id(i))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 320))

        def test_simple_program21(self):
            input = """foo: function integer(out a1: integer) {
                            return 0;
                        }
                        main: function void() {
                            while (a < 100*3) {
                                writeInt(i);
                            }
                            foo(a);
                        }"""
            expect = """Program([
        FuncDecl(foo, IntegerType, [OutParam(a1, IntegerType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(*, IntegerLit(100), IntegerLit(3))), BlockStmt([CallStmt(writeInt, Id(i))])), CallStmt(foo, Id(a))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 321))

        def test_simple_program22(self):
            input = """foo: function integer(out a1: auto) {
                            return 0;
                        }
                        main: function void() {
                            while (a < 100*3) {
                                writeInt(i);
                            }
                            foo(a);
                        }"""
            expect = """Program([
        FuncDecl(foo, IntegerType, [OutParam(a1, AutoType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(*, IntegerLit(100), IntegerLit(3))), BlockStmt([CallStmt(writeInt, Id(i))])), CallStmt(foo, Id(a))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 322))

        def test_simple_program23(self):
            input = """foo: function integer(out a1: auto, inherit a2: string) {
                            return 0;
                        }
                        main: function void() {
                            while (a < 100*3) {
                                writeInt(i);
                            }
                            foo(a);
                        }"""
            expect = """Program([
        FuncDecl(foo, IntegerType, [OutParam(a1, AutoType), InheritParam(a2, StringType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(*, IntegerLit(100), IntegerLit(3))), BlockStmt([CallStmt(writeInt, Id(i))])), CallStmt(foo, Id(a))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 323))

        def test_simple_program24(self):
            input = """foo: function integer(out a1: auto, inherit out a2: float ) {
                            return 0;
                        }
                        main: function void() {
                            while (a < 100*3) {
                                writeInt(i);
                            }
                            foo(a);
                        }"""
            expect = """Program([
        FuncDecl(foo, IntegerType, [OutParam(a1, AutoType), InheritOutParam(a2, FloatType)], None, BlockStmt([ReturnStmt(IntegerLit(0))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(*, IntegerLit(100), IntegerLit(3))), BlockStmt([CallStmt(writeInt, Id(i))])), CallStmt(foo, Id(a))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 324))

        def test_simple_program25(self):
            input = """foo_parent: function integer() {
                            return 1;
                        }
                        foo: function integer(out a1: auto, inherit out a2: float ) inherit foo_parent {
                            return 0;
                        }
                        main: function void() {
                            while (a < 100*3) {
                                writeInt(i);
                            }
                            foo(a);
                        }"""
            expect = """Program([
        FuncDecl(foo_parent, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
        FuncDecl(foo, IntegerType, [OutParam(a1, AutoType), InheritOutParam(a2, FloatType)], foo_parent, BlockStmt([ReturnStmt(IntegerLit(0))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(*, IntegerLit(100), IntegerLit(3))), BlockStmt([CallStmt(writeInt, Id(i))])), CallStmt(foo, Id(a))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 325))

        def test_simple_program26(self):
            input = """foo_parent: function integer() {
                            return 1;
                        }
                        foo: function integer(out a1: auto, a2: boolean) inherit foo_parent {
                            return 0;
                        }
                        main: function void() {
                            while (a < 100*3) {
                                writeInt(i);
                            }
                            foo(a);
                        }"""
            expect = """Program([
        FuncDecl(foo_parent, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
        FuncDecl(foo, IntegerType, [OutParam(a1, AutoType), Param(a2, BooleanType)], foo_parent, BlockStmt([ReturnStmt(IntegerLit(0))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(*, IntegerLit(100), IntegerLit(3))), BlockStmt([CallStmt(writeInt, Id(i))])), CallStmt(foo, Id(a))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 326))

        def test_simple_program27(self):
            input = """foo_parent: function integer() {
                            return 1;
                        }
                        foo: function integer(out a1: auto, a2: array [10] of integer) inherit foo_parent {
                            return 0;
                        }
                        main: function void() {
                            while (a < 100*3) {
                                writeInt(i);
                            }
                            foo(a);
                        }"""
            expect = """Program([
        FuncDecl(foo_parent, IntegerType, [], None, BlockStmt([ReturnStmt(IntegerLit(1))]))
        FuncDecl(foo, IntegerType, [OutParam(a1, AutoType), Param(a2, ArrayType([10], IntegerType))], foo_parent, BlockStmt([ReturnStmt(IntegerLit(0))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), BinExpr(*, IntegerLit(100), IntegerLit(3))), BlockStmt([CallStmt(writeInt, Id(i))])), CallStmt(foo, Id(a))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 327))

        def test_simple_program28(self):
            input = """main: function void() {
                            a: integer  = 1*2 + 3;
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(+, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 328))

        def test_simple_program29(self):
            input = """main: function void() {
                            a: integer  = 1*2+3;
                            str: string = "Number" :: "String";
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, IntegerType, BinExpr(+, BinExpr(*, IntegerLit(1), IntegerLit(2)), IntegerLit(3))), VarDecl(str, StringType, BinExpr(::, StringLit(Number), StringLit(String)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 329))

        def test_simple_program30(self):
            input = """main: function void() {
                            a: array [20] of integer;
                            a[10] = 1200*2;
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([20], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, IntegerLit(1200), IntegerLit(2)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 330))

        def test_simple_program31(self):
            input = """main: function void() {
                            a: array [20] of integer;
                            a[10] = 1200*2;

                            // if without else
                            if (a[10] < 100) a[10] = a[10]*100;
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([20], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, IntegerLit(1200), IntegerLit(2))), IfStmt(BinExpr(<, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100)), AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100))))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 331))

        def test_simple_program32(self):
            input = """main: function void() {
                            a: array [20] of integer;
                            a[10] = 1200*2;

                            // if with else
                            if (a[10] < 100) a[10] = a[10]*100;
                            else a[10] = 0;
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([20], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, IntegerLit(1200), IntegerLit(2))), IfStmt(BinExpr(<, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100)), AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100))), AssignStmt(ArrayCell(a, [IntegerLit(10)]), IntegerLit(0)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 332))

        def test_simple_program33(self):
            input = """main: function void() {
                            a: array [20] of integer;
                            a[10] = 1200*2;
                            // if out else
                            if (a[10] < 100) {
                                a[10] = a[10]*100;
                                a[1] = a[10];
                            }
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([20], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, IntegerLit(1200), IntegerLit(2))), IfStmt(BinExpr(<, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100))), AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayCell(a, [IntegerLit(10)]))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 333))

        def test_simple_program34(self):
            input = """main: function void() {
                    a,b,c,d: string= 3,2,3,4;
                    }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, IntegerLit(3)), VarDecl(b, StringType, IntegerLit(2)), VarDecl(c, StringType, IntegerLit(3)), VarDecl(d, StringType, IntegerLit(4))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 334))

        def test_simple_program35(self):
            input = """main: function void() {
                            a: array [20] of integer;
                            a[10] = 1200*2;
                            i: integer;
                            // if with else
                            if (a[10] < 100) {
                                a[10] = a[10]*100;
                                a[1] = a[10];
                                for (i = 0, i<10, i+1) {
                                    printInteger(a[i]);
                                }
                            }
                            else a[10] = 0;
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([20], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, IntegerLit(1200), IntegerLit(2))), VarDecl(i, IntegerType), IfStmt(BinExpr(<, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100))), AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayCell(a, [IntegerLit(10)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printInteger, ArrayCell(a, [Id(i)]))]))]), AssignStmt(ArrayCell(a, [IntegerLit(10)]), IntegerLit(0)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 335))

        def test_simple_program36(self):
            input = """main: function void() {
                            a: array [20] of integer;
                            a[10] = 1200*2;
                            i: integer;
                            // if with else
                            if (a[10] < 100) {
                                    a[10] = a[10]*100;
                                    a[1] = a[10];
                                    while( a < 20 ) {
                                    printf("value of a: %d\n", a);
                                    a=a+1;
                                    if( a > 15) {
                                        /* terminate the loop using break statement */
                                        break;
                                    }
                                }
                                }
                            else a[10] = 0;
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, ArrayType([20], IntegerType)), AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, IntegerLit(1200), IntegerLit(2))), VarDecl(i, IntegerType), IfStmt(BinExpr(<, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100)), BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(10)]), BinExpr(*, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100))), AssignStmt(ArrayCell(a, [IntegerLit(1)]), ArrayCell(a, [IntegerLit(10)])), WhileStmt(BinExpr(<, Id(a), IntegerLit(20)), BlockStmt([CallStmt(printf, StringLit(value of a: %d

    ), Id(a)), AssignStmt(Id(a), BinExpr(+, Id(a), IntegerLit(1))), IfStmt(BinExpr(>, Id(a), IntegerLit(15)), BlockStmt([BreakStmt()]))]))]), AssignStmt(ArrayCell(a, [IntegerLit(10)]), IntegerLit(0)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 336))

        def test_simple_program37(self):
            input = """a,b,c: integer = 3,4,6;"""
            expect = """Program([
        VarDecl(a, IntegerType, IntegerLit(3))
        VarDecl(b, IntegerType, IntegerLit(4))
        VarDecl(c, IntegerType, IntegerLit(6))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 337))

        def test_simple_program38(self):
            input = """main: function void() {
                            i,j,k: integer;
                            i = 0;
                            while(i!=10)
                            {
                                printf("%d", i);
                                continue;
                                i=i+1;
                            }
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(k, IntegerType), AssignStmt(Id(i), IntegerLit(0)), WhileStmt(BinExpr(!=, Id(i), IntegerLit(10)), BlockStmt([CallStmt(printf, StringLit(%d), Id(i)), ContinueStmt(), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 338))

        def test_simple_program39(self):
            input = """main: function void() {
                        foo(2 + x, 4.0 / y);
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 339))

        def test_simple_program40(self):
            input = """main: function void() {
                    a,b,c,d,e: string= 2,2,3,4,6;
                    }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, IntegerLit(2)), VarDecl(b, StringType, IntegerLit(2)), VarDecl(c, StringType, IntegerLit(3)), VarDecl(d, StringType, IntegerLit(4)), VarDecl(e, StringType, IntegerLit(6))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 340))

        def test_simple_program41(self):
            input = """main: function void() {
                        foo(2 + x, 4.0 / y);
                        goo();
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, )]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 341))

        def test_simple_program42(self):
            input = """main: function void() {
                        foo(2 + x, 4.0 / y);
                        goo();
                            if (a < 10)
                                if (a>5)
                                    print(a);
                            else print(a+1);
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, ), IfStmt(BinExpr(<, Id(a), IntegerLit(10)), IfStmt(BinExpr(>, Id(a), IntegerLit(5)), CallStmt(print, Id(a)), CallStmt(print, BinExpr(+, Id(a), IntegerLit(1)))))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 342))

        def test_simple_program43(self):
            input = """main: function void() {
                            foo(2 + x, 4.0 / y);
                            goo();
                            for (i[0] = 1, i[0] < 10, i[0]+1) {
                                print(":");
                            }
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, ), ForStmt(AssignStmt(ArrayCell(i, [IntegerLit(0)]), IntegerLit(1)), BinExpr(<, ArrayCell(i, [IntegerLit(0)]), IntegerLit(10)), BinExpr(+, ArrayCell(i, [IntegerLit(0)]), IntegerLit(1)), BlockStmt([CallStmt(print, StringLit(:))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 343))

    # 	def test_simple_program44(self):   # TODO:
    #     	input = """for (i[0] = 1, i[0] < 10, i[0]+1)
    #         	print(":");"""
    #     	expect = """Program([
    #
    # ])"""
    #     	self.assertTrue(TestAST.test(input, expect, 344))

        def test_simple_program45(self):
            input = """main: function void() {
                        foo(2 + x, 4.0 / y);
                        goo();
                            for (i = 1, i <= (n * (n + 1)) / 2, i+1) {
                                printf("%d ", i);
                                if (i == (j * (j + 1)) / 2) {
                                    printf("\n");
                                    j=j+1;
                                }
                            }

                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, ), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), BinExpr(/, BinExpr(*, Id(n), BinExpr(+, Id(n), IntegerLit(1))), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(printf, StringLit(%d ), Id(i)), IfStmt(BinExpr(==, Id(i), BinExpr(/, BinExpr(*, Id(j), BinExpr(+, Id(j), IntegerLit(1))), IntegerLit(2))), BlockStmt([CallStmt(printf, StringLit(

    )), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))]))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 345))

        def test_simple_program46(self):
            input = """main: function void() {
                        foo(2 + x, 4.0 / y);
                        goo();
                            while (i <= (n * (n + 1)) / 2) {
                            printf("%d ", i);
                            // condition for what element has to print and
                                // how many times
                                if (i == (j * (j + 1)) / 2) {
                                    printf("\n");
                                    j=j+1;
                                }
                                i=i+1;
                            }
                        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, ), WhileStmt(BinExpr(<=, Id(i), BinExpr(/, BinExpr(*, Id(n), BinExpr(+, Id(n), IntegerLit(1))), IntegerLit(2))), BlockStmt([CallStmt(printf, StringLit(%d ), Id(i)), IfStmt(BinExpr(==, Id(i), BinExpr(/, BinExpr(*, Id(j), BinExpr(+, Id(j), IntegerLit(1))), IntegerLit(2))), BlockStmt([CallStmt(printf, StringLit(

    )), AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))])), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 346))

        def test_simple_program47(self):
            input = """floyd: function void(n: integer)
                        {
                            // base condition
                            if (n == 0)
                                return;
                            j: integer;
                            for (j = 1, j <= row, j+1)
                                printf("%d ", i+1);
                            row = row+1;
                            printf("\n");
                            floyd(n - 1);
                        }
                        main: function void() {
                        foo(2 + x, 4.0 / y);
                        goo();
                            floyd(6);
                        }"""
            expect = """Program([
        FuncDecl(floyd, VoidType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt()), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(j), IntegerLit(1)), BinExpr(<=, Id(j), Id(row)), BinExpr(+, Id(j), IntegerLit(1)), CallStmt(printf, StringLit(%d ), BinExpr(+, Id(i), IntegerLit(1)))), AssignStmt(Id(row), BinExpr(+, Id(row), IntegerLit(1))), CallStmt(printf, StringLit(

    )), CallStmt(floyd, BinExpr(-, Id(n), IntegerLit(1)))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, ), CallStmt(floyd, IntegerLit(6))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 347))

        def test_simple_program48(self):
            input = """floyd: function void(inherit out n: integer)
                        {
                            // base condition
                            if (n == 0)
                                return;
                            j: integer;
                            row = row+1;
                            printf("\n");
                            floyd(n - 1);
                        }
                        main: function void() {
                            foo(2 + x, 4.0 / y);
                            goo();
                            floyd(6);
                        }"""
            expect = """Program([
        FuncDecl(floyd, VoidType, [InheritOutParam(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt()), VarDecl(j, IntegerType), AssignStmt(Id(row), BinExpr(+, Id(row), IntegerLit(1))), CallStmt(printf, StringLit(

    )), CallStmt(floyd, BinExpr(-, Id(n), IntegerLit(1)))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y))), CallStmt(goo, ), CallStmt(floyd, IntegerLit(6))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 348))

        def test_simple_program49(self):
            input = """checkYear: function boolean(year: integer)
                        {
                            if (year % 400 == 0)
                                return true;
                            if (year % 100 == 0)
                                return false;
                            if (year % 4 == 0)
                                return true;
                            return false;
                        }
                        main: function void() {
                            print(checkYear(2023));
                        }"""
            expect = """Program([
        FuncDecl(checkYear, BooleanType, [Param(year, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(year), IntegerLit(400)), IntegerLit(0)), ReturnStmt(BooleanLit(True))), IfStmt(BinExpr(==, BinExpr(%, Id(year), IntegerLit(100)), IntegerLit(0)), ReturnStmt(BooleanLit(True))), IfStmt(BinExpr(==, BinExpr(%, Id(year), IntegerLit(4)), IntegerLit(0)), ReturnStmt(BooleanLit(True))), ReturnStmt(BooleanLit(True))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(checkYear, [IntegerLit(2023)]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 349))

        def test_simple_program50(self):
            input = """checkYear: function boolean(year: integer)
        {
            return (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0));
        }
        main: function void() {
            print(checkYear(2023));
        }"""
            expect = """Program([
        FuncDecl(checkYear, BooleanType, [Param(year, IntegerType)], None, BlockStmt([ReturnStmt(BinExpr(||, BinExpr(&&, BinExpr(==, BinExpr(%, Id(year), IntegerLit(4)), IntegerLit(0)), BinExpr(!=, BinExpr(%, Id(year), IntegerLit(100)), IntegerLit(0))), BinExpr(==, BinExpr(%, Id(year), IntegerLit(400)), IntegerLit(0))))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(checkYear, [IntegerLit(2023)]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 350))

        def test_simple_program51(self):
            input = """fib: function integer(n: integer)
        {
            if (n <= 1)
                return n;
            return fib(n - 1) + fib(n - 2);
        }
        main: function void() {
            print(fib(10));
        }"""
            expect = """Program([
        FuncDecl(fib, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), ReturnStmt(Id(n))), ReturnStmt(BinExpr(+, FuncCall(fib, [BinExpr(-, Id(n), IntegerLit(1))]), FuncCall(fib, [BinExpr(-, Id(n), IntegerLit(2))])))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(fib, [IntegerLit(10)]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 351))

        def test_simple_program52(self):
            input = """fib: function integer(n: integer)
                        {
                            f: array [100] of integer;
                            i: integer;
                            f[0] = 0;
                            f[1] = 1;
                            for (i = 2, i <= n, i+1) {
                                f[i] = f[i - 1] + f[i - 2];
                            }
                            return f[n];
                        }
                        main: function void() {
                            print(fib(10));
                        }"""
            expect = """Program([
        FuncDecl(fib, IntegerType, [Param(n, IntegerType)], None, BlockStmt([VarDecl(f, ArrayType([100], IntegerType)), VarDecl(i, IntegerType), AssignStmt(ArrayCell(f, [IntegerLit(0)]), IntegerLit(0)), AssignStmt(ArrayCell(f, [IntegerLit(1)]), IntegerLit(1)), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(f, [Id(i)]), BinExpr(+, ArrayCell(f, [BinExpr(-, Id(i), IntegerLit(1))]), ArrayCell(f, [BinExpr(-, Id(i), IntegerLit(2))])))])), ReturnStmt(ArrayCell(f, [Id(n)]))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(print, FuncCall(fib, [IntegerLit(10)]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 352))

        def test_simple_program53(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
        }"""
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 353))

        def test_simple_program54(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 354))

        def test_simple_program55(self):
            input = """main: function void(){
            r, s: string;
            r = "hello";
            s = "world";
            a: array [2] of string;
            a = {"abc","xyz"};
            a[0] = 1::2*2;
        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, StringType), VarDecl(s, StringType), AssignStmt(Id(r), StringLit(hello)), AssignStmt(Id(s), StringLit(world)), VarDecl(a, ArrayType([2], StringType)), AssignStmt(Id(a), ArrayLit([StringLit(abc), StringLit(xyz)])), AssignStmt(ArrayCell(a, [IntegerLit(0)]), BinExpr(::, IntegerLit(1), BinExpr(*, IntegerLit(2), IntegerLit(2))))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 355))

        def test_simple_program56(self):
            input = """main: function void(){
            r,e,t,y,d,s: integer = 1,2,3,4,5,6;
            r = r + e + t + y + d + s;
        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType, IntegerLit(1)), VarDecl(e, IntegerType, IntegerLit(2)), VarDecl(t, IntegerType, IntegerLit(3)), VarDecl(y, IntegerType, IntegerLit(4)), VarDecl(d, IntegerType, IntegerLit(5)), VarDecl(s, IntegerType, IntegerLit(6)), AssignStmt(Id(r), BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, BinExpr(+, Id(r), Id(e)), Id(t)), Id(y)), Id(d)), Id(s)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 356))

        def test_simple_program57(self):
            input = """foo: function void(a: integer, b: boolean){
            print("fadsf");
        }
        main: function void(){
        x: integer = 0;
        y: float = 1.2;
            foo(2 + x, 4.0 / y);
        }"""
            expect = """Program([
        FuncDecl(foo, VoidType, [Param(a, IntegerType), Param(b, BooleanType)], None, BlockStmt([CallStmt(print, StringLit(fadsf))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(0)), VarDecl(y, FloatType, FloatLit(1.2)), CallStmt(foo, BinExpr(+, IntegerLit(2), Id(x)), BinExpr(/, FloatLit(4.0), Id(y)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 357))

        def test_simple_program58(self):
            input = """main: function void(){
        r, s, t, k: string = "heeloo", "woeirsdf", "asdtdg" , "asertd";
        r = r::(s::(t::k));
        }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, StringType, StringLit(heeloo)), VarDecl(s, StringType, StringLit(woeirsdf)), VarDecl(t, StringType, StringLit(asdtdg)), VarDecl(k, StringType, StringLit(asertd)), AssignStmt(Id(r), BinExpr(::, Id(r), BinExpr(::, Id(s), BinExpr(::, Id(t), Id(k)))))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 358))

        def test_simple_program59(self):
            input = """main: function void(){
            arr: array [5] of integer;
            arr = {1, 2, 3, 4, 5};
            i, sum: integer = 0, 0;
            avg: float;
            for (i = 0, i < 5, i+1) {
                sum = sum + arr[i] ;
            }
            avg = sum / 5;
            printString("Average = ");
            writeFloat(avg);
        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([5], IntegerType)), AssignStmt(Id(arr), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)])), VarDecl(i, IntegerType, IntegerLit(0)), VarDecl(sum, IntegerType, IntegerLit(0)), VarDecl(avg, FloatType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), ArrayCell(arr, [Id(i)])))])), AssignStmt(Id(avg), BinExpr(/, Id(sum), IntegerLit(5))), CallStmt(printString, StringLit(Average = )), CallStmt(writeFloat, Id(avg))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 359))

        def test_simple_program60(self):
            input = """main: function void(){
            a: float = 9.34354;
            b: integer = 23445;
        for(i = 0 , i < 10, i+1){
                if((a > 1) && (b < 5))
                {
                    while (1!=0){
                        printString("acss");
                        break;
                    }
                }
            }
        }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FloatLit(9.34354)), VarDecl(b, IntegerType, IntegerLit(23445)), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(&&, BinExpr(>, Id(a), IntegerLit(1)), BinExpr(<, Id(b), IntegerLit(5))), BlockStmt([WhileStmt(BinExpr(!=, IntegerLit(1), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(acss)), BreakStmt()]))]))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 360))

        def test_simple_program61(self):
            input = """main: function void() {
        printString("Enter an integer: ");
            num: integer = readInt();
            printInt(num);
        }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printString, StringLit(Enter an integer: )), VarDecl(num, IntegerType, FuncCall(readInt, [])), CallStmt(printInt, Id(num))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 361))

        def test_simple_program62(self):
            input = """ main: function void(){
            a, b, x: float;
            printString("Enter coefficients a and b: ");
            readFloat(a);
            readFloat(b);
            if (a == 0) {
                if (b == 0) {
                    printString("The equation has infinite solutions.\\n");
                } else {
                    printString("The equation has no solution.\\n");
                }
            } else {
                x = -b / a;
                writeFloat(x);
            }
        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType), VarDecl(b, FloatType), VarDecl(x, FloatType), CallStmt(printString, StringLit(Enter coefficients a and b: )), CallStmt(readFloat, Id(a)), CallStmt(readFloat, Id(b)), IfStmt(BinExpr(==, Id(a), IntegerLit(0)), BlockStmt([IfStmt(BinExpr(==, Id(b), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(The equation has infinite solutions.\\n))]), BlockStmt([CallStmt(printString, StringLit(The equation has no solution.\\n))]))]), BlockStmt([AssignStmt(Id(x), BinExpr(/, UnExpr(<class 'str'>, Id(b)), Id(a))), CallStmt(writeFloat, Id(x))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 362))  # TODO: \n

        def test_simple_program63(self):
            input = """main: function void(){
            a, b, c, delta, x1, x2 : float = readFloat(), readFloat(), readFloat(), readFloat(), readFloat(), readFloat();
            delta = b * b - 4 * a * c;
            if (delta < 0) {
                printString("The equation has no real roots.\\n");
            } else  {
                x1 = -b / (2 * a);
                printString("The only solution is: \\n");
            }
        }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, FloatType, FuncCall(readFloat, [])), VarDecl(b, FloatType, FuncCall(readFloat, [])), VarDecl(c, FloatType, FuncCall(readFloat, [])), VarDecl(delta, FloatType, FuncCall(readFloat, [])), VarDecl(x1, FloatType, FuncCall(readFloat, [])), VarDecl(x2, FloatType, FuncCall(readFloat, [])), AssignStmt(Id(delta), BinExpr(-, BinExpr(*, Id(b), Id(b)), BinExpr(*, BinExpr(*, IntegerLit(4), Id(a)), Id(c)))), IfStmt(BinExpr(<, Id(delta), IntegerLit(0)), BlockStmt([CallStmt(printString, StringLit(The equation has no real roots.\\n))]), BlockStmt([AssignStmt(Id(x1), BinExpr(/, UnExpr(<class 'str'>, Id(b)), BinExpr(*, IntegerLit(2), Id(a)))), CallStmt(printString, StringLit(The only solution is: \\n))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 363))   # TODO: \n

        def test_simple_program64(self):
            input = """main: function void() {
                    i, j, temp: integer;
                    arr: array [5] of integer ;
                    arr = {5, 4, 3, 2, 1};
                    for (i = 0, i < 5 - 1, i+1) {
            for (j = i + 1, j < 5, j+1) {
                if (arr[i] > arr[j]) {
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(i, IntegerType), VarDecl(j, IntegerType), VarDecl(temp, IntegerType), VarDecl(arr, ArrayType([5], IntegerType)), AssignStmt(Id(arr), ArrayLit([IntegerLit(5), IntegerLit(4), IntegerLit(3), IntegerLit(2), IntegerLit(1)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(-, IntegerLit(5), IntegerLit(1))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), BinExpr(+, Id(i), IntegerLit(1))), BinExpr(<, Id(j), IntegerLit(5)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(>, ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)])), BlockStmt([AssignStmt(Id(temp), ArrayCell(arr, [Id(i)])), AssignStmt(ArrayCell(arr, [Id(i)]), ArrayCell(arr, [Id(j)])), AssignStmt(ArrayCell(arr, [Id(j)]), Id(temp))]))]))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 364))

        def test_simple_program65(self):
            input = """isPrime: function boolean(n: integer) {
        if(n <= 1) return false;

        for(i = 2, i <= n / 2, i+1) {
            if(n % i == 0) return false;
        }

        return true;
        }
                        main: function void(){

                        }
        """
            expect = """Program([
        FuncDecl(isPrime, BooleanType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(<=, Id(n), IntegerLit(1)), ReturnStmt(BooleanLit(True))), ForStmt(AssignStmt(Id(i), IntegerLit(2)), BinExpr(<=, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, BinExpr(%, Id(n), Id(i)), IntegerLit(0)), ReturnStmt(BooleanLit(True)))])), ReturnStmt(BooleanLit(True))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 365))

        def test_simple_program66(self):
            input = """main: function void(){
                        arr: array [4] of float;
                        arr = {
                        {1,2,3,4},{2,3,4,5},{3,4,5,6},{3,45,2,3}
                        } ;
                        rows, cols : integer = 4,4;
                        i,j : integer;
                            for(i = 0, i < rows, i+1) {
            for(j = 0, j < cols, j+1) {
            arr[i,j] = 1;
            }
        }
                        }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(arr, ArrayType([4], FloatType)), AssignStmt(Id(arr), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4)]), ArrayLit([IntegerLit(2), IntegerLit(3), IntegerLit(4), IntegerLit(5)]), ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(5), IntegerLit(6)]), ArrayLit([IntegerLit(3), IntegerLit(45), IntegerLit(2), IntegerLit(3)])])), VarDecl(rows, IntegerType, IntegerLit(4)), VarDecl(cols, IntegerType, IntegerLit(4)), VarDecl(i, IntegerType), VarDecl(j, IntegerType), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), Id(rows)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(j), IntegerLit(0)), BinExpr(<, Id(j), Id(cols)), BinExpr(+, Id(j), IntegerLit(1)), BlockStmt([AssignStmt(ArrayCell(arr, [Id(i), Id(j)]), IntegerLit(1))]))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 366))

        def test_simple_program67(self):
            input = """main: function void(){
            r,e,t,y,d,s: integer = 1,2,3,4,5,6;
            if((r+3 > t-3) && (e+y == d/s))
            {
            break;
            }

        }

        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType, IntegerLit(1)), VarDecl(e, IntegerType, IntegerLit(2)), VarDecl(t, IntegerType, IntegerLit(3)), VarDecl(y, IntegerType, IntegerLit(4)), VarDecl(d, IntegerType, IntegerLit(5)), VarDecl(s, IntegerType, IntegerLit(6)), IfStmt(BinExpr(&&, BinExpr(>, BinExpr(+, Id(r), IntegerLit(3)), BinExpr(-, Id(t), IntegerLit(3))), BinExpr(==, BinExpr(+, Id(e), Id(y)), BinExpr(/, Id(d), Id(s)))), BlockStmt([BreakStmt()]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 367))

        def test_simple_program68(self):
            input = """xsadgf: float = 6.5;
                    asdf: function float (out t: float, x: float){
                    x = readFloat();
                    t = x* xsadgf;
                    return t;
                    }
                    printflo: function void(sdt: float){
                    writeFloat(std);
                    }
                        main: function void(){
                            ddd, ff, et : float = 0.1, 2.2,3.2;
                            printflo(asdf(ddd-1+2*3, ff*et));

                        }
        """
            expect = """Program([
        VarDecl(xsadgf, FloatType, FloatLit(6.5))
        FuncDecl(asdf, FloatType, [OutParam(t, FloatType), Param(x, FloatType)], None, BlockStmt([AssignStmt(Id(x), FuncCall(readFloat, [])), AssignStmt(Id(t), BinExpr(*, Id(x), Id(xsadgf))), ReturnStmt(Id(t))]))
        FuncDecl(printflo, VoidType, [Param(sdt, FloatType)], None, BlockStmt([CallStmt(writeFloat, Id(std))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(ddd, FloatType, FloatLit(0.1)), VarDecl(ff, FloatType, FloatLit(2.2)), VarDecl(et, FloatType, FloatLit(3.2)), CallStmt(printflo, FuncCall(asdf, [BinExpr(+, BinExpr(-, Id(ddd), IntegerLit(1)), BinExpr(*, IntegerLit(2), IntegerLit(3))), BinExpr(*, Id(ff), Id(et))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 368))

        def test_simple_program69(self):
            input = """main: function void(){
                            printInt(12.3*(123e4 + 343 - 345/(3+5)))  ;
                        }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printInt, BinExpr(*, FloatLit(12.3), BinExpr(-, BinExpr(+, FloatLit(1230000.0), IntegerLit(343)), BinExpr(/, IntegerLit(345), BinExpr(+, IntegerLit(3), IntegerLit(5))))))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 369))

        def test_simple_program70(self):
            input = """main: function void(){
            x: array [3] of integer;
            x = {
            {1,2,3}, {3,4,5},{3,4,5}
            };
            x[0,0] = x [1,2] % x[2,2] ;
        }

        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], IntegerType)), AssignStmt(Id(x), ArrayLit([ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3)]), ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(5)]), ArrayLit([IntegerLit(3), IntegerLit(4), IntegerLit(5)])])), AssignStmt(ArrayCell(x, [IntegerLit(0), IntegerLit(0)]), BinExpr(%, ArrayCell(x, [IntegerLit(1), IntegerLit(2)]), ArrayCell(x, [IntegerLit(2), IntegerLit(2)])))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 370))

        def test_simple_program71(self):
            input = """main: function void(){
            r,e,t,y,d,s: integer = 1,2,3,4,5,6;
            if((r+3 > t-3) && (e+y == d/s))
            {
            break;
            }

        }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType, IntegerLit(1)), VarDecl(e, IntegerType, IntegerLit(2)), VarDecl(t, IntegerType, IntegerLit(3)), VarDecl(y, IntegerType, IntegerLit(4)), VarDecl(d, IntegerType, IntegerLit(5)), VarDecl(s, IntegerType, IntegerLit(6)), IfStmt(BinExpr(&&, BinExpr(>, BinExpr(+, Id(r), IntegerLit(3)), BinExpr(-, Id(t), IntegerLit(3))), BinExpr(==, BinExpr(+, Id(e), Id(y)), BinExpr(/, Id(d), Id(s)))), BlockStmt([BreakStmt()]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 371))

        def test_simple_program72(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                /*else return n * fact(n - 1); */
                }"""
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 372))

        def test_simple_program73(self):
            input = """ main: function integer () {
                n: integer;
                n=readInteger();
                // if (n == 0) return 1;
                /*else return n * fact(n - 1); */
                }
                inc: function void(out n: integer, delta: integer) {
                n = n + delta;
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, []))]))
        FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 373))

        def test_simple_program74(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    break;
                    }
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), BreakStmt()]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 374))

        def test_simple_program75(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    break ; //add more space between "break" and ';'
                    }
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), BreakStmt()]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 375))

        def test_simple_program76(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    continue; // add ()
                    }
                }"""
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), ContinueStmt()]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 376))

        def test_simple_program77(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    if (i>3) {
                    break;}
                    else continue;
                    }
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), BlockStmt([BreakStmt()]), ContinueStmt())]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 377))

        def test_simple_program78(self):
            input = """main: function integer () {
                        n: integer;
                        n=readInteger();
                        if (n == 0) return 1;
                        else
                            return n * fact(n - 1);
                    }
                    inc: function void( n: integer, delta: integer) {
                        n = n + delta;
                        while (n*delta>3||(n-delta<3)){
                            printInteger(n);
                            n = n *9 + 4 /3 % 7;
                            delta=delta+4;
                        }
                    }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), WhileStmt(BinExpr(>, BinExpr(*, Id(n), Id(delta)), BinExpr(||, IntegerLit(3), BinExpr(<, BinExpr(-, Id(n), Id(delta)), IntegerLit(3)))), BlockStmt([CallStmt(printInteger, Id(n)), AssignStmt(Id(n), BinExpr(+, BinExpr(*, Id(n), IntegerLit(9)), BinExpr(%, BinExpr(/, IntegerLit(4), IntegerLit(3)), IntegerLit(7)))), AssignStmt(Id(delta), BinExpr(+, Id(delta), IntegerLit(4)))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 378))

        def test_simple_program79(self):
            input = """main: function integer () {
                        n: integer;
                        n=readInteger();
                        if (n == 0) return 1;
                        else
                            return n * fact(n - 1);
                    }
                    inc: function void( n: integer, delta: integer) {
                        n = n + delta;
                        check: boolean = false;
                        if (n>3&&(delta<3))
                            check=true;
                        while (n>3&&(delta<3)){
                            printInteger(n);
                            delta=delta+4;
                        }
                    }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), VarDecl(check, BooleanType, BooleanLit(True)), IfStmt(BinExpr(>, Id(n), BinExpr(&&, IntegerLit(3), BinExpr(<, Id(delta), IntegerLit(3)))), AssignStmt(Id(check), BooleanLit(True))), WhileStmt(BinExpr(>, Id(n), BinExpr(&&, IntegerLit(3), BinExpr(<, Id(delta), IntegerLit(3)))), BlockStmt([CallStmt(printInteger, Id(n)), AssignStmt(Id(delta), BinExpr(+, Id(delta), IntegerLit(4)))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 379))

        def test_simple_program80(self):
            input = """main: function integer () {
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
                        while ((n>3)&&(delta<3)){
                            printInteger(n);
                            n = 8+9-3%8;
                            delta=delta+4;
                        }
                    }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), VarDecl(check, BooleanType, BooleanLit(True)), IfStmt(BinExpr(&&, BinExpr(>, Id(n), IntegerLit(3)), BinExpr(<, Id(delta), IntegerLit(3))), AssignStmt(Id(check), BooleanLit(True)), AssignStmt(Id(check), BooleanLit(True))), WhileStmt(BinExpr(&&, BinExpr(>, Id(n), IntegerLit(3)), BinExpr(<, Id(delta), IntegerLit(3))), BlockStmt([CallStmt(printInteger, Id(n)), AssignStmt(Id(n), BinExpr(-, BinExpr(+, IntegerLit(8), IntegerLit(9)), BinExpr(%, IntegerLit(3), IntegerLit(8)))), AssignStmt(Id(delta), BinExpr(+, Id(delta), IntegerLit(4)))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 380))

        def test_simple_program81(self):
            input = """main: function integer () {
                        n: integer;
                        n=readInteger();
                        if (n == 0) return 1;
                        else
                            return n * fact(n - 1);
                    }
                    inc: function void( n: integer, delta: integer) {
                        n = n + delta;
                        check: boolean = false;
                        if (n>3 && (delta<3))
                            check=true;
                        else check = false;
                        while (n>3&&(delta<3)){
                            printInteger(n);
                            n = 8+9-3%8;
                            delta=delta+4;
                        }
                    }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), VarDecl(check, BooleanType, BooleanLit(True)), IfStmt(BinExpr(>, Id(n), BinExpr(&&, IntegerLit(3), BinExpr(<, Id(delta), IntegerLit(3)))), AssignStmt(Id(check), BooleanLit(True)), AssignStmt(Id(check), BooleanLit(True))), WhileStmt(BinExpr(>, Id(n), BinExpr(&&, IntegerLit(3), BinExpr(<, Id(delta), IntegerLit(3)))), BlockStmt([CallStmt(printInteger, Id(n)), AssignStmt(Id(n), BinExpr(-, BinExpr(+, IntegerLit(8), IntegerLit(9)), BinExpr(%, IntegerLit(3), IntegerLit(8)))), AssignStmt(Id(delta), BinExpr(+, Id(delta), IntegerLit(4)))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 381))

        def test_simple_program82(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    if (i>3) break;
                    }
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), BreakStmt())]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 382))

        def test_simple_program83(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    continue;
                    }
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), ContinueStmt()]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 383))

        def test_simple_program84(self):
            input = """main: function integer () {
                n: integer;
                // n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                }

        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 384))

        def test_simple_program85(self):
            input = """main: function void() {
                printValue(4);
            }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printValue, IntegerLit(4))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 385))

        def test_simple_program86(self):
            input = """main: function void() {
                x: integer=123.456;
            }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, FloatLit(123.456))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 386))

        def test_simple_program87(self):
            input = """ main: function integer () {
                n: integer;
                // n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 387))

        def test_simple_program88(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    }
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i))]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 388))

        def test_simple_program89(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    break;
                    }
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), BreakStmt()]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 389))

        def test_simple_program90(self):
            input = """main: function integer () {
                n: integer;
                n=readInteger();
                if (n == 0) return 1;
                else return n * fact(n - 1);
                }
                inc: function void( n: integer, delta: integer) {
                n = n + delta;
                for (i = 1, i < 10, i + 1) {
                    writeInt(i);
                    break ; //add more space between "break" and ';'
                    }
                }
        """
            expect = """Program([
        FuncDecl(main, IntegerType, [], None, BlockStmt([VarDecl(n, IntegerType), AssignStmt(Id(n), FuncCall(readInteger, [])), IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
        FuncDecl(inc, VoidType, [Param(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta))), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(writeInt, Id(i)), BreakStmt()]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 390))

        def test_simple_program91(self):
            input = """main: function void(){
                            x: boolean = 1.4;
                            for (i = 1, i < 10, i + 1) {
                                if(i != 4)
                                x = x * i;
                                else
                                continue;
                            }
                            }

        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, BooleanType, FloatLit(1.4)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(!=, Id(i), IntegerLit(4)), AssignStmt(Id(x), BinExpr(*, Id(x), Id(i))), ContinueStmt())]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 391))

        def test_simple_program92(self):
            input = """main: function void(){
                            for (i = 1, i < 10, i + 1) {
                                if(i == 8) break;                	}
                        }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(8)), BreakStmt())]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 392))

        def test_simple_program93(self):
            input = """main: function void() {
                    a,b,c,d: string= 2,2,3,4;
                    }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, IntegerLit(2)), VarDecl(b, StringType, IntegerLit(2)), VarDecl(c, StringType, IntegerLit(3)), VarDecl(d, StringType, IntegerLit(4))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 393))

        def test_simple_program94(self):
            input = """ main: function void(){
                                r, s: integer;
                                r = 3.0;
                                a, b: array [5] of integer;
                                s = r * r * myPI;
                                a[0] = s;
                            }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(r, IntegerType), VarDecl(s, IntegerType), AssignStmt(Id(r), FloatLit(3.0)), VarDecl(a, ArrayType([5], IntegerType)), VarDecl(b, ArrayType([5], IntegerType)), AssignStmt(Id(s), BinExpr(*, BinExpr(*, Id(r), Id(r)), Id(myPI))), AssignStmt(ArrayCell(a, [IntegerLit(0)]), Id(s))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 394))

        def test_simple_program95(self):
            input = """x: string = "abcabc";
                        add: function integer (n: string){
                            return n::"abc";
                        }

                        main: function void(){
                            printstring(add(x));
                        }
        """
            expect = """Program([
        VarDecl(x, StringType, StringLit(abcabc))
        FuncDecl(add, IntegerType, [Param(n, StringType)], None, BlockStmt([ReturnStmt(BinExpr(::, Id(n), StringLit(abc)))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([CallStmt(printstring, FuncCall(add, [Id(x)]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 395))

        def test_simple_program96(self):
            input = """main: function void() {
                    a,b,c,d: string= 2,2,3,4;
                    }"""
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(a, StringType, IntegerLit(2)), VarDecl(b, StringType, IntegerLit(2)), VarDecl(c, StringType, IntegerLit(3)), VarDecl(d, StringType, IntegerLit(4))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 396))

        def test_simple_program97(self):
            input = """x: integer;
                        main: function void(){
                            for (i = 1, i < 10, i + 1) {
                                if(i == 1)
                                { j: integer = i;
                                while(j < 10)
                                {
                                j = j+1;
                                }
                                }
                                else break;
                            }
                        }
        """
            expect = """Program([
        VarDecl(x, IntegerType)
        FuncDecl(main, VoidType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(1)), BlockStmt([VarDecl(j, IntegerType, Id(i)), WhileStmt(BinExpr(<, Id(j), IntegerLit(10)), BlockStmt([AssignStmt(Id(j), BinExpr(+, Id(j), IntegerLit(1)))]))]), BreakStmt())]))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 397))

        def test_simple_program98(self):
            input = """ main: function void(){
                            x: array [3] of string;
                            x = {"Kangxi", "Yongzheng", "Qianlong"};
                            for(i = 0 , i < 3, i + 1)
                            printString(x[i]);
                            }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], StringType)), AssignStmt(Id(x), ArrayLit([StringLit(Kangxi), StringLit(Yongzheng), StringLit(Qianlong)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(+, Id(i), IntegerLit(1)), CallStmt(printString, ArrayCell(x, [Id(i)])))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 398))

        def test_simple_program99(self):
            input = """printSring: function void(){
        x: array [3] of string;
        x = {"Kangxi", "Yongzheng", "Qianlong"};
    }
    main: function void(){
        x: integer = 3;
        if(x>=0) print(x);
        }
        """
            expect = """Program([
        FuncDecl(printSring, VoidType, [], None, BlockStmt([VarDecl(x, ArrayType([3], StringType)), AssignStmt(Id(x), ArrayLit([StringLit(Kangxi), StringLit(Yongzheng), StringLit(Qianlong)]))]))
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(3)), IfStmt(BinExpr(>=, Id(x), IntegerLit(0)), CallStmt(print, Id(x)))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 399))

        def test_simple_program100(self):
            input = """main: function void(){
                            x: integer = 2;
                            if(x>=0) print(x);
                        printString("heello");
                            }
        """
            expect = """Program([
        FuncDecl(main, VoidType, [], None, BlockStmt([VarDecl(x, IntegerType, IntegerLit(2)), IfStmt(BinExpr(>=, Id(x), IntegerLit(0)), CallStmt(print, Id(x))), CallStmt(printString, StringLit(heello))]))
    ])"""
            self.assertTrue(TestAST.test(input, expect, 400))




