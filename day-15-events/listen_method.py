from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def right():
    tim.setheading(0)
    tim.fd(30)    
    

def left():
    tim.setheading(180)
    tim.fd(30)
    

def up():
    tim.setheading(90)
    tim.fd(30)
    

def down():
    tim.setheading(270)
    tim.fd(30)

screen.listen()
screen.onkeypress(key="Right", fun=right)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Up", fun=up)
screen.onkey(key="Down", fun=down)
screen.exitonclick()
