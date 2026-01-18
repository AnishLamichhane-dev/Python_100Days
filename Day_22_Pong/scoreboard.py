from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("aliceblue")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 180)
        self.write(self.l_score, align="center",
                   font=("Arial", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center",
                   font=("Arial", 80, "normal"))

    def left_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
