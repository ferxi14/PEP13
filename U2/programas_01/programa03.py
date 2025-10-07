"""
Escribe un programa que pida dos numeros y muestre su división. Se deben tener en
cuenta que no se puede dividir por 0 mostrando en ese caso un aviso.
"""
num1 = float(input("Introduce el primer número (dividendo): "))
num2 = float(input("Introduce el segundo número (divisor): "))
if num2 == 0:
    print("Error: No se puede dividir por 0.")
else:
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")
