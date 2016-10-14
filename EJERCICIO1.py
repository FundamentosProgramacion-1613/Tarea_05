#encoding: UTF-8
#Problema 1 tarea 5
#Marlon Brandon Velasco Pinello,A01379404

from random import randint
from Graphics import *
from math import *

###Menu 1

#funcion para hacer el laberinto
def dibujarLineas(separacion,nombre):
    #Creamos ventana dentro de la funcion para poder usar la variable v
    v=Window(nombre,400,400)
    t=Arrow((200,200),0)
    t.draw(v)
    longitud=separacion
    valorMaximo=int(200/separacion)
    #For principal para las operaciones
    for maestro in range (0,valorMaximo):
        #for secundario para las operaciones
        for i in range (1,5):
            t.penDown()
            r=randint(0,255)
            g=randint(0,255)
            b=randint(0,255)
            t.pen.color= Color(r,g,b)
            t.forward(longitud)
            t.rotate(90)
            t.penUp()
            if i == 2 or i==4:
                longitud+=separacion
    #codigo final de este ejercicio
    t.penDown()
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    t.pen.color= Color(r,g,b)
    t.forward(longitud-separacion)
    #da pausa a la pantalla hasta que se da clic en ella
    v.getMouse()
    #cierra la pantalla
    v.close()
    
#funcion para dibujar circulos
def dibujarCirculos(v,cantidad):
    valorMaximo=int(360/cantidad)
    #inicio del for principal
    for angulo in range (0,361,valorMaximo):
        rad=angulo*pi/180
        x=95*cos(rad)
        y=95*sin(rad)
        circulo = Circle((200+x,200+y),95)
        circulo.fill = None
        circulo.draw(v)
    #pausa y cierre de pantalla
    v.getMouse()
    v.close()

#funcion para los circulos y cuadrados
def dibujarCirculosCuadrados(v,separacion):
    #for para crear el efecto 
    for ancho in range (200,-1,-separacion):
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        #circulos
        circulo = Circle((200,200),ancho)
        circulo.fill = Color(r,g,b)
        circulo.draw(v)
        #rectangulos
        rectangulo=Rectangle((200-ancho,200-ancho),(200+ancho,200+ancho))
        rectangulo.fill = None
        rectangulo.draw(v)
    #pausa y cierre de pantalla
    v.getMouse()
    v.close()

#Dibujar estrella de 5 picos
def dibujarEstrella():
    #Creamos ventana dentro de la funcion para poder usar la variable v
    v=Window("Estrella",400,400)
    t=Arrow((50,250),0)
    t.draw(v)
    #for principal
    for i in range (1,6):
        t.penDown()
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        t.pen.color= Color(r,g,b)
        t.forward(300)
        t.rotate(144)
        t.penUp()
    #pausa y cierre de pantalla
    v.getMouse()
    v.close()

#funcion para dibujar estrellas de varios picos en fase BETA
def dibujarEstrellaPicos(v,picos):
    valorMaximo=int(360/picos)
    contador=0
    #print(valorMaximo)
    #primer for para generar los trazos de los puntos 1 y 2 hacia los 3,n-2 y 4,n-1 respectivamente
    for angulo in range (0,361,valorMaximo):
        contador+=1
        rad=angulo*pi/180
        x1=(150*cos(rad))+200
        y1=(150*sin(rad))+200
        rad2=(angulo+(valorMaximo*2))*pi/180
        x2=(150*cos(rad2))+200
        y2=(150*sin(rad2))+200
        rad3=(angulo+(valorMaximo*(picos-2)))*pi/180
        x3=(150*cos(rad3))+200
        y3=(150*sin(rad3))+200
        lineaA = Line((x1,y1),(x2,y2))
        lineaB = Line ((x1,y1),(x3,y3))
        lineaA.draw(v)
        lineaB.draw(v)
        if(contador==2):
            break
    #for para generar los trazos de los demas puntos de la estrella hacia los correspondientes
    for angulo in range ((2*valorMaximo),(361-valorMaximo),valorMaximo):
        rad=angulo*pi/180
        x1=(150*cos(rad))+200
        y1=(150*sin(rad))+200
        rad3=(angulo+(valorMaximo*(picos-2)))*pi/180
        x3=(150*cos(rad3))+200
        y3=(150*sin(rad3))+200
        lineaB = Line ((x1,y1),(x3,y3))
        lineaB.draw(v)
    #pausa y cierre de pantalla
    v.getMouse()
    v.close()

