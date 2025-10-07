"""
Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de
millas y un número de Km, muestre respectivamente el número de millas y kilómetros. Los
resultados deben estar redondeados a 2 decimales.
"""
MILLA_A_KM = 1.61

millas = float(input("Introduce el número de millas: "))
km = float(input("Introduce el número de kilómetros: "))

km_desde_millas = millas * MILLA_A_KM

millas_desde_km = km / MILLA_A_KM

print(f"{millas} millas equivalen a {km_desde_millas:.2f} km")
print(f"{km} km equivalen a {millas_desde_km:.2f} millas")