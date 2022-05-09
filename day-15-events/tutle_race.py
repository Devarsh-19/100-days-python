from secrets import choice
from tkinter import Y
from turtle import Turtle, Screen
import turtle


screen = Screen()
screen.setup(width = 500, height = 400)
screen.title("TURTLE RACE")
user_bet = screen.textinput(title="Make bet", prompt="Enter color of you turtle:  ")

colors = ["red", "yellow", "blue", "green", "black"]
Ycor = [-70, -40, -10, 20, 50]

all_turtles = []

for i in range(0,5):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.pu()
    tim.goto(x = -230, y= Ycor[i])
    all_turtles.append(tim)

is_raceOn = True

moves = [6, 10, 12, 9]

while is_raceOn:
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_raceOn  = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f'you win. {winner} is the winner')
            else:
                print(f'you lost.{winner} is the winnner.')
            

        turtle.fd(choice(moves))
        
        
        
screen.exitonclick()