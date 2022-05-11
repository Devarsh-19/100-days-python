from turtle import Turtle, right

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]
        
        
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
        self.head.forward(MOVE_DISTANCE)
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
