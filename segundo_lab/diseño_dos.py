numero1 = []
numero2 = []
resultado_suma = []
valor_suma =[]
resultado_resta = []
valor_resta = []
base = 0
tam=0
temp=False
numero_destino = []
lista_caracteres = []



def asignar_diccionario():
    global lista_caracteres
    lista_letras_mayuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L","M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lista_letras_minuscula = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l","m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    special_symbols = [
                       '🁂' , '🁃' , '🁄' , '🁅' , '🁆' , '🁇' , '🁈' , '🁉' , '🁊' , '🁋' , '🁌' , '🁍' , '🁎' , '🁏' , '🁐' , '🁑' , '🁒' , '🁓' ,
                       '🁔' , '🁕' , '🁖' , '🁗' , '🁘' , '🁙','🁢' , '🁣' , '🁤' , '🁥' , '🁦' , '🁧' , '🁨' , '🁩' , '🁪' , '🁫' , '🁬' , '🁭' , '🁮' ,
                       '🁯' , '🁰' , '🁱' , '🁲' , '🁳' , '🁴' , '🁵' , '🁶' , '🁷' , '🁸' , '🁹' , '🁺' , '🁻' , '🁼' , '🁽',
                       '🁾' , '🁿' , '🂀' , '🂁' , '🂂' , '🂃' , '🂄' , '🂅' , '🂆' , '🂇' , '🂈' , '🂉' , '🂊' , '🂋' , '🂌' , '🂍' , '🂎' , '🂏' , '🂐' , '🂐' , '🂑' , '🂒' , '🂓',
                       '⚀', '⚁', '⚂', '⚃', '⚄', '⚅','⛀' , '⛁' , '⛂' , '⛃',
                       '≛' , '⋆' , '★' , '⍣' , '☆' , '✡' , '✦' , '✧' , '✩' , '✪' , '✫' , '✬' , '✭' , '✮' , '✯' , '✰' , '⁂' , '⁎' ,
                       '⁑' , '⌑' , '☸' , '✢' , '✣' , '✤' , '✥' , '✱' , '✲' , '✳' , '✴' , '✵' , '✶' , '✷' , '✸' , '✹' , '✺' , '✻' , '✼' ,
                       '✽' , '✾' , '❂' , '❃' , '❇','↕' , '↖' , '↗' , '↘' , '↙' , '↚' , '↛' , '↜' , '↝' , '↞' , '↟' , '↠' , '↡' , '↢' , '↣' , '↤' ,
                       '↥' , '↦' , '↧' , '↨' , '↩' , '↪' , '↫' , '↬' , '↭' , '↮' , '↯' , '↰' , '↱' , '↲' , '↳' , '↴' , '↶' , '↷' , '↸' , '↹' , '↺' , '↻' ,
                       '↼' , '↽' , '↾' , '↿' , '⇀' , '⇁' , '⇂' , '⇃' , '⇄' , '⇅' , '⇆' , '⇇' , '⇈' , '⇉' , '⇊' , '⇋' , '⇌' , '⇍' , '⇎' , '⇏' , '⇕' , '⇖' , '⇗' ,
                       '⇘' , '⇙' , '⇚' , '⇛' , '⇜' , '⇝' , '⇞' , '⇟' , '⇠',
                       '⇡' , '⇢' , '⇣' , '⇤' , '⇥' , '⇦' , '⇧' , '⇨' , '⇩' , '⇪' , '⌅' , '⌆' , '⌤' , '⏎' , '▶' , '☇' , '☈' , '☊' ,
                       '☋' , '☌' , '☍' , '➔' , '➘' , '➙' , '➚' , '➛' , '➜' , '➝' , '➞' , '➟' , '➠' , '➡' , '➢' , '➣' , '➤' , '➥' , '➦' ,
                       '➧' , '➨' , '➩' , '➪' , '➫' , '➬' , '➭' , '➮' , '➯' , '➱' , '➲' , '➳' , '➴' , '➵' , '➶' , '➷' , '➸' , '➹' , '➺' ,
                       '➻' , '➼' , '➽' , '➾' , '⤴' , '⤵' , '↵' , '↓' , '↔' , '←' , '→' , '↑' , '⇐' , '⇑'
                       '⇒' , '⇓' , '⇔' , '⌦' , '⌧' , '⌫' , '⇰' , '⇫' , '⇬' , '⇭' , '⇳' , '⇮' , '⇯' , '⇱' , '⇲' , '⇴' , '⇵' , '⇶' ,
                       '⇷' , '⇸' , '⇹' , '⇺' , '⟵' , '⟶' , '⟷' , '⬄' , '⬀' , '⬁' , '⬂' , '⬃' , '⬅' , '⮕' , '⬆' , '⬇' , '⬈' , '⬉' ,
                       '⬊' , '⬋' , '⬌' , '⬍' , '⇽' , '⇾' , '⇿' , '⬳' , '⟿' , '⤉' , '⤈' , '⇻' , '⇼' , '⬴' , '⤀' , '⬵' , '⤁' , '⬹' ,
                       '⤔' , '⬺' , '⤕' , '⬶' , '⤅' , '⬻' , '⤖' , '⬷' , '⤐' , '⬼' , '⤗' , '⬽' , '⤘' , '⤝' , '⤞' , '⤟' , '⤠' , '⤡' ,
                       '⤢' , '⤣' , '⤤' , '⤥' , '⤦' , '⤪' , '⤨' , '⤧' , '⤩' , '⤭' , '⤮' , '⤯' , '⤰' , '⤱' , '⤲' , '⤫' , '⤬' , '⬐' , '⬎' ,
                       '⬑' , '⬏' , '⤶' , '⤷' , '⥂' , '⥃' , '⥄',
                       'ぁ' , 'あ' , 'ぃ' , 'い' , 'ぅ' , 'う' , 'ぇ' , 'え' , 'ぉ' , 'お' , 'か' , 'が' , 'き' , 'ぎ',
                       'く' , 'ぐ' , 'け' , 'げ' , 'こ' , 'ご' , 'さ' , 'ざ' , 'し' , 'じ' , 'す' , 'ず' , 'せ' , 'ぜ',
                       'そ' , 'ぞ' , 'た' , 'だ' , 'ち' , 'ぢ' , 'っ' , 'つ' , 'づ' , 'て' , 'で' , 'と' , 'ど' , 'な',
                       '𐌰' , '𐌱' , '𐌲' , '𐌳' , '𐌴' , '𐌵' , '𐌶' , '𐌷' , '𐌸' , '𐌹' , '𐌺' , '𐌻' , '𐌼' , '𐌽' , '𐌾' , '𐌿' , '𐍀' ,
                       '𐍁' , '𐍂' , '𐍃' , '𐍄' , '𐍅' , '𐍆' , '𐍇' , '𐍈' , '𐍉' , '𐍊',
                       'Ѐ' , 'Ё' , 'Ђ' , 'Ѓ' , 'Є' , 'п' , 'І' , 'Ї' , 'Ј' , 'Љ' , 'Њ' , 'Ћ' , 'Ќ' , 'Ѝ' , 'Ў' , 'Џ' , 'А' ,
                       'Б' , 'В' , 'Г' , 'Д' , 'ӿ' , 'Ж' , 'З' , 'И' , 'Й' , 'К' , 'Л','Ҷ' , 'ҷ' , 'Ҹ' , 'ҹ' ,
                       'Һ' , 'һ' , 'Ҽ' , 'ҽ' , 'Ҿ' , 'ҿ' , 'Ӏ' , 'Ӂ' , 'ӂ' , 'Ӄ' , 'ӄ' , 'Ӆ' , 'ӆ' , 'Ӈ' , 'ӈ' , 'Ӊ' ,
                       'ӊ' , 'Ӌ' , 'ӌ' , 'Ӎ' , 'ӎ' , 'ӏ' , 'Ӑ' , 'ӑ' , 'Ӓ' , 'ӓ' , 'Ӕ' , 'ӕ' , 'Ӗ' , 'ӗ' , 'Ә' , 'ә' , 'Ӛ' , 'ӛ' , 'Ӝ' , 'ӝ' , 'Ӟ' , 'ӟ'
                       'ㄱ' , 'ㄲ' , 'ㄳ' , 'ㄴ' , 'ㄵ' , 'ㄶ' , 'ㄷ' , 'ㄸ' , 'ㄹ' , 'ㄺ' , 'ㄻ' , 'ㄼ' , 'ㄽ' , 'ㄾ' , 'ㄿ' , 'ㅀ' , 'ㅁ' ,
                       'ㅂ' , 'ㅃ' , 'ㅄ' , 'ㅅ' , 'ㅆ' , 'ㅇ' , 'ㅈ' , 'ㅉ' , 'ㅊ' , 'ㅋ' , 'ㅌ',
                       'ㅍ' , 'ㅎ' , 'ㅏ' , 'ㅐ' , 'ㅑ' , 'ㅒ' , 'ㅓ' , 'ㅔ' , 'ㅕ' , 'ㅖ' , 'ㅗ' , 'ㅘ' , 'ㅙ' , 'ㅚ' , 'ㅛ' , 'ㅜ' , 'ㅝ' ,
                       'ㅞ' , 'ㅟ' , 'ㅠ' , 'ㅡ' , 'ㅢ' , 'ㅥ' , 'ㅦ' , 'ㅧ' , 'ㅨ' , 'ㅩ' , 'ㅪ',
                       'ㅫ' , 'ㅬ' , 'ㅭ' , 'ㅮ','!', '@', '#', '$', '%', '&', '*', '+', '-', '=', '?', '≋','‥','‵','❜','❞','、','。','〃','「','」','『','』','〝','〞','︰','﹁','﹂','﹃','﹄','﹐','﹒','﹔','﹕','！','＃','＄','％','＆','＊','，','．','：','；','？','＠','～','•','…','¿','“','‘','·','′','”','’','‐','‐','‐','–','—','—','—','―',
                       '‗','‚','‛','„','‟','‣','․','″','‴','‶','‷','ʹ','ʺ','ʻ','ʼ','ʽ','ʾ','ʿ','ˀ','ˁ','˂','˃','˄','˅','ˆ','ˇ','ˈ','ˉ','ˊ','ˋ','ˌ','ˍ','ˎ','ˏ','ː','ˑ','˒','˓','˔','˕','˖','˗','˘','˚','˛','˜','˝','˞','ˠ','ˡ','⁘','⁙','⁚','⁛','⁜','⁜','⁝','⁞'
                        ,'❥', '❤', '♡', '۵', '♥', '❣', 'ღ', 'ლ', '❦', '❧', '☙', 'დ', '✾ ', '✽' , '✣', '✤' , '❀' , '✿' , '❃' , '❁' , '❋' , '❊' ,'⚜' , '✥' , '✻' , '✼' ,'❇','❈','❉','⚘','⁕','ꙮ','ꕤ','ꕥ','☘','֍','֎'
                        '𝄀' , '𝄁' , '𝄂' , '𝄃' , '𝄄' , '𝄅' , '𝄆' , '𝄇' , '𝄈' , '𝄉' , '𝄊' , '𝄋' , '𝄌' , '𝄍' , '𝄎' , '𝄏' , '𝄐' , '𝄑' , '𝄒' , '𝄓' , '𝄔' , '𝄕' , '𝄖' , '𝄗' , '𝄘' , '𝄙' , '𝄚' , '𝄛',
                       'ϟ' , '☀' , '☁' , '☂' , '☃' , '☄' , '☉' , '☼' , '☽' , '☾' , '♁' , '♨' , '❄' , '❅' , '❆' , '༄' , '✺' , '☇' , '☈' , '★' , '☆' , '℃' , '℉',
                        '☠' , '☤' , '☥' , '☦' , '☧' , '☨' , '☩' , '☪' , '☫' , '☬' , '☮' , '☭' , '☯' , '☸' , '☽' , '☾' , '♕' , '♚' , '♛' , '✙' , '✚' , '✛' , '✜' , '✝' , '✞' , '✟' , '✠' , '✡' , '✢' , '卍','卐','†' , '☓' , '♁' , '♆',
                        '‱' , '№' , '℗' , '℠' , '℡' , '℀' , '℁' , '℅' , '℆' , '⅍' , '☊' , '☎' , '☏' , '✁' , '✂' , '✃' , '✄' , '✆' , '✇' , '✈' , '✉' , '✎' , '✏' , '✐' , '✑' , '✒' , '™' , '©' , '®' , '‰' , '§' , '¶' , '⌗' , '⌖' , '⌨' , 'Ⓜ' , '♲' , '♳' , '♴' , '♵' , '♶' , '♷' , '♸' ,
                       '♹' , '♺' , '♻' , '♼' , '♽','♈︎' , '♉︎' , '♊︎' , '♋︎' , '♌︎' , '♍︎' , '♎︎' , '♏︎' , '♐︎' , '♑︎' , '♒︎' , '♓︎',
                       'ˇ' , '∛' , '∜' , '☐' , '☑' , '☒' , '✓' , '✔' , '✗' , '✘' , '∨' , '√︎',
                       '♔' , '♕' , '♖' , '♗' , '♘' , '♙' , '♚' , '♛' , '♜' , '♝' , '♞' , '♟︎',
                       '🀄' , '🀀' , '🀀' , '🀂' , '🀃' , '🀅' , '🀆' , '🀇' , '🀈' , '🀉' , '🀊' , '🀋' , '🀌' , '🀍' , '🀎' , '🀏' , '🀐' , '🀑' , '🀒' , '🀓' , '🀔' , '🀕' , '🀖' , '🀗' , '🀘' , '🀙' ,
                       '🀚' , '🀛' , '🀜' , '🀝' , '🀞' , '🀟' , '🀠' , '🀡' , '🀢' , '🀣' , '🀤' , '🀥' , '🀦' , '🀧' , '🀨' , '🀩' , '🀪' , '🀫︎',
                       '♡' , '♢' , '♤' , '♧' , '♣' , '♦' , '♥' , '♠︎','🀰' , '🀱' , '🀲' , '🀳' , '🀴' , '🀵' , '🀶' , '🀷' , '🀸' , '🀹' , '🀺' ,
                       '🀻' , '🀼' , '🀽' , '🀾' , '🀿' , '🁀' , '🁁'

                       ]
    for temp in range (10): #Asigna los primeros 10 valores
        lista_caracteres.append(str(temp))
    lista_caracteres.extend(lista_letras_mayuscula)
    lista_caracteres.extend(lista_letras_minuscula)
    lista_caracteres.extend(special_symbols)


