#!/bin/python3
import random

rock = """
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
usersChoice = int(input("\nWhat do you want to choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
computersChoice = random.randint(0, 2)
print("\nUser chooses:" + choices[usersChoice])
print("\nComputer chooses:" + choices[computersChoice])
if usersChoice == computersChoice:
    print("\nIT IS A DRAW!\n")
elif usersChoice == 0 and computersChoice == 2:
    print("\nYOU WIN!\n")
elif usersChoice == 2 and computersChoice == 0:
    print("\nYOU LOSE!\n")
elif usersChoice > computersChoice: 
    print("\nYOU WIN!\n")
elif computersChoice > usersChoice: 
    print("\nYOU LOSE!\n")
else:
    exit("\nINVALID KEY! GAME OVER\n")
