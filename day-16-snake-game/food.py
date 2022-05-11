from random import randint
from turtle import Turtle

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed('fastest')
        
        
    
        rand_x = randint(-280,280)
        rand_y = randint(-280,280)
        
        self.goto(rand_x,rand_y)
        
    def refresh():
        pass