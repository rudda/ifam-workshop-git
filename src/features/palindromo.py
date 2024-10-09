x = int(input())

def palindromo():
    string_x = str(x)

    if string_x == string_x[::-1]:
        print("Verdadeiro")
    else:
        print("Falso")
