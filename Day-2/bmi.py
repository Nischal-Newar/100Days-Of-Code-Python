### Calculate BMI and then print as integer ###
height = input('Enter your height (centimeter): ')
weight = input('Enter your weight (kilogram): ')

# calculate the BMI
height_in_meters = float(height)/100
BMI = int(weight)/(height_in_meters ** 2)

print(f'Your Body Mass Index is:',int(BMI))