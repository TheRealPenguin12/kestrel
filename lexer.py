import ply.lex as lex
import sys

tokens = (
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'PRINT',
    'EQ',
    'NEQ',
    'STRING',
    'INPUT',
    'WAIT',
)

literals = { '+', '-', '*', '/', '>', '<', '^', '%', '&' }

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PRINT = r'print:'
t_EQ = r'=='
t_NEQ = r'!='
t_INPUT = r'input:'
t_WAIT = r'wait:'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_EXIT(t):
    r'exit'
    sys.exit()

def t_COMMENT(t):
    r'\&.*'
    pass

def t_STRING(t):
    r'\"[^"\n]*\"'
    t.value = t.value.replace('"', '')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

