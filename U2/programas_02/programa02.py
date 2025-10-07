"""
Escribe un que lea por teclado un número comprendido entre 1 y 10. No se dejara de
pedir el número hasta que no se introduzca correctamente.
"""
numero = 0

while numero < 1 or numero > 10:
    numero = int(input("Introduce un número entre 1 y 10: "))
    if numero < 1 or numero > 10:
        print("Número incorrecto. Inténtalo de nuevo.")

print("Número válido:", numero)