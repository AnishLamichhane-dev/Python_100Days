from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("aliceblue")
        self.hideturtle()
        self.teleport(x=0, y=270, fill_gap=False)
        self.update_score()

    def update_score(self):
        self.clear()

        self.write(arg=f"Score: {self.score}", move=False,
                   align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.teleport(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
