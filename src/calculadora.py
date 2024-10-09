def parimpar(n):
    if n % 2 == 0:
        return f'{n} é divisível por 2 e é par'
    else:
        return f'{n} não é divisível por 2 e é ímpar'

print(parimpar(10))  
print(parimpar(7))   