def encontrar_posiciones(elementos_a_buscar):
    global lista_caracteres
    resultado = []
    for elemento in elementos_a_buscar:
        for i, item in enumerate(lista_caracteres):
            if elemento == item:
                resultado.append(i)
                break
    return resultado

def obtener_valores_por_posicion(posiciones):
    global lista_caracteres
    valores = []
    for pos in posiciones:
        if 0 <= pos < len(lista_caracteres):  # Verificar que la posición sea válida
            valores.append(lista_caracteres[pos])
        else:
            valores.append(None)  # Puedes manejar posiciones inválidas de la forma que desees
    return valores

def traduccion(num):
    cadena_traducida = ""
    global lista_caracteres
    cadena_traducida = lista_caracteres[int(num)]
    return cadena_traducida

def asignar_base(base_num):
    global base
    base = base_num

######################################################################################################################
#----------------------------------------Funciones Segundo Laboratorio-----------------------------------------------#
######################################################################################################################

def operar():
    global resultado_resta, resultado_suma, temp
    global numero1
    global numero2
    global tam
    num=numero1.copy()
    num2=numero2.copy()
    realizar_operacion_suma(num,num2,tam)
    realizar_operacion_resta(num,num2,tam)
    
    

def asignar_numeros(num1, num2):
    global numero1
    global numero2
    numero1 = num1
    numero2 = num2

