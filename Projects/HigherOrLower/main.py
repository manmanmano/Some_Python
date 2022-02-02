import art
import random
from game_data import data
from os import system


def clear():
    """Clear the screen"""
    _ = system("clear")


# Transform account data into printable format
def format_data(account):
    """Make the user data printable"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_guess(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if the guess is right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display the art at the beginning
print(art.logo)
score = 0
game_continues = True
b = random.choice(data)

# Pull out two random names from the game data
while game_continues:
    a = b
    b = random.choice(data)
    while a == b:
        b = random.choice(data)

    print(f"Compare A: {format_data(a)}")
    print(art.vs)
    print(f"Against B: {format_data(b)}")

# Ask the user
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct
    a_followers = a["follower_count"]
    b_followers = b["follower_count"]

# Clear the screen
    clear()
    print(art.logo)
    is_right = check_guess(guess, a_followers, b_followers)

# Give user feedback
# Keep the scores
# Repeat the game until users guess wrong
    if is_right:
        score += 1
        print(f"You're right! Current score: {score}\n")
    else:
        print(f"Sorry, you're wrong! Final score: {score}\n")
        game_continues = False
