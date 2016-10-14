#enconding: UTF-8
#Hector David Hernandez Rodriguez
#A01374009
#Tarea 5

from Graphics import*
from math import*

def dibujarFiguras (v):
    a = 0
    b = a
    a1 = 400
    b1 = a1
    r = 200
    for x in range (0,20,1) :
        cuadrado = Rectangle((a,b),(a1,b1))
        circulo = Circle ((200,200),(r))
        circulo.fill = (None)
        cuadrado.fill = (None)
        cuadrado.draw(v)
        circulo.draw(v)     

        r = r-10
        a1 -= 10
        b1 = a1
        a += 10
        b = a

def dibujarFigura(v):
    t = Arrow((100,200),0)
    t.draw(v)
    t.penDown()
    for i in range (0,5) :
       
        t.forward(160)
        t.rotate(144)

def dibujarCaracol (v) :
    t = Arrow ((200,200),0)
    t.draw(v)
    t.penDown()
    dezplazamiento = 10
    while dezplazamiento <= 410 :
        t.forward (dezplazamiento)
        t.rotate(90)
        t.forward (dezplazamiento)
        t.rotate (90)
        dezplazamiento += 10
        

def dibujarMandala (v):

    for angulo in range(0,360,30):
        radianes = angulo*pi/180
        circulo = Circle((200+(50*cos(radians(angulo))),200-(50*sin(radians(angulo)))),50)
        circulo.fill = (None)
        circulo.draw(v)
        
def calcularPi(n):
    pi=0
    n=n+1
    for x in range (1,n):
        pi=pi+(1/(x*x))
    pi=pi*6
    pi=sqrt(pi)
    print ("el valor de pi segun la formula es",pi) 
    
def Division():
    x=0
    contador=0
    for x in range(1000,10000):
        if x%29==0:
            contador +=1
    print (contador,"numeros de 4 digitos son divisibles entre 29")
    
def chain2():
    x=1
    for y in range(20):
        acumulador=(x*x)
        x=(x*10)+1
        print(acumulador)
def chain():
    x=1
    a=0
    for y in range(1,20):
        a=(a*10)+y
        af=(a*8)+x
        x=x+1 
        print (af)

def menu(m):
    v = Window("Figuras",500,500) 
    while m!=0:
        if m==1:
            dibujarFiguras(v) 
        elif m == 2 : 
            dibujarFigura(v)
        elif m==3:
            dibujarCaracol(v)
        elif m==4: 
            dibujarMandala(v)
        elif m==5:
            n=int(input("Dame un valor para calcular pi"))
            calcularPi(n)
        elif m==6:
            Division()
        elif m==7:
            chain()
        elif m==8:
            chain2()
        else:
            print("No aplica")    
        m=int(input("Elige una nueva opcion, 1 FIGURA1, 2 ESTRELLA, 3 CARACOL, 4 MANDALA, 5 APROXIMAR,Pi, 6 DIVISION, 7 CADENA 1, 8 CADENA 2, 0 SALIR. "))
def main(): 
    m=int(input("selecciona la actividad "))
    menu(m)



main()