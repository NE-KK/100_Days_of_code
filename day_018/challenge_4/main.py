# 100 Days of code by Angela Yu
# Day 18 - Challenge 4 - Random walk

from turtle import Turtle
from random import choice

angle = [0, 90, 180, 270]
color = ["red", "green", "blue", "orange"]

my_turtle = Turtle()
my_turtle.pendown()
my_turtle.pensize(5)
my_turtle.shape("circle")
my_turtle.speed("fastest")

while True:
    my_turtle.left(choice(angle))
    my_turtle.color(choice(color))

    my_turtle.forward(20)
