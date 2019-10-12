import sys
sys.path.insert(0, "../..")

import re
import ply.lex as lex

# stack for indentation width
indents = [0]



#Reserved Words
keywords = ('if','elsif','else','begin','end','then',
			'while','for','do',
			'in','repeat','unless','puts',
			'break','continue','gets','int', 
			'float','boolean', 'True', 'False')

tokens = keywords + ('EQUALS','DIFFERENT', 'PLUS','MINUS', 
					'ASTERISK', 'DIVIDE','LPAREN', 
					'RPAREN','LBRACKET','RBRACKET', 'LT', 
					'LE', 'GT', 'GE', 'ASSIGNMENT', 'MODULE',
					'AND','OR','NOT','COMMA','ID','CONST_INTERGER',
					'CONST_REAL','QUOTATION','DQUOTATION',
					'CONST_STRING', 'POINT','DPOINT','POINTPOINT','SEMICOLON',
					'DSING','INDENT','DEDENT','LAND')

#Tokens

t_EQUALS 			= r'=='
t_DIFFERENT 		= r'!='
t_ASSIGNMENT 		= r'='

t_PLUS 				= r'\+'
t_MINUS 			= r'-'
t_ASTERISK 			= r'\*'
t_DIVIDE 			= r'/'
t_MODULE 			= r'\%'

t_AND			 	= r'\&\&'
t_OR 				= r'\|\|'
t_NOT 				= r'\!'
t_LAND				= r'&'

t_LPAREN 			= r'\('
t_RPAREN 			= r'\)'
t_LBRACKET 			= r'\['
t_RBRACKET 			= r'\]'

t_LT 				= r'<'
t_LE 				= r'<='
t_GT 				= r'>'
t_GE 				= r'>='

t_DSING				= r'\$'
t_COMMA 			= r'\,'
t_QUOTATION 		= r'\''
t_DQUOTATION		= r'\"'
t_POINT 			= r'\.'
t_POINTPOINT 		= r'\.\.'
t_DPOINT 			= r':'
t_SEMICOLON 		= r';'


#t_ignore = '\r'

states = (
  	('dedents', 'inclusive'),
)


def t_dedents_DEDENT(t):
	r'\n\t*|\t+'
	if indents[-1] <= t.lexer.width:
		t.lexer.begin('INITIAL')
		return None
	else:
		indents.pop()
		t.lexer.skip(-1)
		t.type = 'DEDENT'
		t.lexer.begin('dedents')
		return t

def t_indent(t):
	r'(\n\t*|^\t+)'
	if t.lexer.lexpos >= len(t.lexer.lexdata) or t.lexer.lexdata[t.lexer.lexpos] == "\n": # empty line
		return None # ignore empty line
	t.lexer.width = len(t.value) - (t.value[0] == '\n')
	if t.lexer.width == indents[-1]:
		return None # same indentation level
	elif t.lexer.width > indents[-1]: # one more level
		t.type = 'INDENT'
		indents.append(t.lexer.width)
		return t
	else: # try one or more DEDENTS
		t.lexer.skip(-1) #return one character to match the regular expression \t+ in dedents state
		t.lexer.begin('dedents')


def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value in keywords:
        t.type = t.value
    return t

def t_CONST_STRING(t):
	r'\".(\n|.)*?\"'
	return t

def t_CONST_REAL(t):
	r'([0-9]*[.][0-9]+((E|e)[+|-]?[0-9]+)?)'
	return t

def t_CONST_INTERGER(t):
	r'\d+'
	return t

def t_COMMENT_MONOLINE(t):
	r'\#.*'
	pass

def t_CODE_COMMENT(t):
	r'(=begin(.|\n)*?=end)'
	pass

def t_eof(t):
	while len(indents) > 1:
		indents.pop()
		t.type = 'DEDENT'
		return t


def t_space(t):
	r'[ ]+'

# ignore tabs occuring elsewhere in the code
def t_tab(t):
	r'\t'

# re.MULTILINE is enabled because original Python recognizes INDENT in first line,
# therefore it is needed for ^ matches the start of a line.
lexer = lex.lex(reflags = re.MULTILINE)

# current tabs' width for INDENT and DEDENT tokens
lexer.width = 0


def test():
	arq = open('arquivo.txt','r')
	data = arq.read()
	lexer.input(data)

	while True:
		tok = lexer.token()
		if not tok:
			break
		print(tok)
	arq.close()

#test()
