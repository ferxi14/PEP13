"""
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
"""
dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
valida = True

if mes < 1 or mes > 12:
    valida = False
else:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_mes = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_mes = 30
    elif mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            dias_mes = 29
        else:
            dias_mes = 28

    if dia < 1 or dia > dias_mes:
        valida = False

if valida:
    print("La fecha es correcta")
else:
    print("La fecha no es valida")        