from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed(40)
        self.dx = 1.7
        self.dy = 1.7


    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

        # Collision with walls
        if self.ycor() > 390:
            self.sety(390)
            self.dy *= -1

        if self.ycor() < -390:
            self.sety(-390)
            self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
