import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from line import Line


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#1f1f1f")
screen.title("Cross the road")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
line = Line()

screen.listen()
screen.onkey(player.go_up_arrow, "Up")
screen.onkey(player.go_up_space, "space")
screen.onkey(player.go_up_w, "w")
screen.onkey(player.go_right_arrow, "Right")
screen.onkey(player.go_right_d, "d")
screen.onkey(player.go_left_arrow, "Left")
screen.onkey(player.go_left_a, "a")


game_is_on = True
while game_is_on:
    
    time.sleep(0.1)
    
    # Spawns the obstacles
    car_manager.spawn_car()
    car_manager.send_car_to_start()
    car_manager.moving_car()
    
    # Detects collision with obstacles
    for each_car in car_manager.all_cars:
        if player.distance(each_car) <= 20:
            scoreboard.game_over()
            game_is_on = False
    
    # Increases speed of wobstacles per new level and starts new level
    if player.ycor() >= 244:
        time.sleep(0.2)
        car_manager.increase_speed()
        player.new_level()
        scoreboard.update_scoreboard()

    screen.update()

screen.exitonclick()
