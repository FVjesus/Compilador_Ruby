from printer import*

class program(object):

	def __init__(self,program,statment):
		self.program = program
		self.statment = statment

	def accept(self,visitor):
		visitor.visit_program(self)

	def program(self):
		return self.program

	def statment(self):
		return self.statment

class bloco(object):

	def __init__(self, program):
		self.program = program

	def accept(self,visitor):
		visitor.visit_bloco(self)

	def program(self):
		return self.program	

class stop(object):

	def __init__(self,value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_stop(self)

class conti(object):

	def __init__(self,value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_conti(self)

class matrix_declaration(object):

	def __init__(self, id_, matrix):
		self.id_ = id_
		self.matrix = matrix

	def accept(self,visitor):
		visitor.visit_matrix_declaration(self)

	def matrix(self):
		return	self.matrix
		
class expression_declaration(object):

	def __init__(self, id_, expression):
		self.id_ = id_
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_expression_declaration(self)

	def expression(self):
		return	self.expression

class int_declaration(object):

	def __init__(self,id_,expression):
		self.id_ = id_
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_int_declaration(self)

	def evaluate(self):
		return self.expression

	def expression(self):
		return self.expression

class float_declaration(object):

	def __init__(self, id_, expression):
		self.id_ = id_
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_float_expression(self)

	def evaluate(self):
		return self.expression

	def expression(self):
		return self.expression

class boolean_declaration(object):

	def __init__(self, id_, expression):
		self.id_ = id_
		self.expression = expression 

	def accept(self,visitor):
		visitor.visit_boolean_expression(self)

	def evaluate(self):
		return self.expression

	def expression(self):
		return self.expression

class conditional(object):

	def __init__(self,expression,bloco):
		self.expression = expression
		self.bloco = bloco

	def accept(self,visitor):
		visitor.visit_conditional(self)

	def bloco(self):
		return self.bloco

	def expression(self):
		return self.expression

class conditional2(object):
	
	def __init__(self, expression, bloco, morebloco):
		self.expression = expression
		self.bloco = bloco
		self.morebloco = morebloco

	def accept(self,visitor):
		visitor.visit_conditional2(self)

	def expression(self):
		return self.expression

	def bloco(self):
		return self.bloco

	def morebloco(self):
		return self.morebloco

class conditional3(object):
	
	def __init__(self, expression, bloco, expression1, bloco2, bloco3):
		self.expression = expression
		self.bloco = bloco
		self.expression1 = expression1
		self.bloco2 = bloco2
		self.bloco3 = bloco3
	
	def accept(self,visitor):
		visitor.visit_conditional3(self)

	def expression(self):
		return self.expression

	def bloco(self):
		return self.bloco

	def expression1(self):
		return self.expression1

	def bloco2(self):
		return self.bloco2

	def bloco3(self):
		return self.bloco3


class whiles(object):

	def __init__(self, expression, bloco):
		self.expression = expression
		self.bloco = bloco

	def accept(self,visitor):
		visitor.visit_whiles(self)

	def expression(self):
		return self.expression

	def bloco(self):
		return self.bloco

class whiles2(object):

	def __init__(self, bloco, expression):
		self.bloco = bloco
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_whiles2(self)

	def bloco(self):
		return self.bloco

	def expression(self):
		return self.expression


class fors(object):

	def __init__(self, expression_variable, expression_variable2,expression, bloco):
		self.expression_variable = expression_variable
		self.expression_variable2 = expression_variable2
		self.expression = expression
		self.bloco = bloco

	def accept(self,visitor):
		visitor.visit_fors(self)

	def expression_variable(self):
		return self.expression_variable

	def expression_variable2(self):
		return self.expression_variable2

	def expression(self):
		return self.expression

	def bloco(self):
		return self.bloco

class fors2(object):

	def __init__(self, expression, const_interger, const_interger2, bloco):
		self.expression = expression
		self.bloco = bloco
		self.const_interger = const_interger
		self.const_interger2 = const_interger2
		

	def accept(self,visitor):
		visitor.visit_fors2(self)

	def expression(self):
		return self.expression

	def bloco(self):
		return self.bloco

class repeats(object):

	def __init__(self,const_interger,bloco):
		self.const_interger = const_interger
		self.bloco = bloco

	def accept(self,visitor):
		visitor.visit_repeats(self)

	def const_interger(self):
		return self.const_interger

	def bloco(self):
		return self.bloco

class unlesss(object):

	def __init__(self, expression, bloco, bloco2):
		self.expression = expression
		self.bloco = bloco
		self.bloco2 =  bloco2

	def accept(self,visitor):
		visitor.visit_unlesss(self)

	def expression(self):
		return self.expression

	def bloco(self):
		return self.bloco

	def bloco2(self):
		return self.bloco2

class expression(object):
	pass

class expression_const_real(expression):

	def __init__(self,value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_expression_const_real(self)

class expression_const_interger(expression):

	def __init__(self,value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_expression_const_interger(self)

class expression_const_string(expression):

	def __init__(self,value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_expression_const_string(self)

class expression_true(expression):

	def __init__(self, value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_expression_true(self)

class expression_false(expression):

	def __init__(self, value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_expression_false(self)

class expression_variable(expression):

	def __init__(self, value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_expression_variable(self)

class expression_variable2(object):
	
	def __init__(self, value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_expression_variable2(self)
		
class expression_land(expression):

	def __init__(self, expression):
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_expression_land(self)

	def expression(self):
		return self.expression

class unitary_not(expression):

	def __init__(self, expression):
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_unitary_not(self)

	def expression(self):
		return self.expression

class unitary_asterisk(expression):

	def __init__(self, expression):
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_unitary_asterisk(self)

	def expression(self):
		return self.expression

class unitary_plus(expression):

	def __init__(self,expression):
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_unitary_plus(self)

	def expression(self):
		return self.expression

class unitary_minus(expression):

	def __init__(self,expression):
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_unitary_minus(self)

	def expression(self):
		return self.expression

class expression_and(expression):

	def __init__(self,expression_left,expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_and(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	

class expression_or(expression):

	def __init__(self,expression_left,expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_or(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	
	

class expression_gt(expression):

	def __init__(self, expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_gt(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
		

class expression_ge(expression):

	def __init__(self, expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_ge(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	

class expression_lt(expression):

	def __init__(self, expression_left, expression_rigth):
		self.expression_lt = expression_lt
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_lt(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	

class expression_le(expression):

	def __init__(self, expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_le(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	

class expression_minus(expression):

	def __init__(self,expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth =expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_minus(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	

class expression_plus(expression):

	def __init__(self, expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_plus(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	
	
class expression_mult(expression):

	def __init__(self,expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_mult()

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	
	

class expression_divide(expression):

	def __init__(self, expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_divide(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	
	

class expression_module(expression):

	def __init__(self, expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_module(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	

class expression_equals(expression):

	def __init__(self, expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_equals(self)

	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	

class expression_different(expression):

	def __init__(self, expression_left, expression_rigth):
		self.expression_left = expression_left
		self.expression_rigth = expression_rigth

	def accept(self,visitor):
		visitor.visit_expression_different(self)
	
	def expression_left(self):
		return self.expression_left

	def expression_rigth(self):
		return self.expression_rigth
	

class argumentlist(object):

	def __init__(self, id_, id_2, id_3,id_4):
		self.id_ =	id_
		self.id_2 = id_2
		self.id_3 = id_3
		self.id_4 = id_4

	def accept(self,visitor):
		visitor.visit_argumentlist(self)

class argumentlist2(object):

	def __init__(self, id_, id_2):
		self.id_ = id_
		self.id_2 = id_2

	def accept(self,visitor):
		visitor.visit_argumentlist2(self)
		
class argumentlist3(object):

	def __init__(self,id_):
		self.id_

	def accept(self,visitor):
		visitor.visit_argumentlist3(self)

class read_gets(object):

	def __init__(self,id_):
		self.id_ = id_

	def accept(self,visitor):
		visitor.visit_read_gets(self)

class puts_const_string(object):

	def __init__(self,const_string):
		self.const_string = const_string

	def accept(self,visitor):
		visitor.visit_puts_const_string(self)

	def const_string(self):
		return self.const_string

class puts_expression(object):

	def __init__(self,expression_variable):
		self.expression_variable = expression_variable

	def accept(self,visitor):
		visitor.visit_puts_expression(self)

	def expression_variable(self):
		return self.expression_variable

class puts_string(object):

	def __init__(self, const_string):
		self.cosnt_string = const_string

	def accept(self,visitor):
		visitor.visit_puts_string(self)

	def const_string(self):
		return self.const_string

class puts_expressionq(object):

	def __init__(self,expression_variable):
		self.expression_variable = expression_variable

	def accept(self,visitor):
		visitor.visit_puts_expressionq(self)

	def expression_variable(self):
		return self.expression_variable


class puts_string_dq(object):

	def __init__(self, cosnt_string):
		self.const_string = cosnt_string

	def accept(self,visitor):
		visitor.visit_puts_string_dq(self)

	def cosnt_string(self):
		return self.const_string

class puts_expression_dq(object):

	def __init__(self,expression_variable):
		self.expression_variable = expression_variable

	def accept(self,visitor):
		visitor.visit_puts_expresion_dq(self)

	def expression_variable(self):
		return self.expression_variable

class pointer(object):

	def __init__(self, value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_pointer(self)

class asterisk(object):

	def __init__(self,value):
		self.value = '*'

	def accept(self,visitor):
		visitor.visit_astersik(self)

class pointer_acess(object):

	def __init__(self, value):
		self.value = value

	def accept(self,visitor):
		visitor.visit_pointer_acess(self)

class token_land(object):

	def __init__(self,land):
		self.land = land

	def accept(self, visitor):
		visitor.visit_token_land(self)

class token_and(object):

	def __init__(self,and_):
		self.and_ = and_

	def accept(self,visitor):
		visitor.visit_token_and(self)

class declaration_pointer(object):

	def __init__(self,id_):
		self.id_ = id_

	def accept(self,visitor):
		visitor.visit_declaration_pointer(self)

class acess_pointer(object):

	def __init__(self, id_):
		self.id_ = id_

	def accept(self,visitor):
		visitor.visit_acess_pointer(self)

class matrix(object):

	def __init__(self, argument, matrix):
		self.argument = argument
		self.matrix = matrix

	def accept(self,visitor):
		visitor.visit_matrix(self)

	def argument(self):
		return self.argument

	def matrix(self):
		return self.matrix

class matrix2(object):

	def __init__(self, argument, matrix):
		self.argument = argument
		self.matrix = matrix

	def accept(self,visitor):
		visitor.visit_matrix2(self)

	def argument(self):
		return self.argument

	def matrix(self):
		return self.matrix

class matrix_arg(object):

	def __init__(self, argument):
		self.argument = argument

	def accept(self,visitor):
		visitor.visit_matrix_arg(self)

	def argument(self):
		return self.argument

class matrix_rec(object):

	def __init__(self,matrix):
		self.matrix = matrix

	def accept(self,visitor):
		visitor.visit_matrix_rec(self)

	def matrix(self):
		return self.matrix


class argument(object):

	def __init__(self,argument, expression):
		self.argument = argument
		self.expression = expression

	def accept(self,visitor):
		visitor.visit_argument(self)

	def argument(self):
		return self.argument

	def expression(self):
		return self.expression
