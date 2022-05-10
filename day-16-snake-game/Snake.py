from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:


    def __init__(self):
        self.segments = []
        self.createSnake()
        
        
    def createSnake(self):
        for i in START_POS:
            t = Turtle('square')
            t.color('white')
            t.pu()
            t.goto(i)
            self.segments.append(t)

    def move(self):
        for n in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[n - 1].xcor()
            new_y = self.segments[n - 1].ycor()
            self.segments[n].goto(new_x, new_y)
        self.segments[0].fd(20)
            

