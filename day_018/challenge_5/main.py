# 100 Days of code by Angela Yu
# Day 18 - Challenge 5 - Spirograph

from turtle import Turtle, Screen
from random import choice


spiro = Turtle()
screen = Screen()
spiro.speed("fastest")

color_list = ["red", "green", "blue",  "orange"]

for _ in range(72):
    spiro.color(choice(color_list))
    spiro.circle(100)
    spiro.left(5)

screen.exitonclick()
