import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")

# List of some colors in Turtle Module!
colors = ["cyan", "blue", "lime", "gold", "pink", "red", "dark violet", 
"orange", "purple"]

def draw_shape(num_sides):
    angle = 360 / num_sides

    for n in range(num_sides):
        t.forward(100)
        t.right(angle)

for n in range(3,11):
    t.pencolor(random.choice(colors))
    draw_shape(n)

screen.exitonclick()