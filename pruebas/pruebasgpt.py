import tkinter as tk
from tkinter import ttk

# Función para crear y mostrar la tabla en la interfaz
def mostrar_tabla():
    # Eliminar cualquier widget previo en el contenedor de la tabla
    for widget in tabla_frame.winfo_children():
        widget.destroy()

    # Datos a mostrar en la tabla
    datos = [['A', 'B', '0', '1', '0+A', '0+A+B'],['0', '0', '0', '1', '0', '0'],['0', '1', '0', '1', '0', '1'],['1', '0', '0', '1', '1', '1'],['1', '1', '0', '1', '1', '1']]

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
ventana.title("Tabla en la Interfaz")

# Crear un marco para la tabla
tabla_frame = ttk.Frame(ventana)
tabla_frame.pack()

# Botón para mostrar la tabla
mostrar_btn = ttk.Button(ventana, text="Mostrar Tabla", command=mostrar_tabla)
mostrar_btn.pack()

# Ejecutar la aplicación
ventana.mainloop()
