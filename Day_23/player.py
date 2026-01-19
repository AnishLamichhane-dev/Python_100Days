from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("aliceblue")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def new_level(self):
        self.goto(STARTING_POSITION)

    def go_up_arrow(self):    
        self.forward(MOVE_DISTANCE)

    def go_up_space(self):
        self.forward(MOVE_DISTANCE)

    def go_up_w(self):
        self.forward(MOVE_DISTANCE)

    def go_right_arrow(self):
        self.right(90)
        self.forward(MOVE_DISTANCE)

    def go_right_d(self):
        self.right(90)
        self.forward(MOVE_DISTANCE)

    def go_left_arrow(self):
        self.left(90)
        self.forward(MOVE_DISTANCE)

    def go_left_a(self):
        self.left(90)
        self.forward(MOVE_DISTANCE)
