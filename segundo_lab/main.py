import tkinter as tk
import diseño_dos

ventana = tk.Tk()
ventana.title("Suma y resta bases iguales")
entrada_habilitada = True

numeros_lista1 = []  # Lista para almacenar los números de la primera lista
numeros_lista2 = []  # Lista para almacenar los números de la segunda lista

def igualar_longitud_listas(lista1, lista2):
    len1 = len(lista1)
    len2 = len(lista2)

    if len1 < len2:
        diferencia = len2 - len1
        lista1 = [0] * diferencia + lista1
    elif len2 < len1:
        diferencia = len1 - len2
        lista2 = [0] * diferencia + lista2

    return lista1, lista2

def agregar_numero_lista1():
    numero = entrada_lista1.get()
    if numero.isdigit():
        numeros_lista1.append(int(numero))
        entrada_lista1.delete(0, tk.END)  # Limpiar la entrada de texto
        mostrar_numeros()
    else:
        etiqueta_estado.config(text="Por favor, ingresa un número válido en la Lista 1.")

def agregar_numero_lista2():
    numero = entrada_lista2.get()
    if numero.isdigit():
        numeros_lista2.append(int(numero))
        entrada_lista2.delete(0, tk.END)  # Limpiar la entrada de texto
        mostrar_numeros()
    else:
        etiqueta_estado.config(text="Por favor, ingresa un elemento válido en la Lista 2.")

def mostrar_numeros():
    texto_lista1 = "Número 1: " + ', '.join(map(str, numeros_lista1))
    texto_lista2 = "Número 2: " + ', '.join(map(str, numeros_lista2))
    diseño_dos.asignar_numeros(numeros_lista1, numeros_lista2)
    etiqueta_estado.config(text=texto_lista1 + "\n" + texto_lista2)

def restaurar():
    global numeros_lista1, numeros_lista2, entrada_habilitada
    diseño_dos.resultado_resta=[]
    diseño_dos.resultado_suma=[]
    diseño_dos.numero1=[]
    diseño_dos.numero2=[]
    diseño_dos.base=0
    diseño_dos.tam=0
    diseño_dos.temp=False
    
    numeros_lista1 = []
    numeros_lista2 = []
    entrada_habilitada = True
    entrada_base.config(state=tk.NORMAL)
    entrada_base.delete(0, tk.END)
    entrada_base.focus_set()
    etiqueta_resta.config(text="")
    etiqueta_suma.config(text="")
    etiqueta_estado.config(text="")

def asignar_bas():
    global entrada_habilitada
    base = entrada_base.get()
    diseño_dos.asignar_base(base)
    entrada_habilitada = False
    entrada_base.config(state=tk.DISABLED)
    entrada_lista1.focus_set()

def operar():
    global numeros_lista1, numeros_lista2
    diseño_dos.numero1.clear
    diseño_dos.numero2.clear
    diseño_dos.resultado_resta.clear
    diseño_dos.resultado_suma.clear
    diseño_dos.temp = False
    mostrar_numeros()
    numeros_lista1, numeros_lista2 =igualar_longitud_listas(numeros_lista1, numeros_lista2)
    diseño_dos.numero1 = numeros_lista1
    diseño_dos.numero2 = numeros_lista2
    print(numeros_lista1, numeros_lista2)
    diseño_dos.operar()
    texto_suma = "La suma de los numeros es: " + ', '.join(map(str, diseño_dos.resultado_suma))
    texto_resta = "La resta de los numeros es: " + ', '.join(map(str,diseño_dos.resultado_resta))
    etiqueta_suma.config(text=texto_suma)
    etiqueta_resta.config(text=texto_resta)

def asignar_suma_numero():
    global numeros_lista1
    numeros_lista1 = diseño_dos.resultado_suma
    mostrar_numeros()

def asignar_resta_numero():
    global numeros_lista1
    numeros_lista1 = diseño_dos.resultado_resta
    mostrar_numeros()

def asignar_suma_numero_2():
    global numeros_lista2
    numeros_lista2 = diseño_dos.resultado_suma
    mostrar_numeros()

def asignar_resta_numero_2():
    global numeros_lista2
    numeros_lista2 = diseño_dos.resultado_resta
    mostrar_numeros()

base = tk.Label(ventana, text="Ingrese la base de los numeros a trabajar:")
entrada_base = tk.Entry(ventana)
boton_base = tk.Button(ventana, text="Guardar base", command=asignar_bas)

etiqueta_lista1 = tk.Label(ventana, text="Numero 1: Ingresa el elemento:")
entrada_lista1 = tk.Entry(ventana)
boton_agregar_lista1 = tk.Button(ventana, text="Agregar al numero 1", command=agregar_numero_lista1)

etiqueta_lista2 = tk.Label(ventana, text="Numero 2: Ingresa el elemento:")
entrada_lista2 = tk.Entry(ventana)
boton_agregar_lista2 = tk.Button(ventana, text="Agregar a numero 2", command=agregar_numero_lista2)

boton_mostrar = tk.Button(ventana, text="Restaurar", command=restaurar)

etiqueta_estado = tk.Label(ventana, text="")

entrada_base.bind("<Return>", lambda event=None: asignar_bas())
entrada_lista1.bind("<Return>", lambda event=None: agregar_numero_lista1())
entrada_lista2.bind("<Return>", lambda event=None: agregar_numero_lista2())

base.pack()
entrada_base.pack()
boton_base.pack()
etiqueta_lista1.pack()
entrada_lista1.pack()
boton_agregar_lista1.pack()

etiqueta_lista2.pack()
entrada_lista2.pack()
boton_agregar_lista2.pack()

boton_mostrar.pack()

etiqueta_estado.pack()
boton_operar = tk.Button(ventana, text="Operar", command=operar)

boton_operar.pack()
etiqueta_suma = tk.Label(ventana, text="")
etiqueta_suma.pack()
boton_asignar_suma_num_1 = tk.Button(ventana, text="+Num1", command=asignar_suma_numero)
boton_asignar_suma_num_1.pack(side=tk.TOP)
boton_asignar_suma_num_2 = tk.Button(ventana, text="+Num2", command=asignar_suma_numero_2)
boton_asignar_suma_num_2.pack(side=tk.TOP)

etiqueta_resta = tk.Label(ventana, text="")
etiqueta_resta.pack()
boton_asignar_resta_num_1 = tk.Button(ventana, text="+Num1", command=asignar_resta_numero)
boton_asignar_resta_num_1.pack(side=tk.TOP)
boton_asignar_resta_num_2 = tk.Button(ventana, text="+Num2", command=asignar_resta_numero_2)
boton_asignar_resta_num_2.pack(side=tk.TOP)

ventana.mainloop()
