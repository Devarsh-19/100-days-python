from turtle import Screen, Turtle
import turtle


screen = Screen()
screen.bgcolor("black")

screen.setup(width=800, height=600)
screen.title("PONG")


paddle = Turtle()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.pu()
paddle.goto(350, 0)


screen.exitonclick()