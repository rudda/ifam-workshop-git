def par_ou_impar():
    try:
        n = float(input("Digite um número inteiro: "))  # Captura a entrada do usuário como float
        
        # Verifica se o número é inteiro
        if n.is_integer():
            n = int(n)  # Converte para inteiro
            
            if n == 0:
                return "Erro: O número não pode ser zero."
            
            if n % 2 == 0:
                return "par"
            else:
                return "ímpar"
        else:
            return "Erro: A entrada deve ser um número inteiro."
    except ValueError:
        return "Erro: A entrada deve ser um número."

# Chamando a função e exibindo o resultado
resultado = par_ou_impar()
print(resultado)
