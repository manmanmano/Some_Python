# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
names = name1 + name2
names = names.lower()

# Count the letters in the word TRUE
letterCounter1 = 0
letterCounter1 += names.count('t')
letterCounter1 += names.count('r')
letterCounter1 += names.count('u')
letterCounter1 += names.count('e')

# Count the letters in the word LOVE
letterCounter2 = 0
letterCounter2 += names.count('l')
letterCounter2 += names.count('o')
letterCounter2 += names.count('v')
letterCounter2 += names.count('e')

# FINAL SCORE
finalScore = int(str(letterCounter1) + str(letterCounter2))
if finalScore < 10 or finalScore > 90:
    print(f"Your score is {finalScore}, you go together like coke and mentos.")
elif finalScore >= 40 and finalScore <= 50:
    print(f"Your score is {finalScore}, you are alright together.")
else:
    print(f"Your score is {finalScore}.")
