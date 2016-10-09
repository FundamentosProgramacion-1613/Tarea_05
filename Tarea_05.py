#encoding: UTF-8
#Marina Itzel Haro Hernández, A01373471
#Tarea 05 - for

from Graphics import*
from random import randint
from math import*
import time

#Ejercicio 1 inciso a)
def dibujarFigura(): 
    v = Window ("Figura", 400, 400)
    a=0
    a1=a+400
    a2=a+200
    for f in range(20):
        a+=10
        a1-=10
        a2-=10
        rectangulo = Rectangle((a, a), (a1, a1))
        rectangulo.fill = Color((randint(0,255)),(randint(0,255)),(randint(0,255)))
        rectangulo.draw(v)
        circulo = Circle((200,200), a2)
        circulo.fill = Color((randint(0,255)),(randint(0,255)),(randint(0,255)))
        circulo.draw(v)
    time.sleep(2)
    v.close()
   
#Ejercicio 1 inciso b)    
def dibujarEstrella():
    v = Window ("Estrella", 400, 400)
    t = Arrow ((100, 200), 0)
    t.draw(v)
    t.penDown()
    for e in range(1,6):
        t.pen.color = Color((randint(0,255)),(randint(0,255)),(randint(0,255)))
        t.forward(200)
        t.rotate(144)
    time.sleep(2)
    v.close()
    
#Ejercicio 1 inciso c)          
def dibujarCuadrado(): 
    v = Window ("Cuadrado", 400, 400)
    t = Arrow ((190, 200), 0)
    t.draw(v)
    t.penDown()
    t.rotate(180)
    for c in range(1, 401, 10):
        t.pen.color = Color((randint(0,255)),(randint(0,255)),(randint(0,255)))
        t.forward(c)
        t.rotate(90)
        t.forward(c)
        t.rotate(90)    
    time.sleep(2)
    v.close()
    
#Ejercicio 1 inciso d)    
def dibujarMandala():  
    v = Window ("Estrella", 400, 400)
    for m in range(0, 361, 30) :
        circulo = Circle((200+(75*cos(radians(m))),200-(75*sin(radians(m)))),75)
        circulo.fill = None
        circulo.draw(v)
    time.sleep(2)
    v.close()

#Ejercicio 2
def calcularPi(n):
    a = 0
    for i in range (1, n+1):
        a = a + (1/(i**2))
    pi = sqrt(6*a)
    return pi
    
#Ejercicio 3    
def calcularMultiplos(n):
    c = 0
    for i in range(1000, 10000):
        if (i % n) == 0 :
            c += 1
    print ("La cantidad de los números de 4 dígitos divisibles entre", n, "es:", c, "números")
    
#Ejercicio 4
def calcularListas():
    a = 1
    ac = 1
    acum=10
    print(a, "* 8 +", a, "=", (a*8+a)) 
    for b in range(2,10):
        a += acum
        ac += a
        acum *= 10
        print(ac, "* 8 +", b, "=", (ac*8+b))    
    
    print("\n")
    
    a = 1
    ac = 10 
    print (a ,"*", a, "=", a*a)
    for e in range(8):
        a += ac
        ac *= 10
        print(a ,"*", a, "=", a*a) 
                  
    
def main():
    opcion = 0
    while opcion != 8 :
        opcion = int(input("1. Figura A\n2. Figura B\n3. Figura C\n4. Figura D\n5. Ejercicio 2\n6. Ejercicio 3\n7. Ejercicio 4\n8. Salir\n\n0. Teclea tu opción: "))
        if opcion == 1 :
            dibujarFigura()
        elif opcion == 2 :
            dibujarEstrella()
        elif opcion == 3 :
            dibujarCuadrado()
        elif opcion == 4 :
            dibujarMandala()
        elif opcion == 5 :
            print("\n")
            valor = int(input("Coloca el valor de n"))
            pi = calcularPi(valor)
            print('La aproximación del valor de pi según el valor de " n=', valor, '" es: ', pi) 
        elif opcion == 6 :
            print("\n")
            calcularMultiplos(29)
        elif opcion == 7 :
            print("\n")
            calcularListas()
        elif opcion == 8 :
            print("\n")
            print("Adios")
        else:
            print("\n")
            print("Opción incorrecta")
           
    
main()
        