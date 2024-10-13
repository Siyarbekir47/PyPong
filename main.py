from turtle import Screen
import time
from Class.paddle import Paddle
STARTING_POSITION = [(-370,0),(+370,0)]

screen = Screen()
screen.bgcolor("black")
screen.setup(height=800,width=800)
screen.title("PyPong")

screen.listen()

paddle = []
for _ in range(0,2):
    paddle.append(Paddle(STARTING_POSITION[_]))
player = paddle[0]

screen.onkeypress(player.up,"Up")
screen.onkeypress(player.down,"Down")

game_is_on =  True
while not game_is_on:
    time.sleep(0.1)




screen.exitonclick()