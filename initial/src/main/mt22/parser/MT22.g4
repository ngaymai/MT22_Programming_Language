grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (declaration|function)+  EOF;
declaration 
    : varDecl SEMICOLON
    ;
function
    : functionPrototype functionBody    
    ;

varDecl
    : identifierList COLON datatype 
    | Identifier temp1 intExpression
    | Identifier temp2 stringExpression
    | Identifier temp3 expression
    | Identifier temp4 boolExpression 
    | Identifier temp5 floatExpression
    | identifierList COLON ARRAY dimensions OF datatype 
    ;
temp1
    : COMMA Identifier temp1 intExpression COMMA    
    | COLON 'integer' ASSIGN
    ; 
temp2
    : COMMA Identifier temp2 stringExpression COMMA
    | COLON 'string' ASSIGN
    ;
temp3 
    : COMMA Identifier temp3 expression COMMA
    | COLON 'auto' ASSIGN
    ;
temp4
    : COMMA Identifier temp4 boolExpression COMMA
    | COLON 'boolean' ASSIGN 
    ;
temp5
    : COMMA Identifier temp5 floatExpression COMMA
    | COLON 'float' ASSIGN 
    ;
// vardatatype
//     : INTEGER
//     | FLOAT
//     | BOOLEAN
//     ;
functionPrototype 
	: Identifier COLON FUNCTION datatype listPara inherSubpart?
    ;
dimensions
    : LSB listIndex RSB
    ;
listIndex
    : IntegerLiteral (COMMA IntegerLiteral)* 
    | identifierList
    | expression (COMMA expression)*
    ;
identifierList
    : Identifier (COMMA Identifier)*
    ;
initialization
    : ASSIGN expression (COMMA expression)*
    ;
paramDecl
    :   OUT? Identifier COLON datatype
    ;
listPara 
    : LP paradeclList* RP ;
paradeclList 
    : (paramDecl|varDecl) (COMMA (paramDecl|varDecl))*
    ;
inherSubpart 
    : INHERIT Identifier 
    ;
functionBody :  blockStatement ;
datatype    
    : ARRAY
    | VOID
    | AUTO
    | BOOLEAN
    | INTEGER
    | FLOAT
    | STRING
    ;

// ======================== Expression =================================== \\
expression 
    : stringExpression 
    | numberExpression       
    | boolExpression
    | intExpression
    | floatExpression
    | constant
    ;
numberExpression
    : relationalExpression
    ;
floatExpression
    : floatRelationalExpression
    ;
floatRelationalExpression
    : floatLogicalExpression (Less|Greater|LessEqual|GreaterEqual|Equal|NotEqual) floatLogicalExpression
    | floatLogicalExpression
    ;
floatLogicalExpression
    : floatLogicalExpression (And|Or) floatAdditiveExpression
    | floatAdditiveExpression
    ;
floatAdditiveExpression
    : floatAdditiveExpression (Plus|Minus) floatMultiplicativeExpression 
    | floatMultiplicativeExpression
    ;
floatMultiplicativeExpression
    : floatMultiplicativeExpression (Multiple|Division) floatNegationSignExpression
    | floatNegationSignExpression
    ;
intExpression
    : intRelationalExpression
    ;
intRelationalExpression
    : intLogicalExpression (Less|Greater|LessEqual|GreaterEqual|Equal|NotEqual) intLogicalExpression
    | intLogicalExpression
    ;
intLogicalExpression
    : intLogicalExpression (And|Or) intAdditiveExpression
    | intAdditiveExpression
    ;
intAdditiveExpression
    : intAdditiveExpression (Plus|Minus) intMultiplicativeExpression 
    | intMultiplicativeExpression
    ;
intMultiplicativeExpression
    : intMultiplicativeExpression (Multiple|Division|Remain) intNegationSignExpression
    | intNegationSignExpression
    ;
relationalExpression
    : logicalExpression (Less|Greater|LessEqual|GreaterEqual|Equal|NotEqual) logicalExpression
    | logicalExpression
    ;
logicalExpression
    : logicalExpression (And|Or) additiveExpression
    | additiveExpression
    ;
