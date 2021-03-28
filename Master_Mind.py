from random import *
from turtle import *

#Generacion de colores random
colors = ["Red","Yellow","Green","Blue","Orange","Purple" ]
lista = choices(colors,k=4)
print()
print("╔═  .*. ══════════╗")
print(" Colores aleatorios")
print("╚══════════  .*. ═╝")
print("lista",lista)
print()



#BORRAR prueba de comparacion de colores para no digitar cada vez
codebreaker = ["Green","Orange","Red","Blue"]
print("Codebreaker",codebreaker)

#Comparacion de random con cada linea de code breaker
for x in range(4):
    for y in range(4):
        print ("lista",lista[x],"codebreaker",codebreaker[y])
        if lista[x] == codebreaker[y]:
            print("Color en fila",lista[x],codebreaker[y])
        
    
#Comparacion de colores lineas en misma posicion
for n in range(len(codebreaker)):
    if lista[n] == codebreaker[n]:
        print(codebreaker[n])
        print("Coincide")
    else:
        print(codebreaker[n])
        print("No Coincide")



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



