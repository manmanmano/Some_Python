from os import system
from art import logo


def clear():
    _ = system('clear')


def find_max(offers):
    max_bid, winner = 0, ""
    for bidder in offers:
        bid = int(offers[bidder])
        if bid > max_bid:
            max_bid = bid
            winner = bidder
    print(f"The winner is {winner} with a bid of {max_bid}$.\n")


offers = {}
while True:
    print("\n", logo, "\n")
    name = input("What is your name: ")
    bid = input("What is your bid (usd): ")
    if not bid.isnumeric() or not name.isalpha():
        exit("Illegal input found!")
    offers[name] = bid
    others = input("Are there any other bidders? ").lower()
    if others == 'yes' or others == 'no':
        if others == 'no':
            clear()
            break
        clear()
    else:
        exit("Illegal input found!")
print("\n", logo, "\n")
find_max(offers)
