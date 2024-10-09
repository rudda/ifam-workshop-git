def palindromo(x):
    # Verifica se x é negativo
    if x < 0:
        return False
    
    # Converte o número em string
    str_x = str(x)
    
    # Compara a string com sua reversa
    return str_x == str_x[::-1]

# Testando os exemplos
print(palindromo(121))   # Saída: True
print(palindromo(-121))  # Saída: False
print(palindromo(10))    # Saída: False
