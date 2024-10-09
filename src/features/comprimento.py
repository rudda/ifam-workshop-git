def comprimento(s:str):
    palavras = s.split()
    
    ultima_palavra = palavras[-1]
    comprimento = len(ultima_palavra)
    print(comprimento)