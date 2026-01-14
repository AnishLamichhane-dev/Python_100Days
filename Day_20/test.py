import turtle as tim


def func_up():

    tim.seth(to_angle=90)
    tim.forward(20)


def func_down():
    tim.seth(to_angle=270)
    tim.forward(20)


def func_right():
    tim.seth(to_angle=0)
    tim.forward(20)


def func_left():
    tim.seth(to_angle=180)
    tim.forward(20)


tim.Turtle(shape="turtle")
tim.listen()
tim.onkey(func_up, "Up")
tim.onkey(func_down, "Down")
tim.onkey(func_right, "Right")
tim.onkey(func_left, "Left")


tim.exitonclick()
