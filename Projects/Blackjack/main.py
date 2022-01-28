############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.


from art import logo
from os import system
import random


def clear():
    _ = system('clear')


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    # check for blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # check for an ace and if score exceeds 21, if so ace has value 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def find_winner(my_score, dealer_score):
    if my_score == dealer_score:
        return "DRAW"
    elif dealer_score == 0:
        return "YOU LOSE AGAINST A BLACKJACK"
    elif my_score == 0:
        return "YOU WIN WITH A BLACKJACK"
    elif my_score > 21:
        return "YOU LOSE, YOU WENT OVER"
    elif dealer_score > 21:
        return "YOU WIN, DEALER WENT OVER"
    else:
        return "YOU LOSE"


def play():
    print(logo)
    my_cards = []
    dealer_cards = []
    for i in range(2):
        my_cards.append(deal_card())
        dealer_cards.append(deal_card())

    game_over = False
    while not game_over:
        my_score = calculate_score(my_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {my_cards}, your score at the moment: {my_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if my_score == 0 or dealer_score == 0 or my_score > 21:
            game_over = True
        else:
            answer = input("Type 'y' to get another card, type 'n' to pass: ")
            if answer == 'y':
                my_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final cards: {my_cards}, final score: {my_score}")
    print(f"Dealer's final cards: {my_cards}, final score: {dealer_score}")
    winner_is = find_winner(my_score, dealer_score)
    print(winner_is)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    play()
