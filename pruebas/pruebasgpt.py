import tkinter as tk

ventana = tk.Tk()
ventana.title("Bloquear entrada de texto")

# Variable de estado para controlar si la entrada de texto está habilitada o no
entrada_habilitada = True

def asignar_base():
    global entrada_habilitada
    entrada_habilitada = False
    entrada_base.config(state=tk.DISABLED)

base = tk.Label(ventana, text="Ingrese la base de los números a trabajar:")
entrada_base = tk.Entry(ventana, state=tk.NORMAL)  # Comienza habilitada
boton_base = tk.Button(ventana, text="Guardar base", command=asignar_base)

base.pack()
entrada_base.pack()
boton_base.pack()

ventana.mainloop()
