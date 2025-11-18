# Fernando Gómez Rodríguez 
# REGLAS
# El jugador empieza con 3 vidas y 0 puntos
# En cada turno:
#   Se muestran vidas del jugador
#   El jugador elige un tipo de ataque (que condiciona la tirada del enemigo) entre:
#       Fuerza carta entre 5 y 10. El enemigo se defiende mejor (carta entre 3 y 10).
#       Precision carta entre 3 y 8. El enemigo tambien estable (carta entre 2 y 9).
#       Riesgo carta entre 1 y 10. El enemigo se confunde (carta entre 1 y 8).
#   Si la carta del jugador es mayor, gana el turno y suma 1 punto
#   Si la carta del enemigo es mayor, el jugador pierde una vida
#   Si las cartas son iguales, hay un empate y no se suman puntos ni se pierden vidas
#   El juego continua mientras el jugador tenga vidas
#   Al terminar, se muestra la puntuacion final

import random

# Variables de uso en el programa
vidasJugador = 3
puntosJugador = 0
nivel = 1
seguir = True

# Bucle donde se desarrolla el juego
while seguir:
    print("Ahora mismo tienes ", vidasJugador)
    turno = input("Elige el tipo de ataque (f, p, r): ")

    if (turno == "f" or turno == "F"):
        cartaJugador = random.randrange(5, 11) 
        cartaEnemigo = random.randrange(3, 11)

        print(f"Tienes un {cartaJugador}")
        print(f"El enemigo tiene un {cartaEnemigo}")

        if (cartaJugador > cartaEnemigo):
            puntosJugador += 1
            print("Has sumado un punto")
        elif (cartaEnemigo > cartaJugador):
            vidasJugador -= 1
            print("Lo siento has perdido una vida")
        else:
            print("Ha habido empate, se continúa el juego")            

    
    elif (turno == "p" or turno == "P"):
        cartaJugador = random.randrange(3, 9)
        cartaEnemigo = random.randrange(2, 10)

        if (cartaJugador > cartaEnemigo):
            puntosJugador += 1
            print("Has sumado un punto")
        elif (cartaEnemigo > cartaJugador):
            vidasJugador -= 1
            print("Lo siento has perdido una vida")
        else:
            print("Ha habido empate, se continúa el juego")

    elif (turno == "r" or turno == "R"):
        cartaJugador = random.randrange(1, 11)
        cartaEnemigo = random.randrange(1, 9)

        if (cartaJugador > cartaEnemigo):
            puntosJugador += 1
            print("Has sumado un punto")
        elif (cartaEnemigo > cartaJugador):
            vidasJugador -= 1
            print("Lo siento has perdido una vida")
        else:
            print("Ha habido empate, se continúa el juego")
    
    else:
        print("Opción no válida. Escribe una opcion entre (f, p, r)")

    # Sube de nivel el jugador y recupera una vida cada 3 puntos que haga siempre y cuando tenga menos de 3 vidas
    if (puntosJugador % 3 == 0 and vidasJugador < 3):
        nivel += 1
        vidasJugador += 1

    #Si el jugador se queda sin vidas se acaba el juego y muestra el resultado de la partida con los puntos y nivel del jugador
    if (vidasJugador == 0):
        seguir = False
        print("El jugador ha conseguido: ", puntosJugador ," puntos en la partida  y ha llegado al nivel ", nivel)

    

