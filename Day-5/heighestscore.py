#### Highest Score Calculator ####
# Write a program that will provide the highest score in the list#

# input from the user
student_score = input('Input a list of students heights ').split()

# convert the value to integer and store in the same list
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])

# for loop and if condition to check the highest value
highest = 0
for i in range(0, len(student_score)):
    if highest < student_score[i]:
        highest = student_score[i]

print(f'The highest score is: {highest}')