import random

hangman_text = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

hangman_stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]


word_list = [
    "crane", "baboon", "shadow", "puzzle", "forest", "silver", "planet",
    "coffee", "jungle", "castle", "pirate", "bridge", "danger", "hunter",
    "rocket", "banana", "pepper", "dragon", "window", "secret", "button",
    "oxygen", "mirror", "candle", "storm", "thunder", "cloud", "rabbit",
    "garden", "pencil", "whisper", "meteor", "flame", "river", "galaxy",
    "marble", "wizard", "flower", "tunnel", "magnet", "camera", "spirit",
    "cookie", "planet", "circle", "velvet", "hammer", "anchor", "voyage"
]

random_num = random.randint(0, len(word_list)-1)
chosen_word = word_list[random_num]


empty_list = []
for item_empty_list in range(0, len(chosen_word)):
    empty_list.insert(0, '_')

lives = 6
game_end = False

print(hangman_text)

while game_end == False:
    print(hangman_stages[lives])
    guess_word = input("Guess a letter: ").lower()
    letter_position = -1
    if guess_word in empty_list:
        print(f"You have already guessed the letter {guess_word}!!!")
    for letter in chosen_word:
        letter_position += 1

        if guess_word == letter:
            del empty_list[letter_position]
            empty_list.insert(letter_position, letter)
    print("\n")
    print(f"{''.join(empty_list)}")
    print("\n")

    if guess_word not in chosen_word:
        lives -= 1
        print(f"The letter {guess_word} is not correct!!!")
        if lives == 0:
            game_end = True
    if '_' not in empty_list:
        print(hangman_stages[6])
        print(f"The word is {chosen_word}.")
        print("YOU WON!!!")
        game_end = True
    if lives == 0:
        print(hangman_stages[0])
        print(f"The word was {chosen_word}.")
        print("You lose!!!")
