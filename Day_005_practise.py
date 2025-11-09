import random

name_string = input("Enter Name in Format (Anish, Sam, James): \n >>>")
names = name_string.split(", ")

num_names = len(names)
select_person = random.randint(0, num_names - 1)
choosen_name = names[select_person]
print(f"{choosen_name} is going to buy the meal today!")


import random

line1 = ["▓","▓","▓"]
line2 = ["▓","▓","▓"]
line3 = ["▓","▓","▓"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Choose a spot to hide the treasure like (A1, B2, C3): \n >>>")

first_Letter = position[0]
lower_first_Letter = first_Letter.lower()
abc = ["a", "b", "c"]
first_Letter_index = abc.index(lower_first_Letter)

number_index = int(position[1]) - 1

map[number_index][first_Letter_index]= "X"

print(f"{line1}\n{line2}\n{line3}")
