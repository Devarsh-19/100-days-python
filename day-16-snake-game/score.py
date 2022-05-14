from turtle import Turtle, Screen

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pen()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        
    def update(self):
        self.score +=1