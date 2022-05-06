from secrets import choice
from tkinter import Y
from turtle import Turtle, Screen
import turtle

from click import prompt

screen = Screen()
screen.setup(width = 500, height = 400)
#screen.title("TURTLE RACE", prompt= "Enter color of you turtle:  ")
colors = ["red", "yellow", "blue", "green", "black"]
Ycor = [-70, -40, -10, 20, 50]

for i in range(0,5):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.pu()
    tim.goto(x = -230, y= Ycor[i])




screen.exitonclick()