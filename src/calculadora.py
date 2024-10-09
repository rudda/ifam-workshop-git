from features import add
from features import sub
from features import times
from features import div
def calculadora():
    """
    Função que realiza operações aritméticas básicas (soma, subtração, multiplicação, divisão).
    
    :return: A soma, subtração, multiplicação ou divisão dos números fornecidos.
    """
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))
    
    
    if operador == "+":
        add(num1, num2)
        print(f"Resultado: {add(num1, num2)}")
    if operador == "-":
        sub(num1, num2)
    if operador == "*":
        times(num1, num2)
        print(f"Resultado: {num1 * num2}")
    if operador == "/":
        if num2 == 0:
            print("Não é possível dividir por zero.")
        else:
            div(num1, num2)
            print(f"Resultado: {div(num1, num2)}")
