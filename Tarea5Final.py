#encoding: utf-8
#autor: Allan Sánchez Iparrazar
#Menú de funciones

from Graphics import *
from math import *
#-----------------------------------------------------
def dibujarHorizonte (v):
    x = 0
    y = x
    x1 = 400
    y1 = x1
    r = 200
    for i in range (0,20,1) :
        cuadrado = Rectangle((x,y),(x1,y1))
        circulo = Circle ((200,200),(r))
        circulo.fill = (None)
        cuadrado.fill = (None)
#Dibuja las figuras
        cuadrado.draw(v)
        circulo.draw(v)     
#Reduce valores para las siguientes figuras
        r = r-10
        x1 = x1-10
        y1 = x1
        x = x+10
        y = x
#----------------------------------------------------
def dibujarEstrella(v):
    t = Arrow((100,200),0)
    t.draw(v)
    t.penDown()
    for i in range (0,5,1) :
#Avanza la flecha y cambia de ángulo        
        t.forward(160)
        t.rotate(144)
#----------------------------------------------------

def dibujarSerpiente (v) :
    t = Arrow ((200,200),0)
    t.draw(v)
    t.penDown()
    avanza = 10
    while avanza <= 410 :
        t.forward (avanza)
        t.rotate(90)
        t.forward (avanza)
        t.rotate (90)
        
        avanza = avanza + 10
        
#----------------------------------------------

def dibujarFlor (v):

    for angulo in range(0,360,30):
        radianes = angulo*pi/180
        #x = 200*cos(radianes)
        #y = 200*sin(radianes)
        #circulo = Circle((200+x,200 - y),(100))
        circulo = Circle((200+(50*cos(radians(angulo))),200-(50*sin(radians(angulo)))),50)
        circulo.fill = (None)
        circulo.draw(v)
#----------------------------------------------

def calcularPi(n):
    pi=0
    #n = n+1
    for x in range (1,n+1,1):
        pi = pi+(1/(x*x))
    pi = sqrt((pi*6))
    return pi
#--------------------------------------------------------
        
def divisibleEntre29():

    numerosDivisibles = 0
    
    for x in range(1000,10000):
        if x%29==0:
            numerosDivisibles += 1
    return numerosDivisibles
    
#-------------------------------------------------------    

def mostrarCadena2():
    x = 1
    for i in range(10):
        acumulador=(x*x)
        x=(x*10)+1
        print(acumulador)

#---------------------------------------------------------

def mostrarCadena():
    x=1
    a=0
    for y in range(1,10):
        a=(a*10)+y
        af=(a*8)+x
        x=x+1 
        print (af)

#----------------------------------------------
def main():
    v = Window("Dibujo",400,400) 
    menu = 0 #int (input("Ingresa Figura"))

    while menu != 9 :
        menu = int(input("Elige una nueva opción, si deseas ver el menú presiona teclea 0"))
        
        if menu == 1 :
            dibujarHorizonte (v) 
        elif menu == 2 : 
            dibujarEstrella (v)
        elif menu == 3 :
            dibujarSerpiente (v)
        elif menu == 4 : 
            dibujarFlor(v)
#-------Acaban los dibujos----------

        elif menu == 5 :
            n = int(input("Escribe el numero de aproximaciones a pi que quieres que calcule")) 
            pi = calcularPi (n)
            print ("El valor aproximado de pi es:",pi)
            
        elif menu == 6 :
            
            numerosDivisibles = divisibleEntre29()
            print ("El total de números divisibles entre 29 son:",numerosDivisibles)
            
        elif menu == 7 :
            mostrarCadena()
            print ("***** Segunda cadena *****")
            mostrarCadena2() 
            
            
        elif menu == 8 :
            print("****** Adiós ******")
            menu = 9
            
            
        elif menu == 0 : 
            print ("1.Horizonte\n2.Estrella\n3.Serpiente\n4.Flor\n5.Aproximar pi\n6.Divisibles entre 29\n7.Cadenas de numeros\n8.Salir")
            
        



main()