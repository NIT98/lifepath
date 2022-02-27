
def printerr(key : str, msg : str):
    print("%s : %s" % (key,msg))

def errlex(msg : str):
    printerr("Lexical Error",msg)

def errpars(msg : str):
    printerr("Parser Error",msg)

def errsem(msg : str):
    printerr("Semantic Error",msg)