import itertools

tabla_verdad=[]

def generar_tabla(variables,n):
    global tabla_verdad
    tabla_verdad.clear
    combinacion_variables = list(itertools.product([0, 1], repeat=n))
    tabla_verdad.append(variables)
    for combinacion in combinacion_variables:
        valores = [str(value) for value in combinacion]
        tabla_verdad.append(valores)
    for sublista in tabla_verdad:
        sublista.append('|')


def suma(tabla,val1,val2):
    global tabla_verdad
    if tabla_verdad[0][val1] == '|':
        return tabla_verdad[0][val2]
    result=[f'{tabla_verdad[0][val1]}+{tabla_verdad[0][val2]}']
    texto=result[0]
    for x in range(len(tabla_verdad)-1):
        valor1=tabla_verdad[x+1][val1]
        valor2=tabla_verdad[x+1][val2]
        operacion = int(valor1) or int(valor2)
        result.append(str(operacion))
    result=unir_tablas(tabla_verdad,result)
    tabla_verdad=result
    return texto

def multiplicacion(tabla,val1,val2):
    global tabla_verdad
    if tabla_verdad[0][val1] == '|':
        return tabla_verdad[0][val2]
    result=[f'{tabla_verdad[0][val1]}*{tabla_verdad[0][val2]}']
    texto=result[0]
    for x in range(len(tabla_verdad)-1):
        valor1=tabla_verdad[x+1][val1]
        valor2=tabla_verdad[x+1][val2]
        operacion = int(valor1) and int(valor2)
        result.append(str(operacion))
    result=unir_tablas(tabla_verdad,result)
    tabla_verdad=result
    return texto

def negacion(tabla,n):
    global tabla_verdad
    result=[f'-({tabla[0][n]})']
    texto=result[0]
    for x in range(len(tabla)-1):
        valor1=tabla[x+1][n]
        operacion = not int(valor1)
        result.append(int(operacion))
    result=unir_tablas(tabla,result)
    tabla_verdad=result
    return texto


def unir_tablas(tabla_base, tabla_resultado):
    # Asegúrate de que la longitud de tabla_base y tabla_resultado coincida
    if len(tabla_base) != len(tabla_resultado):
        raise ValueError("Las tablas deben tener la misma longitud")

    # Encabezado de la tabla final
    tabla_final = [tabla_base[0] + [tabla_resultado[0]]]

    for i in range(1, len(tabla_base)):
        fila_base = tabla_base[i]
        fila_resultado = [fila_base[0]] + fila_base[1:] + [tabla_resultado[i]]
        tabla_final.append(fila_resultado)

    return tabla_final