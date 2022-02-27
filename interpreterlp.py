import astlp as AST
from stacklp import StackLP

stk = StackLP(1024)

def interpreter( ast : AST.Node ):
    if isinstance(ast,AST.ASTLp):
        pass
    else:
        print("ast error: please entered root ast LP");

def lp( ast : AST.Node ):
    if isinstance(ast,AST.ASTLp1):
        stmt(ast.stmt)
        interpreter(ast.lp)

def stmt(ast : AST.Node):
    if isinstance(ast,AST.ASTStmtPrint):
        pass
    if isinstance(ast,AST.ASTStmtPush):
        pass
    if isinstance(ast,AST.ASTStmtLoad):
        pass
    if isinstance(ast,AST.ASTStmtStore):
        pass
    if isinstance(ast,AST.ASTStmtPlus):
        pass
    if isinstance(ast,AST.ASTStmtMin):
        pass
    if isinstance(ast,AST.ASTStmtMul):
        pass
    if isinstance(ast,AST.ASTStmtDiv):
        pass
    if isinstance(ast,AST.ASTStmtPer):
        pass


def stmtprint():
    num = stk.pop()
    print(num)
