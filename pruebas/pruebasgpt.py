import tkinter as tk

ventana = tk.Tk()
ventana.title("Suma y resta entre numeros en una base n")

# Base, entrada de base y botón de base
base = tk.Label(ventana, text="Base de los numeros:")
base.place(x=10, y=10)

entrada_base = tk.Entry(ventana)
entrada_base.place(x=200, y=10)

boton_base = tk.Button(ventana, text="Guardar base")
boton_base.place(x=400, y=10)

# Etiqueta y entrada de la Lista 1
etiqueta_lista1 = tk.Label(ventana, text="Número 1: Ingresa el elemento:")
etiqueta_lista1.place(x=10, y=50)

entrada_lista1 = tk.Entry(ventana)
entrada_lista1.place(x=200, y=50)

# Botón Limpiar Lista 1
boton_limpiar_lista1 = tk.Button(ventana, text="Limpiar")
boton_limpiar_lista1.place(x=400, y=50)

# Botón Agregar a Lista 1
boton_agregar_lista1 = tk.Button(ventana, text="Agregar al número 1")
boton_agregar_lista1.place(x=500, y=50)

# Etiqueta y entrada de la Lista 2
etiqueta_lista2 = tk.Label(ventana, text="Número 2: Ingresa el elemento:")
etiqueta_lista2.place(x=10, y=90)

entrada_lista2 = tk.Entry(ventana)
entrada_lista2.place(x=200, y=90)

# Botón Agregar a Lista 2
boton_agregar_lista2 = tk.Button(ventana, text="Agregar a número 2")
boton_agregar_lista2.place(x=400, y=90)

# Botón Mostrar Numeros
boton_mostrar = tk.Button(ventana, text="Mostrar Numeros")
boton_mostrar.place(x=10, y=130)

# Etiqueta de Estado
etiqueta_estado = tk.Label(ventana, text="")
etiqueta_estado.place(x=10, y=170)

# Botón Operar
boton_operar = tk.Button(ventana, text="Operar")
boton_operar.place(x=10, y=210)

# Etiqueta Suma y botones de asignación
etiqueta_suma = tk.Label(ventana, text="")
etiqueta_suma.place(x=10, y=250)

boton_asignar_suma_num_1 = tk.Button(ventana, text="+Num1")
boton_asignar_suma_num_1.place(x=200, y=250)

boton_asignar_suma_num_2 = tk.Button(ventana, text="+Num2")
boton_asignar_suma_num_2.place(x=300, y=250)

# Etiqueta Resta y botones de asignación
etiqueta_resta = tk.Label(ventana, text="")
etiqueta_resta.place(x=10, y=290)

boton_asignar_resta_num_1 = tk.Button(ventana, text="+Num1")
boton_asignar_resta_num_1.place(x=200, y=290)

boton_asignar_resta_num_2 = tk.Button(ventana, text="+Num2")
boton_asignar_resta_num_2.place(x=300, y=290)

ventana.mainloop()
