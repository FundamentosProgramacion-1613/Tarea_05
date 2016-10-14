#Encoding: UTF-8
#By Diego Perez
#Codigo Multi Usos

from Graphics import *
from Myro import *
from math import *
#/////////////////FIGURA 1///////////////////
def dibujarFigura_1(v):
    
    #Definir Tamanio
    size = 10
    #Ciclo 
    while (size < 390):
    #Coords. del Cuadrado
        rectangle0 = Rectangle(Point(200-size,200-size),Point(200+size,200+size))
        rectangle0.fill = None
    #Dibujar en Ventana    
        rectangle0.draw(v)
    #Dibujar el Circulo    
        if (size/10)%2 == 0:
            circle = Circle((200,200),size/2)
            circle.fill = None
            circle.draw(v)
    #Aumentar Tamano 
        size+=10
        
#/////////////////FIGURA 2///////////////////
def dibujarFigura_2(v):
    #CREAR TORTUGA
    t = Arrow((100,200),0)  
    
    #DEFINIR REPETICIONES
    repeticiones = 0
    
    #DIBUJAR ESTRELLA
    while (repeticiones < 5):
        t.penDown()
        t.forward(200)
        t.rotate(144)
        t.draw(v)
        repeticiones +=1

#/////////////////FIGURA 3///////////////////
def dibujarFigura_3(v):  
   #CREAR TORTUGA 
    t = Arrow((200,200),0)  
   #DEFINIR TAMANIO INICIAL
    size = 5
   #REPETIR HASTA LLEGAR A MEDIDA FINAL
    while (size<390):
        t.penDown()
        t.forward(size)
        t.rotate(90)
        t.draw(v)
        size +=5
        
#/////////////////FIGURA 4///////////////////
def dibujarFigura_4(v):   
    angle = 0
    while (angle < 360):
        ang = pi/2 - radians(angle)
        x = 200+(30*cos(ang))
        y = 200+(30*sin(ang))
        circ0 = Circle((x,y),30)
        circ0.fill = None
        circ0.draw(v)
        angle+=30
        
#//////PI///////
def aproximarPi(n):
    num = 0
    n0 = 1
    while (n0 < n):
        num+=(1/(n0**2))
        n0 +=1
    else:
        pi = sqrt(6*num)
    return pi
    
#/////////DIVISIBLES ENTRE 29//////

def numerosDivisibles():
    num = 0
    n0 = 1000
    while(n0 < 9999):
        if (n0 % 29 == 0):
            num +=1
        n0 +=1
    return num

#//////MULTIPLICACIONES////////
def mulitiplicarNumeros():
    n = 1
    n0 = 1
    n1 = 1
    n2 = 1
    while (n < 10):
        print(n0,"* 8 +",n ,"=", (n0*8)+n)
        n +=1
        n0 = (n0*10)+n
    else:
        while(n2 < 10):
            print(n1,"*",n1,"+",n1*n1)
            n2 +=1
            n1 = n1*10+1
        
                                                                                   
def main():

    #ESCRIBIR MENU Y ENTRADA, DIBUJAR VENTANA
    print("Bienvenido al menu demo de Python")
    print ("Presione 1 para ver Figura 1")
    print ("Presione 2 para ver Figura 2")
    print ("Presione 3 para ver Figura 3")
    print ("Presione 4 para ver Figura 4")
    print ("Presione 5 para una aproximacion a PI")
    print ("Presione 6 para numeros de 4 digitos divisibles entre 29")
    print ("Presione 7 para ver tablas de multiplicaciones raras")
    print ("Presione 0 para salir")
    entrada = int(input("Ingrese un numero"))   
    v = Window("Figuras",400,400)    
    #WHILE QUE CONTROLA EL MENU
    while (entrada > 0):
        if (entrada == 1):
            v = Window("Figuras",400,400)
            dibujarFigura_1(v)
            entrada = int(input("Ingrese un numero")) 
            
        if (entrada == 2):
            v = Window("Figuras",400,400)
            dibujarFigura_2(v)
            entrada = int(input("Ingrese un numero")) 
                    
        if (entrada == 3):
            v = Window("Figuras",400,400)
            dibujarFigura_3(v)
            entrada = int(input("Ingrese un numero")) 
            
        if (entrada == 4):
            v = Window("Figuras",400,400)
            dibujarFigura_4(v)
            entrada = int(input("Ingrese un numero")) 
            
        if (entrada == 5):
            v.close()
            n = int(input("Escribe un parametro (Numero) para estimar PI"))
            pi = aproximarPi(n)
            print(pi)
            entrada = int(input("Ingrese un numero"))
            
        if (entrada == 6):
            v.close()
            num = numerosDivisibles()
            print(num,"numeros de 4 digitos son divisibles entre 29")
            entrada = int(input("Ingrese un numero"))
        
        if (entrada == 7):
            v.close()
            mulitiplicarNumeros()
            entrada = int(input("Ingrese un numero"))
        
    if (entrada == 0):
        v.close()
     
main()