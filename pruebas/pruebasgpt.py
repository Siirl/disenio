def igualar_longitud_listas(lista1, lista2):
    
    lista1.append(0)
    lista2.append(0)
    len1 = len(lista1)
    len2 = len(lista2)
    print(lista1, lista2)
    if len1 < len2:
        diferencia = len2 - len1
        lista1 = [0] * diferencia + lista1
        
    elif len2 < len1:
        diferencia = len1 - len2
        lista2 = [0] * diferencia + lista2

    return lista1, lista2

# Ejemplo de uso:
lista1 = [1, 2, 3, 4, 5,6,7,8,9,0,9,8,6,5]
lista2 = [1, 2, 3]
lista1, lista2 = igualar_longitud_listas(lista1, lista2)
print(lista1)  # Salida: [0, 1, 2, 3, 4, 5]
print(lista2)  # Salida: [0, 0, 0, 1, 2, 3]
