""" 
Escribe un programa que pida primero un número par y luego un número impar (positivos
o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
impar respectivamente), se mostrará un aviso.
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
