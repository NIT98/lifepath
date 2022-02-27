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
    pass