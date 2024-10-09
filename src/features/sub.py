def sub_integers(a: int, b: int):
    return a - b

def sub_floats(a: float, b: float):
    return a - b

def sub_invalid_params(a, b):
    try:
        a, b = int(a), int(b)
        
        return "OK"
    except:

        return None

def sub_with_zero(a, b):
    return a - b

def sub_multiple_integers(a, b, c, d = None):
    if d is not None:
        return a - b - c - d
    else:
        return a - b - c

def sub_mixed_types(a, b, c):
    return a - b - c
