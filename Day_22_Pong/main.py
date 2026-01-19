from turtle import Screen
from Day_22_Pong.paddle import Paddle
from Day_22_Pong.ball import Ball
from Day_22_Pong.scoreboard import Scoreboard
from turtle import Turtle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#1f1f1f")
screen.title("Pong")

screen.tracer(0)


# Dotted line at middle
y_coordinate_of_dotted_line=-300
for dotted_line in range(60):
    tom = Turtle(shape="square")
    tom.color("aliceblue")
    tom.shapesize(stretch_wid=1,stretch_len=0.3)
    tom.teleport(0,y_coordinate_of_dotted_line)
    y_coordinate_of_dotted_line+=40

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.moving_ball()

    # Detect collision of ball with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision of ball with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:

        ball.bounce_x()


    # ball is missed by one side
    if ball.xcor() > 400:
        ball.clear()
        ball = Ball()
        ball.bounce_x()
        ball.bounce_y()
        scoreboard.left_point()

    if ball.xcor() < -400:
        ball.clear()
        ball = Ball()
        scoreboard.right_point()

screen.exitonclick()
