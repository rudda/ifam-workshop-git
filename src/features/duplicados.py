def duplicados(array:list):
    sem_duplicatas = set(array)
    tam_array = len(array)
    valores_unicos = len(sem_duplicatas)
    
    if (tam_array == valores_unicos):
        return False
    else:
        return True
    