result = []
grupos = []

# Divide cada número en dígitos y almacénalos en la lista 'result'
for number in lista:
    number_str = str(number)
    result.extend(map(str, number_str))

# Invierte la lista resultante
lista2 = result[::-1]
# Agrupa en grupos de 3
for i in range(0, len(lista2), numeeee):  # Cambio de 2 a 3 aquí
    grupo = lista2[i:i + numeeee]
    grupos.append(str(''.join(map(str, grupo))))

# Invierte nuevamente cada número en los grupos
grup = [int(str(num)[::-1]) for num in grupos]

