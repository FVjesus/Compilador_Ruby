from ply import *
import sys
import lexical_analysis_generator
from operations import*


tokens = lexical_analysis_generator.tokens

precedence = (
	('right', 'else'),
	('left', 'OR'),
	('left', 'AND'),
	('left', 'EQUALS','DIFFERENT'),
	('left','GT','GE','LT','LE'),
	('left', 'PLUS','MINUS'),
	('left','ASTERISK','DIVIDE','MODULE'),
	('right','NOT'),
	('right', 'ASSIGNMENT'),
	('right','LAND'),
	('right', 'DEDENT'),
	('right', 'RBRACKET'),
	)


def p_program(p):
	'''program 	: program statment
				| '''			
	if len(p) == 3:
		p[0] = program(program = p[1], statment = p[2])
	else:
		pass
			
def p_bloco(p):
	" bloco 	: INDENT program DEDENT "
	p[0] = bloco(program = p[2])

def p_statment(p):
	'''statment 	: conditional
					| loops
					| stop
					| conti
					| argumentlist
					| bloco 
					| expression
					| declaration
					| read_gets 
					| create_puts'''
	p[0] = p[1]

def p_stop(p):
	" stop 	: break"
	p[0] = stop(p[1])

def p_conti(p):
	"conti 	: continue"
	p[0] = conti(p[1])

def p_declaration(p):
	''' declaration 	: simple_declaration
						| complex_declaration
						| declaration_pointer
						| acess_pointer'''
	p[0] = p[1]

def p_simple_declaration(p):
	''' simple_declaration 	: matrix_declaration
							| expression_declaration'''
	p[0] = p[1]

def p_matrix_declaration(p):
	" matrix_declaration 	: ID ASSIGNMENT matrix"
	p[0] = matrix_declaration(id_ = p[1], matrix = p[3])

def p_expression_declaration(p):
	" expression_declaration 	: ID ASSIGNMENT expression"
	p[0] = expression_declaration(id_ = p[1], expression = p[3])

def p_complex_declaration(p):
	''' complex_declaration 	: int_declaration
								| float_declaration
								| boolean_declaration'''
	p[0] = p[1]

def p_int_declaration(p):
	" int_declaration 	: int ID ASSIGNMENT expression"
	p[0] = int_declaration(id_ = p[2], expression = p[4])

def p_float_declaration(p):
	" float_declaration 	: float ID ASSIGNMENT expression"
	p[0] = float_declaration(id_ = p[2], expression = p[4])

def p_boolean_declaration(p):
	" boolean_declaration 	: boolean ID ASSIGNMENT expression_declaration"
	p[0] = boolean_declaration(id_ = p[2], expression = p[4])

def p_conditional(p):
	''' conditional 	: if  expression  begin bloco end SEMICOLON
						| if  expression  begin bloco else bloco end SEMICOLON
						| if  expression  begin bloco elsif  expression  bloco else bloco end SEMICOLON'''
	if len(p) == 7:
		p[0] = conditional(expression = p[2], bloco = p[4])

	elif len(p) == 9:
		p[0] = conditional2(expression = p[2], bloco = p[4], morebloco = p[6])

	else:
		p[0] = conditional3(expression = p[2], bloco = p[4], expression1 = p[6], bloco2 = p[7], bloco3 = p[9])

def p_loops(p):
	''' loops 	: fors
				| whiles
				| repeats
				| unlesss'''
	p[0] = p[1]

def p_fors(p):
	''' fors 	: for expression_variable LBRACKET expression_variable RBRACKET in expression LBRACKET do RBRACKET begin bloco end 
				| for expression in CONST_INTERGER POINTPOINT CONST_INTERGER bloco end'''
	if len(p) == 14:
		p[0] = fors(expression_variable = p[2], expression_variable2 = p[4], expression = p[7], bloco = p[12])

	else:
		p[0] = fors2(expression = p[2], const_interger = p[4], const_interger2 = p[6], bloco = p[7])

def p_whiles(p):
	''' whiles 	: while expression do bloco end
				| do bloco break if expression end'''
	if len(p) == 6:
		p[0] = whiles(expression = p[2], bloco = p[4])

	else:
		p[0] = whiles2(bloco = p[2], expression = p[5])

def p_repeats(p):
	''' repeats 	: repeat CONST_INTERGER DPOINT bloco end SEMICOLON'''
	p[0] = repeats(const_interger = p[2], bloco = p[4])

def p_unlesss(p):
	''' unlesss 	: unless expression then bloco RBRACKET else bloco LBRACKET end'''
	p[0] = unlesss(expression = p[2], bloco = p[4], bloco2 = p[7])

