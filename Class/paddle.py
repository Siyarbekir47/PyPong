from turtle import Turtle
PLAYERSPEED = 20


class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.create_paddle(pos)

    def create_paddle(self,pos):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(pos)
        self.shapesize(stretch_len=0.5,stretch_wid=4)

    def up(self):
        y = self.ycor() + PLAYERSPEED
        if y > 350:
            y = 350
        self.sety(y)

    def down(self):
        y = self.ycor() - PLAYERSPEED
        if y < -350:
            y = -350
        self.sety(y)