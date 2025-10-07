"""
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue.
"""
print("Versión 1: for sin continue")

for i in range(0, 11):
    if i % 2 == 0:
        print(i)

print("Versión 2: for con continue")

for i in range(0, 11):
    if i % 2 != 0:
        continue  
    print(i)

print("Versión 3: while sin continue")

i = 0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

print("Versión 4: while con continue")

i = 0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue  
    print(i)