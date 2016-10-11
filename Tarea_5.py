#encoding: UTF-8
#Aldo Fuentes A01373294
#Menu con funcionesde calculo y dibujo

from Graphics import *
from math import *

def dibujarCirculosYRectangulos(v):
    p0 = 190
    p1 = 210
    c0 = 10
    for _ in range(1,20):
        square = Rectangle((p0,p1),(p1,p0))
        square.fill = None
        square.draw(v)
        p0 -= 10
        p1 += 10
        circle = Circle((200,200), c0)
        circle.fill = None
        circle.draw(v)
        c0 += 10
        
def dibujarEstrella(v):
    t = Arrow((100,200), 0)
    t.pen.color = Color("blue")
    t.draw(v)
    t.penDown()
    for _ in range(1,6):
        t.forward(200)
        t.rotate(144)

def dibujarEspiral(v):
    l0 = 10
    t = Arrow((200,200),0)
    t.draw(v)
    t.penDown()
    for _ in range(1,74):
        t.forward(l0)
        t.rotate(90)
        l0 += 5

def dibujarCirculos(v):
    angulo0 = 0
    for _ in range(1,13):
        x0 = 50*cos(radians(angulo0))
        y0 = 50*sin(radians(angulo0))
        circulo = Circle((200+x0,200-y0),50)
        circulo.fill = None
        circulo.draw(v)
        angulo0 += 30
      
def aproximarPI(n):
    acumulador = 0
    n += 1
    for denominador in range(1,n):
        acumulador += 1/(denominador**2)
    pi = sqrt(acumulador*6)
    return pi
    
def calcularNumerosDivisiblesEntre29():
    acumulador = 0
    for num in range(1015,9977,29):
        acumulador += 1
    return acumulador

def calcularOperaciones():
    acumulador = 1
    for n in range(1,10):
        print(acumulador,"*",8,"+",n,"=",(acumulador*8+n))
        acumulador *= 10 
        acumulador += (n+1)
    acumulador = 1
    print("""
    """)
    for _ in range(1,10):
        print(acumulador,"*",acumulador,"=",(acumulador**2))
        acumulador *= 10
        acumulador += 1

def main():

    funcion = int(input("""Teclea el numero de funcion:
    
        Circulos y rectangulos : 1
        Estrella 5 picos : 2
        Espiral cuadrada : 3
        Circulos : 4
        Aproximacion de PI : 5
        Numeros de 4 digitos divisibles entre 29 : 6
        Calcular operaciones : 7
        Salir : 0"""))
    
    while funcion != 0:
        if funcion == 1 or funcion == 2 or funcion == 3 or funcion == 4:
            v = Window("VentanaDeDibujo",400,400)
            if funcion == 1:
                dibujarCirculosYRectangulos(v)
            elif funcion == 2:
                dibujarEstrella(v)
            elif funcion == 3:
                dibujarEspiral(v)
            elif funcion == 4:
                dibujarCirculos(v)
        elif funcion == 5:
            n = int(input("Teclea n"))
            pi = aproximarPI(n)
            print("PI = ", pi)
        elif funcion == 6:
            num = calcularNumerosDivisiblesEntre29()
            print("Cantidad de numeros de 4 digitos que son divisibles entre 29: ", num)
        elif funcion == 7:
            calcularOperaciones()
        
        print("-"*50)
        funcion = int(input("""Teclea el numero de funcion:
    
        Circulos y rectangulos : 1
        Estrella 5 picos : 2
        Espiral cuadrada : 3
        Circulos : 4
        Aproximacion de PI : 5
        Numeros de 4 digitos divisibles entre 29 : 6
        Calcular operaciones : 7
        Salir : 0"""))




main()