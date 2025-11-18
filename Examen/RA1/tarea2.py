# Fernando Gómez Rodríguez

# Pedir tres tipos de datos distintos al usuario
dato1 = int(input("Introduce un numero entero: "))
dato2 = float(input("Introduce un numero decimal: "))
dato3 = str(input("Introduce un texto: "))

#Imprimir los datos y sus tipos
print(dato1, type(dato1))
print(dato2, type(dato2))
print(dato3, type(dato3))

# Comprobar si los tipos es correcto y almacenarlo en variables
correctoInt = {int} == {type(dato1)}
correctoFloat = {float} == {type(dato2)} 
correctoStr = {str} == {type(dato3)}

# Comprobar si los tres tipos son True o False
print(f"los tipos de las variables son {correctoInt and correctoFloat and correctoStr}")



