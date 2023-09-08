numero1 = []
numero2 = []
resultado_suma = []
resultado_resta = []
base = 0

def asignar_base(base_num):
    global base
    base = base_num

def asignar_numeros(num1, num2):
    global numero1
    global numero2
    numero1 = num1
    numero2 = num2
    print(numero1, numero2)
    if (len(numero1)>0 and len(numero2)>0):
        tam = arreglar_num()
        realizar_operacion_suma(tam)
    
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
    resultado_suma.clear()
    base = int(base)
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
