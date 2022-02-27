from posixpath import abspath
import sys
from lexerlp import droptoken,init

if len(sys.argv) < 2 :
    print("please entered spesific file path")
    exit(1)

path = sys.argv[1]
fp = init(abspath(path))
c = ' '
while c != None:
    c = droptoken(fp)
    print(c)