additiveExpression
    : additiveExpression (Plus|Minus) multiplicativeExpression 
    | multiplicativeExpression
    ;
multiplicativeExpression
    : multiplicativeExpression (Multiple|Division) primaryExpression
    | primaryExpression
    | multiplicativeExpression Remain intNegationSignExpression 
    | intNegationSignExpression
    ;
negationSingExpression
    : Minus primaryExpression
    | primaryExpression
    ;
primaryExpression
    : intPrimaryExpression
    | floatPrimaryExpression    
    ;
// primaryExpression 
//     : Identifier
//     | constant  
//     | arrayElement
//     | LP expression RP
//     | functionCall    
//     ;
intNegationSignExpression
    : Minus intPrimaryExpression
    | intPrimaryExpression
    ;
intPrimaryExpression
    : Identifier
    | IntegerLiteral    
    | arrayElement
    | LP numberExpression RP
    | functionCall
    ;
floatNegationSignExpression
    : Minus floatPrimaryExpression
    | floatPrimaryExpression
    ;
floatPrimaryExpression
    : Identifier
    | FloatLiteral
    | arrayElement
    | LP numberExpression RP
    | functionCall
    ;
arrayElement
    : Identifier dimensions
    ;
functionCall
    : callStatement
    ;
constant
    : IntegerLiteral
    | FloatLiteral
    | arrayLiteral
    ;

stringExpression
    : stringPrimaryExpression ('::' stringPrimaryExpression)* 
    ;
stringPrimaryExpression
    : StringLiteral
    | Identifier
    | '(' stringExpression ')'
    | arrayElement
    | functionCall
    ;

boolExpression
    : boolExpression (And|Or) negationExpression
    | negationExpression
    ;
negationExpression
    : Negation boolPrimaryExpression
    | boolPrimaryExpression
    ;
boolPrimaryExpression
    : BooleanLiteral
    | Identifier
    | '(' boolExpression ')'
    | arrayElement
    | functionCall
    | numberExpression
    ;
////////////////////////////////


statement
    :   selectionStatement
    |   iterationStatement
    |   assignmentStatement
    |   blockStatement
    |   callStatement SEMICOLON
    |   jumpStatement 
    | declaration
    ;
assignmentStatement
    :   lhs ASSIGN expression SEMICOLON
    ;
lhs
    : Identifier 
    | arrayElement
    ;

selectionStatement
    : IF LP expression RP statement ELSE statement
    | IF LP expression RP statement 
    ;

iterationStatement
    :   WHILE LP expression RP statement
    |   DO statement WHILE LP expression RP SEMICOLON
    |   FOR LP forCondition RP statement
    ;

forCondition
 	:   forDeclaration COMMA conditionExpression COMMA updateExpression
 	;

forDeclaration
    :   Identifier ASSIGN expression
    ;

conditionExpression
    : expression
    ;
updateExpression
    : expression
    ;

blockStatement
    : LCB statement* RCB    
    ;


callStatement
    : identifierList LP argumentList? RP 
    | sepcialFunction
    ;
argumentList
    : expression (COMMA expression)* 
    ;

jumpStatement
    : (CONTINUE|BREAK| (RETURN expression?)) SEMICOLON
    ;

// ========================== Literals ========================= \\

BooleanLiteral 
    : TRUE | FALSE
    ;
IntegerLiteral
    : '0' | [1-9][0-9_]* { self.text = self.text.replace('_','') }       
    ;

FloatLiteral
    :  IntegerLiteral (Decimal|Decimal? Exponent) { self.text = self.text.replace('_','') }    
    ;
fragment
Decimal
    : DOT DIGIT
    ;
fragment
DIGIT
    : [0-9]+
    ;
fragment
Exponent
    : EXPONENT SIGN? DIGIT+
    ;    
fragment
EXPONENT
    : 'e'|'E'
    ;
fragment
SIGN
    : '-'|'+'
    ;
StringLiteral
    : DOUBLEQUOTE (ESC|Char)* DOUBLEQUOTE {self.text = self.text[1:-1]}
    ;
fragment
Char 
    : ~ ('\\'|'\n'|'"')
    ;
