import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
]
symbols = [
    '!', '#', '$', '%', '&', '(', ')', '*', '+'
]

print("Welcome to the Password Generator!!!")
num_letter = int(
    input("How many letters would you like in yourn password? \n>>>"))
num_symbols = int(
    input("How many symbols would you like in yourn password? \n>>>"))
num_numbers = int(
    input("How many numbers would you like in yourn password? \n>>>"))


total_letters = ""
for a in range(0, num_letter):
    total_letters += random.choice(letters)

total_symbols = ""
for b in range(0, num_symbols):
    total_symbols += random.choice(symbols)

total_numbers = ""
for c in range(0, num_numbers):
    total_numbers += random.choice(numbers)

password = total_letters + total_symbols + total_numbers

password_list = list(password)
random.shuffle(password_list)

password = ""
for charecter in password_list:
    password += charecter
print(f"Shuffled password {password}")
