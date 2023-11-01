import tkinter as tk
from tkinter import ttk
import procesos
def calcular(expresion):
    global tabla_de_verdad
    # Esta función de cálculo es similar a la que hemos discutido previamente
    stack = []
    resultado = '|' #posicion de 0
    operador = "+" #si se suma 0 el resultado es la misma variable
    negacion = ""
    expresion_lista=list(expresion) 
    expresion_lista = list(expresion)
    for i in range(len(expresion_lista)):
        print(i," Nueva operacion")
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
letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
respaldo=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

variables = []
tabla_de_verdad=[]
def imprimir_tabla(tabla):
    for fila in tabla:
        fila_str = " | ".join(map(str, fila))
        print(f"| {fila_str} |")

def guardar_tabla_en_txt(tabla, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for fila in tabla:
            fila_str = " | ".join(map(str, fila))
            archivo.write(f"| {fila_str} |\n")

expresion_actual = "-(((A*B)+(K*L))*((C*D)+(I*J)))+(-(-(E*F)+(-(G*H))))"
expresion_actual = expresion_actual.upper()
for elemento in expresion_actual:
    if elemento in letras:
        variables.append(elemento)
        letras.remove(elemento) 

procesos.generar_tabla(variables, len(variables))
prueba = calcular(expresion_actual)
tabla_de_verdad = procesos.tabla_verdad.copy()

# Guardar la tabla de verdad en un archivo .txt
guardar_tabla_en_txt(tabla_de_verdad, "tabla_de_verdad.txt")
print("Tabla de verdad guardada en tabla_de_verdad.txt")
print("Resultado de la expresión:", prueba)
