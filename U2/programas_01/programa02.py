"""
Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no
es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o
negativo) y si el valor no es correcto, mostrará un aviso.
"""
num_par = int(input("Introduce un número par: "))
if num_par % 2 != 0:
    print("El número introducido no es par.")
else:
    num_impar = int(input("Introduce un número impar: "))
    if num_impar % 2 == 0:
        print("El número introducido no es impar.")
    else:
        print(f"Números correctos: par {num_par} e impar {num_impar}.")