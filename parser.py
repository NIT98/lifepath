from iolp import iseof


def parse(fp):
    pass

def lp(fp):
    if iseof(fp):
        return
    
    stmt(fp)
    lp(fp)

def stmt(fp):
    pass

# stmt with number after keyword
def stmtn(fp) -> int:
    pass