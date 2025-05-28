// 2212036
grammar MiniGo;

@lexer::header {
from lexererr import *
}



@lexer::members {

last_token = None

def emitSemicolon(self):
    self.type = self.SEMICOLON ;
    self.text = ";";
    return super().emit();

def emit(self):
    global last_token
    
    tk = self.type

    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        unclosed_text = result.text.rstrip("\r\n");
        raise UncloseString(unclosed_text);

    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        illegal_text = result.text;
        raise IllegalEscape(illegal_text);

    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 

    elif tk == self.NL: 
        if last_token is not None and (
            last_token.type in [
                self.IDENTIFIER, self.INTEGER_LIT, self.FLOAT_LIT,
                self.BOOLEAN_LIT, self.STRING_LIT, self.KW_INT,
                self.KW_FLOAT, self.KW_BOOL, self.KW_STRING, self.KW_RETURN,
                self.KW_CONTINUE, self.KW_BREAK, self.RPAREN, self.RBRACK, self.RBRACE
            ]):
            semicolon_token = self.emitSemicolon()
            last_token = semicolon_token
            return semicolon_token
        else: 
            return self.nextToken()

    else:
        last_token = super().emit()
        return last_token
}

options{
	language=Python3;
}


SINGLE_COMMENT: '//' ~[\r\n]* -> skip ;

MULTI_COMMENT: '/*' ( MULTI_COMMENT | .)*? '*/' -> skip ;


PLUS    : '+' ;
MINUS   : '-' ;
MUL     : '*' ;
DIV     : '/' ;
MOD     : '%' ;

EQ      : '==' ;
NEQ     : '!=' ;
LT      : '<' ;
LE      : '<=' ;
GT      : '>' ;
GE      : '>=' ;

AND     : '&&' ;
OR      : '||' ;
NOT     : '!' ;

ASSIGN  : ':=' ;
ADD_ASSIGN : '+=' ;
SUB_ASSIGN : '-=' ;
MUL_ASSIGN : '*=' ;
DIV_ASSIGN : '/=' ;
MOD_ASSIGN : '%=' ;

EQUAL   : '=' ;

COLON: ':' ;
SEMICOLON: ';' ;

BOOLEAN_LIT: KW_TRUE | KW_FALSE ;

KW_IF : 'if' ;
KW_ELSE : 'else' ;
KW_FOR : 'for' ;
KW_STRUCT : 'struct' ;
KW_INTERFACE : 'interface' ;
KW_STRING : 'string' ;
KW_CONST : 'const' ;
KW_VAR : 'var' ;
KW_RETURN : 'return' ;
KW_FUNC : 'func' ;
KW_INT : 'int' ;
KW_TYPE : 'type' ;
KW_FLOAT : 'float' ;
KW_BOOL : 'boolean' ;
KW_CONTINUE : 'continue' ;
KW_BREAK : 'break' ;
KW_RANGE : 'range' ;
KW_TRUE : 'true' ;
KW_FALSE : 'false' ;
KW_NIL : 'nil' ;


IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]* ;


LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
LBRACK : '[' ;
RBRACK : ']' ;
COMMA  : ',' ;
DOT    : '.' ;
UNDERLINE: '_' ;

fragment DEC_INT: [0] | [1-9][0-9]* ;

fragment BIN_INT: ('0b' | '0B') [0-1]+ ;

fragment OCT_INT: ('0o' | '0O') [0-7]+ ;

fragment HEX_INT: ('0x' | '0X') ([0-9] | [A-F] | [a-f])+ ;

INTEGER_LIT: DEC_INT | BIN_INT | OCT_INT | HEX_INT;

FLOAT_LIT: [0-9]+ '.' [0-9]* (('e' | 'E') [+-]? [0-9]+)* ;

fragment ESC_SEQ: '\\' ( 'n' | 't' | 'r' | '"' | '\\' ) ; 

