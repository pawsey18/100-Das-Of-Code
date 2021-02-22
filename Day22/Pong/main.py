from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()


screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
screen.listen()

screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down, 'Down')

screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down, 's')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()

screen.exitonclick()
