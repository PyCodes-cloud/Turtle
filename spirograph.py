import turtle
import random

p = turtle.Turtle()
p.shape("circle")

screen = turtle.Screen()

turtle.colormode(255)

def generate_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b

"""
Creating Spirograph involves many visualizations and understanding i.e. how a spirograph is actually drawn

Spirograph is drawn by drawing circles side by side tilted at some different angles continuosly 

In turtle the methods useful in this are :

turtle.circle(radius) : creates a circle of some radius r

turtle.heading() : returns the turtle's current heading

turtle.setheading() : set's the value of heading 

heading is just a number which tells about the tilt of some shape!
"""
def draw_spirograph(size_of_gap):
    for n in range(int(360 / size_of_gap)):
        p.speed("fastest")
        # generate random color
        p.color(generate_colors())
        # creates a circle
        p.circle(50)
        # updates the heading 
        # size_of_gap is the space bwtween two adjacent circle
        # size_of_gap is controlling the amount of tilt 
        p.setheading(p.heading() + size_of_gap)

draw_spirograph(8)

screen.exitonclick()
