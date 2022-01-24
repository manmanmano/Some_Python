import random

from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"{guess} has been already guessed")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word... try again")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYOU LOSE\n")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("\nYOU WIN\n")

    print(stages[lives])
