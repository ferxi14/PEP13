"""
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no.
"""
suma = 0
contador = 0

while True:
    numero = int(input("Introduce un número (0 para salir): "))
    if numero == 0:
        break
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print("Suma:", suma)
    print("Media:", media)
else:
    print("No se introdujeron números.")

suma = 0
contador = 0
numero = -1  

while numero != 0:
    numero = int(input("Introduce un número (0 para salir): "))
    if numero != 0:
        suma += numero
        contador += 1

if contador > 0:
    media = suma / contador
    print("Suma:", suma)
    print("Media:", media)
else:
    print("No se introdujeron números.")