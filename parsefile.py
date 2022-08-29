import lexer
import parser
import sys

parser.env = "file"
s = open(sys.argv[1]).read()
for line in s.split("\n"):
    try:
        result = parser.parser.parse(line)
    except EOFError:
        break
