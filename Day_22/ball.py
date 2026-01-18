from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("aliceblue")
        self.shape("circle")
        self.penup()
        self.change_in_x = 10
        self.change_in_y = 10
        # self.setheading(37)

    def moving_ball(self):
        # self.forward(10)
        new_x = self.xcor()+self.change_in_x
        new_y = self.ycor()+self.change_in_y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.change_in_y *= -1

    def bounce_x(self):
        self.change_in_x *= -1
        if self.change_in_x < 0:
            self.change_in_x -= 5
        else:
            self.change_in_x += 5