def realizar_operacion_suma(nume,nume2,tam):
    global resultado_suma,valor_suma
    global base
    operacion=0
    resultado_suma.clear()
    num=nume.copy()
    num2=nume2.copy()
    num.reverse()
    num2.reverse()
    num.append(0)
    num2.append(0)
    base = int(base)
    for x in range(tam+1):
        operacion = int(num[x])+int(num2[x])
        if (operacion>base or operacion==base):
            num[x+1]= num[x+1]+1
            operacion = operacion - int(base) 
        resultado_suma.append(operacion)
    resultado_suma.reverse()
    valor_suma=resultado_suma
    resultado_suma=obtener_valores_por_posicion(resultado_suma)

def realizar_operacion_resta(num,num2,tam):
    global resultado_resta, valor_resta
    global base
    resultado_resta.clear()
    base = int(base)

    nume=num.copy()
    nume2=num2.copy()
    nume.reverse()
    nume2.reverse()
    print(nume,nume2)
    if (tam==1):
        tam=tam+1
    for x in range(tam-1):
        print(nume[x],nume2[x])
        if (int(nume[x])<int(nume2[x])):
            nume[x+1]=nume[x+1]-1
            nume[x]=nume[x]+base
        operacion = int(nume[x])-int(nume2[x])
        print(operacion)
        resultado_resta.append(operacion)
    resultado_resta.reverse()
    valor_resta = resultado_resta
    resultado_resta = obtener_valores_por_posicion(resultado_resta)

