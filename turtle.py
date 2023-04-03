import turtle
turtle.bgcolor("black")

squary = turtle.Turtle()
screen = turtle.Screen()
squary.speed(20)
squary.pencolor("red")
for i in range(4000):
    squary.forward(i)
    squary.left(91)

