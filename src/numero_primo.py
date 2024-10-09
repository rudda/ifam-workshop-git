def numero_primo(a):
    """
    Verifica se um número é primo.
    
    :param a: Número a ser verificado
    :return: True se o número é primo, False caso contrário
    """
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True