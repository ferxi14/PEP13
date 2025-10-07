"""
Escribe un programa que realice las siguientes operaciones:
•Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
no se introduzca el número correcto.
•Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
•Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
indica que no quiere continuar el programa finaliza.
"""
continuar = "s"

while continuar == "s":
    numero = 0
    while numero < 1 or numero > 10:
        numero = int(input("Introduce un número entre 1 y 10: "))
        if numero < 1 or numero > 10:
            print("Número incorrecto. Inténtalo de nuevo.")

    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    continuar = input("Deseas introducir otro número? (s/n): ")
    print()  

print("Programa finalizado, hasta luego!")