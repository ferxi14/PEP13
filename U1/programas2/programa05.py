"""
Escribe un programa que pregunte al usuario dos números y calcule su suma, resta,
multiplicación, división, módulo y potencia.
"""
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if num2 != 0:
    division = num1 / num2
    modulo = num1 % num2
else:
    division = "No se puede dividir entre 0"
    modulo = "No se puede calcular módulo con 0"

potencia = num1 ** num2

print("Resultados:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")