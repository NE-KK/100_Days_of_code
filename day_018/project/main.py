# 100 Days of code by Angela Yu
# Day 18 - Project - Hirst Painting

from random import choice
from turtle import Turtle, Screen
import colorgram
colors_list = []
PENSIZE = 60
LOWER_COLOR_THRESHOLD = 10
UPPER_COLOR_THRESHOLD = 220
colors = colorgram.extract('hirst_painting.jpg', 21)


for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b

    if red < LOWER_COLOR_THRESHOLD and green < LOWER_COLOR_THRESHOLD and blue < LOWER_COLOR_THRESHOLD:
        continue
    elif red > UPPER_COLOR_THRESHOLD and green > UPPER_COLOR_THRESHOLD and blue > UPPER_COLOR_THRESHOLD:
        continue
    else:
        single_color_list = [red, green, blue]
        colors_list.append(single_color_list)


def starting_position():
    tim.penup()
    tim.setheading(180)
    tim.forward(205)
    tim.setheading(90)
    tim.forward(205)
    tim.setheading(0)


def draw_dots():

    tim.pensize(PENSIZE)
    for _ in range(1, 6):
        for _ in range(1, 6):
            random_color = choice(colors_list)
            tim.pencolor(random_color[0], random_color[1], random_color[2])

            tim.pendown()
            tim.forward(1)
            tim.penup()
            tim.forward(99)

        tim.setheading(270)
        tim.forward(100)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


tim = Turtle()
screen = Screen()
screen.setup(height=480, width=480)
screen.colormode(255)
screen.title("Hirst Painting Generator")

starting_position()
draw_dots()

screen.mainloop()