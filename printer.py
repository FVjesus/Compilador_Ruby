class printer(object):

	def visit_program (self,program):
		if program.program != None:
			program.program.accept(self)
		program.statment.accept(self)

	def visit_bloco (self,bloco):
		bloco.program.accept(self)
	

	def visit_stop (self,stop):
		print(stop.value, end = '')

	def visit_conti (self,conti):
		print(conti.value, end = '')

	def visit_matrix_declaration (self,matrix_declaration):
		print(matrix_declaration.id_,end = '')
		print('=', end = '')
		matrix_declaration.matrix.accept(self)

	def visit_expression_declaration (self,expression_declaration):
		print(expression_declaration.id_, end = '')
		print('=', end = '')
		expression_declaration.expression.accept(self)


	def visit_int_declaration (self,int_declaration):
		print('int', end = '')
		print(int_declaration.id_, end = '')
		print('=', end = '')
		int_declaration.expression.accept(self)

	def visit_float_declaration (self,float_declaration):
		print('float', end = '')
		print(float_declaration.id_, end = '')
		print('=', end = '')
		float_declaration.expression.accept(self)

	def visit_boolean_declaration (self,boolean_declaration):
		print('boolean', end = '')
		print(boolean_declaration.id_, end = '')
		print('=', end = '')
		boolean_declaration.expression.accept(self)

	def visit_conditional (self,conditional):
		print('if', end = '')
		conditional.expression.accept(self)
		print('begin', end = '')
		conditional.bloco.accept(self)
		print('end', end = '')
		print(';', end = '')

	def visit_conditional2(self, conditional2):
		print('if', end = '')
		conditional2.expression.accept(self)
		print('begin', end = '')
		conditional2.bloco.accept(self)
		print('else', end = '')
		conditional2.morebloco.accept(self)
		print('end', end = '')
		print(';', end = '')

	def visit_conditional3(self,conditional3):
		print('if', end = '')
		conditional3.expression.accept(self)
		print('begin', end = '')
		conditional3.bloco.accept(self)
		print('elsif', end = '')
		conditional3.expression1.accept(self)
		conditional3.bloco2.accept(self)
		print('else', end = '')
		conditional3.bloco3.accept(self)
		print('end', end = '')
		print(';', end = '')

	def visit_whiles (self,whiles):
		print('while ', end = '')
		whiles.expression.accept(self)
		print('do ', end = '')
		whiles.bloco.accept(self)
		print('end ', end = '')

	def visit_whiles2(self,whiles2):
		print('do', end = '')
		whiles2.bloco.accept(self)
		print('break', end = '')
		print('if', end = '')
		whiles2.expression.accept(self)
		print('end', end = '')


	def visit_fors (self,fors):
		print(' for ', end = '')
		fors.expression_variable.accept(self)
		print(' [ ', end = '')
		fors.expression_variable2.accept(self)
		print(' ] ', end = '')
		print(' in ', end = '')
		fors.expression.accept(self)
		print(' [ ', end = '')
		print(' d ', end = '')
		print(' ] ', end = '')
		print(' begin ', end = '')
		fors.bloco.accept(self)
		print(' end ', end = '')

	def visit_fors2(self, fors2):
		print(' for ', end = '')
		fors2.expression.accept(self)
		print(' in ', end = '')
		print(fors2.const_interger, end = '')
		print(' .. ', end = '')
		print(fors2.const_interger2, end = '')
		fors2.bloco.accept(self)
		print(' end ', end = '')

	def visit_repeats (self,repeats):
		print('repeat', end = '')
		repeats.const_interger.accept(self)
		print(':', end = '')
		repeats.bloco.accept(self)
		print('end', end = '')
		print(';', end = '')

	def visit_unlesss (self,unlesss):
		print('unless', end = '')
		unlesss.expression.accept(self)
		print('then', end = '')
		unlesss.bloco.accept(self)
		print('[', end = '')
		print('else', end = '')
		unlesss.bloco2.accept(self)
		print(']', end = '')
		print('end', end = '')

	def visit_expression_const_real (self,expression_const_real):
		print(expression_const_real.value, end = '')

	def visit_expression_const_interger (self,expression_const_interger):
		print(expression_const_interger.value, end = '')

	def visit_expression_const_string (self,expression_const_string):
		print(expression_const_string.value, end = '')

	def visit_expression_true (self,expression_true):
		print(expression_true.value, end = '')

	def visit_expression_false (self,expression_false):
		print(expression_false.value, end = '')

	def visit_expression_variable (self,expression_variable):
		print(expression_variable.value, end = '')

	def visit_expression_variable2(self,expression_variable2):
		print(expression_variable2.value, end = '')

	def visit_expression_land (self,expression_land):
		print(' & ', end = '')
		expression_land.expression.accept(self)

	def visit_unitary_not (self,unitary_not):
		print(' ! ', end = '')
		unitary_not.expression.accept(self)

	def visit_unitary_asterisk (self,unitary_asterisk):
		print(' * ', end = '')
		unitary_asterisk.expression.accept()

	def visit_unitary_plus (self,unitary_plus):
		print(' + ', end = '')
		unitary_plus.expression.accept(self)

	def visit_unitary_minus (self,unitary_minus):
		print(' - ', end = '')
		unitary_minus.expression.accept(self)

	def visit_expressioin_and (self,expression_and):
		expression_and.expression_left.accept(self)
		print(' && ', end = '')
		expression_and.expression_rigth.accept(self)

	def visit_expression_or (self,expression_or):
		expression_or.expression_left.accept(self)
		print(' || ', end = '')
		expression_or.expression_rigth.accept(self)

	def visit_expression_gt (self,expression_gt):
		expression_gt.expression_left.accept(self)
		print(' > ', end = '')
		expression_gt.expression_rigth.accept(self)

	def visit_expression_ge (self,expression_ge):
		expression_ge.expression_left.accept(self)
		print(' >= ', end = '')
		expression_ge.expression_rigth.accept(self)

	def visit_expression_lt (self,expression_lt):
		print(expression_lt.expression_left)
		print(' < ', end = '')
		print(expression_lt.expression_rigth)

	def visit_expression_le (self,expression_le):
		expression_left.expression_left.accept(self)
		print(' <= ', end = '')
		expression_le.expression_rigth.accept(self)

	def visit_expressioin_minus (self,expression_minus):
		expression_minus.expression_left.accept(self)
		print(' - ', end = '')
		expression_minus.expression_rigth.accept(self)

	def visit_expression_plus (self,expression_plus):
		expression_plus.expression_left.accept(self)
		print(' + ', end = '')
		expression_plus.expression_rigth.accept(self)

	def visit_expression_mult (self,expression_mult):
		expression_mult.expression_left.accept(self)
		print(' * ', end = '')
		expression_mult.expression_rigth.accept(self)

	def visit_expression_divide (self,expression_divide):
		expression_divide.expression_left.accept(self)
		print(' / ', end = '')
		expression_divide.expression_rigth.accept(self)

	def visit_expression_module (self,expression_module):
		expression_module.expression_left.accept(self)
		print(' % ', end = '')
		expression_module.expression_rigth.accept(self)

	def visit_expression_equals (self,expression_equals):
		expression_equals.expression_left.accept(self)
		print(' == ', end = '')
		expression_equals.expression_rigth.accept(self)

	def visit_expression_different (self,expression_different):
		expression_different.expression_left.accept(self)
		print('!=', end = '')
		expression_different.expression_rigth.accept(self)

	def visit_argumentlist (self,argumentlist):
		print(argumentlist.id_, end = '')
		print('(', end = '')
		print(',',end = '')
		print(argumentlist.id_2, end = '')
		print(')', end = '')
		print('*', end = '')
		print('[', end = '')
		print(',', end = '')
		print('*', end = '')
		print('[', end = '')
		print(argumentlist.id_3, end = '')
		print(']', end = '')
		print(']', end = '')
		print('[', end = '')
		print(',', end = '')
		print('&', end = '')
		print(argumentlist.id_4, end = '')
		print(']', end = '')

	def visit_argumentlist2(self, argumentlist2):
		print('*', end = '')
		print(argumentlist2.id_, end = '')
		print('[', end = '')
		print(',', end = '')
		print('&', end = '')
		print(argumentlist2.id_2, end = '')
		print(']', end = '')

	def vist_argumentlist3(self, argumentlist3):
		print('[', end = '')
		print('&', end = '')
		print(argumentlist3.id_, end = '')
		print(']', end = '')

	def visit_read_gets (self,read_gets):
		print(read_gets.id_, end = '')
		print('=', end = '')
		print('gets', end = '')

	def visit_puts_const_string(self,puts_const_string):
		print('puts', end = '')
		puts_const_string.const_string.accept(self)

	def visit_puts_expression(self,puts_expression):
		print('puts', end = '')
		puts_expression.expression_variable.accept(self)

	def visit_puts_string(self,puts_string):
		print('puts', end = '')
		print('\'', end = '')
		puts_string.const_string.accept(self)
		print('\'', end = '')

	def visit_puts_expressionq(self,puts_expressionq):
		print('puts', end = '')
		print('\'', end = '')
		puts_expressionq.expression_variable.accept(self)
		print('\'', end = '')

	def visit_puts_string_dq(self,puts_string_dq):
		print('puts', end = '')
		print('"', end = '')
		puts_string_dq.const_string.accept(self)
		print('"', end = '')

	def visit_puts_expression_dq(self,puts_expression_dq):
		print('puts', end = '')
		print('"', end = '')
		puts_expression_dq.expression_variable.accept(self)
		print('"', end = '')


	def visit_pointer (self,pointer):
		print(pointer.value, end = '')

	def visit_asterisk(self,asterisk):
		print(asterisk.value, end = '')

	def visit_pointer_acess(self,pointer_acess):
		print(pointer_acess.value, end = '')

	def visit_token_land(self,token_land):
		print(token_land.land, end = '')

	def vist_token_and(self,token_and):
		print(token_and.and_, end = '')

	def visit_declaration_pointer (self,declaration_pointer):
		print(declaration_pointer.id_,end = '')

	def visit_acess_pointer (self,acess_pointer):
		print(acess_pointer.id_, end = '')

	def visit_matrix (self,matrix):
		print('[',end = '')
		matrix.argument.accept(self)
		print(']', end = '')
		matrix.matrix.accept(self)

	def visit_matrix2(self, matrix2):
		print('[', end = '')
		matrix2.argument.accept(self)
		print(']', end = '')
		print(',', end = '')
		matrix2.matrix.accept(self)

	def visit_matrix_arg(self,matrix_arg):
		print('[', end = '')
		matrix_arg.argument.accept(self)
		print(']', end = '')

	def visit_matrix_rec(self,matrix_rec):
		print('[', end = '')
		matrix_rec.matrix.accept(self)
		print(']', end = '')

	def visit_argument (self,argument):
		argument.argument.accept(self)
		print(',', end = '')
		argument.expression.accept(self)