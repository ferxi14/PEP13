"""
Escribe un programa que calcule la calificación de estudiante en un módulo.
La calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2, 60% y RA3 20%).
"""
ra1 = float(input("Introduce la calificación de RA1 (20%): "))
ra2 = float(input("Introduce la calificación de RA2 (60%): "))
ra3 = float(input("Introduce la calificación de RA3 (20%): "))

calificacion_final = ra1 * 0.2 + ra2 * 0.6 + ra3 * 0.2

print(f"La calificación final del estudiante es: {calificacion_final:.2f}")