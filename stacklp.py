class StackLP:
    def __init__(self,size:int) -> None:
        self.size = size
        self.board = [0] * size
        self.curidx = -1 