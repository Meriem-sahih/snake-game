from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score=0
        self.penup()
        self.goto(0,200)
        self.scoore()
    def scoore(self):
          self.write(f"Score:{self.score}",font=("Arial",18,"normal"),align="center")
    def add_score(self):
         self.score +=1   
         self.clear()
         self.scoore()
    def game_over(self):
         self.screen.bgcolor("darkred") 
         self.goto(0,0)
         self.write(f"Game Over\nFinal score:{self.score}",font=("arial",18,"normal"),align="center")
         
