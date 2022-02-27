from io import TextIOWrapper as FILE

def init(file : str) -> FILE:
    fp : FILE = open(file)
    return fp

