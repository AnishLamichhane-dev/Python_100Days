from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, user_goal):
        super().__init__()
        self.color("aliceblue")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard(user_goal)

    def update_scoreboard(self, user_goal):
        self.goto(-100, 180)
        self.write(self.l_score, align="center",
                   font=("Arial", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center",
                   font=("Arial", 80, "normal"))
        if self.l_score == user_goal:

            self.left_user_wins()

        if self.r_score == user_goal:

            self.right_user_wins()

    def right_user_wins(self):
        self.goto(177, 0)
        self.color("yellow")
        self.write("Right User WINS!!!", False, align="center",
                   font=("Courier", 24, "bold"))

    def left_user_wins(self):
        self.goto(-170, 0)
        self.color("yellow")
        self.write("Left User WINS!!!", False, align="center",
                   font=("Courier", 24, "bold"))

    def left_point(self, user_goal):
        self.clear()
        self.l_score += 1
        self.update_scoreboard(user_goal)

    def right_point(self, user_goal):
        self.clear()
        self.r_score += 1
        self.update_scoreboard(user_goal)
