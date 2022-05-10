import time
from tracemalloc import start
from turtle import Turtle, Screen, exitonclick

screen = Screen()

screen.screensize(600,400)
screen.title("SNAKE GAME")
screen.bgcolor('black')
screen.tracer(0)

start_pos = [(0, 0), (-20, 0), (-40, 0 )]

seg = []

for i in start_pos:
    t = Turtle('square')
    t.color('white')
    t.pu()
    t.goto(i)
    seg.append(t)
    
is_gameOn = True
while is_gameOn:
    screen.update()
    time.sleep(0.1)
    
    for n in range(len(seg)-1 ,0, -1):
        new_x = seg[n - 1].xcor()
        new_y = seg[n - 1].ycor()
        seg[n].goto(new_x, new_y)
               

    
screen.exitonclick()