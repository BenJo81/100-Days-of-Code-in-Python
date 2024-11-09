# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from tarfile import TruncatedHeaderError

import art
print(art.logo)
bids = {}
prog_cont = True

print("Welcome to the secret auction program.")

while prog_cont:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bids[name] = bid

    yes_or_no = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if yes_or_no == "no":
        prog_cont = False
        high_bid = 0
        winner = ""
        for key in bids:
            if (key[0]) > high_bid:
                high_bid = bids[key]
                winner = key
        print(f"The winner of the auction is {winner} and they bid an amount of ${high_bid}")

    else:
        if yes_or_no == "yes":
