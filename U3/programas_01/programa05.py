"""
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).
"""
mensaje = "Soy una variable GLOBAL"

def funcion_externa():
    mensaje_externo = "Soy una variable LOCAL en funcion_externa"

    def funcion_interna():
        mensaje_interno = "Soy una variable LOCAL en funcion_interna"
        print("Dentro de funcion_interna:")
        print("→ mensaje_interno:", mensaje_interno)
        print("→ mensaje_externo (accedida desde funcion_interna):", mensaje_externo)
        print("→ mensaje (global):", mensaje)

    funcion_interna()

def funcion_modificar_global():
    global mensaje 
    mensaje = "He sido modificada dentro de funcion_modificar_global"

def funcion_con_nonlocal():
    texto = "Texto en funcion_con_nonlocal"

    def interna():
        nonlocal texto  
        texto = "Texto modificado por nonlocal"

    print("Antes de llamar a interna():", texto)
    interna()
    print("Después de llamar a interna():", texto)

print("=== DEMOSTRACIÓN DE ÁMBITOS DE VARIABLES ===")

print("Acceso desde fuera de cualquier función:")
print("→ mensaje (global):", mensaje)

print("Llamada a funcion_externa():")
funcion_externa()

print("Llamada a funcion_con_nonlocal():")
funcion_con_nonlocal()

print("Llamada a funcion_modificar_global():")
print("→ Antes:", mensaje)
funcion_modificar_global()
print("→ Después:", mensaje)
