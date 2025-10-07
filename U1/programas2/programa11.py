"""
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo
de viaje hasta llegar a otra ciudad B es de N segundos. Escribie un programa que
determine la hora de llegada a la ciudad B.
"""
hora = int(input("Introduce la hora de salida (HH): "))
minuto = int(input("Introduce los minutos de salida (MM): "))
segundo = int(input("Introduce los segundos de salida (SS): "))

tiempo_viaje = int(input("Introduce el tiempo de viaje en segundos: "))

total_segundos_salida = hora * 3600 + minuto * 60 + segundo

total_segundos_llegada = total_segundos_salida + tiempo_viaje

hora_llegada = (total_segundos_llegada // 3600) % 24
minuto_llegada = (total_segundos_llegada % 3600) // 60
segundo_llegada = total_segundos_llegada % 60

print(f"La hora de llegada es: {hora_llegada:02d}:{minuto_llegada:02d}:{segundo_llegada:02d}")