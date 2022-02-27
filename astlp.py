class Node( object ):
    def __init__( self ):
        self.label = "AST"
        self.parent = None
        self.value = dict()
        self.children = []

    def first(self):
        return self.children[0]


class ASTLp( Node ):
    def __init__(self):
        self.label = "lp"
        super().__init__()

class ASTStmt ( Node ):
    def __init__(self):
        self.label = "stmt"
        super().__init__()