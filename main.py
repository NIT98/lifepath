from posixpath import abspath
import sys
from interpreterlp import interpreter

from parserlp import parse
from lexerlp import init as lexerinit

if len(sys.argv) < 2 :
    print("please entered spesific file path")
    exit(1)

path = sys.argv[1]
lex = lexerinit(abspath(path))
ast = parse(lex)
interpreter(ast)