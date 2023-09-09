numero1 = []
numero2 = []
resultado_suma = []
resultado_resta = []
base = 0
tam=0
temp=False

def asignar_base(base_num):
    global base
    base = base_num

def operar():
    global numero1
    global numero2
    global tam
    num=numero1.copy()
    num2=numero2.copy()
    if temp==False:
        tam = arreglar_num()
        realizar_operacion_resta(num,num2,tam)
        realizar_operacion_suma(num,num2,tam)
        print(num,num2)
    else:
        num.reverse()
        num2.reverse()
        realizar_operacion_resta(num,num2,tam)
        realizar_operacion_suma(num,num2,tam)
        print(num,num2)
    
    

def asignar_numeros(num1, num2):
    global numero1
    global numero2
    numero1 = num1
    numero2 = num2

def arreglar_num():
    global numero1
    global numero2
    global temp
    tam = max(len(numero1), len(numero2))
    numero1 = [0] * (tam - len(numero1)) + numero1
    numero2 = [0] * (tam - len(numero2)) + numero2
    numero1.reverse()
    numero1.append(0)
    numero2.reverse()
    numero2.append(0)
    temp=True
    return tam

def realizar_operacion_suma(num,num2,tam):
    global resultado_suma
    global base
    resultado_suma.clear()
    num,num2=verificar_numeros(num,num2,tam)
    num.append(0)
    num2.append(0)
    base = int(base)
    for x in range(tam+1):
        operacion = int(num[x])+int(num2[x])
        if operacion>=base:
            num[x+1]= num[x+1]+1
            operacion = operacion-base
        resultado_suma.append(operacion)
    resultado_suma.reverse()

def realizar_operacion_resta(num,num2,tam):
    global resultado_resta
    global base
    resultado_resta.clear()
    base = int(base)
    num,num2=verificar_numeros(num,num2,tam)
    num.reverse()
    num2.reverse()
    print("Resta: ",num,num2)
    for x in range(tam):
        if (int(num[x])<int(num2[x])):
            num[x+1]=num[x+1]-1
            num[x]=num[x]+base
        operacion = int(num[x])-int(num2[x])
        print("operacion: ",operacion)
        resultado_resta.append(operacion)
    resultado_resta.reverse()

        
def verificar_numeros(num,num2,tam):
    global numero1
    global numero2
    numero1.reverse()
    numero2.reverse()
    num=numero1.copy()
    num2=numero2.copy()
    for x in range(tam):
        if num[tam-x-1] < num2[tam-x-1]:
            return num2,num
        else:
            return num2,num