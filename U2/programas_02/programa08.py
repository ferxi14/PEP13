"""
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).
Mejora el programa de forma que el usuario tenga solo 3 intentos.
"""
import random

numero_secreto = random.randrange(1, 21)

intentos = 0
max_intentos = 3
acertado = False

print("Adivina el número entre 1 y 20")
print(f"Tienes {max_intentos} intentos")

while intentos < max_intentos and not acertado:
    intento = int(input("Introduce un número: "))
    intentos += 1

    if intento == numero_secreto:
        acertado = True
        print(f"Felicidades! Has acertado el número en {intentos} intento(s).")
    elif intento < numero_secreto:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

if not acertado:
    print(f"Lo siento, no acertaste. El número secreto era {numero_secreto}")