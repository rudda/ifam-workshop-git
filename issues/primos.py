def crivo_de_eraatostenes(n):
    primos = [True] * (n + 1)
    primos[0] = primos[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primos[i]:
            for j in range(i * i, n + 1, i):
                primos[j] = False

    n_primos = [i for i in range(2, n + 1) if primos[i]]
    return n_primos
    
limite = 100
primes = crivo_de_eraatostenes(limite)
print(primes)