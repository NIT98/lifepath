from io import TextIOWrapper as FILE
from errorlp import errlex

from iolp import nextch, seekprv

def init(file : str) -> FILE:
    fp : FILE = open(file)
    return fp

def droptoken(fp : FILE) -> str:
    c =  nextch(fp)
    seekprv(fp)

    if c == '':
        return None
    if c.isspace():
        wspace(fp)
        return droptoken(fp)
    if c == '-':
        comment(fp)
        return droptoken(fp)
    if c.isalpha():
        return iden(fp)
    if c.isnumeric():
        return num(fp)

    errlex("near token '%s'" % c)
    exit(1)

def gettoken(fp : FILE):
    pos =  fp.tell()
    t = droptoken(fp)
    fp.seek(pos, 0)
    return t

def wspace(fp : FILE):
    c = nextch(fp)

    while c.isspace():
        c = nextch(fp)

    if c != '':
        seekprv(fp)

def comment(fp : FILE):
    nextch(fp)
    if nextch(fp) != '-':
        errlex("expected -")

    while nextch(fp) != '\n':
        pass

def iden(fp : FILE):
    c = nextch(fp)
    t = ''

    while c.isalpha():
        t += c
        c = nextch(fp)
    
    if c != '':
        seekprv(fp)

    return t

def num(fp : FILE):
    c = nextch(fp)
    t = ''

    while c.isnumeric():
        t += c
        c = nextch(fp)
    
    if c != '':
        seekprv(fp)

    return t
