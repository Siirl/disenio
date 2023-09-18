import tkinter as tk
from tkinter import ttk
import diseño_dos

ventana = tk.Tk()
ventana.title("Diseño logico")
notebook = ttk.Notebook(ventana)
notebook.grid(row=0, column=0)

# Pestaña 1
conversion = ttk.Frame(notebook)
notebook.add(conversion, text="Conversion")

operacion = ttk.Frame(notebook)
notebook.add(operacion, text="Operacion")

tam=0
entrada_habilitada_base = True
entrada_habilitada_num1 = True
entrada_habilitada_num2 = True
entrada_habilitada_conv_base = True
entrada_habilitada_conv_num1 = True
entrada_habilitada_conv_num2 = True

numeros_lista1 = []  # Lista para almacenar los números de la primera lista
numeros_lista2 = []  # Lista para almacenar los números de la segunda lista
nume1 = []
nume2 = []


def igualar_longitud_listas(lista1, lista2):
    global tam
    len1 = len(lista1)
    len2 = len(lista2)

    if len1 < len2:
        diferencia = len2 - len1
        lista1 = [0] * diferencia + lista1
        tam=len2
    elif len2 < len1:
        diferencia = len1 - len2
        lista2 = [0] * diferencia + lista2
        tam=len1
    elif len1 == len2:
        diferencia = 0
        tam=len1

    return lista1, lista2

def agregar_numero_lista1():
    global entrada_habilitada_num1,numeros_lista1, nume1
    numero = entrada_lista1.get()
    numeros_lista1 = list(numero)
    entrada_habilitada_num1 = False
    entrada_lista1.config(state=tk.DISABLED)
    entrada_lista2.focus_set()
    cadena="".join(numeros_lista1)
    cadena2="".join(numeros_lista2)
    list_str = [str(num) for num in diseño_dos.encontrar_posiciones(numeros_lista1)]
    resultado = ",".join(list_str)
    list_str2 = [str(num) for num in diseño_dos.encontrar_posiciones(numeros_lista2)]
    resultado2 = ",".join(list_str2)
    texto_lista1 = "Número 1: " + cadena +" valores: " +resultado
    texto_lista2 = "Número 2: " + cadena2 +" valores: "+resultado2
    etiqueta_estado.config(text=texto_lista1 + "\n" + texto_lista2)
    nume1=diseño_dos.encontrar_posiciones(numeros_lista1)

def agregar_numero_lista2():
    global entrada_habilitada_num2,numeros_lista2, nume2
    numero = entrada_lista2.get()
    numeros_lista2 = list(numero)
    entrada_habilitada_num2 = False
    entrada_lista2.config(state=tk.DISABLED)
    entrada_numero_a_traducir.focus_set()
    cadena="".join(numeros_lista1)
    cadena2="".join(numeros_lista2)
    list_str = [str(num) for num in diseño_dos.encontrar_posiciones(numeros_lista1)]
    resultado = ",".join(list_str)
    list_str2 = [str(num) for num in diseño_dos.encontrar_posiciones(numeros_lista2)]
    resultado2 = ",".join(list_str2)
    texto_lista1 = "Número 1: " + cadena +" valores: " +resultado
    texto_lista2 = "Número 2: " + cadena2 +" valores: "+resultado2
    etiqueta_estado.config(text=texto_lista1 + "\n" + texto_lista2)
    nume2=diseño_dos.encontrar_posiciones(numeros_lista2)


def restaurar():

    limpiar2()
    limpiar1()
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
    global nume1,nume2,tam
    diseño_dos.numero1.clear
    diseño_dos.numero2.clear
    diseño_dos.resultado_resta.clear
    diseño_dos.resultado_suma.clear
    diseño_dos.temp = False
    if (len(nume1) != len(nume2)):
        nume1, nume2 =igualar_longitud_listas(nume1, nume2)
    tam = len(nume1)
    diseño_dos.numero1 = nume1
    diseño_dos.numero2 = nume2
    diseño_dos.tam = tam
    diseño_dos.operar()
    cadena="".join(diseño_dos.resultado_suma)
    cadena2="".join(diseño_dos.resultado_resta)
    list_str1 = [str(num) for num in diseño_dos.valor_suma]
    resultado1 = ",".join(list_str1) + ","
    list_str2 = [str(num) for num in diseño_dos.valor_resta]
    resultado2 = ",".join(list_str2) + ","
    texto_suma = "Numero: "+str((cadena))+" Valores: "+resultado1
    texto_resta = "Numero: "+str((cadena2))+" Valores: "+resultado2
    etiqueta_suma.config(text=texto_suma)
    etiqueta_resta.config(text=texto_resta)


