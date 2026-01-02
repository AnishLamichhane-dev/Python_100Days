from turtle import Turtle, Screen
import random


race_is_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet!", prompt="Which turtle will win the race? Enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_racers = []

b = -110
for racing_turtles in range(0, 6):
    new_racer = Turtle(shape="turtle")
    new_racer.speed("fast")
    new_racer.penup()
    new_racer.color(colors[racing_turtles])
    new_racer.goto(x=-230, y=b)
    all_racers.append(new_racer)
    b += 40


if user_bet:
    race_is_on = True

while race_is_on:

    for racer in all_racers:
        if racer.xcor() > 225:
            race_is_on = False
            if user_bet == racer.pencolor():
                print(f"You've Won. {racer.pencolor()} won the race.")
            else:
                print(f"You've lost. {racer.pencolor()} won the race.")
        else:
            random_distance = random.randint(0,10)
            racer.forward(random_distance)


screen.exitonclick()
