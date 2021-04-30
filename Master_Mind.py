
from turtle import *
from random import *
import pickle
import os.path

#Declaracion de listas a usar
#Generacion de colores random
colors = ["r","y","g","b","o","p"]
lista = []
codebreaker = []
#Si declaraba lista vacia a la hora de comparar, error decia que guess estaba fuera de rango
guess = ["-","-","-","-"]

#Variable global puntaje con pickle
if os.path.isfile("puntuaciones_mm") == False:
    puntuaciones = []
    archivo = open("puntuaciones_mm", "wb")
    pickle.dump(puntuaciones, archivo)
    archivo.close()    
else:
    archivo = open("puntuaciones_mm", "rb")
    puntuaciones = pickle.load(archivo)
    archivo.close()

#Recibir intento de usuario
def ingresar_intento(color1,color2,color3,color4,intento_guess):
    nuevo_intento = [color1,color2,color3,color4]
    intento_guess.append(nuevo_intento)
    return intento_guess

#Comparacion de colores lineas en misma posicion
def comparar(lista,codebreaker):
    for n in range(len(codebreaker)):
        if lista[n] == codebreaker[n]:
            guess[n] = "X"

    #Comparacion de lista random con cada linea de codebreaker
    for x in range(len(codebreaker)):
        for y in range(len(codebreaker)):
            if guess[x] != "X":
                if codebreaker[x] == lista[y]:
                    guess[x] = "O"
            else:
                break
    print("Su intento es: ", codebreaker)
    print("╔═  .*.  ══════╗")
    print("      Pistas ")
    print("╚══════  .*.  ═╝")
    print(guess)
    print()
    return guess

def evaluacion_guess(guess):
    #Ciclo de intentos, evaluando
    guess = ["-","-","-","-"]
    suma_puntaje=0
    evaluation = True

    
    while evaluation:
        #Conteo para puntaje 
        suma_puntaje += 1
        
        if guess == ["X","X","X","X"]:
            print("╔═  .*. ═══════════════╗")
            print("     Codigo acertado    ")
            print(" Puntos logrados: ", suma_puntaje)
            print("╚═══════════════  .*. ═╝")
            print()
            evaluation = False
            #para guardar el puntaje 
            puntaje = [player,suma_puntaje]
            #guardar mi lista de puntajes
            puntuaciones.append(puntaje)
            #Archivo en pickle
            archivo = open("puntuaciones_mm", "wb")
            pickle.dump(puntuaciones, archivo)
            archivo.close()
            graphic(lista)
            print("")
                
        else:
            print("╔═  .*. ═══════════╗")
            print(" Intentos agotados ")
            print ("      (x_x)")
            print("╚═══════════  .*. ═╝")
            print("")
            #incluyendo para que agregue puntaje en caso que agote intentos
            #para guardar el puntaje 
            puntaje = [player,suma_puntaje]
            #guardar mi lista de puntajes
            puntuaciones.append(puntaje)
            #Archivo en pickle
            archivo = open("puntuaciones_mm", "wb")
            pickle.dump(puntuaciones, archivo)
            archivo.close()
            evaluation = False

    
#Borrar todos los elementos de la variable que recibe los intentos, por que no puede sobre escribir en elementos ya establecidos
def limpiar_codebreaker(codebreaker):
    codebreaker.clear()

#Ordenar lista de posiciones
def sort(puntuaciones2):
    l = len(puntuaciones2)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (puntuaciones2[j][1] > puntuaciones2[j + 1][1]):
                tempo = puntuaciones2[j]
                puntuaciones2[j]= puntuaciones2[j + 1]
                puntuaciones2[j + 1]= tempo
        print (i+1,"Jugador: ", puntuaciones2[i][0], "Puntos:", puntuaciones2[i][1])
    print()
    return puntuaciones2
      

#Funcion Turtle solo se muesta cuando el usuario acierta
def graphic(lista):
    #Setup Turtle  Python 
    setup(550,400)
    tl = Turtle()
    tl.up()
    tl.speed(0)
    #Muestra de colores en Pantalla Turtle
    position=-150
    i = 0
    while i < (len(lista)):
        tl.goto(position,0)
        
        if lista[i] == "r" or lista[i] == "R":
            tl.color("red")
        elif lista[i] == "y" or lista[i] == "Y":
            tl.color("yellow")
        elif lista[i] == "g" or lista[i] == "G":
            tl.color("green")
        elif lista[i] == "b" or lista[i] == "B":
            tl.color("blue")
        elif lista[i] == "o" or lista[i] == "O":
            tl.color("orange")
        elif lista[i] == "p" or lista[i] == "P":
            tl.color("purple")
        else:
            continue
        
        tl.begin_fill()
        tl.circle(50)
        tl.end_fill()
        position += 110
        i += 1
        tl.up()


