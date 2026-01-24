# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Day_24_Mail/Input/Letters/starting_letter.txt", "r") as letter_format:
    whole_format = letter_format.read()

with open("./Day_24_Mail/Input/Names/invited_names.txt", "r") as all_names:
    for each_name in all_names:
        adjusted_names = whole_format.replace("[name]", f"{each_name}".strip("\n"))

        with open(f"./Day_24_Mail/Output/ReadyToSend/{each_name.strip("\n")}.txt", "w") as letter_to_each_person:
            letter_to_each_person.write(adjusted_names)
