import tkinter as tk
import diseño_dos

ventana = tk.Tk()
ventana.title("Suma y resta bases iguales")
entrada_habilitada = True

numeros_lista1 = []  # Lista para almacenar los números de la primera lista
numeros_lista2 = []  # Lista para almacenar los números de la segunda lista

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

def asignar_bas():
    global entrada_habilitada
    base = entrada_base.get()
    diseño_dos.asignar_base(base)
    entrada_habilitada = False
    entrada_base.config(state=tk.DISABLED)

def sumar():
    texto_suma = "La suma de los numeros es: " + ', '.join(map(str, diseño_dos.resultado_suma))
    etiqueta_suma.config(text=texto_suma)

base = tk.Label(ventana, text="Ingrese la base de los numeros a trabajar:")
entrada_base = tk.Entry(ventana)
boton_base = tk.Button(ventana, text="Guardar base", command=asignar_bas)

etiqueta_lista1 = tk.Label(ventana, text="Numero 1: Ingresa el elemento:")
entrada_lista1 = tk.Entry(ventana)
boton_agregar_lista1 = tk.Button(ventana, text="Agregar al numero 1", command=agregar_numero_lista1)

etiqueta_lista2 = tk.Label(ventana, text="Numero 2: Ingresa el elemento:")
entrada_lista2 = tk.Entry(ventana)
boton_agregar_lista2 = tk.Button(ventana, text="Agregar a numero 2", command=agregar_numero_lista2)

boton_mostrar = tk.Button(ventana, text="Mostrar Numeros", command=mostrar_numeros)

etiqueta_estado = tk.Label(ventana, text="")
boton_suma = tk.Button(ventana, text="Sumar", command=sumar)
etiqueta_suma = tk.Label(ventana, text="")

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
boton_suma.pack()
etiqueta_suma.pack()

ventana.mainloop()
