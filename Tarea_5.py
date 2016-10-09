#encoding: UTF-8
#Lenin Silva Gutiérrez A01373214
#Posee 4 programas diferentes con un menú para seleccionar entre estos

from Graphics import *
from math import cos,sin,radians,sqrt

#Programa 1: Dibujos en Graphics
def dibujarCuadros_Circulos(): #dibuja cuadros y círculos con una separación de 10 pixeles
    v=Window("Cuadros y Círculos",400,400)
    for i in range(10,200,10):
        #Coordenadas del punto 1 del rectángulo; dependen de la variable del loop 'i'
        x1=200-i 
        y1=200-i
        #Coordenadas del punto 2 del rectángulo; dependen de la variable del loop 'i'
        x2=200+i
        y2=200+i
        #Define y dibuja el rectángulo para las coordenadas obtenidas
        rectangulo=Rectangle((x1,y1),(x2,y2))
        rectangulo.fill=None
        rectangulo.draw(v)
        #Define y dibuja el círculo
        circulo=Circle((200,200),i)#El radio depende de la variable 'i' del loop
        circulo.fill=None
        circulo.draw(v)

def dibujarEstrella():
    v=Window("Estrella",400,400)
    t=Arrow((75,150),0)
    t.draw(v)
    t.penDown()
    for j in range(5): #repite el loop 5 veces
        t.forward(250) #Avanza 250 pixeles
        t.rotate(216) #Rota 216 grados para formar el triángulo de la punta de la estrella
        
def dibujarLaberinto():
    v=Window("Laberinto",400,400)
    t=Arrow((200,200),0)
    t.draw(v)
    t.penDown()
    
    for k in range(10,375,5): #Avanza de 5 en cinco para que la separación sea de 10 pixeles
        t.forward(k) #La distancia que recorre depende de la variable del loop 'k'
        t.rotate(90)
        
def dibujarMandala():
    v=Window("Mandala",400,400)
    for g in range(0,360,30): #Avanza cada 30 grados porque son 12 círculos y 360/12=30. 
        #El centro del círculo depende de la variable del loop 'g'
        #El radio para todos los círculos es constante
        circulo=Circle((200+(75*cos(radians(g))),200-(75*sin(radians(g)))),75)
        circulo.fill=None
        circulo.draw(v)
        
#Programa 2: aproximar pi según el límite establecido por el usuario
def aproximarPi(n):
    serie=0.0
    for i in range(1,n+1): #Se considera el valor de n en la serie
        serie+=1/(i**2)
    pi=sqrt(6*serie) 
    return pi #regresa la aproximación de pi

#Programa 3: calcula los numeros de 4 dígitos que son divisibles entre 29
def calcularDiv29():
    contador=0
    for i in range(1000,10000):#Empieza en 1000 y acaba en 9999
        if i%29==0: #Si el residuo de la variable del loop entre 29 es cero, el contador aumenta en 1
            contador+=1              
    return contador #regresa el contador
    
#Programa 4: genera cadenas de multiplicaciones con sumas
def generarCadena1(): #Genera la siguiente cadena: '1*8+1=9, 12*8+2=98,123*8+3=987,...,123456789*8+9=987654321
    valor_inicial=0
    for i in range(1,10):
        #Los valores dependen de la variable del loop 'i'
        valor_inicial=(valor_inicial*10)+i #Genera el primer número de la cadena
        resultado=(valor_inicial*8)+i #Calcula el resultado
        print ("%d*8+%d=%d"%(valor_inicial,i,resultado)) #Imprime la multipliación y resultado para cada caso
        
def generarCadena2(): #Genera la siguiente cadena: '1*1=1, 11*11=121,...,111111111*111111111=12345678987654321
    valor=0
    for j in range(9):#se repite 9 veces
        #El valor no depende de la variable del loop 'j'
        valor=(valor*10)+1
        print("%d*%d=%d"%(valor,valor,valor*valor))


def main():
    #Muestra al usuario las opciones de programa y lee su elección
    menu=int(input("¿Qué programa quieres? 1-Dibujos, 2-Aproximación Pi, 3-Divisibles entre 29, 4-Cadenas"))
    
    #En tanto la elección se encuentre entre las posibilidades [1,2,3,4], el programa se ejecuta
    while menu>0 and menu<5:
        if menu==1: #Ejecuta el programa 1: Dibujos
        
            #El usuario escoge entre las 4 opciones de dibujos
            dibujo=int(input("¿Qué dibujo quieres? 1-Círculos y cuadrados, 2-Estrella, 3-Laberinto, 4-Mandala"))
            while dibujo>0 and dibujo<5:
                #Según la elección, se hace el dibujo en Graphics
                if dibujo==1:
                    dibujarCuadros_Circulos()
                elif dibujo==2:
                    dibujarEstrella()
                elif dibujo==3:
                    dibujarLaberinto()
                else:
                    dibujarMandala()
                
                #Pregunta nuevamente el dibujo que se desea mostrar
                #Así, el programa se ejecuta hasta que el usuario escoge un valor diferente a los aceptados
                dibujo=int(input("1-Círculos y cuadrados, 2-Estrella, 3-Laberinto, 4-Mandala"))
            #Si se escoge un valor diferente a [1,2,3,4], se regresa al menú inicial
            
        elif menu==2: #Ejecuta el programa 2
            #Lee el valor del último divisor a poner en la función 'aproximarPi()'
            n=int(input("Valor del último divisor"))
            
            while n>0: #Así se pueden probar distintos valores de 'n' sin regresar al menú
                print ("La aproximación de pi es: %.6f"%aproximarPi(n))
                n=int(input("Valor del último divisor"))
            
            print ("Valor igual o menor a 0; se regresará al menú inicial")
            print ("")
            #Si se escribe un valor menor a 1, se regresa al menú inicial                  
               
        elif menu==3: #Ejecuta el programa 3
            
            numeros_div_29=calcularDiv29()#Llama a la función y almacena el valor que regresa
            print ("Hay %d números de 4 dígitos divisibles entre 29"%numeros_div_29) #Imprime el resultado
            print ("")
            #Se regresa al menú inicial
                
        else: #Ejecuta el programa 4
            generarCadena1()
            print ("")
            generarCadena2()
            print ("")
            #Se regresa al menú inicial
            
        #Lee nuevamente la elección de programa del usuario
        #Si la entrada no pertenece a [1,2,3,4], el programa finaliza    
        menu=int(input("1-Dibujos,2-Aproximación Pi, 3-Divisibles entre 29, 4-Cadenas"))
    
    print ("Programa finalizado")           

main()        














                    