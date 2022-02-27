from io import TextIOWrapper as FILE

def nextch(fp : FILE):
    return fp.read(1)

def seeknxt(fp : FILE):
    nextch(fp)
    return fp.tell()

def seekprv(fp : FILE):
    tel = fp.tell() - 1
    fp.seek(tel,0)
    return tel