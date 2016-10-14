#encoding: UTF-8
#Autor: Jesus Perea
#Tarea 5

from Graphics import *
    
def dibujarCirculos(v):               #dibuja cirucilos
    for i in range (0,200,10):
        circulos = Circle((200,200),i)
        circulos.fill = None
        circulos.draw(v)
                
def dibujarCuadrados(v):            #Dibuja cuadrados
    linea1 = Line((190,210),(210,210))
    linea1.draw(v)
    linea2 = Line((210,210),(210,190))
    linea2.draw(v)
    linea3 = Line((210,190),(190,190))
    linea3.draw(v)
    linea4 = Line((190,190),(190,210))
    linea4.draw(v)
    for i in range (0,400,10):
        linea1 = Line((190-i,210+i),(210+i,210+i))
        linea1.draw(v)
        linea2 = Line((210+i,210+i),(210+i,190-i))
        linea2.draw(v)
        linea3 = Line((210+i,190-i),(190-i,190-i))
        linea3.draw(v)
        linea4 = Line((190-i,190-i),(190-i,210+i))
        linea4.draw(v)

def dibujarEstrella(v,t):               #dibuja la estrella
    t.draw(v)
    t.penDown()
    t.forward(200)
    t.penUp()
    t.rotate(150)
    for i in range (0,4):
        t.penDown()
        t.forward(190)
        t.penUp()
        t.rotate(140)

def dibujarLaberinto(v,t):              #Dibuja el laberinto
    t.draw(v)
    for i in range (0,400,10):
        t.penDown()
        t.forward(i)
        t.rotate(90)

def dibujar12Circulos(v):           #Dibuja los 12 circulos
    circulo = Circle((210,200),20)
    circulo.fill=None
    circulo.draw(v)
    for i in range (0,11):
        circulo = Circle((210,200+i),20)
        circulo.fill= None
        circulo.draw(v) 
        
def definirDivisibleEntre29():          #calcula si es divisible entre 29
    print("Numeros divisibles entre 29")
    for i in range (0,1000,1):
        numero = i % 29
        if numero == 0:
            print(i)        

def calcularAproximacionDePi(n):     #Calcula la aproximacion de pi
    n2 = 0
    for i in range (1,n+1):
        n1 = ((1)/(i**2))
        n2 = n2 + n1
    n2 = n2 * 6
    n2 = n2 ** (1/2)
    print(n2)
    
def calcularOperaciones():
    for i in range (1,8):
        for j in range (1,i):
            print(j)
        
                                                             
def main():
    opcion = 0
    while ( opcion != 8):
        opcion = int(input("Teclea tu opcion: \n 1.Cuadrados y Circulos \n 2.Flecha \n 3. Laberinto \n 4.Circulos \n 5.Aproximacion de Pi \n 6.Divisible entre 29 \n 7.Operaciones "))
        if opcion == 1:
            v = Window(400,400)
            t = Arrow((100,190),0)
            f = Arrow((200,200),0)
            dibujarCirculos(v)    
            dibujarCuadrados(v)  
        elif opcion == 2:
            w = Window(400,400)
            dibujarEstrella(w,t)      
        elif opcion == 3:
            e = Window(400,400)
            dibujarLaberinto(e,f)
        elif opcion == 4:
            r = Window(400,400)
            dibujar12Circulos(r)
        elif opcion == 5:
            definirDivisibleEntre29()                 
        elif opcion == 6:
            numero = int(input("Teclea el numero finito para calcular PI"))
            calcularAproximacionDePi(numero)
        elif opcion == 7:
            calcularOperaciones()
        else:   
            print("Adios")
                        
    
    

    
main()