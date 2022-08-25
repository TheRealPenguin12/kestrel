import ply.lex as lex
import re

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PRINT',
    'LPAREN',
    'RPAREN',
    'INPUT',
)
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_PRINT = r'print'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_INPUT = r'input'
t_ignore  = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_COMMENT(t):
    r'\%.*'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

