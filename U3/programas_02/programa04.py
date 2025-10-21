"""
El módulo turtle es una biblioteca estándar de Python que permite crear gráficos y dibujos
de manera sencilla, moviendo una “tortuga” virtual por la pantalla. El módulo está instalado
por defecto en el interprete de Python.
Investiga la documentación del módulo https://docs.python.org/3/library/turtle.html y
escribe un programa que:
•Dibuje un cuadrado rojo sin rellenar.
•Dibuje un circulo verde relleno.
"""
import turtle
ventana = turtle.Screen()
ventana.title("Dibujo con Turtle")
ventana.bgcolor("white") 

t = turtle.Turtle()
t.speed(3)  

t.color("red")  
t.penup()
t.goto(-100, 50)  
t.pendown()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.goto(100, -50)  
t.pendown()

t.fillcolor("green")  
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()