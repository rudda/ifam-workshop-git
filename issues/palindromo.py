'''
Palíndromo de Inteiro
Dado um inteiro x, retorne verdadeiro se x for um palíndromo e falso caso contrário.

Exemplos
Exemplo 1:
Entrada: x = 121
Saída: verdadeiro
Explicação: 121 lido da esquerda para a direita e da direita para a esquerda é o mesmo.
Exemplo 2:
Entrada: x = -121
Saída: falso
Explicação: Da esquerda para a direita, lê-se -121. Da direita para a esquerda, torna-se 121-. Portanto, não é um palíndromo.
Exemplo 3:
Entrada: x = 10
Saída: falso
Explicação: Lendo da direita para a esquerda, temos 01. Portanto, não é um palíndromo.'''

def palindromo(num):
    if num < 0:
        return False
    
    string_num = str(num)
    string_reversa = string_num[ :: -1]

    return string_num == string_reversa

numero_teste = 121

if palindromo(numero_teste):
    print(f"O numero {numero_teste} é palindromo")
else:
    print(f"O numero {numero_teste} não é palindromo")