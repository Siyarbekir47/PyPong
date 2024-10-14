from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,350)
        self.score_a = 0
        self.score_b = 0

    def update_score(self):
        self.clear()
        self.write(f"{self.score_a} : {self.score_b}",align="center",font=("Arial",20,"normal"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over! Final score: {self.score_a} : {self.score_b} ",align="center",font=("Arial",20,"normal"))
