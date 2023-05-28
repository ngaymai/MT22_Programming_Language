import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_simple_program1(self):
        """Simple program: int main() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_simple_program2(self):
        """Simple program: int main() {} """
        input = """x: integer = 65;
                fact: function integer (n: integer){
                    if(n==0) return 1;
                    else return n * fact(n-1);                    
                }
                inc: function void (out n: integer, delta: integer){
                    n = n+ delta;
                }
                main: function void(){
                    delta: integer = fact(3);
                    inc(x, delta);
                    printint(x);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_simple_program3(self):
        """Simple program: int main() {} """
        input = """x: integer;                
                main: function void(){
                    for (i = 1, i < 10, i + 1) {
                        writeInt(i);
                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_simple_program4(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x = 123;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_simple_program5(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x: integer = 2;
                    if(x>=0) print(x);     
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_simple_program6(self):
        """Simple program: int main() {} """
        input = """main: function void() {
            i: integer = 0;
            while(i<10) i= i+1;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_simple_program7(self):
        """Simple program: int main() {} """
        input = """x: integer = 65;                
                main: function void(){
                    do{
                        x = x -5;
                    }

                    while(x>=0);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_simple_program8(self):
        """Simple program: int main() {} """
        input = """               
                main: function void(){
                    for (i = 1, i < 10, i + 1) {
                        if(i == 8) break;                    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_simple_program9(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x: boolean = 1.4;
                    for (i = 1, i < 10, i + 1) {
                        if(i != 4)
                        x = x * i;
                        else 
                        continue;
                    }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_simple_program10(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r, s: integer;
                         r = 2.0;
                         a, b: array [5] of integer;
                         s = r * r * myPI;
                         a[0] = s;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_simple_program11(self):
        """Simple program: int main() {} """
        input = """x: string = "abcabc";
                add: function integer (n: string){
                    return n::"abc";                   
                }
                
                main: function void(){                    
                    printstring(add(x));
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_simple_program12(self):
        """Simple program: int main() {} """
        input = """    
                main: function void(){                    
                    a: array [4] of integer;
                    a = {1, 5, 7, 12} ;
                    for(i =0 ,i<4,i+1)
                    printint(a[i]);
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_simple_program13(self):
        """Simple program: int main() {} """
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
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_simple_program14(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x: array [3] of string;
                    x = {"Kangxi", "Yongzheng", "Qianlong"};
                    for(i = 0 , i < 3, i + 1)
                    printString(x[i]);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_simple_program15(self):
        """Simple program: int main() {} """
        input = """        
                printSring(){
                    x: array [3] of string;
                    x = {"Kangxi", "Yongzheng", "Qianlong"};
                }    
                main: function void(){
                    x: integer = 2;
                    if(x>=0) print(x);     
                    }
                """
        expect = "Error on line 2 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_simple_program16(self):
        """Simple program: int main() {} """
        input = """      main: function void(){
                    x: integer = 2;
                    if(x>=0) print(x); 
				printString("heello");    
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_simple_program17(self):
        """Simple program: int main() {} """
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
                    ddd, ff, et : float = 0, 2,3;
                    printflo(asdf(ddd, ff*et));
                    
                }"""
        expect = "Error on line 11 col 42: 0"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_simple_program18(self):
        """Simple program: int main() {} """
        input = """               
                main: function void(){
                    printInt(123*(1234 + 343 - 345/(3+5)))  ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_simple_program19(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x: array [3] of array;
                    x = {
                    {1,2,3}, {3,4,5},{3,4,5}
                    };
                    x[0,0] = x [1,2] + x[2,2] ;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_simple_program20(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r, s: string;
                         r = "hello";                         
                         s = "world";
                         a: array [2] of string;
                         a = {"abc","xyz"};
                         a[0] = a[1] :: r :: s;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_simple_program21(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r,e,t,y,d,s: integer = 1,2,3,4,5,6;
                         r = r + e + t + y + d + s;                         
                        
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_simple_program22(self):
        """Simple program: int main() {} """
        input = """      main: function void(){
                    x: integer = 2;
                    if(x>=0) print(x); 
				printString("heello");    
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_simple_program23(self):
        """Simple program: int main() {} """
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
                    ddd, ff, et : float = 0, 2,3;
                    printflo(asdf(ddd, ff*et));
                    
                }"""
        expect = "Error on line 11 col 42: 0"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_simple_program24(self):
        """Simple program: int main() {} """
        input = """               
                main: function void(){
                    printInt(123*(1234 + 343 - 345/(3+5)))  ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_simple_program25(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x: array [3] of array;
                    x = {
                    {1,2,3}, {3,4,5},{3,4,5}
                    };
                    x[0,0] = x [1,2] + x[2,2] ;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_simple_program26(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r, s: string;
                         r = "hello";                         
                         s = "world";
                         a: array [2] of string;
                         a = {"abc","xyz"};
                         a[0] = a[1] :: r :: s;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_simple_program27(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r,e,t,y,d,s: integer = 1,2,3,4,5,6;
                         r = r + e + t + y + d + s;                         
                        
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_simple_program28(self):
        """Simple program: int main() {} """
        input = """   
                foo: function void(a: integer, b: boolean){
                
                }            
                main: function void(){
                x: integer = 0;
                y: float = 1.2;
                    foo(2 + x, 4.0 / y);

                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_simple_program29(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    while(true){
                    printInt(1);
                    }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_simple_program30(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r, s, t, k: string = "heeloo", "woeirsdf", "asdtdg" , "asertd";
                       r = r::s::t::k;
                         
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_simple_program31(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))
# =================================================================

    def test_simple_program32(self):
        """Simple program: int main() {} """
        input = """main: function void() {
          printString("Enter an integer: ");
            num: integer = readInt();
            printInt(num);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_simple_program33(self):
        """Simple program: int main() {} """
        input = """
                main: function void(){
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_simple_program34(self):
        """Simple program: int main() {} """
        input = """              
                main: function void(){
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
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_simple_program35(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    a, b, c, delta, x1, x2 : float = readFloat(), readFloat(), readFloat(), readFloat(), readFloat(), readFloat();   

    delta = b * b - 4 * a * c;

    if (delta < 0) {
        printString("The equation has no real roots.\\n");
    } else (delta == 0) {
        x1 = -b / (2 * a);
        printString("The only solution is: \\n");
                    }
                }"""
        expect = "Error on line 9 col 11: ("
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_simple_program36(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x: integer = 2;
                    for (i = 1; i <= 9; i+1) {
    for (j = 1; j <= 9; j+1) {
        break;
    }
  
}
                    }
                """
        expect = "Error on line 4 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_simple_program37(self):
        """Simple program: int main() {} """
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

        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))

    def test_simple_program38(self):
        """Simple program: int main() {} """
        input = """           
                main: function void(){                     
 len: integer = 10;  
 temp : string;
 str: array [5] of string;
 str = {"asdfds", "aedsf", "awefasdfas", "sdfew", "edc"};
    for (i = 0, i < len / 2, i+1) {
        temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_simple_program39(self):
        """Simple program: int main() {} """
        input = """    
            isPrime: function boolean(n: integer) {
  if(n <= 1) return false;
  
  for(i = 2, i <= n / 2, i+1) {
    if(n % i == 0) return false;
  }
  
  return true;
}           
                main: function void(){
                    
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_simple_program40(self):
        """Simple program: int main() {} """
        input = """     
        isPrime: function boolean(n: integer) {
  if(n <= 1) return false;
  
  for(i = 2, i <= n / 2, i+1) {
    if(n % i == 0) return false;
  }
  
  return true;
}                  
                main: function void(){
                    n: integer;

  if(isPrime(n)) {
    n = 1;
  } else {
    n = 0;
  }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_simple_program41(self):
        """Simple program: int main() {} """
        input = """     
        search: function integer(arr: array [5] of integer , n: integer, x: integer) {
            i: integer;
   for(i = 0, i < n, i+1) {
    if(arr[i] == x) {
      return i;
    }
  }
  
  return -1;
}       
                main: function void(){
                        arr: array [6] of integer ;
                        arr = {5, 2, 8, 4, 1, 3};
                        n, x: integer;
  n = 6;
  x = 4;
  
  result = search(arr, n, x);
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))

    def test_simple_program42(self):
        """Simple program: int main() {} """
        input = """                
                main: function void(){      
                arr: array [4] of array;
                arr = {
                {1,2,3,4},{2,3,4,5},{3,4,5,6},{3,45,2,3}
                } ;     
                rows, cols : integer = 4,4;  
                i,j : integer;      
                    for(i = 0, i < rows, i+1) {
    for(j = 0, j < cols, j+1) {      
      arr[i][j] = 1;
    }
  }
                }"""
        expect = "Error on line 11 col 12: ["
        self.assertTrue(TestParser.test(input, expect, 242))

    def test_simple_program43(self):
        """Simple program: int main() {} """
        input = """    
                main: function void(){                    
                    number: integer;
   
   do {
       printString(" ");
       number = readInt();
       
       if (number < 0) {
           printString(".\\n");
       }
   } while (number < 0);
   
    number = readInt();
   
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))

    def test_simple_program44(self):
        """Simple program: int main() {} """
        input = """               
                main: function void(){
                    for (i = 1, i < 10, i + 1) {
                        if(i != 1)
                        { j: int = i;
                        while(j < 10)
                        {
                        j = j+1;
                        }
                        }
                        else break;
                    }
                }"""
        expect = "Error on line 5 col 29: int"
        self.assertTrue(TestParser.test(input, expect, 244))

    def test_simple_program45(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x: tring;
                    x = "Kangxi ;
                    for(i = 0 , i < 3, i + 1)
                    printString(x[i]);
                    }
                """
        expect = """Kangxi ;"""
        self.assertTrue(TestParser.test(input, expect, 245))

    def test_simple_program46(self):
        """Simple program: int main() {} """
        input = """        
                prin: function void(){
                    x: array [3] of string;
                    x = {"Kangx\i", "Yon"gzheng", "Qianlong"};
                }    
                main: function void(){
                    x: integer = 2;
                    if(x>=0) print(x);     
                    }
                """
        expect = """Kangx\ """
        self.assertTrue(TestParser.test(input, expect, 246))

    def test_simple_program47(self):
        """Simple program: int main() {} """
        input = """      main: function void(){
                    x: string = "asdfkj"dsaf";
                    if(x>=0) print(x); 
				printString("heello");    
                    }
                """
        expect = """ " """
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_simple_program48(self):
        """Simple program: int main() {} """
        input = """
                main: function void(){                  
                    ddd, ff, et : float = 1, 2,3;
                    ddd = ddd - ff * et /ddd ;
                    
                }"""
        expect = "Error on line 3 col 42: 1"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_simple_program49(self):
        """Simple program: int main() {} """
        input = """               
                main: function void(){
                    printString("acd" :: "decxd" :: "esdfe" :: "edatedf")  ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_simple_program50(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x: array [3] of array;
                    x = {
                    {1,2,3}, {3,4,5},{3,4,5}
                    };
                    x[0,0] = x [1,2] + x[2,2] * x[1,0] / x[1,1];
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))

    def test_simple_program51(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         x: array [3,3] of string;
                    x = {
                    {"aaa","bbb","ccc"}, {"eee","edc","esae"},{"ewq","eew","erwd"}
                    };
                    x[0,0] = x [1,2] :: x[2,2] :: x[1,0] :: x[1,1];
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_simple_program52(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r,e,t,y,d,s: integer = 1,2,3,4,5,6;
                         r = r + e * t / y - d % s;                         
                        
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_simple_program53(self):
        """Simple program: int main() {} """
        input = """      main: function void(){
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
      printString("a lon hon b\\n");
   } else {
      printString("a nho hon hoac bang b\\n");
   } 
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_simple_program54(self):
        """Simple program: int main() {} """
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
                    
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_simple_program55(self):
        """Simple program: int main() {} """
        input = """               
                main: function void(){
                    printInt(12.3*(123e4 + 343 - 345/(3+5)))  ;
                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_simple_program56(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    x: array [3] of array;
                    x = {
                    {1,2,3}, {3,4,5},{3,4,5}
                    };
                    x[0,0] = x [1,2] % x[2,2] ;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_simple_program57(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r, s: string = "hello", "world" ;                       
                         a: array [2] of string;
                         a = {"abc","xyz"};
                         a[0] = a[1] :: r :: s;
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_simple_program58(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r,e,t,y,d,s: integer = 1,2,3,4,5,6;
                        if((r+3 > t-3) && (e+y == d/s))
                        {
                        break;
                        }                         
                        
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_simple_program59(self):
        """Simple program: int main() {} """
        input = """   
                foo: function boolean(a: integer, b: boolean){
                if ((a>=b) || (b==0))
                return true;
                else 
                return false;
                }            
                main: function void(){
                x: integer = 0;
                y: float = 1.2;
                    foo(2 + x, 4.0 / y);

                }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_simple_program60(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                    while(true){
                   if(true || false)
                   continue;
                   else 
                   break;
                    }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_simple_program61(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                         r, s, t, k: string = "heeloo", "woeirsdf", "asdtdg" , "asertd";
                       if(r::s == t::k)
                       {r=s;}
                         
                    }
                """
        expect = "Error on line 4 col 31: =="
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_simple_program62(self):
        """Simple program: int main() {} """
        input = """            
                main: function void(){
                a: float = 9.34354;
                b: integer = 23445;
                        for(i = 0 , i < 10, i+1){
                        if(a > 1 && b != 5)
                        {
                        while (1!=0){
                        printString("acss");
                        break;
                        }
                        }
                        }
                    }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))

    def test_simple_program63(self):
        """Simple program: int main() {} """
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
                       a, b: array [5] of integer;
                   }
                   while (n>3);
               }
               main: function void() {
                   delta: integer = fact(3);
                   inc(x, delta);
                   printInteger(x);
               }

                """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_simple_program64(self):
        """Simple program: int main() {} """
        """Simple program: int main() {} """
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
                   while (n>3)
               }"""
        expect = "Error on line 22 col 15: }"

        self.assertTrue(TestParser.test(input, expect, 264))

    def test_simple_program65(self):
        """Simple program: int main() {} """
        """Simple program: int main() {} """
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
             //  if (i>3) {n++;
               break; }
               else continue; // add ()
               }
           }
                """
        expect = "Error on line 14 col 15: else"

        self.assertTrue(TestParser.test(input, expect, 265))

    def test_simple_program66(self):
        """Simple program: int main() {} """
        input = """main: function void() {
       a,b,c,d: string = 1,2,3,4;
       }"""
        expect = "Error on line 2 col 25: 1"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_simple_program67(self):
        """Simple program: int main() {} """
        input = """main: function void() {
       a,b,c,d: string= "1,2,3,4";
       }"""
        expect = "Error on line 2 col 33: ;"

        self.assertTrue(TestParser.test(input, expect, 267))

    def test_simple_program68(self):
        """Simple program: int main() {} """
        input = """main: function void() {
                        x: integer=123,456;
        }
        """
        expect = "Error on line 2 col 38: ,"

        self.assertTrue(TestParser.test(input, expect, 268))

    def test_simple_program69(self):
        """Simple program: int main() {} """
        input = """main: function void() {
                        x: integer=123.456;
        }
        """
        expect = "Error on line 2 col 35: 123.456"

        self.assertTrue(TestParser.test(input, expect, 269))

    def test_simple_program70(self):
        """Simple program: int main() {} """
        input = """main: function void() {
                        x: integer="123";
        }
        """
        expect = "Error on line 2 col 35: 123"

        self.assertTrue(TestParser.test(input, expect, 270))

    def test_simple_program71(self):
        """Simple program: int main() {} """
        input = """main: function void() {
                        x: integer=123;
                        y: float = 1.2 + 3.4;

        }
        """
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 271))

    def test_simple_program72(self):
        """Simple program: int main() {} """
        input = """main: function void() {                  
                        y: float;
                    y = 1 + 3.2 / 2;
                        
        }
        """
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 272))

    def test_simple_program73(self):
        """Simple program: int main() {} """
        input = """main: function void() {                  
                     if(true || 1+2 > 0)
                     {
                     x : integer;
                     }
                        
        }
        """
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 273))

    def test_simple_program74(self):
        """Simple program: int main() {} """
        input = """main: function void() { 
                arr: array [2] of boolean;
                arr = {true, false};                 
                     if(true || arr[1])
                     {
                     x : integer;
                     }
                        
        }
        """
        expect = "successful"

        self.assertTrue(TestParser.test(input, expect, 274))

    def test_simple_program75(self):
        """Simple program: int main() {} """
        input = """main: function void() { 
                arr: array [2] of string;
                arr = {"asdfds", "sdfaesdf"};                 
                     if(true || "sdfer")
                     {
                     x : integer;
                     }
                        
        }
        """
        expect = "Error on line 4 col 32: sdfer"
        self.assertTrue(TestParser.test(input, expect, 275))

############################

    def test_simple_program76(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);"""
        expect = "Error on line 5 col 39: <EOF>"

        self.assertTrue(TestParser.test(input, expect, 276))

    def test_program77(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_program78(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           /*else return n * fact(n - 1);
           }"""
        expect = "Error on line 5 col 11: /"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_program79(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           /*else return n * fact(n - 1); */
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_program80(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           // if (n == 0) return 1;
           /*else return n * fact(n - 1); */
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_program81(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           // if (n == 0) return 1;
           /*else return n * fact(n - 1); */
           }
           inc: function void(out n: integer, delta: integer) {
           n = n + delta;
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_program82(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         // n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_program83(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         // n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_program84(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           // if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           }"""
        expect = "Error on line 5 col 11: else"
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_Program85(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
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
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_Program86(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
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
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_Program87(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
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
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_Program88(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               break() ; //add () after "break"
               }
           }"""
        expect = "Error on line 11 col 20: ("
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_Program89(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
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
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_Program90(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
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
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_Program91(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
               continue(); // add ()
               }
           }"""
        expect = "Error on line 11 col 23: ("
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_Program92(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
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
               else continue; // add ()
               }
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_Program93(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
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
               else continue; // add ()
               }
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_Program94(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
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
               break;
               else continue; // add ()
               }
           }"""
        expect = "Error on line 13 col 15: else"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_Program95(self):
        """Simple program: int main() {} """
        input = """   main: function integer () {
         n: integer;
         n=readInteger();
           if (n == 0) return 1;
           else return n * fact(n - 1);
           }
           inc: function void( n: integer, delta: integer) {
           n = n + delta;
           for (i = 1, i < 10, i + 1) {
               writeInt(i);
             //  if (i>3) {
               break; }
               else continue; // add ()
               }
           }"""
        expect = "Error on line 13 col 15: else"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_Program_96(self):
        """Simple program: int main() {} """
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
                   while (n*delta>3||n-delta<3){
                       printInteger(n);
                       n = n *9 + 4 /3 % 7;
                       delta=delta+4;
                   }
               }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_Program_97(self):
        """Simple program: int main() {} """
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
                   if (n>3&&delta<3)
                       check=true;
                   while (n>3&&delta<3){
                       printInteger(n);
                       n--;
                       delta=delta+4;
                   }
               }"""
        expect = "Error on line 16 col 24: -"
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_Program_98(self):
        """Simple program: int main() {} """
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
                   if (n>3&&delta<3)
                       check=true;
                   else check = false;
                   while (n>3&&delta<3){
                       printInteger(n);
                       n = 8+9-3%8;
                       delta=delta+4;
                   }
               }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_Program_99(self):
        """Simple program: int main() {} """
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
                   if (n>3&&delta<3)
                       check=true;
                   else check = false;
                   while (n>3&&delta<3){
                       printInteger(n);
                       n--;
                       delta=delta+4;
                       if (n==5) break;
                   }
               }"""
        expect = "Error on line 17 col 24: -"
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_Program_100(self):
        """Simple program: int main() {} """
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
                   if (n>3&&delta<3)
                       check=true;
                   else check = false;
                   while (n>3&&delta<3){
                       printInteger(n);
                       
                       delta=delta+4;
                       if (n==5) printNum(delta);
                   }
               }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))
