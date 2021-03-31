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

#Si declaraba lista vacia a la hora de comparar, error decia que guess estaba fuera de rango
guess = ["O","O","O","O"]


#BORRAR prueba de comparacion de colores para no digitar cada vez
codebreaker = ["Green","Orange","Red","Blue"]
print("Codebreaker",codebreaker)



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
        player = input("Introduzca un nombre: ")
        
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




