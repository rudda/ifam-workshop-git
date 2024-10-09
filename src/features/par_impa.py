def par_ou_impar():
    try:
        n = int(input("Digite um número inteiro: "))  # Captura a entrada do usuário e tenta converter para inteiro
        
        if n == 0:
            return "Erro: O número não pode ser zero."
        
        if n % 2 == 0:
            return "par"
        else:
            return "ímpar"
    except ValueError:
        return "Erro: A entrada deve ser um número inteiro."

# Chamando a função e exibindo o resultado
resultado = par_ou_impar()
print(resultado)