def comparar_listas_numeros(lista1, lista2):
    # Verifica si las listas tienen la misma longitud
    if len(lista1) != len(lista2):
        return "Las listas no tienen la misma longitud"
    
    # Invierte las listas para comparar desde la posición de mayor peso
    lista1 = lista1[::-1]
    lista2 = lista2[::-1]

    for i in range(len(lista1)):
        if lista1[i] > lista2[i]:
            return True
        elif lista2[i] > lista1[i]:
            return False
    
    return "Ambas listas son iguales"
        
        
######################################################################################################################
#----------------------------------------Funciones Primer Laboratorio------------------------------------------------#
######################################################################################################################


def convert_to_base_10(num_str, base_ori):
    exponente = len(num_str)
    resultado_base_10 = 0
    for x in range(1, exponente+1):
        resultado_base_10 += num_str[x-1]*((base_ori)**(exponente-x))
    return resultado_base_10

def convert_from_base_10(number, base):
    numer = ''.join(str(digit) for digit in number)
    numero = int(numer)
    result = ""
    while numero > 0:
        digit = numero % base
        numero_destino.insert(0,digit)
        num_traducido = lista_caracteres[digit]
        result = num_traducido+ result
        numero //= base
    return result

def convertir_from_base_10(number, base):
    result = ""
    while number > 0:
        digit = number % base
        numero_destino.insert(0,digit)
        num_traducido = lista_caracteres[digit]
        result = num_traducido+ result
        number //= base
    return result


