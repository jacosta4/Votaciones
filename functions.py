def CountFrequency(my_list):
    """ Counts the frecuency of a item in a list
        and returns a dictionary with the frecuency of
        each item """

    count = {}
    for i in my_list:
        count[i] = count.get(i, 0) + 1
    return count


def sortedDicc(dicc):
    """ Ordena el diccionario de menor a mayor frecuencia y retorna el ultimo
    valor (el item con mas frecuencia) """
    # Ordena el diccionario de menor a mayor precuencia
    sd = {k: v for k, v in sorted(dicc.items(), key=lambda item: item[1])}
    # Selecciona el ultimo elemento del diccionario
    return list(sd)[-1]
