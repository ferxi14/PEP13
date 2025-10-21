"""
Escribe un programa en Python que importe el modulo math completo y que le pregunte al
usuario que operación matemática quiere hacer:
1. Seno de un ángulo
2. Coseno de ángulo
3. Raíz cuadrada de un número
4. Potencia de dos números.
Le pida los datos necesarios y muestre los resultados por pantalla.
"""
import math

def menu() :
    print("1. Seno de un ángulo")
    print("2. Coseno de un ángulo")
    print("3. Raíz cuadrada de un número")
    print("4. Potencia de dos números")
    print("5. Salir")
def main():
    salir = False
    while not salir:
        menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            angulo = float(input("Introduce el ángulo en grados: "))
            resultado = math.sin(math.radians(angulo))
            print(f"El seno de {angulo}° es: {resultado:.4f}")

        elif opcion == "2":
            angulo = float(input("Introduce el ángulo en grados: "))
            resultado = math.cos(math.radians(angulo))
            print(f"El coseno de {angulo}° es: {resultado:.4f}")

        elif opcion == "3":
            numero = float(input("Introduce un número: "))
            if numero < 0:
                print("No se puede calcular la raíz cuadrada de un número negativo.")
            else:
                resultado = math.sqrt(numero)
                print(f"La raíz cuadrada de {numero} es: {resultado:.4f}")

        elif opcion == "4":
            base = float(input("Introduce la base: "))
            exponente = float(input("Introduce el exponente: "))
            resultado = math.pow(base, exponente)
            print(f"{base} elevado a {exponente} es: {resultado:.4f}")

        elif opcion == "5":
            print("👋 Hasta pronto.")
            salir = True
        else:
            print("Opción no válida. Por favor, elige entre 1 y 5.")

if __name__ == "__main__":
    main()