def limpiar1():
    global numeros_lista1, entrada_habilitada_num1
    diseño_dos.numero1 =[]
    numeros_lista1 = []
    entrada_habilitada_num1 = True
    entrada_lista1.config(state=tk.NORMAL)
    entrada_lista1.focus_set()
    entrada_lista1.delete(0, tk.END)
    texto_lista1 = "Número 1: " + ', '.join(map(str, numeros_lista1))
    texto_lista2 = "Número 2: " + ', '.join(map(str, numeros_lista2))
    etiqueta_estado.config(text=texto_lista1 + "\n" + texto_lista2)
    
def limpiar2():
    global numeros_lista2, entrada_habilitada_num2
    diseño_dos.numero2 =[]
    numeros_lista2 = []
    entrada_habilitada_num2 = True
    entrada_lista2.config(state=tk.NORMAL)
    entrada_lista2.focus_set()
    entrada_lista2.delete(0, tk.END)
    texto_lista1 = "Número 1: " + ', '.join(map(str, numeros_lista1))
    texto_lista2 = "Número 2: " + ', '.join(map(str, numeros_lista2))
    etiqueta_estado.config(text=texto_lista1 + "\n" + texto_lista2)

def traducir_num():
    num=entrada_numero_a_traducir.get()
    resultado=diseño_dos.traduccion(int(num))
    resultado_traduccion.config(state="normal")  # Habilita la edición
    resultado_traduccion.delete("1.0", tk.END)
    resultado_traduccion.insert(tk.END, resultado)
    resultado_traduccion.config(state="disabled")  # Vuelve a deshabilitar la edición

def copiar():
    resultado_texto= resultado_traduccion.get("1.0", "end-1c")
    ventana.clipboard_clear()
    ventana.clipboard_append(resultado_texto)
    ventana.update()

def convertir():
    base_ori = entrada_base_origen.get()
    base_origen = int(base_ori)
    numero = entrada_numero.get()
    list_digito = list(numero)
    list_numero = diseño_dos.encontrar_posiciones(list_digito)
    base_dest =entrada_base_destino.get()
    base_destino = int(base_dest)
    exponente = 0
    print(list_numero)
    if base_origen>base_destino:
        exponente = diseño_dos.encontrar_exponente(base_destino, base_origen)
        invertido = True
    else:
        exponente = diseño_dos.encontrar_exponente(base_origen, base_destino)
        invertido = False
    if exponente is None:
        resultado = diseño_dos.convert_between_bases(list_numero, base_origen, base_destino)
        text= (f"Convirtiendo de base {base_origen} a base 10: \n{list_numero} = {diseño_dos.convert_to_base_10(list_numero, base_origen)}\n Convirtiendo a base {base_destino}: {list_numero} = {resultado}")
    else:
        if invertido:
            resultado = diseño_dos.rela_potencias_mayor_a_menor(base_destino,list_numero, base_origen)
            text = (f"El número {list_numero} en base {base_origen} es equivalente a {resultado} en base {base_destino}.")

        else:
            resultado = diseño_dos.convert_bases_relation_normal(list_numero, base_origen, exponente)
            text = (f"El número {list_numero} en base {base_origen} es equivalente a {resultado} en base {base_destino}.")
    resultado_conversion.config(state="normal")  # Habilita la edición
    resultado_conversion.delete("1.0", tk.END)
    resultado_conversion.insert(tk.END, text) # Vuelve a deshabilitar la edición
    

diseño_dos.asignar_diccionario()
######################################################################################################################
#----------------------------------------Interfaz Primer Laboratorio------------------------------------------------#
######################################################################################################################

etiqueta_base_origen = tk.Label(conversion, text="Base origen:")
etiqueta_base_origen.grid(row=0, column=0)

