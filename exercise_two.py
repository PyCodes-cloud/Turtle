"""
Creating dashed lines 
"""

import turtle

cursor = turtle.Turtle()
cursor.color("yellow")

screen = turtle.Screen()
screen.bgcolor("blue")

turtle.ht()

"""
Classes and methods 

The drawing is controlled by pen and it is required to learn about method of pens!

1) pendown() : The drawing is shown on the turtle screen
2) pendown() : The drawing is not displayed on the screen 

"""

for n in range(10):
    turtle.speed(5)
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

turtle.done()
