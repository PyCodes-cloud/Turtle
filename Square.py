# Creating Square Using Turtle

import turtle

cursor = turtle.Turtle()
cursor.shape("circle")
cursor.color("blue")

# Movement for drawing a square using for loop!
for n in range(4):
    turtle.forward(100)
    turtle.left(90)