"""
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.
"""
import random

banca = random.randrange(17, 22)
print("La banca ha realizado su jugada (entre 17 y 21).\n")

num_jugadores = int(input("Introduce el número de jugadores: "))

for jugador in range(1, num_jugadores + 1):
    print(f"Turno del jugador {jugador}:")
    puntuacion_jugador = 0

    while True:
        print("Tu puntuación actual:", puntuacion_jugador)
        opcion = input("Deseas sacar una carta? (s/n): ").lower()

        if opcion == "s":
            carta = random.randrange(1, 6) 
            puntuacion_jugador += carta
            print(f"Has sacado una carta de valor {carta}. Nueva puntuación: {puntuacion_jugador}")

            if puntuacion_jugador > 21:
                print("Te has pasado de 21. Pierdes ")
                break
        elif opcion == "n":
            print("Has decidido plantarte con puntuación:", puntuacion_jugador)
            if puntuacion_jugador > 21:
                print("Te has pasado de 21. Pierdes ")
            elif puntuacion_jugador > banca:
                print(f"Felicidades, tu puntuación {puntuacion_jugador} supera a la banca ({banca}). Ganas! ")
            else:
                print(f"Tu puntuación {puntuacion_jugador} no supera a la banca ({banca}). Pierdes")
            break
        else:
            print("Opción no válida. Escribe 's' para sacar carta o 'n' para plantarte.")

print(f"La puntuación de la banca fue: {banca}")
print("Fin del juego.")