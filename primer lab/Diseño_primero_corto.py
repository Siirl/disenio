diccionario = {}
dic_traducido = []
max = 27
min = 0
letrasMayus = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"Ñ",
               16:"O",17:"P",18:"Q",19:"R",20:"S",21:"T",22:"U",23:"V",24:"W",25:"X",26:"Y",27:"Z"}
letras = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j",11:"k",12:"l",13:"m",14:"n",15:"ñ",
          16:"o",17:"p",18:"q",19:"r",20:"s",21:"t",22:"u",23:"v",24:"w",25:"x",26:"y",27:"z"}
simbolos = {1:"!",2:"@",3:"$",4:"%",5:"^",6:"&",7:"(",8:")",9:"_",10:"=",11:"{",12:"}",13:"[",14:"]",15:"?",16:":",17:"<",18:">",19:"/"}
dic_digito =[]
numero_destino = []
def asignar_base_datos():
    minn=min
    temp=0
    num= 1
    for temp in range (10): #Asigna los primeros 10 valores
        
        diccionario.update({temp:str(temp)})
    for minn in range (max): #Asigna los valores 10 al 36
        temp +=1
        diccionario.update({temp:letrasMayus.get(minn+1)})
    minn = min
    for minn in range (max): #Asigna los valores del 37 al 63
        temp +=1
        diccionario.update({temp:letras.get(minn+1)})
    minn = min
    for num in range (19): #Rellena los valores que faltan repitiendo los procesos pasados 20 veces mas
        for minn in range (max):
            temp +=1
            letra = simbolos.get(num+1)+letrasMayus.get(minn+1)
            diccionario.update({temp:letra})
        minn = min
        for minn in range (max):
            temp +=1
            letra = simbolos.get(num+1)+letras.get(minn+1)
            diccionario.update({temp:letra})
        minn = min

def convert_to_base_10(num_str, base_ori):
    exponente = len(num_str)
    resultado_base_10 = 0
    for x in range(1, exponente+1):
        resultado_base_10 += num_str[x-1]*((base_ori)**(exponente-x))
    return resultado_base_10

def convert_from_base_10(number, base):
    numer = ''.join(str(digit) for digit in number)
    numero = int(numer)
    result = ""
    while numero > 0:
        digit = numero % base
        numero_destino.insert(0,digit)
        traducir = traduccion_digitos(digit)
        result = traducir+ result
        numero //= base
    return result

def convertir_from_base_10(number, base):
    result = ""
    while number > 0:
        digit = number % base
        numero_destino.insert(0,digit)
        traducir = traduccion_digitos(digit)
        result = traducir+ result
        number //= base
    return result

def traduccion_digitos(digito):
    numero = diccionario.get(digito)
    return numero

def convert_between_bases(num_str, base_origin, base_dest):
    if base_origin == base_dest:
        return num_str
    
    if base_origin == 10:
        num_in_base_dest = convert_from_base_10(num_str, base_dest)
    elif base_dest == 10:
        num_in_base_dest = convert_to_base_10(num_str, base_origin)
    else:
        num_in_base_10 = convert_to_base_10(num_str, base_origin)
        num_in_base_dest = convertir_from_base_10(num_in_base_10, base_dest)
    
    return num_in_base_dest

def encontrar_exponente(base_1, base_2):
    exponente = 0
    while base_1 ** exponente != base_2:
        exponente += 1
        if base_1 ** exponente > base_2:
            return None  # No es una relación de potencias exacta
    return exponente

def traducir_para_operar():
    results = []
    for x in range(len(dic_digito)):
        for k, v in diccionario.items():
            if v == dic_digito[x]:
                dic_traducido.append(int(k))
    results = dic_traducido
    return results

def encontrar_exponente(base_destino, base_origen):
    exponente = 0
    while base_destino ** exponente != base_origen:
        exponente += 1
        if base_destino ** exponente > base_origen:
            return None  # No es una relación de potencias exacta
    return exponente

def encontrar_relacion_potencias(base_destino, base_origen):
    exponente = encontrar_exponente(base_destino, base_origen)
    if exponente is not None:
        return exponente
    else:
        return "No hay una relación de potencias exacta"
    

