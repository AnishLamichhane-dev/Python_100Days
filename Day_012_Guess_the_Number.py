import random

logo = """
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
                                                                                          
"""


def each_guess(choosen_number, lives):
    end_of_game = False
    while lives > 0 and not end_of_game:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess:    "))
        if guess > choosen_number:
            print("Too High")
            lives -= 1
            if lives > 0:
                print("Guess again.")
        elif guess < choosen_number:
            print("Too low.")
            lives -= 1
            if lives > 0:
                print("Guess again.")
        elif guess == choosen_number:
            print(f"You got it! The answer was {choosen_number}.")
            end_of_game = True
    if lives == 0:
        print(f"You've run out of guesses. The answer was {choosen_number}.")


print(logo)
print("Welcome to the Number Guessing Game!\nI'm Thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty.Type 'easy' or 'hard'\n>>>").lower()


if difficulty == 'hard':
    each_guess(choosen_number=random.randint(1, 100), lives=5)
elif difficulty == 'easy':
    each_guess(choosen_number=random.randint(1, 100), lives=10)
else:
    print("Either type 'easy' or 'hard'")
