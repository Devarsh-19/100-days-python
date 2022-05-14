from random import randint
from turtle import Turtle

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(0.7, 0.7)
        self.color('blue')
        self.speed('fastest')
        
        
    def refresh(self):
        rand_x = randint(-280,250)
        rand_y = randint(-280,250)
        
        self.goto(rand_x,rand_y)