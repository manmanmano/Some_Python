# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remainingAge = 90 - int(age)
remainingDays = remainingAge * 365
remainingWeeks = remainingAge * 52
remainingMonths = remainingAge * 12

print(f"You have {remainingDays} days, {remainingWeeks} weeks, and {remainingMonths} months left.")
