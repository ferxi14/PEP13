"""
Crea un módulo llamado operaciones que contenga cuatro funciones básicas
relacionadas con operaciones numéricas:
suma(a, b) → devuelve la suma de dos números.
resta(a, b) → devuelve la resta de dos números.
multiplicacion(a, b) → devuelve la multiplicación de dos números.
division(a, b) → devuelve la división de dos números (controlando la división entre
cero).
"""
# ==============================
# imports de la librería estándar
# ==============================
# Ninguna en este ejemplo

# ==============================
# imports de librerías de terceros
# ==============================
# Ninguna en este ejemplo

# ==============================
# imports de módulos propios
# ==============================
import operaciones

# ==============================
# Definición de funciones principales
# ==============================
def main():
    print("Hola, este es el programa principal\n")

    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print(f"Suma: {operaciones.suma(a, b)}")
    print(f"Resta: {operaciones.resta(a, b)}")
    print(f"Multiplicación: {operaciones.multiplicacion(a, b)}")
    print(f"División: {operaciones.division(a, b)}")

# ==============================
# Bloque para asegurar ejecución sólo si el archivo es el principal
# ==============================
if __name__ == "__main__":
    main()