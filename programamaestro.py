#encoding: UTF-8
#Autor: José Javier Rodríguez Mota
#Descripción: Diferentes funciones y figuras a través de un menú

#Importamos las librerías que requerimos para el ejercicio
from Graphics import *
from math import * 

#Inicio

#Opción 1
def crearCirculoRectangulo(v,separacion):
    
    #Iniciamos el loop
    for radio in range(0,200,separacion):
        rectangulo=Rectangle((200-radio,200-radio),(200+radio,200+radio))
        rectangulo.fill= None
        circulo=Circle((200,200),radio)
        circulo.fill=None
        rectangulo.draw(v)
        circulo.draw(v)

#Opción 2
def crearMaze(v,t,separacion):
    
    #Establecemos los valores iniciales de nuestra flecha
    t.draw(v)
    t.penDown()
    salto=separacion/2
    
    #Iniciamos el loop
    for longitud in range (10,375,5):
        t.forward(longitud)
        t.rotate(90)
    
    #Dejamos de escribir
    t.penUp()

#Opción 3
def crearEstrella(v,t):

    #Establecemos los valores iniciales de nuestra flecha
    t.draw(v)
    t.rotate(180)
    t.forward(100)
    t.rotate(180)
    t.penDown()
    t.pen.color=Color("blue")
    
    #Iniciamos el loop
    for vueltas in range (5):
        t.forward(200)
        t.rotate(144)
    
    #Dejamos de escribir
    t.penUp()    

#Opción 4
def crearMandala(v):
    
    #Definimos el número de cículos que queremos (podría ser un input)
    numero=int(360/12)
    
    #Iniciamos nuestro rango
    for ang in range(0,360,numero):
        rad=ang*pi/180
        x=50*cos(rad)
        y=50*sin(rad)
        
        #Establecemos el centro del círculo
        circulo=Circle((200+x,200+y),50)
        circulo.fill=None
        circulo.draw(v)

#Opción 5
def calcularPi(limite):
    
    #Definimos nuestro contador
    contador=0
    
    #Iniciamos la serie
    for termino in range(1,(limite+1)):
        contador+=1/(pow(termino,2))
    
    #Terminamos los cálculos
    pI=sqrt(6*contador)
    return pI                                  

#Opción 6
def dividirEntre29():
    
    #Definimos nuestro contador y nuestro almacén de información
    contador=0
    numeros=""
    
    #Iniciamos a probar los números de cuatro dígitos
    for num in range (1000,10000):
        
        #Establecemos nuestra condición
        if (num%29==0):
            contador+=1
            
            #Convertimos los números en cadenas
            numeros=numeros+","+str(num)
    
    #Hacemos la cadena final        
    numeros="Los números de cuatro dígitos divisibles entre 29 son "+str(contador)+"y estos son:\n"+numeros                 
    return contador                           

#Opción 7
def hacerCiclo():

    #Definimos nuestra constante y nuestra variable de multiplicacion
    constante=8
    multiplicacion=1
    
    #Iniciamos el primer ciclo de operaciones
    for numero in range(1,10):
        if numero!=1:
            multiplicacion*=10
            multiplicacion+=numero
        resultado=multiplicacion*constante+numero   
        print("%d * %d + %d = %d"%(multiplicacion,constante,numero,resultado))
    
    #Reestablecemos el contador de multiplicación
    multiplicacion=1
    
    #Iniciamos el segundo ciclo de operaciones
    for numero in range(9):
        multiplicacion+=pow(10,numero)
        resultado=pow(multiplicacion,2)
        print("%d * %d = %d"%(multiplicacion,multiplicacion,resultado))       

#Definimos nuestra función inicial
def main():

    #Definimos que no hay ninguna opción seleccionada
    opcion=None
    
    #Aquí podemos cambiar la separación de los ejercicios 1 y 3
    separacion=10
    
    #Iniciamos nuestro ciclo, fin con 0
    while (opcion!=0): 
    
        #Pedimos al usuario nos diga qué hacer
        opcion=int(input("Elija una de las siguientes opciones:\n1.Crear un diseño de círculos y rectángulos\n2.Crear una estrella\n3.Crear laberinto\n4.Crear mandala de círculos\n5.Aproximar Pi\n6.Calcular números divisibles entre 29\n7.Ciclo de operaciones\n0.Salir\n"))
        
        #Definimos si la opcion necesita Graphics o no
        if (opcion==1 or opcion==2 or opcion==3 or opcion==4):
            if opcion==1:
                nombre="A"
            if opcion==2:
                nombre="B"
            if opcion==3:
                nombre="C"
            if opcion==4:
                nombre="D"            
            v=Window(nombre,400,400)
            t=Arrow((200,200),0)
        
        #Revisamos las opciones
        
        #Crear diseño de círculos y Rectángulos con cierta separación            
        if (opcion==1):
            crearCirculoRectangulo(v,separacion)
        
        #Crear estrella de cinco picos       
        if (opcion==2):
            crearEstrella(v,t)
        
        #Crear un laberinto con cierta separación        
        if (opcion==3):
            crearMaze(v,t,separacion)
        
        #Crear una serie de círculos que comparten un punto en común
        if (opcion==4):
            crearMandala(v)
        
        #Aproximar PI
        if (opcion==5):
            limite=int(input("Elige el enésimo término de la sucesión"))
            print(calcularPi(limite))
        
        #Números divisibles entre 29 que tengan cuatro dígitos
        if (opcion==6):
            print(dividirEntre29())
        
        #Ciclo de operaciones divertidas
        if (opcion==7):
            hacerCiclo()

#Ponemos a funcionar nuestro programa        
main()
#Fin    
