from io import TextIOWrapper as FILE

def nextch(fp : FILE):
    return fp.read(1)

def seeknxt(fp : FILE):
    nextch(fp)
    return fp.tell()
