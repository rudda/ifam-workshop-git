# src/features/add.py

def add(a, b):
    return a + b

def add_three(a, b, c):
    return a + b + c

def add_multiple_elements(a, b, c, d, e=None):
    if e is not None:
        return a + b + c + d + e
    else:
        return a + b + c + d

def add_invalid_params(a, b, c):
    try:
        a, b, c = int(a), int(b), int(c)

        return "OK"
    except:

        return None

def add_one_element(a):
    return a

def add_no_elements():
    return 0
