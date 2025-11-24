import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
"""


def total_user_score():
    """Finds and returns the sum of all cards of the user."""
    sum_of_user_cards = 0
    for user_card in user_cards:
        sum_of_user_cards += user_card
    return sum_of_user_cards


def total_comp_score():
    """Finds and returns the sum of all cards of the computer."""
    sum_of_comp_cards = 0
    for comp_card in comp_cards:
        sum_of_comp_cards += comp_card
    return sum_of_comp_cards


def comp_getting_card():
    """"Computer keeps on adding a card untill its sum reaches above 17."""
    while total_comp_score() < 17:
        new_comp_card = cards[random.randint(0, 12)]
        comp_cards.append(new_comp_card)
        if new_comp_card == cards[0] and total_comp_score() > 21:
            new_comp_card = new_cards[0]
            del comp_cards[-1]
            comp_cards.append(new_comp_card)


def print_user_comp_score():
    """Prints the current score of user and computer."""
    print(f"Your cards: {user_cards}, current score: {total_user_score()}")
    print(f"Computer's first card: {total_comp_score()}")


def print_user_comp_end_score():
    """Prints the final score of user and computer."""
    print(
        f"  Your final hand: {user_cards}, final score: {total_user_score()}")
    print(
        f"  Computer's final hand: {comp_cards}, final score: {total_comp_score()}")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
new_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_start = input(
    "Do you want to play a game of Blackjack? Type 'y' or 'n'\n>>>").lower()

if game_start == "y":
    end_of_game = False
elif game_start == "n":
    end_of_game = True
else:
    print("Please write 'y' or 'n'.")
    end_of_game = True

while not end_of_game:

    print(logo)

    user_card1 = cards[random.randint(0, 12)]
    user_card2 = cards[random.randint(0, 12)]

    if user_card1 == user_card2 == cards[0]:
        user_card2 = new_cards[0]

    user_cards = [user_card1, user_card2]
    print(f"Your cards: {user_cards}, current score: {total_user_score()}")

    comp_card1 = cards[random.randint(0, 12)]
    comp_cards = [comp_card1]
    print(f"Computer's first card: {total_comp_score()}")

    while total_user_score() < 22 and not end_of_game:
        new_card = input(
            "Type 'y' to get another card, type 'n' too pass:\n>>>").lower()

        if new_card == 'y':
            new_card = cards[random.randint(0, 12)]
            user_cards.append(new_card)
            if new_card == cards[0] and total_user_score() > 21:
                new_card = new_cards[0]
                del user_cards[-1]
                user_cards.append(new_card)

            if total_user_score() > 21:
                print_user_comp_score()
                print("You went over. You lose!😭")
                end_of_game = True
            elif total_user_score() == 21:
                print_user_comp_score()
                print_user_comp_end_score()
                print("You Win! with a BlackJack!🤩")
                end_of_game = True
            else:
                print_user_comp_score()

        elif new_card == 'n':
            print(
                f"  Your final hand: {user_cards}, final score: {total_user_score()}")
            comp_getting_card()
            print(
                f"  Computer's final hand: {comp_cards}, final score: {total_comp_score()}")

            if total_comp_score() > 21:
                print("Opponent went over. You win!😀")
            elif total_comp_score() == total_user_score():
                print("It's a Draw!😐")
            elif total_comp_score() > total_user_score():
                print("You lose!😭")
            elif total_user_score() > total_comp_score():
                print("You win!😀")
            elif total_user_score() == 21:
                print("You Win! with a BlackJack!🤩")
            end_of_game = True

        else:
            print("Write either y or n.")

    game_start = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n'\n>>>").lower()
    if game_start == "y":
        end_of_game = False
    elif game_start == "n":
        end_of_game = True
