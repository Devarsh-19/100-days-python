import imp
import time
from turtle import Turtle, Screen
from Snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.screensize(600,400)
screen.title('SNAKE GAME')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
sc = Score()
segments = []


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    #DETECT COLLISION WITH FOOD
    
    if snake.head.distance(food) < 15:
        food.refresh()
        sc.update

screen.exitonclick()