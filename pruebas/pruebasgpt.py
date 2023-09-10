def comparar_listas_numeros(lista1, lista2):
    # Verifica si las listas tienen la misma longitud
    if len(lista1) != len(lista2):
        return "Las listas no tienen la misma longitud"
    
    # Invierte las listas para comparar desde la posición de mayor peso
    lista1 = lista1[::-1]
    lista2 = lista2[::-1]

    for i in range(len(lista1)):
        if lista1[i] > lista2[i]:
            return True
        elif lista2[i] > lista1[i]:
            return False
    
    return "Ambas listas son iguales"

# Ejemplo de uso
lista1 = [4, 3, 2, 0, 0]  # 1235
lista2 = [4, 3, 2, 1, 0]  # 1234

resultado = comparar_listas_numeros(lista1, lista2)
print(resultado)
