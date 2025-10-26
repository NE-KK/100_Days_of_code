# 100 Days of code by Angela Yu
# Day 18 - Challenge 2 - Draw a dashed line

from turtle import Turtle

my_turtle = Turtle()

for _ in range(10):
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)

my_turtle.screen.mainloop()
