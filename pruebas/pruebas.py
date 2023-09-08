lista_numeros=[]
def encontrar_exponente(base_1, base_2):
    exponente = 0
    while base_1 ** exponente != base_2:
        exponente += 1
        if base_1 ** exponente > base_2:
            return None  # No es una relación de potencias exacta
    return exponente

def encontrar_relacion_potencias(base_destino, base_origen, invertido):
    if invertido:
        exponente = encontrar_exponente(base_destino, base_origen)
        print("Invertido")
    else:
        exponente = encontrar_exponente(base_origen, base_destino)    
        print("Normal")
    if exponente is not None:
        return exponente
    else:
        return "No hay una relación de potencias exacta"
    
def agregar_ceros(exponente):
    numero = 1
    veces = int(exponente)-1
    for x in range(veces):
        numero= int(str(numero)+str(0))
    return numero

def arreglarLista(lista,numeeee):
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

    return grup

def convert_bases_relation_normal(lista_numeros,base_origen,exponente):
    result = ""
    numero=0
    lista_strings = list(map(str, lista_numeros))
    list_arreglada = arreglarLista(lista_strings,exponente)
    lista_arre_str = list(map(str, list_arreglada))
    print(lista_arre_str)
    for x in range(len(lista_arre_str)): #Se opera
        num_in_x = "{:0{exponente}d}".format(int(lista_arre_str[x]), exponente=exponente) #cadena de formato obtenida en GPT
        print(num_in_x)
        for exp in range(exponente):
            dividir = agregar_ceros(exponente-exp)
            temp= int(num_in_x)//dividir
            print("num_in_x al inicio ",num_in_x)
            numero = numero +(temp*(int(base_origen)**(exponente-exp-1)))
            print("numero operado ",numero)
            if len(num_in_x)>1:
                num_in_x=num_in_x[1:]
                print("longitud ",len(num_in_x))
        print("SALIO")
        result=str(numero)+result
        numero=0
    return result

base_destino = int(input("Digite la base destino del numero "))
base_origen = int(input("Digite la base origen del numero "))
tam = int(input("Ingrese la cantidad de elementos de su numero"))
for x in range(tam):
    lista_numeros.append(int(input(f"Ingrese el numero #{x+1} ")))
if base_destino>base_origen:
    invertido=False
else:
    invertido=True
exponente=encontrar_relacion_potencias(base_destino,base_origen,invertido)
print(convert_bases_relation_normal(lista_numeros,base_origen,exponente))
