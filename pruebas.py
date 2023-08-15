def find_power_relation(base, result):
    exponent = 0
    
    # Verificar si base^exponent es igual a result
    while base ** exponent != result:
        exponent += 1
        if base ** exponent > result:
            return None, None  # No hay relación de potencia
    
    return exponent, base

def find_inverse_power_relation(base, result):
    exponent, original_base = find_power_relation(result, base)
    return exponent, original_base

# Ejemplo de uso para la relación directa
base = int(input("Ingresa el número base: "))
result = int(input("Ingresa el resultado: "))

exponent, original_base = find_power_relation(base, result)

if exponent is None:
    print(f"{result} no es una potencia de {base}.")
else:
    print(f"{original_base} elevado a la {exponent} es igual a {result}.")

# Ejemplo de uso para la relación inversa
base_inverse = int(input("Ingresa el número base (relación inversa): "))
result_inverse = int(input("Ingresa el resultado (relación inversa): "))

exponent_inverse, original_base_inverse = find_inverse_power_relation(base_inverse, result_inverse)

if exponent_inverse is None:
    print(f"{result_inverse} no es una potencia de {base_inverse}.")
else:
    print(f"{original_base_inverse} elevado a la {exponent_inverse} es igual a {result_inverse}.")
