#encoding: UTF-8
#Autor: Manuel Alejandro Bracho Mendoza / Matricula: A01378897
#Tarea 4: Ciclos For

from Graphics import *
from math import *
import time

def trazarPatron():
    ventana = Window ("A", 400, 400)
    punto1 = 0 
    punto2 = punto1 + 400
    radio = punto1 + 200
    for repeticiones in range (20):
        punto1+=10
        punto2-=10
        radio-=10
        rectangulo = Rectangle((punto1, punto1), (punto2, punto2))
        rectangulo.fill = None
        rectangulo.draw(ventana)
        circulo = Circle((200,200), radio)
        circulo.fill = None
        circulo.draw(ventana)
    time.sleep(3)
    ventana.close()    
        
def trazarEstrella():
    ventana = Window ("B", 400, 400)
    tortuga=Arrow((50, 225), 0)
    tortuga.color = Color("purple")
    tortuga.border = 1
    tortuga.draw(ventana)   
    tortuga.penDown()
    tortuga.pen.color = Color("blue")
    for lados in range (0, 5):
        tortuga.forward(300)
        tortuga.rotate(144)
    time.sleep(3)
    ventana.close()    
    
def trazarPatron2():
    ventana = Window ("C", 400, 400)
    tortuga = Arrow((200, 200), 180)
    tortuga.draw(ventana)
    tortuga.penDown()
    for espaciado in range (0, 390, 10):
        tortuga.forward(espaciado)
        tortuga.rotate(90)
        tortuga.forward(espaciado)
        tortuga.rotate(90)
    time.sleep(3)
    ventana.close()    
        
def trazarCirculos():
    ventana = Window("D", 400, 400)
    for coordenada in range (0, 361, 30):
        circulo = Circle((200+(50*cos(radians(coordenada))),200-(50*sin(radians(coordenada)))),50)
        circulo.fill = None
        circulo.draw(ventana)
    time.sleep(3)
    ventana.close()          
        
def calcularPi(nivelDeAproximacion):
    acomulador = 0
    for i in range (1, nivelDeAproximacion + 1):
        acomulador = acomulador + (1/(i ** 2))
    pi = sqrt(6 * acomulador)
    return pi
    
def calcularNumeros():
    contador = 0
    for f in range (1000,10000):
        if f % 29 ==0:
            print(f , "es un número divisible entre 29")
            contador+=1
    print("hay",contador, "números divicibles entre 29")
                        
def imprimirOperaciones():
    acumulador1 = 1
    acumulador2 = 1
    acumulador3 =10
    print(acumulador1, "* 8 +", acumulador1, "=", (acumulador1*8+acumulador1))
    for f in range(2,10):
        acumulador1+= acumulador3
        acumulador2+= acumulador1
        acumulador3*= 10
        print(acumulador2, "* 8 +", f, "=", (acumulador2*8+f))    
    print("\n")    
    acumulador1 = 1
    acumulador2 = 10 
    print (acumulador1 ,"*", acumulador1, "=", acumulador1*acumulador1)
    for g in range(8):
        acumulador1+= acumulador2
        acumulador2*= 10
        print(acumulador1 ,"*", acumulador1, "=", acumulador1*acumulador1) 

def main():
    opcion = 0
    while opcion != 8 :
        opcion = int(input("1. Ejercicio 1°:a\n2. Ejercicio 1°: b\n3. Ejercicio 1°:c\n4. Ejercico 1°:d\n5. Ejercicio 2°\n6 .Ejercicio 3°\n7. Ejercicio 4°\n8.Salir\n\nElije un número"))
        if opcion == 1 :
            trazarPatron()
        elif opcion == 2 :
            trazarEstrella()
        elif opcion == 3 :
            trazarPatron2()
        elif opcion == 4 :
            trazarCirculos()
        elif opcion == 5 :
            print("\n")
            nivel = int(input("nivel de aproximación?"))
            pi = calcularPi(nivel)
            print("pi=", pi) 
        elif opcion == 6 :
            calcularNumeros()
        elif opcion == 7 :
            imprimirOperaciones()
        elif opcion == 8 :
            print("hasta pronto!")
        else:
            print("teclea una opcion valida")
main() 