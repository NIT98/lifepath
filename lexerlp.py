from io import TextIOWrapper as FILE

from iolp import nextch, seekprv

def init(file : str) -> FILE:
    fp : FILE = open(file)
    return fp

def droptoken(fp : FILE) -> str:
    c =  nextch(fp)
    seekprv(fp)

    if c == '':
        return None
    if c == '-':
        #impliment comment functionality
        return droptoken(c)
    if c.isalpha():
        return c
    if c.isnumeric():
        return c

    print("Lexical Error : near token '%s'" % c)
    exit(1)