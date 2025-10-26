# 100 Days of code by Angela Yu
# Day 18 - Challenge 3 - Draw different shapes

from turtle import Turtle

my_turtle = Turtle()
my_turtle.pendown()

for i in range(3, 15):    
    angle = 360 / i

    for _ in range(i):
       my_turtle.forward(50)
       my_turtle.left(angle)

my_turtle.screen.mainloop()
