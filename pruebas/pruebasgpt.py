import tkinter as tk
def obtener_numeros(expresion):
    numeros = []
    numero_actual = ""
    
    for caracter in expresion:
        if caracter.isdigit():
            numero_actual += caracter
        elif numero_actual:
            numeros.append(numero_actual)
            numero_actual = ""
    
    if numero_actual:
        numeros.append(numero_actual)
    
    return numeros

def calcular_expresion(expresion):
    
    numeros = obtener_numeros(expresion)
    # Esta función de cálculo es similar a la que hemos discutido previamente
    stack = []
    resultado = 0
    operador = "+"

    for elemento in expresion:
        if elemento == "(":
            stack.append((resultado, operador))
            resultado = 0
            operador = "+"
        elif elemento == ")":
            operando, operador_anterior = stack.pop()
            if operador_anterior == "+":
                resultado = operando + resultado
            elif operador_anterior == "-":
                resultado = operando - resultado
        elif elemento.isnumeric():
            numero = int(elemento)
            if operador == "+":
                resultado += numero
            elif operador == "-":
                resultado -= numero
        elif elemento in ("+", "-"):
            operador = elemento
    
    return resultado

def calcular():
    expresion = entrada.get()  # Obtiene la expresión ingresada por el usuario desde la entrada de texto
    resultado = calcular_expresion(expresion)
    resultado_label.config(text=f"Resultado: {resultado}")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear una entrada de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Botón para calcular
calcular_button = tk.Button(ventana, text="Calcular", command=calcular)
calcular_button.pack()

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Iniciar el bucle principal de la ventana
ventana.mainloop()
