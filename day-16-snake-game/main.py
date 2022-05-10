import time
from turtle import Turtle, Screen
from Snake import Snake

screen = Screen()
screen.screensize(600,400)
screen.title('SNAKE GAME')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()

segments = []


gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()