entrada_base_origen = tk.Entry(conversion)
entrada_base_origen.grid(row=0, column=1)

etiqueta_numero = tk.Label(conversion, text="Número:")
etiqueta_numero.grid(row=1, column=0)

entrada_numero = tk.Entry(conversion)
entrada_numero.grid(row=1, column=1)

etiqueta_base_destino = tk.Label(conversion, text="Base destino:")
etiqueta_base_destino.grid(row=2, column=0)

entrada_base_destino = tk.Entry(conversion)
entrada_base_destino.grid(row=2, column=1)

# Crear un botón para ordenar los datos
tk.Button(conversion, text="Convertir", command=convertir).grid(row=1, column=2)

# Crear un label para mostrar el resultado
resultado_conversion = tk.Text(conversion, wrap=tk.WORD, height=5, width=40)
resultado_conversion.grid(row=4, column=4)

######################################################################################################################
#----------------------------------------Interfaz Segundo Laboratorio------------------------------------------------#
######################################################################################################################

# Etiquetas y entradas
tk.Label(operacion, text="Base de los números:").grid(row=0, column=0)
entrada_base = tk.Entry(operacion)
entrada_base.grid(row=0, column=1)
tk.Button(operacion, text="Guardar base", command=asignar_bas).grid(row=0, column=2)

tk.Label(operacion, text="Número 1: Ingresa el elemento:").grid(row=1, column=0)
entrada_lista1 = tk.Entry(operacion)
entrada_lista1.grid(row=1, column=1)
tk.Button(operacion, text="Agregar al numero 1", command=agregar_numero_lista1).grid(row=1, column=2)
tk.Button(operacion, text="Limpiar", command=limpiar1).grid(row=1, column=3)
etiqueta_estado = tk.Label(operacion, text="")
etiqueta_estado.grid(row=4, column=0)

tk.Label(operacion, text="Número 2: Ingresa el elemento:").grid(row=2, column=0)
entrada_lista2 = tk.Entry(operacion)
entrada_lista2.grid(row=2, column=1)
tk.Button(operacion, text="Agregar a numero 2", command=agregar_numero_lista2).grid(row=2, column=2)
tk.Button(operacion, text="Limpiar", command=limpiar2).grid(row=2, column=3)

tk.Label(operacion, text="Número: ").grid(row=4, column=2)
entrada_numero_a_traducir = tk.Entry(operacion)
entrada_numero_a_traducir.grid(row=4, column=3)
entrada_numero_a_traducir.config(width=5)
tk.Button(operacion, text="Traducir", command=traducir_num).grid(row=4, column=4)

# Resultados
tk.Label(operacion, text="El número traducido es: ").grid(row=5, column=2)
resultado_traduccion = tk.Text(operacion, wrap=tk.WORD, height=1, width=3)
resultado_traduccion.grid(row=5, column=3)
resultado_traduccion.config(state="disabled")  # Para que el usuario no pueda editar el resultado

# Botones
tk.Button(operacion, text="Restaurar", command=restaurar).grid(row=5, column=0)
tk.Button(operacion, text="Operar", command=operar).grid(row=5, column=1)
tk.Button(operacion, text="Copiar", command=copiar).grid(row=5, column=4)

# Etiquetas para resultados
resultado_suma = tk.Text(operacion, wrap=tk.WORD, height=6, width=0)
resultado_resta = tk.Text(operacion, wrap=tk.WORD, height=7, width=0)
tk.Label(operacion, text="Resultado Suma: ").grid(row=6, column=0)
tk.Label(operacion, text="Resultado Resta: ").grid(row=7, column=0)

etiqueta_suma = tk.Label(operacion, text="")
etiqueta_suma.grid(row=6, column=1)

etiqueta_resta = tk.Label(operacion, text="")
etiqueta_resta.grid(row=7, column=1)
entrada_base.bind("<Return>", lambda event=None: asignar_bas())
entrada_lista1.bind("<Return>", lambda event=None: agregar_numero_lista1())
entrada_lista2.bind("<Return>", lambda event=None: agregar_numero_lista2())
entrada_numero_a_traducir.bind("<Return>", lambda event=None: traducir_num())

ventana.mainloop()
