import sys
from posixpath import abspath
from lexerlp import init
from parserlp import parse

if len(sys.argv) < 2 :
    print("please entered spesific file path")
    exit(1)

path = sys.argv[1]
lexfp = init(abspath(path))
parse(lexfp)
