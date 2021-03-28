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

/
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