#encoding: UTF-8
#Autor: José Javier Rodríguez Mota
#Descripción: Diferentes funciones y figuras a través de un menú
from Graphics import *
from math import * 
def crearCirculoRectangulo(v,separacion):
    for radio in range(0,200,separacion):
        rectangulo=Rectangle((200-radio,200-radio),(200+radio,200+radio))
        rectangulo.fill= None
        circulo=Circle((200,200),radio)
        circulo.fill=None
        rectangulo.draw(v)
        circulo.draw(v)
def crearMaze(v,t,separacion):
    t.draw(v)
    t.penDown()
    salto=separacion/2
    for longitud in range (10,375,5):
        t.forward(longitud)
        t.rotate(90)
    t.penUp()
#def crearEstrella(v,t):
def crearMandala(v):
    numero=int(360/12)
    for angulo in range(0,360,numero):
        radangulo=angulo*pi/180
        x=100+cos(radangulo)
        y=100+sin(radangulo)
        circulo=Circle((x,y),50)
        circulo.fill=None
        circulo.draw(v)    
                   
def main():
    v=Window("",400,400)
    separacion=10
    #crearCirculoRectangulo(v,separacion)
    t=Arrow((200,200),0)
    #crearMaze(v,t,separacion)
    #crearMandala(v)
    opcion=int(input("Elija una de las siguientes opciones:\n1.Crear un diseño de círculos y rectángulos\n2.Crear una estrella\n3.Crear laberinto\n4.Crear mandala de círculos\n5.Aproximar Pi\n6.Calcular números divisibles entre 29\n7.Ciclo de operaciones\n0.Salir\n"))
    while (opcion!=0): 
        opcion=int(input("Elija una de las siguientes opciones:\n1.Crear un diseño de círculos y rectángulos\n2.Crear una estrella\n3.Crear laberinto\n4.Crear mandala de círculos\n5.Aproximar Pi\n6.Calcular números divisibles entre 29\n7.Ciclo de operaciones\n0.Salir\n"))
        if (opcion==1):
            crearCorciñpRectangulo(v,separacion)
        #if (opcion==2):
            
        if (opcion==3):
            crearMaze(v,t,separacion)
        if (opcion==4):
            crearMandala(v)
        #if (opcion==5):
        #if (opcion==6):
        #if (opcion==7):
        
main()    