"""
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
•La piedra gana a la tijera pero pierde contra el papel.
•El papel gana a la piedra pero pierde contra la tijera.
•La tijera gana al papel pero pierde contra la piedra.
"""
import random

print("Juego: Piedra, Papel o Tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

opcion = int(input("Selecciona una opcion 1-3: "))

opcion_pc = random.randrange(1,4)

opciones = ["Piedra", "Papel", "Tijera"]
print("Tú elegiste:", opciones[opcion - 1])
print("Tu rival eligió:", opciones[opcion_pc - 1])

if opcion == opcion_pc:
    print("Empate.")
elif (opcion == 1 and opcion_pc == 3) or \
     (opcion == 2 and opcion_pc == 1) or \
     (opcion == 3 and opcion_pc == 2):
    print("Has ganado!")
else:
    print("Has perdido")
