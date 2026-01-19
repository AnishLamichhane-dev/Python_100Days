from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

game_start = True
while game_start:
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("#1f1f1f")
    screen.title("Snake Game")
    screen.tracer(0)
    user_choosen_difficulty = int(screen.textinput(
        title="Choose your Difficulty", prompt="Write a number from 0 to 10:  "))

    snake = Snake(user_choosen_difficulty)

    food = Food()
    scoreboard = ScoreBoard()
    

    screen.listen()
    screen.onkey(snake.up, "W")
    screen.onkey(snake.down, "S")
    screen.onkey(snake.right, "D")
    screen.onkey(snake.left, "A")
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    if 0 <= user_choosen_difficulty <= 10:
        game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(0.09)
            snake.move()

            # Detect collision with food
            if snake.head.distance(food) < 15:
                food.teleport_food()
                snake.extend(user_choosen_difficulty)
                scoreboard.update_score()
            # Detect collision with wall
            if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290):
                game_is_on = False
                scoreboard.game_over()
                user_decision_to_play = (screen.textinput(
                            title="Do you want to play again?", prompt="New game (y/n):  ")).lower()
                if user_decision_to_play == "y":
                    screen.clear()
                elif user_decision_to_play == "n":
                    game_start = False
            # Detect collision with tail
            for segment in snake.all_segments_of_snake[1:]:
                if snake.head.distance(segment) < 10:
                    game_is_on = False
                    scoreboard.game_over()
                    user_decision_to_play = (screen.textinput(
                            title="Do you want to play again?", prompt="New game (y/n):  ")).lower()
                    if user_decision_to_play == "y":
                        screen.clear()
                    elif user_decision_to_play == "n":
                        game_start = False
        
    else:
        print("\nChoose a number from 0 to 10!!!\n")

screen.exitonclick()
