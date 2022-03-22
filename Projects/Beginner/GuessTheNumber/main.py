from art import logo
import random


EASY_MODE_LIVES = 10
HARD_MODE_LIVES = 5


def check_guess(guess, secret_number, lives):
    if guess > secret_number:
        print("Too high.")
        return lives - 1
    elif guess < secret_number:
        print("Too low.")
        return lives - 1
    else:
        print(f"You got it! The number to guess was {secret_number}.")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while True:
        if difficulty == "easy":
            return EASY_MODE_LIVES
        elif difficulty == "hard":
            return HARD_MODE_LIVES
        else:
            print("Difficulty must be easy or hard, nothing else!")
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def play():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)

    lives = set_difficulty()
    guess = 0
    while guess != secret_number:
        print(f"You have {lives} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        lives = check_guess(guess, secret_number, lives)
        if lives == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != secret_number:
            print("Guess again.")


play()
