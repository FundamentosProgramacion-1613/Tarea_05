#encoding: UTF-8
#author: Edgar Eduardo Alvarado Duran    A01371424
#Tarea 5

from Graphics import*
from math import*

def dibujarAbstracto(a):
    x=0
    y=x
    x1=400
    y1=x1
    r=200
    for i in range (0,20,1):
        cuadrado= Rectangle((x,y),(x1,y1))
        circulo= Circle ((200,200),(r))
        circulo.fill= (None)
        cuadrado.fill= (None)
        cuadrado.draw(v)
        circulo.draw(v)
        r= r-10
        x1= x1-10
        y1= x1
        x= x+10
        y= x
        
def dibujarEstrella(a):
    t= Arrow((100,200),0)
    t.draw(a)
    t.penDown()
    for i in range(0,5):
        t.forward(160)
        t.rotate(144)
        
def dibujarFigura3(v):
    t= Arrow((200,200),0)
    t.draw(v)
    t.penDown()
    avanzar= 10
    while avanzar<= 410:
        t.forward(avanzar)
        t.rotate(90)
        t.forward(avanzar)
        t.rotate(90)
        avanzar= avanzar+10
        
def dibujarCirculos(v):
    for angulo in range(0,360,30):
        radianes= (angulo)*(pi/180)
        circulo= Circle((200+(50*cos(radians(angulo))),200-(50*sin(radians(angulo)))),50)
        circulo.draw(v) 
        
def calcularMiniMenu():
    numDibujo=0
    while numDibujo!=5:
        numDibujo= int(input("Ingresa el dibujo que quieras \n (1) Abstracto \n (2) Estrella \n (3) Figura 3 \n (4) Circulos"))
        if numDibujo== 1:
            v=Window("Tortugas",600,600)
            dibujarAbstracto(v)
        if numDibujo== 2:
            v=Window("Tortugas",600,600)
            dibujarEstrella(v)
        if numDibujo== 3:
            v=Window("Tortugas",600,600)
            dibujarFigura3(v)
        if numDibujo== 4:
            v=Window("Tortugas",500,500)
            dibujarCirculos(v)
        if numDibujo<=0 or numDibujo>=5:
            print ("Por favor intrduzca un numero del 1 al 4")

def calcularPI(a):
    PI=0
    a=a+1
    for b in range (1,a):
        PI=PI+(1/(b*b))
    PI=PI*6
    PI=sqrt(PI)
    print ("De acuerdo a la formula pi vale:",PI) 
    
def calcularDigitos():
    a=0
    sumatorias=0
    for c in range(1000,10000):
        if a%29==0:
            sumatorias +=1
    print (sumatorias,"digitos son divisibles entre 29")
    
def calcularValores():
    a=1
    for b in range(20):
        añadiendo=(a*a)
        a=(a*10)+1
        print(añadiendo)
        
def calcularValores2():
    a=1
    b=0
    for c in range(1,20):
        b=(b*10)+c
        operacion=(b*8)+a
        a=a+1 
        print (operacion)

def main():
    numProblema= 0
    while numProblema!= 5:
        numProblema= int(input("Seleccione el problema \n (1) Dibujos \n (2) calcularPi \n (3) calcularDigitos \n (4) calcularValores \n (5) Salir del Programa")) 
        if numProblema==1:
            calcularMiniMenu()
        if numProblema==2:
            a=int(input("Introduce valor de pi"))
            calcularPI(a)
        if numProblema==3:
            calcularDigitos()
        if numProblema==4:
            calcularValores()
            calcularValores2()
        if numProblema<=0 or numProblema>=6:
            print ("Seleccione un valor del 1 al 5")
        if numProblema== 5:
            print ("Gracias")
       
main()