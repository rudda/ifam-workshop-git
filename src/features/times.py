def times_integers(a: int, b: int):
    return a * b

def times_floats(a: float, b: float):
    return a * b

def times_with_zero(a, b):
    return a * b

def times_invalid_params(a, b):
    try:
        a, b = int(a), int(b)

        return "OK"
    except:

        return None
