#encoding: UTF-8
#Autor: Adrian Tellez
#Programas con fo
 
from math import *
from Graphics import *
import time

#Ejercicio 1(a).- Una funcion que dibuje cuadrados y circulos
def dibujarCuadrados(): 
    v = Window ("Cuadrados y Circulos", 400, 400)
    a=0
    b=400
    c=200
    for f in range(20):
        a += 10
        b-=10
        c-=10
        cuadrado = Rectangle((a, a), (b, b))
        cuadrado.fill = None
        cuadrado.draw(v)
        circulo = Circle((200,200), c)
        circulo.fill = None
        circulo.draw(v)
    time.sleep(10)
    v.close()

#Ejercicio 1(b).- Una funcion que dibuje un estrella con 5 picos
def dibujarEstrella():
    v = Window("Estrella",400,400)
    tortuga = Arrow ((100,230),0)
    tortuga.penDown()
    tortuga.draw(v)
    for i in range (0,5):
        tortuga.pen.color = Color ("blue")
        tortuga.forward(200)
        tortuga.rotate(144)
    tortuga.penUp()
    time.sleep(10)
    v.close()
  
#Ejercicio 1(c).- Una funcion que dibuje una figura 
def dibujarEspiral():
    v = Window ("Espiral",400,400)
    tortuga = Arrow ((205,200),0)
    tortuga.penDown()
    tortuga.draw(v)
    for i in range (0,401,5):
        tortuga.forward(i)
        tortuga.rotate(90)
    tortuga.penUp()
    time.sleep(10)
    v.close()
 
#Ejercicio 1(d).- Una funcion que dibuje circulos   
def dibujarCirculos():  
    v = Window ("Circulos", 400, 400)
    for i in range(0, 360, 30) :
        y = sin(radians(i))
        x = cos(radians(i))
        circulo = Circle((200+(75*x),200+(75*y)),75)
        circulo.fill = None      
        circulo.draw(v)
    time.sleep(10)
    v.close()
 
# Ejercicio 2.- Sacar un valor aprox. de Pi
def calcularPi(n):
    p = 0
    for s in range (1, n+1):
        p = p + (1/(s**2))
        pi = sqrt(6*p)
    return pi  
    
#Ejercicio 3.- CCalcular la cantidad de numeros divisibles entre 29 con 4 digitos
def calcularMultiplos():
    global t
    t = 0
    for s in range (1000,10000):
        if s%29== 0:
            t += 1
    return t     

#Ejercicio 4.- Calcular e imprimir operaciones
def calcularOperaciones():
    ac = 1
    c = 1
    d = 1
    for c in range (1,10):
        b = ac * 8 + c
        c += 1
        ac = (ac * 10) +c
        print (ac, "* 8 +", (c-1),"=", b)
        
    for s in range (9):
        f = d * d
        print (d," * ", d, " = ", f)
        d = d * 10 + 1

#Funcion Main :)
def main():
    opcion =0
    while opcion!=8 :
        opcion = int(input("Elige tu opcion:\n1.-Dibujar cuadrados y circulos\n2.-Dibujar estrella\n3.-Dibujar espiral\n4.-Dibujar circulos\n5.-Calcular Pi\n6.- Numeros de 4 digitos divisibles entre 29\n7.- Operaciones\n8.-Salir "))
        if opcion == 1:
            dibujarCuadrados()
        elif opcion == 2:
            dibujarEstrella()
        elif opcion == 3:
            dibujarEspiral()
        elif opcion == 4:
            dibujarCirculos()
        elif opcion== 5:
            n = int(input("Da el valor de n (limite)"))
            calcularPi(n)
            print ("El valor de pi con limite en",n,"es:",pi)
        elif opcion == 6:
            calcularMultiplos()
            print("La cantidad de numeros divisibles entre 29 con 4 digitos es:",t)
        elif opcion == 7:
            calcularOperaciones()
        elif opcion == 8:
            print ("Adios\nBuen dia\n:)")
        else:
            print ("Elige una opcion correcta")
    
main()
