from turtle import Screen
import time
from Class.paddle import Paddle
from Class.ball import Ball
STARTING_POSITION = [(-370,0),(+370,0)]


screen = Screen()
screen.bgcolor("black")
screen.setup(height=800,width=800)
screen.title("PyPong")
screen.tracer(0)

ball = Ball()

paddle_a = Paddle(STARTING_POSITION[0])
paddle_b = Paddle(STARTING_POSITION[1])

screen.listen()
screen.onkeypress(paddle_a.up,"Up")
screen.onkeypress(paddle_a.down,"Down")
screen.onkeypress(paddle_b.up,"w")
screen.onkeypress(paddle_b.down,"s")


game_is_on =  True
while game_is_on:
    screen.update()
    time.sleep(0.01)  # Adjust speed as necessary

    ball.move()

    if ball.xcor() < -360 and paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50:
        ball.bounce_x()

    if ball.xcor() > 360 and paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50:
        ball.bounce_x()

    # Detect if ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_position()

    if ball.xcor() < -380:
        ball.reset_position()


screen.exitonclick()