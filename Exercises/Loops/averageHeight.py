# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights in cm separated by space:\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
nStudents = len(student_heights)
totalHeight = 0
for height in student_heights:
    totalHeight += height
avgHeight = int(round(totalHeight / nStudents, 0))
print(f"The average height is {avgHeight} cm.")
