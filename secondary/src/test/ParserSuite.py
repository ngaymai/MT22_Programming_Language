import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_short_vardecl(self):
        """Test short variable declaration"""
        input = """delta: integer = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_full_vardecl(self):
        """Test full variable declaration"""
        input = """a, b, c: integer = 3, 4, 6;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_wrong_full_vardecl(self):
        """Test wrong full variable declaration"""
        input = """a, b, c, d: integer = 3, 4, 6;"""
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_simple_program(self):
        """Test simple program"""
        input = """main: function void () {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_full_program(self):
        """Test full program"""
        input = """
        main: function void() {
                    r, c: integer;
                    // a[10,10], transpose[10,10]

                    a, transpose: array [10,10] of integer;

                printf("Enter rows and columns: ");
                scanf("", r, c);

                // asssigning elements to the matrix
                printf("Enter matrix elements:");
                for (i = 0, i < r, i+1)
                for (j = 0, j < c, j+1) {
                    printf("Enter element a: ", i + 1, j + 1);
                    scanf("", a[i,j]);
                }

                // printing the matrix a[][]
                printf("Entered matrix: ");
                for (i= 0, i < r, i+1)
                for (j = 0, j < c, j+1) {
                    printf("  ", a[i,j]);
                    if (j == c - 1)
                    printf("");
                }

                // computing the transpose
                for (i = 0, i < r, i+1)
                for (j = 0, j < c, j+1) {
                    transpose[j,i] = a[i,j];
                }
            }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
