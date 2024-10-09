def palindromo(x: int) -> bool:
    if x < 0:
        return False
    
    str_x = str(x)
    
    return str_x == str_x[::-1]

print(palindromo(121))
print(palindromo(-121))
print(palindromo(10))
