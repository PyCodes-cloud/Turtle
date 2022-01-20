# Creating sequence of colored dots!
import turtle, random, colorgram
from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
screen.bgcolor('black')
screen.setup(600, 600)
pen.ht()
rows = turtle.numinput("Enter number of rows", 'Enter here:', minval=3, maxval=20)
turtle.colormode(255)

def generate_colors():
    colors = colorgram.extract('C:\Turtle\Week_One\matlab.png', 500)
    mylist = []

    for n in range(len(colors)):
        r = colors[n].rgb.r
        g = colors[n].rgb.g
        b = colors[n].rgb.b
        mylist.append((r,g,b))

    return mylist

color_list = generate_colors()

def generate_spots():
    for n in range(10):
        pen.pencolor(random.choice(color_list))
        pen.pendown()
        pen.dot(20)
        pen.penup()
        pen.goto(pen.xcor()+40, pen.ycor())

row = 1
while row <= rows:
    pen.penup()
    pen.goto(0, -200)
    pen.speed('fastest')
    n = 50*(row-1)
    pen.goto(pen.xcor()-300, pen.ycor()+n)
    pen.pendown()
    generate_spots()
    row += 1

screen.exitonclick()
