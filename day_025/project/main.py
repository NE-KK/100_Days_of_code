import turtle
from turtle import Turtle, Screen

tk = Turtle()
screen = Screen()

screen.title("50 States of the USA")
screen.setup(height=491, width=725)
screen.bgpic("blank_states_img.gif")

tk.hideturtle()
screen.mainloop()
