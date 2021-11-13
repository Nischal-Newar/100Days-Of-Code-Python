### Your life left in week challenge ###
# We have to print days, weeks and months left until you will reach a certain age

print('This program will tell you how much days, weeks, months is left from your current age to your desired age')

# Provide your current age and date of birth
current_age = input('Please provide your current age: ')

# Provide the age for which you want to how many months, month, week and days is left
future_age = input('Please provide the desired age: ')

# Calculate the values
remaining_years = (int(future_age) - int(current_age))
remaining_days = remaining_years * 365
remaining_weeks = remaining_years * 52
remaining_months = remaining_years * 12

print(f'You have {remaining_days} days, {remaining_weeks} weeks, {remaining_months} months left')