import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=600, height=400)


user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, orange, green, yellow, black, blue): ")


colors = ["red", "orange", "green", "blue", "yellow", "black"]
turtles = []

y_positions = [-100, -60, -20, 20, 60, 100]

for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_positions[index])
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost. The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()