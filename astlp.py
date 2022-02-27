class Node( object ):
    def __init__( self ):
        self.label = "AST"
        self.parent = None
        self.value = dict()
        self.children = []

    def first(self):
        return self.children[0]

    def setvalue(self,key : str, data : any):
        self.value[key] = data
    
    def getvalue(self,key : str):
        return self.value.get(key)

class ASTLp( Node ):
    def __init__(self):
        self.label = "lp"
        super().__init__()

class ASTStmt ( Node ):
    def __init__(self):
        self.label = "stmt"
        super().__init__()


class ASTStmtNum( Node ):
    def __init__(self,num):
        self.setvalue("int",int(num))

class ASTLp0( ASTLp ):
    def __init__(self):
        super().__init__()

class ASTLp1( ASTLp ):
    def __init__(self,stmt:ASTStmt,lp:ASTLp):
        self.stmt = stmt
        self.lp = lp
        self.children = [stmt,lp]
        super().__init__()


class ASTStmtPush( ASTStmt ):
    def __init__(self,num : ASTStmtNum):
        self.num = num
        self.children  = [num]
        super().__init__()

class ASTStmtLoad( ASTStmt ):
    def __init__(self,src : ASTStmtNum):
        self.src = src
        self.children  = [src]
        super().__init__()

class ASTStmtStore( ASTStmt ):
    def __init__(self,src : ASTStmtNum):
        self.src = src
        self.children  = [src]
        super().__init__()

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
