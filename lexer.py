from io import TextIOWrapper

fp : TextIOWrapper = None

def init(file : str):
    fp = open(file)
    print(fp)