## Menu del programa:
running = True

while running:
    print("Menu:")
    print("1. Iniciar juego")
    print("2. Ver instrucciones del juego")
    print("3. Ver las mejores 10 puntuaciones")
    print("4. Borrar puntuaciones")
    print("5. Creditos")
    print("6. Salir")
    select_option = input("Seleccione una opcion: ")
    print()

    if select_option == '1':

        count = 0
  
        player = input("Introduzca el nombre: ")
        print("╔═  .*. ══════════════════════╗")
        print(" Colores aleatorios Generados") 
        print("╚══════════════════════  .*. ═╝")
        print()
        lista = choices(colors,k=4)
        

        #PENDIENTE generaciòn de colores ocultado ****************************************
        print("Aleatorio",lista)
        print("contador",count)
        print()
            
        if count < 2:

            print( "Escriba la letra del color que desea elegir: ")
            print("Colores: (Red = r) (Yellow = y) (Green = g) ")
            print("         (Blue = b) (Orange = o) (Purple = p)")
            print()
            color1 = input("Ingrese color #1 ")
            color2 = input("Ingrese color #2 ")
            color3 = input("Ingrese color #3 ")
            color4 = input("Ingrese color #4 ")
            print()
            
            #llamada a funcion Se registraba lista con lista interna [[]], tuve que sustituir variable original por la misma solo con el indice cero,
            #probé varias formas de ingresar datos a lista vacia
            nuevo_ingreso = ingresar_intento(color1,color2,color3,color4,codebreaker)
            codebreaker = codebreaker[0]
            #llamada a funcion de comparacion
            comparar(lista,codebreaker)
            count += 1
            limpiar_codebreaker(codebreaker)
            evaluacion_guess(guess)

               

    elif select_option == '2':
        print("╔═  .*. ═══════════════╗")
        print(" Instrucciones del Juego")
        print("╚═══════════════  .*. ═╝")
        print("Mastermind consiste en un juego de mesa de dos jugadores en el cual un jugador")
        print("crea un codigo de 4 colores (codemaker) y el otro jugador intenta adivinar")
        print("este codigo (codebreaker) basado en pistas que el codemaker debe darle al codebreaker")
        print("Usted tendra una pista en cada intento")
        print(" ∗ Una “x” indica que el color de la adivinanza es correcto y esta en la posicion correcta.")
        print(" ∗ Una “o” indica que en la adivinanza se utilizo un color correcto pero esta en la posicion incorrecta.")
        print(" ∗ Un  “-” indica que hay un elemento de la adivinanza que no esta en el codigo secreto.")
        print()


    elif select_option == '3':
        print("╔═  .*.  ═══════════════╗")
        print(" P U N T U A C I O N E S ")
        print("╚═══════════════  .*.  ═╝")
        
        archivo2 = open("puntuaciones_mm", "rb")
        puntuaciones2 = pickle.load(archivo2)        
        
        if puntuaciones2 == []:
            print ("No hay puntuaciones guardadas")
            print()

        else:
            #funcion de ordenar puntuaciones        
            sort(puntuaciones2)
        
                

    elif select_option == '4':
        print ("¿Desea borrar las puntuaciones?")
        print ("Si, digite el numero 1")
        print ("No, digite el numero 2")
        
        running = True
        while running:
                select = input("Seleccione una opcion: ")
                if select == '1':
                    puntuaciones = []
                    archivo = open("puntuaciones_mm", "wb")
                    pickle.dump(puntuaciones, archivo)
                    archivo.close()
                    print ("Historial de puntuaciones eliminado")
                    print ()

                    break
                break
                if select == '2':
                    break
        print()
    
    elif select_option == '5':
        print("♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪")
        print("   Desarrollado por: Cindy Mora y Diana Alvarez")
        print("   Gracias Especiales a: Andrés Morales(Profesor)")
        print("           Universidad CENFOTEC 2021             ")
        print("♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪")
        print()

    elif select_option == '6':
        running = False

print("Game Over!")



