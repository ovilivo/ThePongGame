import turtle
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

MAX_SCORE = 10
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
score = Score()
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.refresh()
        score.l_point()
    if ball.xcor() < -400:
        ball.refresh()
        score.r_point()
    if score.r_score == MAX_SCORE:
        score.game_over()
        game_on = False
    if score.l_score == MAX_SCORE:
        score.game_over()
        game_on = False


screen.exitonclick()
