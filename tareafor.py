#encoding: UTF-8
#Autor: Carlos E. Carbajal Nogués
#Descripición: Programa que utiliza menús, for, y while

#Inicio
from Graphics import * #Importamos la libreria graphics
from math import*

def dibujarFiguras(): #Este programa nos dibujara los cuadrados y los circulos en una sola ventana
    win = Window("A",400,400)
    rad=0
    x=0
    posx1=0
    posy1=0
    posx2=400
    posy2=400
    for x in range(20) : #Este for se encarga de dibujar todos los circulos
        c=Circle((200,200),rad)
        c.fill=None
        c.draw(win)
        rad=rad+10
        x=x+1
    for x in range(20): #Este for se encarga de dibujar todos los rectangulos
        r=Rectangle((posx1,posy1),(posx2,posy2))
        r.fill=None
        r.draw(win)
        x=x+1
        posx1=posx1+10
        posy1=posy1+10
        posx2=posx2-10
        posy2=posy2-10
    win.close()
        
def dibujarEstrella():
    win = Window("B",400,400)
    x=0
    e=Arrow((100,200),0)
    e.penDown()
    e.pen.color=Color("yellow")
    for x in range(5):
        e.draw(win)
        e.forward(200)
        e.rotate(144)
        x=x+1

def dibujarEspiral(): #Esta funcion esta encargada de dibujar la espiral
    win = Window("C",400,400)
    x=0
    dist=10
    a=Arrow((200,200),0)
    a.penDown()
    for x in range(40): #Este for se encarga de dibujar las lineas, separandolas 10 pixeles entre si
        a.draw(win)
        a.forward(dist)
        a.rotate(90)
        a.forward(dist)
        a.rotate(90)
        dist=dist+10
        x=x+1

def dibujarMandala(): #Este funcion se encarga de dibujar la mandala
    win = Window("D",400,400)
    x=0
    posx=200
    posy=200
    for x in range(12): #Este for se encarga de 
        c=Circle((200+posx,200-posy),30)
        c.fill=None
        c.draw(win)
        posx=posx*sin(radians(30))
        posy=posy*cos(radians(30))
        x=x+1
           
def calcularPi(lim):
    x=1
    valor=0
    for x in range(1,lim+1):
        p=1/(x*x)
        valor=valor+p
        x=x+1
        print (valor)
    res=sqrt(valor*6)  
    return res

def dividirNumeros(): #Con esta 
    x=1000
    count=0
    for i in range(1000,10000):
        res1=x%29
        if  res1==0:
            #print(x)
            count=count+1
        x=x+1
    return count
        
def hacerOperaciones():
    x=1
    count=0
    for count in range(9):
        x=(x+1)
        count=count+1
        print(x)
def main():
    print("""
    Elge que accion deseas realizar:
    1. Ver figuras
    2. Saber Pi
    3. Numeros que son divisibles entre 29
    4. Ciclo de operaciones
    0. Salir
    """)
    respuesta=int(input("¿Que accion deseas realizar?"))
    while respuesta!=0:
        if respuesta==1:
            print("""
    Elige que figura quieres ver:
    1. Cuadrados y circulos
    2. Estrella
    3. Espiral
    4. Mandala
    0.Salir
            """)
            seleccion=int(input("Introduce el numero de tu eleccion"))
            while seleccion!=0:
                if seleccion==1:
                    dibujarFiguras()
                    seleccion=int(input("Que accion deseas realizar?"))
                elif seleccion==2:
                    dibujarEstrella()
                    seleccion=int(input("Que accion deseas realizar?"))
                elif seleccion==3:
                    dibujarEspiral()
                    seleccion=int(input("Que accion deseas realizar?"))
                elif seleccion==4:
                    dibujarMandala()
                    seleccion=int(input("Que accion deseas realizar?"))
                else:
                    print("Valor incorrecto")
                    seleccion=int(input("Que accion deseas realizar?"))
        
        elif respuesta==2:
            limite=int(input("¿Hasta que numero deseas realizar esta operacion?"))
            print(calcularPi(limite))
            respuesta=int(input("Selecciona otra accion"))
        elif respuesta==3:
            res2=dividirNumeros()
            print(res2)
            respuesta=int(input("Selecciona otra accion"))
        elif respuesta==4:
            hacerOperaciones()
            respuesta=int(input("Selecciona otra accion"))
        else:
            print ("Datos incorrectos")
            respuesta=int(input("Selecciona otra accion"))
main()