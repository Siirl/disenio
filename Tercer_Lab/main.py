import tkinter as tk
from tkinter import ttk
import procesos

letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
variables = []
tabla_de_verdad=[]

# Función para evaluar la expresión
def calcular():
    global tabla_de_verdad, variables
    variables.clear
    tabla_de_verdad.clear
    procesos.tabla_verdad.clear
    expresion_actual = str(entrada.get())
    for elementos in expresion_actual:
        elemento=elementos.upper()
        if elemento in letras:
            variables.append(elemento)
            letras.remove(elemento) 
    procesos.generar_tabla(variables,len(variables))
    tabla_de_verdad = procesos.tabla_verdad.copy()
    calcular_expresion(expresion_actual)
    mostrar_tabla(procesos.tabla_verdad)
    resultado_label.config(text=expresion_actual)



def calcular_expresion(expresion):
    global tabla_de_verdad
    negar_expresion=False
    # Esta función de cálculo es similar a la que hemos discutido previamente
    stack = []
    resultado = '|' #posicion de 0
    operador = "+" #si se suma 0 el resultado es la misma variable
    negacion = ""
    expresion_lista=list(expresion) 
    for i in range(len(expresion_lista)):
        if expresion_lista[i] == "(":
            if expresion_lista[i-1] == "-":
                stack.append((resultado, operador))
                resultado = '|' #posicion de 0
                operador = '+' #si se suma 0 el resultado es la misma variable
            else:
                stack.append((resultado, operador))
                resultado = '|' #posicion de 0
                operador = '+' #si se suma 0 el resultado es la misma variable
        elif expresion_lista[i] == ")":
            operando, operador_anterior = stack.pop()
            val1=procesos.tabla_verdad[0].index(operando)
            val2=procesos.tabla_verdad[0].index(resultado)
            if operador_anterior == "+":
                resultado = procesos.suma(procesos.tabla_verdad,val1, val2)
            elif operador_anterior == "*":
                resultado = procesos.multiplicacion(procesos.tabla_verdad,val1, val2)
            if negacion == True:
                val_negado = procesos.tabla_verdad[0].index(resultado)
                resultado = procesos.negacion(procesos.tabla_verdad, val_negado)
                negacion = False
        elif expresion_lista[i] in variables:
            val1=procesos.tabla_verdad[0].index(resultado)
            val2=procesos.tabla_verdad[0].index(expresion_lista[i])
            if operador == "+":
                resultado = procesos.suma(procesos.tabla_verdad,val1,val2)
            elif operador == "*":
                resultado = procesos.multiplicacion(procesos.tabla_verdad,val1,val2)
        elif expresion_lista[i] in ("+", "*"):
            operador = expresion_lista[i]
        elif expresion_lista[i] in ("-"):
            if negacion == True:
                negacion = False
            else:
                negacion=True
    
    return resultado

def mostrar_tabla(datos):
    # Eliminar cualquier widget previo en el contenedor de la tabla
    for widget in tabla_frame.winfo_children():
        widget.destroy()

    # Encabezados de columna
    encabezados = datos[0]

    # Crear encabezados de columna
    for col, encabezado in enumerate(encabezados):
        etiqueta = ttk.Label(tabla_frame, text=encabezado, font=("Arial", 12, "bold"))
        etiqueta.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

    # Mostrar datos en la tabla
    for row, fila in enumerate(datos[1:], start=1):
        for col, valor in enumerate(fila):
            etiqueta = ttk.Label(tabla_frame, text=valor, font=("Arial", 12))
            etiqueta.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
        
# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Campo de entrada para la expresión
entrada = tk.Entry(ventana, width=20, font=("Arial", 16))
entrada.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
entrada.bind('<Return>', lambda event=None: calcular())

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="", font=("Arial", 14))
resultado_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Crear un marco para la tabla y configurar su estilo
tabla_frame = ttk.Frame(ventana)
tabla_frame.grid(row=0, column=2, rowspan=2, padx=10, pady=10, sticky="nsew")
tabla_frame.grid_columnconfigure(0, weight=1)  # Hacer que la columna se expanda con la ventana

# Configurar que las filas se expandan con la ventana
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)

# Configurar que la columna 0 se expanda con la ventana
ventana.grid_columnconfigure(0, weight=1)

# Ejecutar la aplicación
ventana.mainloop()
