# Definición de variables globales
numero1 = []
numero2 = []
resultado_suma = []
resultado_resta = []
base = 0

def asignar_base():
    global base
    while True:
        base_input = input("Ingrese la base a trabajar: ")
        if base_input.isdigit() and 2 <= int(base_input) <= 1023:
            base = int(base_input)
            break
        else:
            print("La base ingresada no es válida. Intente nuevamente.")

def ingresar_numero(cant_elementos):
    numero = []
    for x in range(cant_elementos):
        while True:
            try:
                temp = int(input(f"Ingrese el elemento {x+1}: "))
                if 0 <= temp < base:
                    numero.append(temp)
                    break
                else:
                    print(f"El número debe estar en el rango [0, {base-1}]. Intente nuevamente.")
            except ValueError:
                print("Error al agregar el elemento, solo se aceptan números. Intente nuevamente.")
    return numero

def arreglar_num():
    global numero1
    global numero2
    tam = max(len(numero1), len(numero2))

    numero1 = [0] * (tam - len(numero1)) + numero1
    numero2 = [0] * (tam - len(numero2)) + numero2
    numero1.reverse()
    numero1.append(0)
    numero2.reverse()
    numero2.append(0)
    return tam

def realizar_operacion_suma(tam):
    global numero1
    global numero2
    global resultado_suma
    global base
    for x in range(tam+1):
        print(numero1,"    ",numero2)
        operacion = int(numero1[x])+int(numero2[x])
        if operacion>=base:
            numero1[x+1]= numero1[x+1]+1
            operacion = operacion-base
        print(operacion)
        resultado_suma.append(operacion)
    resultado_suma.reverse()
    print(resultado_suma)




print("\nSuma y Resta de números en base n\n")
asignar_base()

cant_1 = int(input("Cuantos elementos tiene su primer número? "))
numero1 = ingresar_numero(cant_1)

cant_2 = int(input("Cuantos elementos tiene su segundo número? "))
numero2 = ingresar_numero(cant_2)
tam = arreglar_num()
realizar_operacion_suma(tam)
