from turtle import *
from random import *



#Generacion de colores random
colors = ["r","y","g","b","o","p"]
lista = choices(colors,k=4)
print()
print("╔═  .*. ══════════════════════╗")
print(" Colores aleatorios Generados")
print("╚══════════════════════  .*. ═╝")
#PENDIENTE borrar antes de enviar entregable
print("Aleatorio",lista)
print()

'''
#Setup Turtle  Python 
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

codebreaker = []
#Si declaraba lista vacia a la hora de comparar, error decia que guess estaba fuera de rango
guess = ["0","0","0","0"]


#Recibir intento de usuario
def ingresar_intento(color1,color2,color3,color4,intento_guess):
    nuevo_intento = [color1,color2,color3,color4]
    intento_guess.append(nuevo_intento)
    return intento_guess

#Comparacion de colores lineas en misma posicion
def comparar(lista,codebreaker):
    #reiniciar variable en cada intento, ya que guardaba info de siguiente funcion
    guess = ["0","0","0","0"]
    for n in range(len(codebreaker)):
        if lista[n] == codebreaker[n]:
            print("Coincide")
            guess[n] = "X"
            print(guess[n])
    print("Lista Pistas 1",guess)

    #Comparacion de lista random con cada linea de codebreaker
    for x in range(len(codebreaker)):
        for y in range(len(codebreaker)):
            if guess[x] != "X":
                if codebreaker[x] == lista[y]:
                    guess[x] = "-"
                    print(guess[x])
            else:
                break
    print("Lista Pistas 2",guess)
    return guess



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
        evaluation = True
        count = 0
        #Ciclo de intentos, evaluando 
        while evaluation and count < 12:
            print( "Opciones de color Red = r Yellow = y Green = g Blue = b Orange = o Purple = p") 
            color1 = input("Ingrese color #1 ")
            color2 = input("Ingrese color #2 ")
            color3 = input("Ingrese color #3 ")
            color4 = input("Ingrese color #4 ")

            #Se registraba lista con lista interna [[]], tuve que sustituir variable original por la misma solo con el indice cero,
            #probé varias formas de ingresar datos a lista vacia
            nuevo_ingreso = ingresar_intento(color1,color2,color3,color4,codebreaker)
            codebreaker = codebreaker[0]
            comparar(lista,codebreaker)
            print(codebreaker)
            count += 1
            if guess == ["X","X","X","X"]:
                print("Codigo acertado")                
                evaluation = False
            print("")
        print("Intentos agotados")
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




