from errorlp import errpars
from iolp import iseof
from lexerlp import droptoken, gettoken
import astlp as AST 

def parse(fp):
    lp(fp)

def lp(fp):
    if iseof(gettoken(fp)):
        return AST.ASTLp0()
    
    return AST.ASTLp1(stmt(fp),lp(fp))

def stmt(fp):
    k = droptoken(fp)
    
    if k == "PUSL":
        return AST.ASTStmtPush(stmtn(fp))
    elif k == "LD":
        return AST.ASTStmtLoad(stmtn(fp))
    elif k == "ST":
        return AST.ASTStmtStore(stmtn(fp))
    elif k == "PLUS":
        return AST.ASTStmtPlus()
    elif k == "MIN":
        return AST.ASTStmtMin()
    elif k == "MUL":
        return AST.ASTStmtMul()
    elif k == "DIV":
        return AST.ASTStmtDiv()
    elif k == "PER":
        return AST.ASTStmtPer()

    errpars("syntax error : expected keyword [%s]" % k)

# stmt with number after keyword
def stmtn(fp) -> int:
    num = droptoken(fp)
    print("stmtn",num)
    if num and num.isnumeric():
        return AST.ASTStmtNum(num)
    
    errpars("expected numeric token [%s]" % num)
    exit(1)