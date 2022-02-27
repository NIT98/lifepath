class StackLP:
    def __init__(self,size:int) -> None:
        self.size = size
        self.board = [0] * size
        self.curidx = -1
    
    def push(self,num):
        if self.curidx + 1 >= len(self.board):
            print("overflow stack!")
            exit(1)

        self.curidx += 1
        self.board[self.curidx] = int(num)