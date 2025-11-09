import random

user_decision_rock_paper_scissors = int(input(
    "What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissors. \n >>>"))

if user_decision_rock_paper_scissors == 0:
    print("You chose: \nRock")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif user_decision_rock_paper_scissors == 1:
    print("You chose: \nPaper")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
elif user_decision_rock_paper_scissors == 2:
    print("You chose: \nScissors")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Choose 0, 1 or 2!")

computer_decision = random.randint(0, 2)

if computer_decision == 0:
    print("Computer chose: \nRock  ")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif computer_decision == 1:
    print("Computer chose: \nPaper")
    print("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")
else:
    print("Computer chose: \nScissors")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

if (user_decision_rock_paper_scissors == 0 and computer_decision == 0) or (user_decision_rock_paper_scissors == 1 and computer_decision == 1) or (user_decision_rock_paper_scissors == 2 and computer_decision == 2):
    print("It's a DRAW!!!")
elif (user_decision_rock_paper_scissors == 0 and computer_decision == 2) or (user_decision_rock_paper_scissors == 1 and computer_decision == 0) or (user_decision_rock_paper_scissors == 2 and computer_decision == 1):
    print("You Win. CONGRATULATIONS!!!")
else:
    print("You lose!!!")
