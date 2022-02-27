from errorlp import errpars
from iolp import iseof
from lexerlp import droptoken

def parse(fp):
    pass

def lp(fp):
    if iseof(fp):
        return
    
    stmt(fp)
    lp(fp)

def stmt(fp):
    k = droptoken(fp)
    
    if k == "PUSL":
        stmtn(fp)
    elif k == "LD":
        stmtn(fp)
    elif k == "ST":
        stmtn(fp)
    elif k == "PLUS":
        pass
    elif k == "MIN":
        pass
    elif k == "MUL":
        pass
    elif k == "DIV":
        pass    
    elif k == "PER":
        pass    

# stmt with number after keyword
def stmtn(fp) -> int:
    num = droptoken(fp)
    if num.isnumeric():
        return num
    
    errpars("expected numeric token [%s]" % num)
    exit(1)