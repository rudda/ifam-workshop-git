

def sub(a, b, c=None, d=None):

    if c is None and d is None:
        return a - b
    elif d is None :
        return a - b - c
    else:
        return a - b - c - d