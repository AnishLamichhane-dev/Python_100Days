
import Day_014_Game_Data
import Day_014_art
import random

end_of_game = False
score = 0

while not end_of_game:

    print(Day_014_art.logo)

    if score == 0:
        first_celebrity = Day_014_Game_Data.data[random.randint(0, 49)]
        second_celebrity = Day_014_Game_Data.data[random.randint(0, 49)]

    print(
        f"Compare A: {first_celebrity['name']}, {first_celebrity['description']}, from {first_celebrity['country']}. ")
    print(Day_014_art.vs)
    print(
        f"Compare B: {second_celebrity['name']}, {second_celebrity['description']}, from {second_celebrity['country']}. ")

    follower_count_a = int(f"{first_celebrity['follower_count']}")
    follower_count_b = int(f"{second_celebrity['follower_count']}")

    user_guess = input("Who has more followers? Type 'A' or 'B':    ").lower()

    if ((follower_count_a >= follower_count_b) and user_guess == 'a') or ((follower_count_a <= follower_count_b) and user_guess == 'b'):
        score += 1
        print(f"You're right! Current score: {score}")
        first_celebrity = second_celebrity
        second_celebrity = Day_014_Game_Data.data[random.randint(0, 49)]
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        end_of_game = True
