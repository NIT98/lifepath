class Node( object ):
    def __init__( self ):
        self.label = "AST"
        self.parent = None
        self.value = dict()
        self.children = []

    def addchild(self, child):
        self.children.append(child)

    def first(self):
        return self.children[0]

    def setvalue(self,key : str, data : any):
        self.value[key] = data

    def getvalue(self,key : str):
        return self.value.get(key)

class ASTLp( Node ):
    def __init__(self):
        super().__init__()
        self.label = "lp"

class ASTStmt ( Node ):
    def __init__(self):
        super().__init__()
        self.label = "stmt"

class ASTStmtNum( Node ):
    def __init__(self,num):
        super().__init__()
        self.setvalue("int",int(num))
        
class ASTLp0( ASTLp ):
    def __init__(self):
        super().__init__()

class ASTLp1( ASTLp ):
    def __init__(self,stmt:ASTStmt,lp:ASTLp):
        super().__init__()
        self.stmt = stmt
        self.lp = lp
        self.addchild(stmt)
        self.addchild(lp)

class ASTStmtPush( ASTStmt ):
    def __init__(self,num : ASTStmtNum):
        super().__init__()
        self.num = num
        self.addchild(num)

class ASTStmtLoad( ASTStmt ):
    def __init__(self,src : ASTStmtNum):
        super().__init__()
        self.src = src
        self.addchild(src)

class ASTStmtStore( ASTStmt ):
    def __init__(self,src : ASTStmtNum):
        super().__init__()
        self.src = src
        self.addchild(src)

class ASTStmtPlus( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtMin( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtMul( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtDiv( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtPer( ASTStmt ):
    def __init__(self):
        super().__init__()

class ASTStmtPrint( ASTStmt ):
    def __init__(self):
        super().__init__()
