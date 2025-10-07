"""
Escribe un programa que lea por teclado un número real entre 1 y 10, simulando una
nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en
cuenta los siguientes rangos:
• Insuficiente: [0, 5)
• Suficiente: [5, 6)
• Bien: [6, 7)
• Notable: [7, 9)
• Sobresaliente: [9, 10]
Si el número introducido no está en ninguno de los rangos anteriores debe mostrar un
mensaje de error indicando que la nota no es válida.
Hay que usar la estructura match.
"""
nota = float(input("Introduce una nota entre 1 y 10: "))
if nota < 0 or nota > 10:
    print("Error: La nota no es válida.")
else:
    match nota:
        case n if 0 <= n < 5:
            print("Calificación: Insuficiente")
        case n if 5 <= n < 6:
            print("Calificación: Suficiente")
        case n if 6 <= n < 7:
            print("Calificación: Bien")
        case n if 7 <= n < 9:
            print("Calificación: Notable")
        case n if 9 <= n <= 10:
            print("Calificación: Sobresaliente")
        case _:
            print("Error: La nota no es válida.")