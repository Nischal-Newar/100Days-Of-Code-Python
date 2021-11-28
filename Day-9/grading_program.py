#### Grading System Program  ####
# You have access to a database of student_scores in the format of a dictionary. 
# The keys in student_scores are the names of the students and the values are their exam scores.

# student scores
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# empty dictionary to store student grades
student_grades = {}

# program to loop through each students score and assign the appropriate grades
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] < 91 and student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] < 81 and student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

# print the grades
print(student_grades)