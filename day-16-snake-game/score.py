from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("courier", 24, "normal")
class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pen()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.color("white")
        self.update()
        
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update()
        
        
    def update(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font = FONT)
