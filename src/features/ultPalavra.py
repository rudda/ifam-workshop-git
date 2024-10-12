def tamanho_ultima_palavra(x: str) -> int:
    x = x.strip()
    palavras = x.split()
    return len(palavras[-1])

# Exemplo de uso:
x = tamanho_ultima_palavra("olá mundo")
print(x)  # Saída: 5 (que é o tamanho da palavra "mundo")