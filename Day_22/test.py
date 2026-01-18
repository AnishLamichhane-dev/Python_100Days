# Create two bats on opposite side of page which are be controlled by arrow keys then wasd
# one bat controlled by arrow keys other by wasd
# make the ball and it moves in a straight line
# when ball touches bats it goes backwards with same angle
# make a dotted line in middle
# when ball goes out of bounds then generate new ball at middle which goes to losers side
# angle of ball and position of ball at middle line, going to losers side is random
# make a scoreboard which increases when the ball goes out of bound of opponent

# ball , scoreboard , bat , main

from turtle import Turtle, Screen

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("#1f1f1f")
screen.title("Pong")
screen.tracer(0)
b=-300
for dotted_line in range(60):
    tom = Turtle(shape="square")
    tom.color("aliceblue")
    tom.teleport(0,b)
    b+=40

screen.exitonclick()

