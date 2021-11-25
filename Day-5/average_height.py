#### Average Height Calculator ####
# Write a program that will count the average height of all the people #

student_heights = input('Input a list of students heights ').split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# store the sum
sum = 0
for i in range(0, len(student_heights)):
    sum += student_heights[i-1]

print(f'Sum of height: {sum}')
print(f'Average height: {sum/len(student_heights)}')