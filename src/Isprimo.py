
def is_primo(n):

    if n <= 1:
        return False
    
    else:
        for i in  range(2, int(n**0.5)+ 1):

            if n % i ==0:
                return False
            
        return True
    

nu = int(input("Informe um número: "))

if is_primo(nu):
    print(f"{nu} é primo")
else:
   print(f"{nu} não é primo")
    



    

