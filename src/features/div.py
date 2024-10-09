def div(a: float, b: float) -> float:
    """
    Divide dois números e retorna o resultado, verificando se os inputs são válidos.

    Args:
    a (float): O primeiro número.
    b (float): O segundo número. Não pode ser zero.

    Returns:
    float: A divisão de a por b.

    Raises:
    ValueError: Se b for zero ou se a ou b não forem números, a função levantará um erro.
    """
    # Verifica se os valores são números
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Os valores 'a' e 'b' devem ser números.")
    
    # Verifica se o divisor é zero
    if b == 0:
        raise ValueError("O divisor 'b' não pode ser zero.")
    
    return a / b
