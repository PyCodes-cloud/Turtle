# Creating Square Using Turtle

import turtle

cursor = turtle.Turtle()
# Setting shape of turtle cursor
cursor.shape("circle")
# Setting color of turtle cursor
cursor.color("blue")

# Movement for drawing a square using for loop!
for n in range(4):
    # It moves pointer forward 
    turtle.forward(100)
    # rotates pointer to left by 90 degrees!
    turtle.left(90)
