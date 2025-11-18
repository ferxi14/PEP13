# Fernando Gómez Rodríguez
from modulos import jugador, enemigo 
def main():
    nombre = input("Introduce tu nombre: ")
    conocimiento = int(input("Introduce el nivel de conocimiento (1-10): "))
    energia = int(input("Introduce la energia inicial (1-5): "))

    jugador.mostrar_jugador(nombre, conocimiento, energia)

    nombreEnemigo, conocimientoEnemigo, energiaEnemigo = enemigo.generar_enemigo()
    enemigo.mostrar_enemigo(nombreEnemigo, conocimientoEnemigo, energiaEnemigo)

    poderMagia = jugador.ataque_jugador(conocimiento, energia)
    poderMagiaEnemigo = enemigo.ataque_enemigo(conocimientoEnemigo, energiaEnemigo)

    for i in range(3):
        print("Ronda ", i)
        print("Magia de ", nombre, " :", poderMagia)
        print("Magia de ", nombreEnemigo, " :" , poderMagiaEnemigo)

        if (poderMagia > poderMagiaEnemigo):
            print("Ataque con exito al enemigo (-1 de energía para el enemigo)")
            energiaEnemigo -= 1
        elif (poderMagiaEnemigo > poderMagia):
            print("El enemigo te ha golpeado (-1 de energía)")
            energia -= 1
        else:
            print("Ambos teneis el mismo poder de Magia, empate")

            
    if (energia > energiaEnemigo):
        print("Enhorabuena has ganado a ", nombreEnemigo)
    elif (energiaEnemigo > energia):
        print(f"{nombreEnemigo} te ha ganado el duelo")
    else:
        print("Habeis empatado")

if __name__ == "__main__":
    main()