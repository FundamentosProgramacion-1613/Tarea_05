#encoding: UTF-8
#Karla Valeria Alcántara Duarte
#Ciclos

from Graphics import *
from math import *

def dibujarCirculoCuadrado():
    v = Window("Formas",400,400)
    for circu in range (0,201,10):
        circulo = Circle((200,200),circu)
        circulo.fill = None 
        circulo.draw(v)
    x = 0
    for cuad in range (0,200,10):
        cuadrado = Line((200+x,200+x),(200+x,200-x),(200-x,200-x),(200-x,200+x),(200+x,200+x))
        x = x+10
        cuadrado.draw(v)
        
def dibujarEstrella():
    v = Window("Formas",400,400)
    t = Arrow((100,200),0)
    t.penDown()
    t.draw(v)
    for e in range (5):
        t.pen.color = Color("Blue")
        t.forward(200)
        t.rotate(144)
   
   
def dibujarLaberinto():
    v = Window("Formas",400,400)
    t = Arrow((200,200),0)
    t.penDown()
    t.draw(v)
    for lab in range(0,390,5):
        t.forward(lab)
        t.rotate(90)
        
def dibujarMandala():
    v = Window("Formas",400,400)
    ang =int(360/12)
    for angulo in range (0, 360, ang):
        circulo = Circle((200+(50*cos(radians(angulo))),200-(50*sin(radians(angulo)))),50)
        circulo.fill = None 
        circulo.draw(v)
        
def calcularPI(n):
    fraccion = 0
    for x in range (1,n+1):
        fraccion += 1/(x**2)
    pi = sqrt(6*fraccion)
    return pi
    

def calcularDivisibles29():
    total = 0
    for digitos in range(1000,10000):
        if digitos%29==0:
            total = total+1
    return total 
        
        
def hacerOperacion1(): 
    valorI=0
    for i in range(1,10):
        valorI =(valorI*10)+i 
        operacion=(valorI*8)+i 
        print ("%d*8+%d=%d"%(valorI,i,operacion)) 

def hacerOperacion2():
    numero = 0
    for a in range (9):
        numero = (numero*10)+1
        operacion = (numero*numero)
        print ("%d*%d=%d"%(numero,numero,operacion))
        
        
       
def main():
    opciones= int(input("¿Que quieres hacer?:\n1-Dibujos\n2-Formulas"))
    while opciones>0 and opciones<3:
        if opciones==1:
            dibujos = int(input("1.Cuadrados y circulos \n2.Estrella \n3.Laberinto \n4.Mandala"))
            while dibujos>0 and dibujos<5:
                if dibujos==1:
                    dibujarCirculoCuadrado()
            
                elif dibujos==2:
                    dibujarEstrella()
            
                elif dibujos==3:
                    dibujarLaberinto()
            
                elif dibujos==4:
                    dibujarMandala()
                
                dibujos = int(input("1.Cuadrados y circulos \n2.Estrella\n3.Laberinto \n4.Mandala"))
            
        elif opciones==2:
            operaciones = int(input("1.Aproximacion de Pi \n2.Numeros de 4 digitos divisibles entre 29 \n3.Cadenas suma y multiplicacion"))
            while operaciones>0 and operaciones<4:
                if operaciones==1:
                    n = int(input("¿Cual es el ultimo divisor?"))
                    calcularPI(n)
                    print("El valor es:",calcularPI(n))
                
            
                if operaciones==2:
                    print("Hay %d numeros de 4 digitos divisibles entre 29"%(calcularDivisibles29()))
                    
                elif operaciones==3:
                    hacerOperacion1()
                    hacerOperacion2()
                    
                operaciones = int(input("1.Aproximacion de Pi \n2.Numeros de 4 digitos divisibles entre 29 \n3.Cadenas suma y multiplicacion"))
            
            
        
        opciones= int(input("Que quieres hacer?:\n1-Dibujos\n2-Formulas"))
    
main()