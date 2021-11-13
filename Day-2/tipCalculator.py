### Split Bill Calculator Challenge ###
print('This program will split the bill in n number of people','\n')

# Provide the details
bill_amount = input('What was the total bill? ')
number_of_people = input('How many poeple to split the bill? ')
tip_percentage = input('What percentage tip would you like to give? ')

# calculation
tip_value = 1 + int(tip_percentage)/100
amount_per_person = (float(bill_amount) * tip_value)/int(number_of_people)

print(f'Each person should pay: {round(amount_per_person, 2)}')