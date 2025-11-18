# Fernando Gómez Rodríguez

import random

def ataque_jugador(conocimiento, energia):
    nivelMagia = conocimiento * energia * random.randrange(1,4)
    return nivelMagia

def mostrar_jugador(nombre, conocimiento, energia):
    return print(f"Jugador: {nombre}, conocimiento: {conocimiento}, energia: {energia}")