STRING_LIT: '"' ( ESC_SEQ | ~["\\] )* '"' ;


func_call: IDENTIFIER LPAREN list_val RPAREN ;//
single_method_call: DOT IDENTIFIER LPAREN list_val RPAREN ;//
list_method_call: single_method_call list_method_call | single_method_call ;//
method_call: (IDENTIFIER | struct_arr_access) list_method_call ;//

struct_arr_access: struct_access | arr_access ;//
struct_access: struct_arr_access_prime DOT IDENTIFIER ;//
arr_access: struct_arr_access_prime ;//
struct_arr_access_prime: struct_arr_access_prime DOT (arr_ele | IDENTIFIER) | (arr_ele | IDENTIFIER) ;//
arr_ele: IDENTIFIER dimension_list_in_var ;//




program : list_declr EOF ;//
list_declr: declr_all list_declr | declr_all;//
list_statement: stmt list_statement | stmt ;//
stmt: (var_dec | const_dec | assignment | if_stmt | for_stmt | break_stmt | continue_stmt | call_stmt | return_stmt) SEMICOLON ;//



primitive_values: INTEGER_LIT | FLOAT_LIT | BOOLEAN_LIT | STRING_LIT | KW_NIL ;//
primitive_types: KW_INT | KW_BOOL | KW_STRING | KW_FLOAT ;//

arr_type: dimension_list_in_lit (primitive_types | IDENTIFIER) ;//

all_types: primitive_types | IDENTIFIER | arr_type ;//

all_var: IDENTIFIER | struct_arr_access ;//

declr_all: (var_dec | const_dec | struct_def | struct_method_def | func_dec | interface_dec) SEMICOLON;//

assign_opp: ASSIGN | ADD_ASSIGN | SUB_ASSIGN | MUL_ASSIGN | DIV_ASSIGN | MOD_ASSIGN ;//


expression: logicalOrExpr ;//
logicalOrExpr: logicalOrExpr OR logicalAndExpr | logicalAndExpr ;//
logicalAndExpr: logicalAndExpr AND equalityExpr | equalityExpr ;//
equalityExpr: equalityExpr (EQ | NEQ | LT | LE | GT | GE) additiveExpr | additiveExpr ;//
additiveExpr: additiveExpr (PLUS | MINUS) multiplicativeExpr | multiplicativeExpr ;//
multiplicativeExpr: multiplicativeExpr (MUL | DIV | MOD) unaryExpr | unaryExpr ;//
unaryExpr: NOT unaryExpr | MINUS unaryExpr | postfixExpr ;//
postfixExpr: primaryExpr
    | postfixExpr DOT IDENTIFIER
    | postfixExpr dimension_list_in_var
    | postfixExpr DOT IDENTIFIER LPAREN list_val RPAREN ;//
primaryExpr: primitive_values | IDENTIFIER | func_call | arr_lit | struct_lit | LPAREN expression RPAREN ;//



var_dec: var_dec_init | var_dec_no_init ;//
var_dec_init: KW_VAR IDENTIFIER (all_types | ) EQUAL expression ;//
var_dec_no_init: KW_VAR IDENTIFIER all_types ;//



const_dec: KW_CONST IDENTIFIER EQUAL expression ;//



func_dec: KW_FUNC IDENTIFIER LPAREN list_arguments RPAREN (all_types | ) LBRACE list_statement RBRACE ;


list_arguments: list_arg_prime | ;//
list_arg_prime: arg COMMA list_arg_prime | arg ;//
arg: arg_prime all_types ;//
arg_prime: IDENTIFIER COMMA arg_prime | IDENTIFIER ;//






//  ARRAY
dimension_list_in_lit: dimension_in_lit dimension_list_in_lit | dimension_in_lit ;//
dimension_list_in_var: dimension_in_var dimension_list_in_var | dimension_in_var ;//
dimension_in_lit: LBRACK (INTEGER_LIT | IDENTIFIER) RBRACK ;//
dimension_in_var: LBRACK expression RBRACK ;//


arr_lit: dimension_list_in_lit all_types nested_list ;//
nested_list: LBRACE element_list RBRACE | LBRACE RBRACE ;//
element_list: element COMMA element_list | element ;//
element: nested_list | (primitive_values | struct_lit | IDENTIFIER);//


list_val: expression_prime | ;//
expression_prime: expression COMMA expression_prime | expression ;//


struct_def: KW_TYPE IDENTIFIER KW_STRUCT LBRACE list_field RBRACE ;//
list_field: (((field_dec | struct_method_def) SEMICOLON) list_field) | ((field_dec | struct_method_def) SEMICOLON) ;//
field_dec: IDENTIFIER all_types ;//


struct_lit: IDENTIFIER LBRACE list_field_init RBRACE ;//
list_field_init: list_field_prime | ;//
list_field_prime: field_init COMMA list_field_prime | field_init ;//
field_init: IDENTIFIER COLON expression ;//



struct_method_def: KW_FUNC LPAREN IDENTIFIER IDENTIFIER RPAREN IDENTIFIER LPAREN list_arguments RPAREN (all_types | ) LBRACE list_statement RBRACE ;//



interface_dec: KW_TYPE IDENTIFIER KW_INTERFACE LBRACE list_method RBRACE ;//
list_method: list_method_prime | ;//
list_method_prime: method_dec  list_method_prime | method_dec ;//
method_dec: IDENTIFIER LPAREN list_prototypes RPAREN (all_types | ) SEMICOLON;//

list_prototypes: list_prototypes_prime | ;//
list_prototypes_prime: prototype COMMA list_prototypes_prime | prototype ;//
prototype: prototype_prime all_types ;//
prototype_prime: IDENTIFIER COMMA prototype_prime | IDENTIFIER ;//




assignment: all_var assign_opp expression | arr_assign | struct_assign ;//
arr_assign: all_var ASSIGN arr_lit ;//
struct_assign: all_var ASSIGN struct_lit ;//




if_stmt: KW_IF LPAREN expression RPAREN LBRACE list_statement RBRACE list_else_if_stmt ;//
list_else_if_stmt: list_else_if_stmt_prime (else_stmt | ) ;//
list_else_if_stmt_prime: one_esle_if_stmt list_else_if_stmt_prime | ;//
one_esle_if_stmt: KW_ELSE KW_IF LPAREN expression RPAREN LBRACE list_statement RBRACE ;//
else_stmt: KW_ELSE LBRACE list_statement RBRACE;//



for_stmt: basic_for_stmt | init_for_stmt | range_for_stmt ;//
basic_for_stmt: KW_FOR expression LBRACE list_statement RBRACE ;//
init_for_stmt: KW_FOR (assignment | var_dec_init) SEMICOLON expression SEMICOLON assignment LBRACE list_statement RBRACE ;//
range_for_stmt: KW_FOR (IDENTIFIER | UNDERLINE) COMMA IDENTIFIER ASSIGN KW_RANGE expression LBRACE list_statement RBRACE ;//


break_stmt: KW_BREAK ;//


continue_stmt: KW_CONTINUE ;//


call_stmt: func_call | method_call ;//


return_stmt: 'return' expression | 'return' ;//






NL: '\n';

WS : [ \t\r\f]+ -> skip ; // skip spaces, tabs  


ILLEGAL_ESCAPE: '"' (~[\r\n"\\] | ESC_SEQ)* '\\' . ;
UNCLOSE_STRING: '"' (~[\r\n"\\] | ESC_SEQ)* ('\r'? '\n' | EOF) ;
ERROR_CHAR: .;

