import pandas

nato_alphabets_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter:row.code for (index,row) in nato_alphabets_data.iterrows()}

user_words =  input("Enter a word:  ").upper()
user_letter = [letter for letter in user_words]

nato_letters = [nato_dict[letter] for letter in user_letter if letter in nato_dict]

print(nato_letters)