#Funcion para crear ventana que se recicla en varios puntos
def crearVentana(opcion,nombre):
    v=Window(nombre,400,400)
    t=Arrow((200,200),0)
    t.draw(v)
    if opcion==1 or opcion==4 or opcion==5:
        valor=v
    return valor
    
###Menu 2
def aproximacionPI(valorMaximo):
    acumulador=0
    #for principal de la funcion
    for i in range (1,valorMaximo+1):
        acumulador+=(1/(i*i))
        pi = sqrt(6*acumulador)
    return pi

###Menu 3
def calcularDivisiblesDe29():
    contador=0
    primerDivisible=0
    #for para determinar el primer numero divisible entre 29
    for i in range (1000,1031):
        if (i%29==0):
            primerDivisible=i
            #print(i)
            break
    #al encontrar el primer divisible entre 29, se detiene el for y comienza una suma de 29 en 29 para ir más rapido
    for i in range (primerDivisible,10000,29):
        contador+=1
    return contador

###Menu 4
def hacerOperacionUno(x,i):
    #simple operacion
    y=x*8+i
    return y 
    
def hacerOperacionDos(x):
    #Simple operacion 2
    y=x*x
    return y

#funcion principal
def main():
    #Hacemos el while True para que no tengamos que usar una variable desde el inicio y hasta que el usuario diga, el programa cierre
    while True:
        print("\n1. Figuras\n2. Aprox. de Pi.\n3. Divisibles de 29\n4. Series \n5. Salir\n")
        menu=int(input("Ingresa la opcion del menu a ver"))
        #condiciones para generar el menu
        if menu==1:
            print("\n\n\n1. Circulos y Cuadros\n2. Estrella\n3. Lineas\n4. Circulos \n5. Estrellas de 5 o mas picos\n6. Salir")
            print("Nota, para cerrar las pantallas, solo darle clic dentro de la pantalla('area de trabajo')")
            opcion=int(input("Ingresa la opcion a ver"))
            if opcion==1:
                nombre="Circulos y Cuadros"
                separacion=int(input("Ingresa la separacion que quieres que exista entre las lineas"))
                v=crearVentana(opcion,nombre)
                dibujarCirculosCuadrados(v,separacion)
        
            elif opcion==2:
                dibujarEstrella()
        
            elif opcion==3:
                nombre="Lineas"
                separacion=int(input("Ingresa la separacion que quieres que exista entre las lineas"))
                dibujarLineas(separacion,nombre)
        
            elif opcion==4:
                nombre="Circulos"
                cantidad=int(input("Ingresa la cantidad de circulos que deseas ver"))
                v=crearVentana(opcion,nombre)
                dibujarCirculos(v,cantidad)
        
            elif opcion==5:
                #Este problema esta en vias de desarrollo
                #Por lo cual se considera en fase BETA
                #Disculpe la tardanza de entrega, este ejercicio se complico
                #pero valia la pena, le pido que lo vea de favor
                nombre="Estrellas"
                picos=int(input("Ingresa la cantida de picos que quieres que la estrella tenga\nMinimo 5"))
                v=crearVentana(opcion,nombre)
                dibujarEstrellaPicos(v,picos)
                
            elif opcion==6:
                print("")
                
            else:
                print("opcion invalida")
                
        elif menu==2:
            valorMaximo=int(input("ingresa el valor maximo"))
            pi=aproximacionPI(valorMaximo)
            print("El valor aproximado de pi es:",pi)
        
        elif menu==3:
            totalDivisibles=calcularDivisiblesDe29()
            print("el total de numeros de 4 digitos, divisibles entre 29 son:",totalDivisibles)
        
        elif menu==4:
            x=0
            print("El el resultado de la primera operacion es:")
            for i in range (1,10):
                x=(x*10)+i
                resultado=hacerOperacionUno(x,i)
                print("%d X 8 = %d"%(x,resultado))
            x=0
            print("El el resultado de la segunda operacion es:")
            for i in range (1,10):
                x=(x*10)+1
                resultado=hacerOperacionDos(x)
                print("%d X %d = %d"%(x,x,resultado))
        
        #Si el usuario se quiere salir, el while se rompe y el programa se cierra
        elif menu==5:
            break
            
        else:
            print("Opcion Invalida vuelva a intentar")
            
main()