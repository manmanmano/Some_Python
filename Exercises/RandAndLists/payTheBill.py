import random

# 🚨 Don't change the code below 👇
# Split string method
names_string = input("Give me everybody's names, separated by a comma and a space. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_of_names = len(names)
random_name = random.randint(0, number_of_names - 1)
print(names[random_name] + " is going to buy the meal today!")
