#########################################################################
# Name: Misha Belle
# Date: 6/4/24
# File: main.py
# Desc: uses turtle module to create lil race of rainbow turtles.
#########################################################################

from turtle import Turtle, Screen
import random
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def add_turtles():
    turtles = []
    for color in colors:
        turtle = Turtle(shape='turtle')
        turtle.color(color)
        turtles.append(turtle)
    return turtles


def bring_to_start(turtles):
    space = 30
    y_position = -100
    for turtle in turtles:
        turtle.penup()
        y_position += space
        turtle.goto(x=-230, y=y_position)


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
racing_turtles = add_turtles()
bring_to_start(racing_turtles)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in racing_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost. the {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
