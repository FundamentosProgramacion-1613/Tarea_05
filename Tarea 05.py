#encoding: UTF-8
#Oscar Zuñiga Lara
#A01654827

import pygame
import sys
import time
import turtle
import math

ANCHO = 400
ALTO = 400
BLANCO = (255,255,255)
Negro = (0, 0, 0)
tamano =400

def dibujarA():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
#//////////////////////////////////////
        ventana.fill(BLANCO)
#///////DIBUJOS/////////////////////
        tamano = 20
        for tamano in range(0,400,20):
            pygame.draw.rect(ventana, Negro, ((ANCHO - tamano) // 2, (ALTO - tamano) // 2, tamano, tamano), 1)
        for tamano in range(0,190,10):
            pygame.draw.circle(ventana, Negro, (ANCHO // 2, ALTO // 2), 190 - tamano, 1)
        #/////////////////////////////////////
        pygame.display.flip()
        reloj.tick(40)
    pygame.quit()


def dibujarD():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
#///////////////////////////////////////////////////////////////////////
        ventana.fill(BLANCO)
#///////DIBUJOS/////////////////////////////////////////////////////////
        ubicacion = 1
        for angulo in range(0,361,30):
            a = 0
            x = ANCHO//2
            y = ALTO//2
            for a in range(0,360,30):
                radian = a * math.pi // 180
                x = int(60 * math.cos(radian))
                y = int(60 * math.sin(radian))
                print(x)
                print(y)
                pygame.draw.circle(ventana, Negro, (200 + x , 200 + y ),60, 1)

                #////////////////////////////////////////////////////////////////////////
        pygame.display.flip()
        reloj.tick(30)
    pygame.quit()


def dibujarB():
    import turtle
    largo = 200
    picos = 5
    turtle.setup(400,400)
    angulo = 180/picos
    for picos in range(0,picos,1):
        turtle.fd(largo)
        turtle.rt(angulo + 180)
    turtle.exitonclick()


def dibujarC():
    import turtle
    turtle.setup(400, 400)
    for a in range(10, 350, 5):
        turtle.fd(a)
        turtle.lt(90)
    turtle.fd(a)
    turtle.lt(90)
    turtle.exitonclick()

def calcular3():
    a = 1015
    x = 0
    for a in range(1000,9999,29):
        x = x + 1
    print(x)

def ejercicio4():
    b = 0
    e = 1
    f = 0
    e = 0
    r = 4
    for d in range(1,10,1):
        e = e * 10 + d
        r = e * 8  + d
        print("%d * 8 + %d = %d"%(e,d,r))
    for a in range(0,10,1):
        b = 10 ** a + b
        c = b * b
        print(b, "*", b ,"=" , c)



def calcularPI():
    serie = 1
    for divisor in range(2,1000,1):
        serie = 1/(divisor**2) + serie
        pi = (6 *serie)**.5
    print(pi)

def main():
    aas = True
    while aas == True:
        usuario = (input("Inserte el ejercicio que quiere ejecutar: "))
        if usuario == "1":
            usuario1 = (input("Inserte el inciso que quiere ejecutar(a,b,c,d):"))
            if usuario1 == "a":
                dibujarA()
            elif usuario1 == "b":
                dibujarB()
            elif usuario1 == "c":
                dibujarC()
            elif usuario1 == "d":
                dibujarD()
            else:
                print("Inserte un dato valido")
        elif usuario == "2":
            calcularPI()
        elif usuario == "3":
            calcular3()
        elif usuario == "4":
            ejercicio4()
        else:
            print("Inserte un dato valido")
main()
