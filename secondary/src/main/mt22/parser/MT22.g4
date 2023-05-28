grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decls  EOF;
decls
	: decl decls
	| decl 
	;
decl 
	: varDecl 
	| funcDecl
	;
funcDecl
    : functionPrototype functionBody    
    ;

varDecl
    : (formalDecl|initializationDecl) SEMICOLON
	;
formalDecl
	: identifierList COLON varType     
	;
initializationDecl
	: Identifier term expression 
	;
term
    : COMMA Identifier term expression COMMA    	
    | COLON varType ASSIGN
    ; 
varType
    : atomicType
    | AUTO
    | arrayType
    ;
arrayType
    : ARRAY dimensions OF atomicType
    ;

dimensions
    : LSB IntegerLiteral (COMMA IntegerLiteral)* RSB
    ;

identifierList
    : Identifier (COMMA Identifier)*
    ;
functionPrototype 
	: Identifier COLON FUNCTION dataType listPara inherSubpart?
    ;
paramDecl
    :   INHERIT? OUT? Identifier COLON varType
    ;
listPara 
    : LP paradeclList? RP ;
paradeclList 
    : argument (COMMA argument)*
    ;
argument
    : paramDecl
    | varDecl
    ;
inherSubpart 
    : INHERIT Identifier 
    ;
functionBody :  blockStatement ;
dataType    
    : atomicType
    | VOID
    | AUTO
    | arrayType
    ;
atomicType
	: INTEGER
	| FLOAT
	| BOOLEAN
	| STRING
	;
// ======================== Expression =================================== \\
exprList 
    : expression (COMMA expression)*
    ;

expression 
    : relationalExpression CONCATENATE relationalExpression
    | relationalExpression
    ;

relationalExpression
    : logicalExpression relationalOperator logicalExpression
    | logicalExpression
    ;
relationalOperator
    : Less
    | Greater
    | LessEqual
    | GreaterEqual
    | Equal
    | NotEqual
    ;
logicalExpression
    : logicalExpression logicalOperator additiveExpression
    | additiveExpression
    ;
logicalOperator
    : And
    | Or
    ;
additiveExpression
    : additiveExpression additiveOperator multiplicativeExpression 
    | multiplicativeExpression
    ;
additiveOperator
    : Plus
    | Minus
    ;
multiplicativeExpression
    : multiplicativeExpression multiplicativeOperator negationExpression
    | negationExpression
    ;
multiplicativeOperator
    : Multiple
    | Division
    | Remain
    ;
negationExpression
    : Negation negationExpression
    | negationSignExpression
    ;
negationSignExpression
    : Minus negationSignExpression 
    | primaryExpression
    ;
primaryExpression 
    : Identifier
    | constant  
    | arrayElement
    | LP expression RP
    |  functionCall    
    ;
arrayElement
    : Identifier LSB exprList? RSB
    ;
// listIndex
//     : LSB exprList? RSB
//     ;
functionCall
    : callStatement
    ;
constant
    : IntegerLiteral
    | FloatLiteral
    | BooleanLiteral
    | StringLiteral
	| arrayLiteral
    ;
//////////////////////////////// statement /////////////////////////////////////////////////////////


statement
    :   selectionStatement
    |   others
    ;
others
    :   iterationStatement
    |   assignmentStatement SEMICOLON
    |   blockStatement
    |   callStatement SEMICOLON
    |   jumpStatement 
    ;
assignmentStatement
    :   lhs ASSIGN expression 
    ;
    
lhs
    : Identifier 
    | arrayElement    
    ;

selectionStatement
    : matchStatement
    | unmatchStatement
    ;
matchStatement
    : IF LP expression RP matchStatement ELSE matchStatement
    | others
    ;
unmatchStatement
    : IF LP expression RP statement
    | IF LP expression RP matchStatement ELSE unmatchStatement
    ;
iterationStatement
    :   WHILE LP expression RP statement
    |   DO blockStatement WHILE LP expression RP SEMICOLON
    |   FOR LP forCondition RP statement
    ;

forCondition
 	:   assignmentStatement COMMA expression COMMA expression
 	;

// forAssign
//     :   lhs ASSIGN expression
//     ;

// conditionExpression
//     : expression
//     ;
// updateExpression
//     : expression
//     ;

blockStatement
    : LCB content* RCB    
    ;
content
    : statement
    | varDecl
    ;
callStatement
    : Identifier LP exprList? RP 
    // | specialFunction
    ;
// argumentList
//     : expression (COMMA expression)* 
//     ;

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
    |  Decimal Exponent
    ;
fragment
Decimal
    : DOT DIGIT?
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
    : ~ ('\\'|'"')
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
    : LCB exprList? RCB
    ;
// element
//     : expression (COMMA expression)*    
//     ;




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
// specialFunction
//     : 'readInteger()'
//     | 'printInteger' LP intArgument RP
//     | 'writeFloat'LP floatArgument RP
//     | 'readFloat()' 
//     | 'printBoolean' LP boolArgument RP
//     | 'readString()'
//     | 'printString' LP stringArgument RP
//     | 'super' LP listexpr RP
//     | 'preventDefault()'
//     ;
//     intArgument
//     : IntegerLiteral
//     | Identifier
//     | expression
//     ;
// floatArgument
//     : FloatLiteral
//     | Identifier
//     | expression
//     ;
// stringArgument
//     : StringLiteral
//     | Identifier
//     | expression
//     ;
// boolArgument
//     : BooleanLiteral
//     | Identifier 
//     | expression
//     ;
// listexpr
//     : expression (COMMA expression)*
//     ;

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
ILLEGAL_ESCAPE: '"' (ESC|Char)* '\\' ~[btnfr"'\\]
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	}
	;

// fragment STR_CHAR: ~[\n"'\\] | ESC_SEQ ;

// fragment ESC_SEQ: '\\' [btnfr"'\\] ;

//fragment ESC_ILLEGAL: ["'\\] ;

