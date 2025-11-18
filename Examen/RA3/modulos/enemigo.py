# Fernando Gómez Rodríguez

import random

def generar_enemigo():
    nombres = ["Hydra", "Kraken", "Minotauro", "Gorgona", "Titán"]
    nombre = random.choice(nombres)

    conocimiento = random.randrange(1, 11)
    energia = random.randrange(1, 6)

    return nombre, conocimiento, energia

def ataque_enemigo(conocimiento, energia):
    nivelMagia = conocimiento * energia * random.randrange(1,4)
    return nivelMagia

def mostrar_enemigo(nombre, conocimiento, energia):
    return print(f"Enemigo: {nombre}, conocimiento: {conocimiento}, energia: {energia}")