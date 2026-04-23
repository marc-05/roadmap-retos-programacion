"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# Operadores Aritméticos
print(f"suma: {10 + 3}")
print(f"resta: {10 - 3}")
print(f"multiplicación: {10 * 3}")
print(f"división: {10 / 3}")
print(f"módulo: {10 % 3}")
print(f"exponente: {10 ** 3}")
print(f"división entera: {10 // 3}")

# Operadores de comparación
print(f"Igualdad: {10 == 3}")
print(f"Desigualdad: {10 != 3}")
print(f"Mayor que: {10 > 3}")
print(f"Menor que: {10 < 3}")
print(f"Mayor o igual que: {10 >= 3}")
print(f"Menor o igual que: {10 <= 3}")

# Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 10 - 3 == 7 es {10 + 3 == 13 and 10 - 3 == 7}")
print(f"OR ||: 10 + 3 == 13 or 10 - 3 == 7 es {10 + 3 == 13 or 10 - 3 == 7}")
print(f"NOT !: not (10 + 3 == 13) es {not (10 + 3 == 13)}")

# Operadores de asignación
un_numero = 10 # Asignación simple
print(un_numero)
un_numero += 5 # Suma y asignación
print(un_numero)
un_numero -= 3 # Resta y asignación
print(un_numero)  
un_numero *= 2 # Multiplicación y asignación
print(un_numero)
un_numero /= 4 # División y asignación
print(un_numero)
un_numero %= 3 # Módulo y asignación
print(un_numero)
un_numero **= 2 # Exponente y asignación
print(un_numero)
un_numero //= 3 # División entera y asignación
print(un_numero) 

# Operadores de identidad
my_new_numero = un_numero
print(f"my_new_numero es my_numero: {my_new_numero is un_numero}")
print(f"my_new_numero no es my_numero: {my_new_numero is not un_numero}")

# Operadores de pertenencia
my_cadena = ("Hola", "Mundo", "Python")
print(f"H está en my_cadena: {"H" in my_cadena}")
print(f"Mundo está en my_cadena: {"Mundo" in my_cadena}")

# Operadores de bits
print(f"AND bit a bit: {10 & 3}")
print(f"OR bit a bit: {10 | 3}")
print(f"XOR bit a bit: {10 ^ 3}")
print(f"Desplazamiento a la izquierda: {10 << 1}")
print(f"Desplazamiento a la derecha: {10 >> 1}")
print(f"NOT bit a bit: {~10}")
print(f"Complemento a uno: {~10 + 1}")

# Estructuras de control
for i in range(5):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")
        



"""DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 """

for num in range (10, 55):
    if num % 2 == 0 and num != 16 and num % 3 != 0:
        print(num)
