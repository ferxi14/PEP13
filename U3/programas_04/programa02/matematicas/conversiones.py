def a_binario(n):
    return bin(n)[2:]  

def a_hexadecimal(n):
    return hex(n)[2:]  

def a_entero(texto):
    try:
        return int(texto)
    except ValueError:
        return "Error: La cadena no es un número válido"