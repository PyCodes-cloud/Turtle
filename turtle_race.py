from random import randint, choice
from turtle import Turtle, Screen, textinput

positions = [300, 200, 100, 0, -100, -200, -300]
colors = ['red', 'green', 'purple', 'blue', 'pink', 'yellow', 'orange']

screen = Screen()
screen.bgcolor('black')

turtles = []

for number in range(0, 7):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.shapesize(2.0)
    new_turtle.penup()
    new_turtle.color(colors[number])
    new_turtle.goto(-330, positions[number])
    turtles.append(new_turtle)

bet = textinput('Bet', 'Enter any color:')
pen = Turtle()
pen.color('white')
pen.penup()

FONT = ('Arial', 16, 'normal')

game_on = True

while game_on:
    choice(turtles).forward(randint(10,20))

    for turt in turtles:
        if turt.xcor() >= 320:
            game_on = False
            winner = turt.color()[0]

            if bet == winner:
                pen.write(f"You're right!\n {winner} wins the race", font = FONT)

            else:
                pen.write(f"You're wrong!\n {winner} wins the race", font = FONT)

        else:
            pass

screen.exitonclick()
