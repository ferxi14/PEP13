"""
Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos
GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario.

Decimal (SI, 1000) → lo usan fabricantes de discos, redes, marketing de
almacenamiento.
Binario (IEC, 1024) → lo usan sistemas operativos, memoria RAM, tamaños de
archivos
"""
bytes_totales = int(input("Introduce el número de bytes: "))

GB_SI = bytes_totales // 1_000_000_000
resto_SI = bytes_totales % 1_000_000_000

MB_SI = resto_SI // 1_000_000
resto_SI = resto_SI % 1_000_000

KB_SI = resto_SI // 1_000
B_SI = resto_SI % 1_000

GiB = bytes_totales // (1024**3)
resto_IEC = bytes_totales % (1024**3)

MiB = resto_IEC // (1024**2)
resto_IEC = resto_IEC % (1024**2)

KiB = resto_IEC // 1024
B_IEC = resto_IEC % 1024

print(f"\n{bytes_totales} bytes en sistema decimal (SI): {GB_SI} GB, {MB_SI} MB, {KB_SI} KB, {B_SI} bytes")
print(f"{bytes_totales} bytes en sistema binario (IEC): {GiB} GiB, {MiB} MiB, {KiB} KiB, {B_IEC} bytes")