from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from turtle import Turtle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#1f1f1f")
screen.title("Pong")
user_goal = int(screen.textinput(
    title="Points to win", prompt="How many points to win?:  "))

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
scoreboard = Scoreboard(user_goal)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

if 0 < user_goal :
    while game_is_on :
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
            scoreboard.left_point(user_goal)

        if ball.xcor() < -400:
            ball.clear()
            ball = Ball()
            scoreboard.right_point(user_goal)
        
        if scoreboard.l_score == user_goal or scoreboard.r_score == user_goal:
            tom.ht()
            tom.clear()
            game_is_on = False
else:
    print("\nChoose a positive number as goal!!!\n")
    screen.bye()
    
    
    

screen.exitonclick()
