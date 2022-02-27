from errorlp import errpars
from iolp import iseof
from lexerlp import droptoken, gettoken
import astlp as AST 

def parse(fp) -> AST.ASTLp:
    return lp(fp)

def lp(fp) -> AST.ASTLp:
    if iseof(gettoken(fp)):
        return AST.ASTLp0()
    
    return AST.ASTLp1(stmt(fp),lp(fp))

def stmt(fp) -> AST.ASTStmt:
    k = droptoken(fp)
    
    if k == "PUSH":
        return AST.ASTStmtPush(stmtn(fp))
    elif k == "LD":
        return AST.ASTStmtLoad(stmtn(fp))
    elif k == "ST":
        return AST.ASTStmtStore(stmtn(fp))
    elif k == "PRINT":
        return AST.ASTStmtPrint()
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

    errpars("expected keyword [%s]" % k)

# stmt with number after keyword
def stmtn(fp) -> AST.ASTStmtNum:
    num = droptoken(fp)

    if num and num.isnumeric():
        return AST.ASTStmtNum(num)
    
    errpars("expected numeric token [%s]" % num)
    exit(1)