def rela_potencias_mayor_a_menor(base_destino,lista_elementos,base_origen):
    divisor = base_destino
    base = base_origen
    potencia = encontrar_relacion_potencias(divisor,base)
    tamaño_lista=len(lista_elementos)
    resultado_final=""
    primer_numero=""
    for x in range(tamaño_lista):
        nume_a_operar = int(lista_elementos[tamaño_lista-x-1])
        for exp in range (potencia+1):
            cociente = nume_a_operar // (divisor**(int(potencia-exp)))
            residuo = nume_a_operar % (divisor**(int(potencia-exp)))
            primer_numero = str(primer_numero)+str(cociente)
            nume_a_operar = residuo
            
        resultado_final=str(int(primer_numero))+resultado_final
        primer_numero=""
    final=int(resultado_final)
    return final

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
    for x in range(len(lista_arre_str)): #Se opera
        num_in_x = "{:0{exponente}d}".format(int(lista_arre_str[x]), exponente=exponente) #cadena de formato obtenida en GPT
        for exp in range(exponente):
            dividir = agregar_ceros(exponente-exp)
            temp= int(num_in_x)//dividir
            numero = numero +(temp*(int(base_origen)**(exponente-exp-1)))
            if len(num_in_x)>1:
                num_in_x=num_in_x[1:]
        result=str(diccionario.get(numero))+result
        numero=0
    return result

def main(): 
    asignar_base_datos()
    respuesta = input("Manejar el codigo con numeros?")
    cantidad_elementos = input("Ingrese cuantos elementos tiene su numero: ")
    if int(cantidad_elementos)>0:
        for numeros in range (int(cantidad_elementos)):
            temp=input(f"Ingrese el digito #{numeros+1}: ")

            dic_digito.append(temp)
        base_origen = int(input("Ingrese la base origen (entre 2 y 1024): "))
        base_destino = int(input("Ingrese la base destino (entre 2 y 1024): "))
        if base_origen < 2 or base_origen > 1024 or base_destino < 2 or base_destino > 1024:
            print("Las bases deben estar en el rango de 2 a 1024.")
            return
        
        exponente = 0
        tupla_int = []
        if base_origen>base_destino:
            exponente = encontrar_exponente(base_destino, base_origen)
            invertido = True
        else:
            exponente = encontrar_exponente(base_origen, base_destino)
            invertido = False
        if respuesta == "y":
            son_numeros = True
            dic_digito_numeros = dic_digito
            tupla_int = tuple(int(item) for item in dic_digito_numeros)
        elif respuesta == "n":
            son_numeros = False
            dicc_traducido=traducir_para_operar()
        if son_numeros:
            print("Los valores estan en numeros")
            if exponente is None:
                print("NO relacion de potencia")
                resultado = convert_between_bases(tupla_int, base_origen, base_destino)
                print(f"Convirtiendo de base {base_origen} a base 10: {tupla_int} = {convert_to_base_10(tupla_int, base_origen)}")
                print(f"Convirtiendo a base {base_destino}: {tupla_int} = {resultado}")
            else:
                print("relacion de potencia")
                if invertido:
                    print("Invertido")
                    resultado = rela_potencias_mayor_a_menor(base_destino,tupla_int, base_origen)
                    print(f"El número {tupla_int} en base {base_origen} es equivalente a {resultado} en base {base_destino}.")

                else:
                    print("normal")
                    resultado = convert_bases_relation_normal(tupla_int, base_origen, exponente)
                    print(f"El número {tupla_int} en base {base_origen} es equivalente a {resultado} en base {base_destino}.")
        else:
            print("Los valores NO estan en numeros")
            if exponente is None:
                resultado = convert_between_bases(dic_traducido, base_origen, base_destino)
                print("NO relacion de potencia")                
                print(f"Convirtiendo de base {base_origen} a base 10: {dic_traducido} = {convert_to_base_10(dic_traducido, base_origen)}")
                print(f"Convirtiendo a base {base_destino}: {dic_traducido} = {resultado}")
            else:
                print("relacion de potencia")
                if invertido:
                    print("Invertido")
                    resultado = rela_potencias_mayor_a_menor(base_destino,dicc_traducido, base_origen)
                    print(f"El número {dicc_traducido} en base {base_origen} es equivalente a {resultado} en base {base_destino}.")

                else:
                    print("normal")
                    resultado = convert_bases_relation_normal(dicc_traducido, base_origen, exponente)
                    print(f"El número {dicc_traducido} en base {base_origen} es equivalente a {resultado} en base {base_destino}.")
    else:
        print("Por favor digite una cantidad valida.")
if __name__ == "__main__":
    main()

