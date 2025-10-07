"""
Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita
obtener el número invertido.
"""
numero = int(input("Introduce un número de dos cifras: "))

if 10 <= numero <= 99:
    decenas = numero // 10
    unidades = numero % 10

    invertido = unidades * 10 + decenas

    print(f"El número invertido de {numero} es {invertido}.")
else:
    print("El número introducido no tiene dos cifras.")