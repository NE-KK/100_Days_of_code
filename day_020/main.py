# 100 Days of code by Angela Yu
# Day 20 - Snake Game

from turtle import Turtle, Screen
import time

screen = Screen()
screen.title("Snake game")
screen.setup(height=600, width=600)
screen.tracer(0)

snake = []

for i in range(3):
    new_segment = Turtle()
    new_segment.penup()
    new_segment.shape("square")
    new_segment.color("blue")
    new_segment.goto(i * -20, 0)

    snake.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in snake:
        segment.forward(20)

screen.exitonclick()
