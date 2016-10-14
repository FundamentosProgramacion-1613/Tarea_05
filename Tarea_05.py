#encoding: UTF-8
#Autor: Ian González Pámanes
from Graphics import *

def dibujarCircle():
    ventana  = Window("Ventana", 400, 400)
    for i in range (400, 0, -20):
        circulo = Circle((200,200),(i/2))
        circulo.fill = None
        circulo.draw(ventana)
        rectangulo = Rectangle(((400 - i/2) , (400 - i/2)),((0+i/2),(0+i/2)))
        rectangulo.fill = None
        rectangulo.draw(ventana)
        
def dibujarEspiral():
    ventana  = Window("Ventana", 400, 400)
    turtle = Arrow((200,200),0)
    turtle.draw(ventana)
    turtle.penDown()
    for i in range (10, 400, 10):
        turtle.forward(i)
        turtle.rotate(90)
        turtle.forward(i)
        turtle.rotate(90)
        
def aproximarPi(x):
    temp = 0
    for i in range (1,x):
        temp = temp + 1/(i**2)
        
    return (6*temp)**.5        
        
def calcularDivision():
    temp = 0
    for i in range (1000,9999):
        if i % 29 == 0:
            temp = temp + 1
            
    return temp
    
def calcularCadenas():
    pot = 0
    num = 0
    for i in range (1,10):
        pot = (pot*10) + 1
        num = pot + num
        print (num, "*", 8, "+", i, "=", (num*8+i))
    
    pot = 0
    for i in range (1,10):
        pot = pot*10 + 1
        print (pot, "*", pot, "=", (pot*pot))

def main():
    opcion = 0
    while opcion != 6:
        print ("1. Dibujar Circulo, 2. Dibujar Espiral, 3. Aproximar Pi, 4. Calcular Division, 5. Calcular Cadenas, 6. Salir")
        opcion = int(input("Ingrese la opcion que desee"))
        if opcion == 1:
            dibujarCircle()
        elif opcion == 2:
            dibujarEspiral()
        elif opcion == 3:
            factores = int(input("Ingrese el numero de factores"))
            print (aproximarPi(factores))
        elif opcion == 4:
            print (calcularDivision())
        elif opcion == 5:
            calcularCadenas()
        elif opcion == 6:
            print ("Adios")
        else:
            print ("opcion no valida")
    
main()    