def convert_between_bases(num_str, base_origin, base_dest):
    if base_origin == base_dest:
        return num_str
    
    if base_origin == 10:
        num_in_base_dest = convert_from_base_10(num_str, base_dest)
    elif base_dest == 10:
        num_in_base_dest = convert_to_base_10(num_str, base_origin)
    else:
        num_in_base_10 = convert_to_base_10(num_str, base_origin)
        num_in_base_dest = convertir_from_base_10(num_in_base_10, base_dest)
    
    return num_in_base_dest

def encontrar_exponente(base_1, base_2):
    exponente = 0
    while base_1 ** exponente != base_2:
        exponente += 1
        if base_1 ** exponente > base_2:
            return None  # No es una relación de potencias exacta
    return exponente


def encontrar_exponente(base_destino, base_origen):
    exponente = 0
    while base_destino ** exponente != base_origen:
        exponente += 1
        if base_destino ** exponente > base_origen:
            return None  # No es una relación de potencias exacta
    return exponente

def encontrar_relacion_potencias(base_destino, base_origen):
    exponente = encontrar_exponente(base_destino, base_origen)
    if exponente is not None:
        return exponente
    else:
        return "No hay una relación de potencias exacta"
    

def rela_potencias_mayor_a_menor(base_destino,lista_elementos,base_origen):
    divisor = base_destino
    base = base_origen
    potencia = encontrar_relacion_potencias(divisor,base)
    tamaño_lista=len(lista_elementos)
    resultado_final=""
    primer_numero=""
    for x in range(tamaño_lista):
        nume_a_operar = int(lista_elementos[tamaño_lista-x-1])
        for exp in range (potencia+1):
            cociente = nume_a_operar // (divisor**(int(potencia-exp)))
            residuo = nume_a_operar % (divisor**(int(potencia-exp)))
            primer_numero = str(primer_numero)+str(cociente)
            nume_a_operar = residuo
        print(primer_numero)
        resultado_final=str(int(primer_numero))+resultado_final
        primer_numero=""
    final=int(resultado_final)
    return final

def agregar_ceros(exponente):
    numero = 1
    veces = int(exponente)-1
    for x in range(veces):
        numero= int(str(numero)+str(0))
    return numero

def arreglarLista(lista,numeeee):
    result = []
    grupos = []

    # Divide cada número en dígitos y almacénalos en la lista 'result'
    for number in lista:
        number_str = str(number)
        result.extend(map(str, number_str))

    # Invierte la lista resultante
    lista2 = result[::-1]
    # Agrupa en grupos de 3
    for i in range(0, len(lista2), numeeee):  # Cambio de 2 a 3 aquí
        grupo = lista2[i:i + numeeee]
        grupos.append(str(''.join(map(str, grupo))))

    # Invierte nuevamente cada número en los grupos
    grup = [int(str(num)[::-1]) for num in grupos]

    return grup

def convert_bases_relation_normal(lista_numeros,base_origen,exponente):
    result = ""
    numero=0
    lista_strings = list(map(str, lista_numeros))
    list_arreglada = arreglarLista(lista_strings,exponente)
    lista_arre_str = list(map(str, list_arreglada))
    for x in range(len(lista_arre_str)): #Se opera
        num_in_x = "{:0{exponente}d}".format(int(lista_arre_str[x]), exponente=exponente) #cadena de formato obtenida en GPT
        for exp in range(exponente):
            dividir = agregar_ceros(exponente-exp)
            temp= int(num_in_x)//dividir
            numero = numero +(temp*(int(base_origen)**(exponente-exp-1)))
            if len(num_in_x)>1:
                num_in_x=num_in_x[1:]
        result=lista_caracteres[numero]+result
        numero=0
    return result