def p_expression(p):
	''' expression 	: expression_binop
					| expression_unitary
					| expression_const_real
					| expression_const_interger
					| expression_const_string
					| expression_true
					| expression_false
					| expression_variable 
					| expression_land
					 '''
	p[0] = p[1]

def p_expression_unitary(p):
	''' expression_unitary 	: unitary_not
							| unitary_asterisk
							| unitary_plus
							| unitary_minus'''
	p[0] = p[1]

def p_expression_binop(p):
	''' expression_binop 	: expression_and
							| expression_or
							| expression_gt
							| expression_ge
							| expression_lt
							| expression_le
							| expression_minus
							| expression_plus
							| expression_mult
							| expression_divide
							| expression_module
							| expression_equals
							| expression_different '''
	p[0] = p[1]

def p_unitary_minus(p):
	" unitary_minus 	: MINUS expression"
	p[0] = unitary_minus(expression = p[2])

def p_unitary_plus(p):
	" unitary_plus 		: PLUS expression"
	p[0] = unitary_plus(expression = p[2])

def p_unitary_asterisk(p):
	" unitary_asterisk 	: ASTERISK expression"
	p[0] = unitary_asterisk(expression = p[2])

def p_unitary_not(p):
	" unitary_not 	: NOT expression"
	p[0] = unitary_not(expression = p[2])

def p_expression_and(p):
	" expression_and 	: expression AND expression"
	p[0] = expression_and(expression_left = p[1], expression_rigth = p[3])

def p_expression_or(p):
	" expression_or 	: expression OR expression"
	p[0] = expression_or(expression_left = p[1], expression_rigth = p[3])

def p_expression_gt(p):
	" expression_gt 	: expression GT expression"
	p[0] = expression_gt(expression_left = p[1], expression_rigth = p[3])

def p_expression_ge(p):
	" expression_ge 	: expression GE expression"
	p[0] = expression_ge(expression_left = p[1], expression_rigth = p[3])

def p_expression_lt(p):
	" expression_lt 	: expression LT expression"
	p[0] = expression_lt(expression_left = p[1], expression_rigth = p[3])

def p_expression_le(p):
	" expression_le 	: expression LE expression"
	p[0] = expression_le(expression_left = p[1], expression_rigth = p[3])

def p_expression_land(p):
	" expression_land 	: LAND expression"
	p[0] = expression_land(expression = p[2])

def p_expression_const_real(p):
	" expression_const_real 	: CONST_REAL"
	p[0] = expression_const_real(p[1])

def p_expression_const_interger(p):
	" expression_const_interger 	: CONST_INTERGER"
	p[0] = expression_const_interger(p[1])

def p_expression_const_string(p):
	" expression_const_string 	: CONST_STRING"
	p[0] = expression_const_string(p[1])

def p_expression_true(p):
	" expression_true 	: True"
	p[0] = expression_true(p[1])

def p_expression_false(p):
	" expression_false 	: False"
	p[0] = expression_false(p[1])

def p_expression_plus(p):
	" expression_plus 	: expression PLUS expression"
	p[0] = expression_plus(expression_left = p[1], expression_rigth = p[3])

def p_expression_equals(p):
	" expression_equals 	: expression EQUALS expression"
	p[0] = expression_equals(expression_left = p[1], expression_rigth = p[3])

def p_expression_different(p):
	" expression_different 	: expression DIFFERENT expression"
	p[0] = expression_different(expression_left = p[1], expression_rigth = p[3])

def p_expression_minus(p):
	" expression_minus 	: expression MINUS expression"
	p[0] = expression_minus(expression_left = p[1],expression_rigth = p[3])

def p_expression_mult(p):
	" expression_mult 	: expression ASTERISK expression"
	p[0] = expression_mult(expression_left = p[1], expression_rigth = p[3])

def p_expression_divide(p):
	" expression_divide 	: expression DIVIDE expression"
	p[0] = expression_divide(expression_left = p[1], expression_rigth = p[3])

def p_expression_module(p):
	" expression_module 	: expression MODULE expression"
	p[0] = expression_module(expression_left = p[1], expression_rigth = p[3])

