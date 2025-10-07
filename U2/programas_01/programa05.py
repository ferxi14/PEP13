"""
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
o que indique que son iguales.
"""
n1 = int(input("Introduce el primer numero: "))
n2 = int(input("introduce el segundo numero: "))

if n1 > n2:
    print(f"El número {n1} es el mayor y el número {n2} es el menor")
else:
    if n2 > n1:
        print(f"El número {n2} es el mayor y el número {n1} es el menor")
    else:
        print("Los números son iguales")