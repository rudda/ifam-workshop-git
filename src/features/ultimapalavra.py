def comprimento_ultima_palavra(s: str) -> int:

    palavras = s.strip().split()

    return len(palavras[-1])

# Testando os exemplos
print(comprimento_ultima_palavra("Sabriza Frazão"))
print(comprimento_ultima_palavra("   workshop LG ZLACademy"))  
print(comprimento_ultima_palavra("Olá mundo!")) 
