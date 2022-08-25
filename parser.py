import ply.yacc as yacc
from lexer import tokens

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_term_print(p):
    'term : PRINT term'
    print(p[2])

def p_term_input(p):
    'term : INPUT term'
    p[0] = input(p[2])

def p_term_paren(p):
    'term : LPAREN term RPAREN'

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input")

parser = yacc.yacc()

while True:
    s = input('Kestrel -> ')
    result = parser.parse(s)
