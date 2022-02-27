class Node( object ):
    def __init__( self ):
        self.label = "AST"
        self.parent = None
        self.value = dict()
        self.children = []

    def first(self):
        return self.children[0]
