# 100 Days of code by Angela Yu
# Day 18 - Challenge 1 - Turtle draw a square

from turtle import Turtle

my_turtle = Turtle()
my_turtle.pendown()

for _ in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

my_turtle.screen.mainloop()
