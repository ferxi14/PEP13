"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor.
"""
import math

def calcular_area_circulo(radio) :
    return math.pi * radio ** 2
def calcular_area_triangulo(base, altura) :
    return (base * altura)/2
def calcular_area_rectangulo(base, altura) :
    return base * altura

def menu() :
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")

def leer_numero_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor que 0. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Debes introducir un número.")

def opcion1():
    radio = leer_numero_positivo("Introduce el radio del círculo: ")
    area = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area:.2f}")

def opcion2():
    base = leer_numero_positivo("Introduce la base del triángulo: ")
    altura = leer_numero_positivo("Introduce la altura del triángulo: ")
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area:.2f}")

def opcion3():
    base = leer_numero_positivo("Introduce la base del rectángulo: ")
    altura = leer_numero_positivo("Introduce la altura del rectángulo: ")
    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area:.2f}")


def main():
    salir = False
    while not salir:
        menu()
        opcion = input("Introduce una opción (1-4): ")

        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            print("Hasta pronto")
            break
        else:
            print("Opción no válida. Por favor, selecciona un número entre 1 y 4.")
if __name__ == "__main__":
    main()