"""
Escribe un programa que use los módulos platform y os para,
Mostrar el procesador donde se ejecuta el programa.
Mostrar el sistema operativo y versión donde se ejecuta el programa.
Mostrar el nombre el host donde se ejecuta el programa.
Mostrar el directorio actual.
"""
import platform
import os
def main():
    print("=== INFORMACIÓN DEL SISTEMA ===\n")

    print(f"Procesador: {platform.processor()}")

    print(f"Sistema operativo: {platform.system()} {platform.release()}")
    print(f"Versión completa: {platform.version()}")

    print(f"Nombre del host: {platform.node()}")

    print(f"Directorio actual: {os.getcwd()}")

if __name__ == "__main__":
    main()