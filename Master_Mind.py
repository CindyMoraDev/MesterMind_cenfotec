from turtle import *
from random import *



#Generacion de colores random
colors = ["Red","Yellow","Green","Blue","Orange","Purple" ]
lista = choices(colors,k=4)
print()
print("╔═  .*. ══════════╗")
print(" Colores aleatorios")
print("╚══════════  .*. ═╝")
print("lista",lista)
print()

'''
#Setup Turtle  
setup(550,400)
tl = Turtle()
tl.up()
tl.speed(0)
tl.hideturtle()


#Muestra de colores en Pantalla Turtle
position=-150
i = 0

while i < (len(lista)):
    tl.goto(position,0)
    tl.color(lista[i])
    tl.begin_fill()
    tl.circle(50)
    tl.end_fill()
    position += 110
    i += 1
    tl.up()
''' 

#PENDIENTE Funcion agregar, me da problema que me crea una lista dentro de otra lista
codebreaker = []
#Si declaraba lista vacia a la hora de comparar, error decia que guess estaba fuera de rango
guess = ["0","0","0","0"]




#Recibir intento de usuario
def ingresar_intento(color1,color2,color3,color4,intento_guess):
    nuevo_intento = [color1,color2,color3,color4]
    intento_guess.append(nuevo_intento)
    return intento_guess

#PENDIENTE colocar evaluacion despues de ingreso de datos, ahora se reproduce antes del ingreso y no evalua
#Comparacion de colores lineas en misma posicion 
for n in range(len(codebreaker)):
    if lista[n] == codebreaker[n]:
        print("Coincide")
        guess[n] = "X"
        print(guess[n])
print("Lista",guess)

#Comparacion de lista random con cada linea de code breaker
for x in range(len(codebreaker)):
    for y in range(len(codebreaker)):
        if guess[x] != "X":
            if codebreaker[x] == lista[y]:
                guess[x] = "-"
                print(guess[x])
        else:
            break
print("Lista",guess)



## Menu del programa:
running = True

while running:
    print("Menu:")
    print("1. Iniciar Juego")
    print("2. Ver instrucciones del juego")
    print("3. Ver las mejores 10 puntuaciones")
    print("4. Borrar puntuaciones")
    print("5. Creditos")
    print("6. Salir")
    select_option = input("Seleccione una opcion: ")
    print()
    
    if select_option == '1':
        player = input("Introduzca el nombre: ")
        color1 = input("Ingrese color #1")
        color2 = input("Ingrese color #2")
        color3 = input("Ingrese color #3")
        color4 = input("Ingrese color #4")

#PENDIENTE probar si eliminando nuevo_ingreso no se registra doble lista 
        nuevo_ingreso = ingresar_intento(color1,color2,color3,color4,codebreaker)
        print(codebreaker)    
        print()

    elif select_option == '2':
        print()
        print("╔═  .*. ═══════════════╗")
        print(" Instrucciones del Juego")
        print("╚═══════════════  .*. ═╝")
        print("Mastermind consiste en un juego de mesa de dos jugadores en el cual un jugador")
        print("crea un codigo de 4 colores (codemaker) y el otro jugador intenta adivinar")
        print("este codigo (codebreaker) basado en pistas que el codemaker debe darle al code-")
        print("breaker.")
        print()

    elif select_option == '3':
        print("Ver las mejores 10 puntuaciones en desarrollo! Proximamente!")
        print()

    elif select_option == '4':
        print("Borrar puntuaciones en desarrollo! Proximamente!")
        print()
    
    elif select_option == '5':
        print("♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪")
        print("   Desarrollado por: Cindy Mora")
        print("♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪*•.¸¸.•*¨¨*•.♪ღ♪")
        print()

    elif select_option == '6':
        running = False

print("Game Over!")




