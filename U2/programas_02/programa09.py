"""
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana.
"""
import random

banca = random.randrange(17, 22)
print("La banca ha realizado su jugada (entre 17 y 21).")

puntuacion_jugador = 0

while True:
    print("Tu puntuación actual:", puntuacion_jugador)
    opcion = input("¿Deseas sacar una carta? (s/n): ")

    if opcion == "s":
        carta = random.randrange(1, 6)  
        puntuacion_jugador += carta
        print(f"Has sacado una carta de valor {carta}. Nueva puntuación: {puntuacion_jugador}")

        if puntuacion_jugador > 21:
            print("Te has pasado de 21 pierdes")
            break
    elif opcion == "n":
        print("Has decidido plantarte con puntuación:", puntuacion_jugador)
        if puntuacion_jugador > 21:
            print("Te has pasado de 21 pierdes")
        elif puntuacion_jugador > banca:
            print(f"Felicidades, tu puntuación {puntuacion_jugador} supera a la banca ({banca}). Ganas! ")
        else:
            print(f"Tu puntuación {puntuacion_jugador} no supera a la banca ({banca}). Pierdes")
        break
    else:
        print("Opción no válida. Escribe 's' para sacar carta o 'n' para plantarte.")