fragment
DOUBLEQUOTE
    : '"' 	
    ;
fragment
ESC
    : '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\'|'"')
    ;

arrayLiteral
    : arrayIndex
    ;
arrayIndex 
    : LCB elements* RCB
    ;
elements
    : element (COMMA element)*    
    ;

element
    : BooleanLiteral
    | IntegerLiteral
    | FloatLiteral
    | StringLiteral
    | arrayLiteral
    ;


// ========================= END ===================== \\
// ================== Keywords ================== \\

AUTO
    : 'auto'
    ;
BREAK
    : 'break'
    ;
BOOLEAN
    : 'boolean'
    ;    
DO
    : 'do'
    ;
ELSE
    : 'else'
    ;
FALSE
    : 'false'
    ;
FLOAT 
    : 'float'
    ;
FOR 
    : 'for'
    ;    
FUNCTION 
    : 'function'
    ;
IF 
    : 'if'
    ;
INTEGER 
    : 'integer'
    ;
RETURN 
    : 'return'
    ;
STRING 
    : 'string'
    ;
TRUE 
    : 'true'
    ;
VOID 
    : 'void'
    ;
WHILE 
    : 'while'
    ;
OUT 
    : 'out'
    ;
CONTINUE
    : 'continue'
    ;
OF 
    : 'of'
    ;
INHERIT 
    : 'inherit'
    ;

ARRAY 
    : 'array'
    ;

// =================== end ======================= \\

// ====================== Operators ===================== \\

Plus
    : '+'
    ;
Minus
    : '-'
    ;
Multiple
    : '*'
    ;
Division
    : '/'
    ;
Remain
    : '%'
    ;
Negation
    : '!'
    ;    
And  
    : '&&'
    ;
Or  
    : '||'
    ;
Equal
    : '=='
    ;
NotEqual
    : '!='
    ;
Less 
    : '<'
    ;
LessEqual
    : '<='
    ;
Greater
    : '>'
    ;
GreaterEqual
    : '>='
    ;
CONCATENATE
    : '::'    
    ;

// =================== end ======================= \\

// ================== Seperators ================= \\

LP
    : '('
    ;
RP
    : ')'
    ;
LSB
    : '['
    ;
RSB
    : ']'
    ;
COMMA
    : ','
    ;
COLON
    : ':'
    ;
SEMICOLON
    : ';'
    ;
LCB
    : '{'
    ;
RCB
    : '}'
    ;
ASSIGN
    : '='
    ;
DOT 
    : '.'
    ;
// ================ end ==================== \\

// ================ Special function =================== \\
sepcialFunction
    : 'readInt()'
    | 'printInt' LP intArgument RP
    | 'writeFloat'LP floatArgument RP
    | 'readFloat()' 
    | 'printBoolean' LP boolArgument RP
    | 'readString()'
    | 'printString' LP stringArgument RP
    | 'super' LP listexpr RP
    | 'preventDefault()'
    ;
    intArgument
    : IntegerLiteral
    | Identifier
    | expression
    ;
floatArgument
    : FloatLiteral
    | Identifier
    | expression
    ;
stringArgument
    : StringLiteral
    | Identifier
    | expression
    ;
boolArgument
    : BooleanLiteral
    | Identifier 
    | expression
    ;
listexpr
    : expression (COMMA expression)*
    ;

// ================== End =============================\\
// ================ Identifier ======================= \\    

Identifier
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

// ===================== end ========================== \\

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newline

// ================ Program comment ===================== \\
BlockComment 
    :   '/*' .*? '*/'
        -> skip
    ; 

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;
// ==================== end ========================\\
ERROR_CHAR: .{raise ErrorToken(self.text)}
;

UNCLOSE_STRING: '"' (ESC|Char)* ( EOF ) 
	{	
			raise UncloseString(y[1:])
	}
	;
ILLEGAL_ESCAPE: '"' (ESC|Char)* ESC_ILLEGAL
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;

// fragment STR_CHAR: ~[\n"'\\] | ESC_SEQ ;

// fragment ESC_SEQ: '\\' [btnfr"'\\] ;

fragment ESC_ILLEGAL: ["'\\] ;

