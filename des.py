def contem_duplicados(a1, a2):
    duplicados  = [ ]
    for valores_a2 in a2: 
        for valores_a1 in a1:
            if valores_a1 == valores_a2:
                duplicados.append(valores_a1)

    return duplicados


a1 = [1,2,3,4,5,6]
a2 = [2,3,5,8,9]
print(contem_duplicados(a1, a2))

