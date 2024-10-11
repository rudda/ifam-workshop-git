def comprimento_ultima_palavra(s: str) -> int:
    
    s = s.rstrip()

    palavras = s.split()

    return len(palavras[-1]) if palavras else 0


print(comprimento_ultima_palavra("Hello World"))               
print(comprimento_ultima_palavra("   fly me   to   the moon  ")) 
print(comprimento_ultima_palavra("luffy is still joyboy"))      