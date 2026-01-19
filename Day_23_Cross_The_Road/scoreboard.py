from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("aliceblue")
        self.penup()
        self.ht()
        self.score = -1
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.score += 1
        self.teleport(-280,260)
        self.clear()
        self.write(f"Level: {self.score}", False, align="left", font=(FONT))

    def game_over(self):
        self.goto(0,0)
        self.color("cyan")
        self.write("GAME OVER", False, align="center", font=("Courier", 24, "bold"))