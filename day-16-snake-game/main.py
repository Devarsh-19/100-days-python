import imp
from turtle import Turtle, Screen, exitonclick

screen = Screen()

screen.screensize(600,400)
screen.title("SNAKE GAME")
screen.bgcolor('black')

start_pos = [(0, 0), (-20, 0), (-40, 0 )]

seg = []

for i in start_pos:
    t = Turtle('square')
    t.color('white')
    t.goto(i)
    seg.append(t)
    
is_gameOn = True

while is_gameOn:
    for x in seg:
        x.fd(20)
    
screen.exitonclick()