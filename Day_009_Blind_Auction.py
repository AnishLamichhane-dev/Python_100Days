import os


def clear_screen():
    os.system('cls')


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("\n")
print("Welcome to the secret auction program")

end_of_auction = False
names_and_bids_dictionary = {}


while not end_of_auction:
    name = input("What is your name?\n>>>")
    bid = input("What's your bid?\n>>>$")
    auction_continue = input(
        "Are there any other bidders? Type'yes' or 'no'.").lower()
    names_and_bids_dictionary[name] = bid
    if auction_continue == 'yes':
        clear_screen()
    elif auction_continue == 'no':
        end_of_auction = True


highest_bid = 0
winner = ""
for bidder in names_and_bids_dictionary:
    bid_amount = int(names_and_bids_dictionary[bidder])
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}.")
