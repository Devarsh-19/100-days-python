from turtle import Turtle, Screen

from click import prompt

screen = Screen()
screen.setup(width = 500, height = 400)
screen.title("TURTLE RACE", prompt= "Enter color of you turtle:  ")
screen.exitonclick()