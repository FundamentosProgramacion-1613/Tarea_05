#Oswaldo Morales Rodriguez A01378566
#Dibujar lo que el usuario pida de las 4 opciones
#Encoding: UTF-8

from Graphics import*
from math import*

def funcionCuadrado():
    radio=200
    x1=10
    x2=390
    y1=10 
    y2=390
    win=Window("Cuadro y Circulo", 400, 400)

    for i  in range (0,19):
        cuadrado = Rectangle((x1,y1), (x2, y2))
        cuadrado.fill = Color(r=0,g=0,b=0,a=0)
        cuadrado.draw(win)
        x1=x1+10
        x2=x2-10
        y1=y1+10
        y2=y2-10   
    
    for e in range (0,20):
        circulo = Circle((200,200), radio)
        circulo.fill = Color(r=0,g=0,b=0,a=0)
        circulo.draw(win)
        radio=radio-10
  
def funcionEstrella():
    win=Window("Estrella", 400, 400)
    tortuga=Arrow((100,200),0)
    tortuga.draw(win)   
    tortuga.penDown()   
    for e in range (0,5):
        tortuga.forward(200)
        tortuga.rotate(144)

def funcionLaberinto():
    win=Window("Laberinto", 400, 400)
    distancia=10
    tortuga=Arrow((200,200),0)
    tortuga.draw(win)   
    tortuga.penDown()   
    for e in range (0,74):
        tortuga.forward(distancia)
        tortuga.rotate(90)
        distancia+=5

def funcionCirculos():
    win=Window("Circulos", 400, 400)
    for i in range (0,360, 30):
        x=cos(i)
        y=sin(i)
        circulo = Circle((x,y), 50)
        circulo.fill = Color(r=0,g=0,b=0,a=0)
        circulo.draw(win)
        

def funcionPi(numero):
    suma=0
    for i in range (1,numero):
        division=(1/(i)**2)
        suma=suma+division
    
    multiplicacion=6*suma
    pi=(multiplicacion**0.5)    
    return pi
    
def funcionDivisibles():
    for i in range (1000,10000):
        divisor=i%29
        if divisor==0:
            resultado=(i/29)
            print(i,"/29=",resultado)
            
    
def funcionSumas():
    contador=1
    contador2=1
    contador3=1
    for i in range (9):
        resultado=contador*contador
        print(contador,"x",contador,"=",resultado)
        resultado2=contador3*8+contador2 
        print(contador3,"x 8 +",contador2,"=",resultado2)  
        contador=(contador*10)+1
        contador2=contador2+1
        contador3=contador3+contador

def main():
    opcion=0
    while opcion!=8:
        opcion=int(input("1. Dibujar cuadros y circulos \n2. Dibujar estrella \n3. Dibujar laberinto \n4. Dibujar circulos \n5. Calculo Pi \n6. Divisibles 29 \n7.Sumas \n8. Salir."))
        if opcion==1:
            funcionCuadrado()
        elif opcion==2:
            funcionEstrella()
        elif opcion==3:
            funcionLaberinto()
        elif opcion==4:
            funcionCirculos()
        elif opcion==5:
            numero=int(input("Numero de veces"))
            resultado=funcionPi(numero)
            print("Valor aproximado de Pi",resultado)
        elif opcion==6:
            funcionDivisibles()
        elif opcion==7:
            funcionSumas()
        elif opcion==8:
            print("ADIOS")
        else:
            print("Escoja un numero existente")
            
main()