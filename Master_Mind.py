from random import *

colors = ["Rojo","Amarillo","Verde","Azul","Anaranjado","Morado" ]
lista = choices(colors,k=4)
print()
print("╔═  .*. ══════════╗")
print(" Colores aleatorios")
print("╚══════════  .*. ═╝")
print(lista)
print()

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
        print("Iniciar Juego en desarrollo! Proximamente!")
        print()

    elif select_option == '2':
        print()
        print("╔═  .*. ═══════════════╗")
        print(" Instrucciones del Juego")
        print("╚═══════════════  .*. ═╝")
        print("Mastermind consiste en un juego de mesa de dos jugadores en el cual un jugador")
        print("crea un codigo de 4 colores (codemaker) y el otro jugador intenta adivinar")
        print("este codigo (codebreaker) basado en pistas que el codemaker debe darle al code-")
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



