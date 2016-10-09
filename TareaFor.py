# encoding: UTF-8
# Autor: Rodrigo García López, A01373670
# Descripcion: Programa con varias funciones donde se aplican ciclos for

from Graphics import *
from math import cos, radians, sin

#Función que dibuja una serie de círculos inscritos en cuadrados
def dibujarA():
    ventana = Window("Dibujo A: Círculos y Cuadrados", 400, 400)
    for i in range(0, 200, 10):
        cuadrado = Rectangle((0+i,0+i),(400-i,400-i))
        cuadrado.fill = None
        cuadrado.draw(ventana)
        circulo = Circle((200,200), 0+i)
        circulo.fill = None
        circulo.draw(ventana)

#Función que dibuja una estrella de 5 picos        
def dibujarB():
    ventana = Window("Dibujo B: Estrella de 5 picos", 400, 400)
    lapiz = Arrow ((175, 250), 0)
    lapiz.draw(ventana)
    lapiz.penDown()
    PICOS = 5 #Número de picos de la estrella
    CUERDA = 50 #Longitud de la bas de la estrella
    alfa = 360/PICOS 
    beta = (180-alfa)/2
    phi = 180 - 2*alfa
    h = CUERDA/(2*cos(radians(alfa)))
    for i in range(0,PICOS):
        lapiz.forward(CUERDA)
        lapiz.rotate(-2*beta)
        lapiz.forward(h)
        lapiz.rotate(phi-180)
        lapiz.forward(h)
        lapiz.rotate(-2*beta)
        lapiz.forward(CUERDA)
        lapiz.rotate(alfa)
    
#Función que dibuja una greca de cuadrados    
def dibujarC():
    ventana = Window("Dibujo C: Greca", 400, 400)
    lapiz = Arrow((200, 200), 0)
    lapiz.draw(ventana)
    lapiz.penDown()
    for i in range (10, 400-30, 10):
        lapiz.forward(i)
        lapiz.rotate(90)
        lapiz.forward(i)
        lapiz.rotate(90)
    lapiz.forward(370)

#Función que dibuja un aro de círculos
def dibujarD():
    ventana = Window("Dibujo D: Círculos", 400, 400)
    RADIO = 50
    CIRCULOS = 12
    for i in range (0, 360, int(360/CIRCULOS)):
        x1Cor = 200 + RADIO*cos(radians(i)) #Coordenada en x del punto 1
        y1Cor = 200 - RADIO*sin(radians(i)) #Coordenada en y del punto 1
        circulo = Circle((x1Cor, y1Cor), RADIO)
        circulo.fill = None
        circulo.draw(ventana)
        
#Función que aproxima el valor de pi
def aproximarPi(n):
    suma = 0 #acumulador
    for i in range (1, n+1):
        suma += (1/i**2)
    aproximacion = (6*suma)**(1/2)
    return aproximacion

#Función que calcula el total de números de 4 dígitos divisibles entre 29
def calcular29():
    contador = 0
    for i in range (1000, 10000, 1):
        if i%29 == 0:
            contador += 1
    return contador

#Función que imprime dos conjuntos de operaciones
def imprimirOperaciones():
    a = 0
    multiplicando = 0
    for i in range(0,9):
        a += 10**i
        multiplicando += a
        print(multiplicando, "* 8 +", i+1, "=", multiplicando*8+i+1)  
    print("\n")   
    multiplicando = 0
    for i in range(0,9):
        multiplicando += 10**i
        print(multiplicando, "*", multiplicando, "=", multiplicando**2)
            
def main():
    opcion = 1
    while opcion != 0:
        opciones_cadena = ("Introduce el número de la tarea que deseas ejecutar: \n 0. Salir del programa\n1. Ver dibujo A: Círculos y Cuadrados \n2. Ver dibujo B: Estrella\n3. Ver dibujo C: Greca \n4. Ver dibujo D: Círculos \n5. Aproximar PI \n6. Obtener el total de números de 4 dígitos divisibles entre 29 \n7. Imprimir Operaciones")
        opcion = int(input(opciones_cadena))
        if opcion == 0:
            print("Adios")
        elif opcion ==1:
            dibujarA()
        elif opcion == 2:
            dibujarB()
        elif opcion == 3:
            dibujarC()
        elif opcion == 4:
            dibujarD()
        elif opcion == 5:
            ultimo = int(input("Introduce el valor del último divisor para la aproximación"))
            print("El valor de pi es aproximadadmente ",aproximarPi(ultimo))
        elif opcion == 6:
            print("El total de números de 4 dígitos divisibles entre 29 es ", calcular29())
        elif opcion == 7:
            imprimirOperaciones()
        else:
            print("Opción no válida")
main()