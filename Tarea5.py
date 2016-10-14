#encoding: UTF-8
#Autor: Luis Martín Barbosa Galindo A01337485
#Tarea_FOR
from Graphics import *
from math import *
def dibujarCirculosYRectangulos(figura):
    v = Window("Circulos y Rectangulos",400,400)
    cen = 0
    b = 400
    r = 200
    for l in range(0,20):
        cen+=10
        b-=10
        r-=10
        rect = Rectangle((cen,cen),(b,b))
        rect.fill = None
        rect.draw(v)
        circ = Circle((200,200),r)
        circ.fill = None
        circ.draw(v)
        
def dibujarLaberinto(figura):
    v = Window("Laberinto",400,400)
    t = Arrow ((100,150),0)
    t.penDown()
    t.draw(v)
    for laberinto in range (0,390,10):
        t.forward(laberinto)
        t.rotate(90)
        
def dibujarFlorCirculos(figura):
    v = Window("Circulitos",400,400)
    for ángulo in range (0,360,30):
        circulito = Circle((200+(50*cos(radians(ángulo))),200-(50*cos(radians(ángulo)))),50)
        circulito.fill = None
        circulito.draw(v)
        
def aproximacionPi(nr):
    f = 0
    #denominador
    for d in range (1,nr+1):
        f += 1/(d**2)
    pi = sqrt(6*f)
    return pi
    
def divisionDeCuatroDigitos(n):
    veces = 0
    num = n/29
    while num in range (1000,n):
        if n%29 == 0:
            veces = veces+1
            return veces
    return veces
    
def hacerOperacionCíclica():
    num1=0
    num2=0
    for cons in range(1,10):
        num1 = (num1*10)+cons
        op = (num1*8)+cons
        print (num1,"*8+",cons,"=",op)
    for cons in range (9):
        num2 = (num2*10) + 1
        op2 = (num2*num2)
        print(num2,"*",num2,"=",op2)

def main():
    print("1.-Figuras geometricas")
    print("2.-Aproximación a pi")
    print("3.-Números de 4 digitos divisibles en 29")
    print("4.-Operaciones ciclicas")
    funcionamiento= int(input("¿Qué función es la que deborealizar?"))
    if funcionamiento == 1 :
        print("1.-Circulos y rectangulos")
        print("2.-Estrella")
        print("3.-Laberinto")
        print("4.-Circulos maniacos")
        figura = int(input("¿Qué figura quieres?"))
        if figura == 1:
            dibujarCirculosYRectangulos(figura)
        elif figura == 2:
            dibujarEstrella(figura)
        elif figura == 3:
            dibujarLaberinto(figura)
        elif figura == 4:
            dibujarFlorCirculos(figura)
    elif funcionamiento == 2 :
        nr = int(input("¿Cuantas veces quieres repetir este proceso?"))
        pi = aproximacionPi(nr)
        print (pi)
    elif funcionamiento == 3:
        n = int(input("Dame un número mayor a 1000 o un número de 4 digitos"))
        if n > 1000 :
            division = divisionDeCuatroDigitos(n)
            print(veces)
        else:
            print("No puedo hacer eso")
    elif funcionamiento == 4:
        operacion = hacerOperacionCíclica()
main()