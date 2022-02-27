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
        stmtprint()
    if isinstance(ast,AST.ASTStmtPush):
        stmtpush(ast)
    if isinstance(ast,AST.ASTStmtLoad):
        stmtload(ast)
    if isinstance(ast,AST.ASTStmtStore):
        stmtstore(ast)
    if isinstance(ast,AST.ASTStmtPlus):
        stmtplus()
    if isinstance(ast,AST.ASTStmtMin):
        stmtmin()
    if isinstance(ast,AST.ASTStmtMul):
        stmtmul()
    if isinstance(ast,AST.ASTStmtDiv):
        stmtdiv()
    if isinstance(ast,AST.ASTStmtPer):
        stmtper()

    stk.print()

def stmtprint():
    num = stk.pop()
    print(num)

def stmtpush(ast : AST.ASTStmtPush):
    num = int(ast.num.getvalue("int"))
    stk.push(num)

def stmtstore(ast : AST.ASTStmtStore):
    src = ast.src.getvalue("int")

    if src < 0 or src > stk.curidx:
        print("out of bounds source",src)
        exit(1)

    last = stk.pop()
    stk.set(src,last)

def stmtload(ast : AST.ASTStmtLoad):
    num = stk.get(ast.src.getvalue("int"))
    stk.push(num)

def stmtplus():
    nums = stk.popn(2)
    stk.push(nums[0] + nums[1])

def stmtmin():
    nums = stk.popn(2)
    stk.push(nums[0] - nums[1])

def stmtmul():
    nums = stk.popn(2)
    stk.push(nums[0] * nums[1])

def stmtdiv():
    nums = stk.popn(2)
    stk.push(nums[0] / nums[1])

def stmtper():
    nums = stk.popn(2)
    stk.push(nums[0] % nums[1])
