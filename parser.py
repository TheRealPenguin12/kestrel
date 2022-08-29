import ply.yacc as yacc
from lexer import tokens
import lexer
import sys
from colorama import *
import time

env = ""


def p_expression_plus(p):
    'expression : expression "+" term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression "-" term'
    p[0] = p[1] - p[3]

def p_expression_eq(p):
    'factor : factor EQ term'
    p[0] = p[1] == p[3]

def p_expression_neq(p):
    'factor : factor NEQ term'
    p[0] = p[1] != p[3]

def p_expression_gt(p):
    'factor : factor ">" term'
    p[0] = p[1] > p[3]

def p_expression_lt(p):
    'factor : factor "<" term'
    p[0] = p[1] < p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term "*" factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term "/" factor'
    try:
        p[0] = p[1] / p[3]
    except ZeroDivisionError:
        print(f"{Fore.RED}{Style.BRIGHT}DivisionByZeroError: {Style.NORMAL}Division by zero not aloud.{Style.RESET_ALL}")

def p_term_string(p):
    'term : STRING'
    p[0] = p[1]

def p_term_print(p):
    'term : PRINT term'
    if env == "ide":
        print(p[2], end="")
        p[0] = ""
    elif env == "file":
        print(p[2])

def p_term_input(p):
    'term : INPUT term'
    p[0] = input(p[2])

def p_term_wait(p):
    'term : WAIT term'
    try:
        time.sleep(int(p[2]))
    except ValueError:
        print(f"{Fore.RED}{Style.BRIGHT}IntegerError: {Style.NORMAL}Wait only excepts integer arguments.{Style.RESET_ALL}")

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_term_simpletimes(p):
    'term : term LPAREN expression RPAREN'
    p[0] = p[1] * p[3]

def p_error(p):
    try:
        print(f"{Fore.RED}{Style.BRIGHT}{p.value}:{Style.NORMAL} Syntax error on line {lexer.lexer.lineno}{Style.RESET_ALL}")
    except AttributeError as e:
        print(f"{Fore.RED}{Style.BRIGHT}line {lexer.lexer.lineno}:{Style.NORMAL} Syntax error{Style.RESET_ALL}")

parser = yacc.yacc()
