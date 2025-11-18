# Fernando Gómez Rodríguez
minutos = int(input("Introduce una cantidad de minutos: "))

horas = minutos / 60
horasEnteras = int(horas)
resto = minutos - horasEnteras * 60


print("Equivale a " + str(horasEnteras) + " horas y " + str(resto) + " minutos")