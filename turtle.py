#Setup Turtle  
setup(550,400)
tl = Turtle()
tl.up()
tl.speed(0)
tl.hideturtle()


#Muestra de colores en Pantalla Turtle
position=-100
i = 0

while i < (len(lista)):
    tl.goto(position,0)
    tl.color(lista[i])
    tl.begin_fill()
    tl.circle(50)
    tl.end_fill()
    position += 100
    i += 1
    tl.up()