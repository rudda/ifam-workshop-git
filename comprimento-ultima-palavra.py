# Conta as letras da última palavra
# @frase: string = Frase a ser utilizada para contagem de caracteres da última palavra
def comprimento_ultima_palavra(frase):
    cont = 0

    palavras = frase.split()

    ult_palabra = palavras[-1]

    for caractere in ult_palabra:
        if caractere.isalpha():
            cont += 1
    
    return cont

# Teste do componente acima

# Input para captura de frase
frase = input("Escreva uma palavra ou frase: ")

# Retorno da contagem
cont = comprimento_ultima_palavra(frase)

# Exibição do teste
print(f"Contagem de letras na última palavra: {cont}")
