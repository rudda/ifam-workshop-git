# Verifica se o número no parâmetro numero é primo
# @numero: int
def numero_primo(numero):
    
    if numero >= 1:
        for i in range(1, numero):
            if numero % i != 0:
                print(numero, 'é primo')
            else:
                print(numero, 'não é primo')
                break
    elif numero == 0:
        print(numero, 'é zero')
    else:
        print(numero, 'é negativo')