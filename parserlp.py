from errorlp import errpars
from iolp import iseof
from lexerlp import droptoken, gettoken

def parse(fp):
    lp(fp)

def lp(fp):
    if iseof(gettoken(fp)):
        return
    
    print("lp")
    stmt(fp)
    lp(fp)

def stmt(fp):
    k = droptoken(fp)
    print("stmt",k)
    
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
    print("stmtn",num)
    if num and num.isnumeric():
        return num
    
    errpars("expected numeric token [%s]" % num)
    exit(1)