def p_argumentlist(p):
	''' argumentlist 	: ID LPAREN COMMA ID RPAREN ASTERISK LBRACKET COMMA ASTERISK LBRACKET ID RBRACKET RBRACKET LBRACKET COMMA LAND ID RBRACKET
						| ASTERISK ID LBRACKET COMMA LAND ID RBRACKET
						| LBRACKET LAND ID RBRACKET'''
	if len(p) == 19:
		p[0] = argumentlist(id_ = p[1],id_2 = p[4],id_3 = p[11], id_4 = p[17])

	elif len(p) == 8:
		p[0] = argumentlist2(id_ = p[2], id_2 = p[6])

	else:
		p[0] = argumentlist3(id_ = p[3])

def p_expression_variable(p):
	''' expression_variable 	: ID
								| DSING ID'''
	if len(p) == 2:
		p[0] = expression_variable(p[1])
	else:
		p[0] = expression_variable2(p[1])

def p_read_gets(p):
	"read_gets 	: ID ASSIGNMENT gets"
	p[0] = read_gets(p[1])

def p_create_puts(p):
	''' create_puts 	: puts_const_string
						| puts_expression
						| puts_quotation
						| puts_dquotation '''
	p[0] = p[1]

def p_puts_const_string(p):
	"puts_const_string 	: puts CONST_STRING"
	p[0] = puts_const_string(p[2])

def p_puts_expression(p):
	"puts_expression 	: puts expression_variable"
	p[0] = puts_expression(p[2])

def p_puts_quotation(p):
	'''puts_quotation 	: puts_string
						| puts_expressionq'''
	p[0] = p[1]

def p_puts_string(p):
	"puts_string 	: puts QUOTATION CONST_STRING QUOTATION"
	p[0] = puts_string(p[3])

def p_puts_expressionq(p):
	"puts_expressionq 	: puts QUOTATION expression_variable QUOTATION"
	p[0] = puts_expressionq(p[3])

def p_puts_dquotation(p):
	'''puts_dquotation 	: puts_string_dq
						| puts_expression_dq'''
	p[0] = p[1]

def p_puts_string_dq(p):
	"puts_string_dq 	: puts DQUOTATION CONST_STRING DQUOTATION"
	p[0] = puts_string_dq(p[3])

def p_puts_expression_dq(p):
	"puts_expression_dq 	: puts DQUOTATION expression_variable DQUOTATION"
	p[0] = puts_expression_dq(p[3])


def p_pointer(p):
	''' pointer 	: ASTERISK pointer
					| ASTERISK '''
	if len(p) == 3:
		p[0] = pointer(p[2])
	else:
		p[0] = asterisk(p[1])

def p_pointer_acess(p):
	'''pointer_acess 	: and pointer_acess
						| and'''
	if len(p) == 3:
		p[0] = pointer_acess(p[2])
	else:
		p[0] = p[1]

def p_and(p):
	''' and 	: token_and
				| token_land'''
	p[0] = p[1]

def p_token_and(p):
	"token_and 	: AND"
	p[0] = token_and(p[1])

def p_token_land(p):
	"token_land 	: LAND"
	p[0] = token_land(p[1])

def p_declaration_pointer(p):
	"declaration_pointer 	: pointer ID"
	p[0] = declaration_pointer(p[1])

def p_acess_pointer(p):
	"acess_pointer 	: pointer_acess ID"
	p[0] = acess_pointer(p[1])

def p_matrix(p):
	'''matrix 	: matrix_arg
				| matrix_rec
				| LBRACKET argument RBRACKET matrix
				| LBRACKET argument RBRACKET COMMA matrix'''
	if len(p) == 6:
		p[0] = matrix(argument = p[2], matrix = p[5])

	elif len(p) == 5:
		p[0] = matrix2(argument = p[2], matrix = p[4])

	else:
		p[0] = p[1]

def  p_matrix_arg(p):
	"matrix_arg 	: LBRACKET argument RBRACKET"
	p[0] = matrix_arg(p[2])

def p_matrix_rec(p):
	"matrix_rec 	: LBRACKET matrix RBRACKET"
	p[0] = matrix_rec(p[2])
				
def p_argument(p):
	'''argument 	: expression
					| argument COMMA expression
					| argument POINT expression
					| '''
	if len(p) == 4:
		p[0] = argument(argument = p[1], expression = p[3])

	elif len(p) == 2:
		p[0] = p[1]

	else:
		pass

def p_error(p):
	'''ID LPAREN error RPAREN'''
	print(p)
	print ("Syntax error in arguments")

printer = printer()
parser = yacc.yacc()

def parse(data, debug = 0):
	parser.error = 0
	p = parser.parse(data, debug = debug)
	if parser.error:
		return None
	return p

arq = open(sys.argv[1],'r')
data = arq.read()
arq.close()

parse(data).accept(printer)