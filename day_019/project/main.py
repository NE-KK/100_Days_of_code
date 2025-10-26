from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green",  "blue", "purple"]
y_position = [-125, -75, -25, 25, 75, 125]

all_turtles = []
is_race_on = False

screen = Screen()
screen.title("Turtle race")
screen.setup(height=400, width=500)

user_bet = screen.textinput(title="Place a bet", prompt="Choose the that will win!")

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.setposition(-200, y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        distance = randint(0, 10)
        turtle.forward(distance)

        if turtle.xcor() >= 200:
            winner = turtle.color()
            is_race_on = False

print(f"The winner is {winner[0]}!")

screen.exitonclick()