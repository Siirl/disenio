import procesos
val1=0
val2=1
letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

letras2=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
variables = []


entrada_ope=input("Ingrese la operacion a realizar")
operacion=list(entrada_ope)
for elementos in operacion:
    elemento=elementos.upper()
    if elemento in letras:
        variables.append(elemento)
        letras.remove(elemento)
tabla=procesos.generar_tabla(len(variables), variables)




