def div_integers(a: int, b: int):
    if b == 0:
        return None
    else:
        return a / b

def div_floats(a: float, b: float):
    if b == 0:
        return None
    else:
        return a / b
    
def div_by_zero(a, b):
    return None

def div_invalid_params(a, b):
    try:
        a, b = int(a), int(b)

        return "OK"
    except:

        return None

def div_numerator_zero(a, b):
    return 0