"""
Crea un paquete llamado matemáticas que contenga tres módulos:
operaciones: creado en la práctica anterior.
figuras: tendrá las siguientes funciones.

◦area_rectangulo(base, altura): devuelve el área.
◦area_triangulo(base, altura): devuelve el área.
◦area_circulo(radio): devuelve el área.
conversiones.py: tendrá las siguientes funciones
◦a_binario(n): devuelve la representación binaria de un número entero en forma
de cadena.
◦a_hexadecimal(n): devuelve la representación hexadecimal de un número
entero en forma de cadena.
◦a_entero(texto): convierte una cadena numérica en un entero (controlando
errores si el texto no es válido)
Recuerda que debes incluir el fichero __init__.py aunque esté vacío.
Crea un programa principal main.py que muestre un menú que permita elegir entre:
Operaciones matemáticas
Cálculo de áreas geométricas
Según la opción elegida, pida al usuario los datos necesarios y muestre el resultado
correspondiente.
"""

from matematicas import conversiones, figuras, operaciones

def main() :
    print("Hola, este es el programa principal")
    salir = True
    while salir:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Operaciones matemáticas")
        print("2. Cálculo de áreas geométricas")
        print("3. Salir")

        opcion = input("Selecciona una opción (1-3): ")

        if opcion == "1":
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))

            print(f"Suma: {operaciones.suma(a, b)}")
            print(f"Resta: {operaciones.resta(a, b)}")
            print(f"Multiplicación: {operaciones.multiplicacion(a, b)}")
            print(f"División: {operaciones.division(a, b)}")

        elif opcion == "2":
            print("--- Áreas geométricas ---")
            print("1. Rectángulo")
            print("2. Triángulo")
            print("3. Círculo")
            tipo = input("Selecciona figura (1-3): ")

            if tipo == "1":
                base = float(input("Introduce la base: "))
                altura = float(input("Introduce la altura: "))
                print(f"Área del rectángulo: {figuras.area_rectangulo(base, altura):.2f}")

            elif tipo == "2":
                base = float(input("Introduce la base: "))
                altura = float(input("Introduce la altura: "))
                print(f"Área del triángulo: {figuras.area_triangulo(base, altura):.2f}")

            elif tipo == "3":
                radio = float(input("Introduce el radio: "))
                print(f"Área del círculo: {figuras.area_circulo(radio):.2f}")

            else:
                print("Opción no válida.")

        elif opcion == "3":
            print("Saliendo...")
            salir = False

        else:
            print("Opción no válida. Por favor, selecciona 1, 2 o 3.")


if __name__ == "__main__":
    main()