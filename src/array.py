
def verifica_duplicata():      
    array = [1,2,3,4,5,1]
    if not(len(array) == len(set(array))) == False: 
        print(False)
        print("Não há elementos distintos")
    else:
        print(True)
        print("Há elementos distintos")

verifica_duplicata()