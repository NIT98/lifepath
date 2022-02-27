import astlp as AST
from stacklp import StackLP

stk = StackLP(1024)

def interpreter( ast : AST.Node ):
    if isinstance(ast,AST.ASTLp):
        pass
    else:
        print("ast error: please entered root ast LP");