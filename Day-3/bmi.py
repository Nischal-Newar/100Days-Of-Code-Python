####
# Write a program to calculate BMI and provide message if they are underweight, normal weight
# obese, clinically obese
# under 18.5 underweight
# between 18.5 and 25 normal weight
# between 25 and 30 overweight
# between 30 and 35 obese
# above 35 clinically obese
####

# input from the user
height = int(input('Please enter your height in cm: '))
weight = int(input('Please provide your weight in kg: '))

# calculate BMI
height_in_meters = float(height)/100
BMI = round(int(weight)/(height_in_meters ** 2), 2)

# print the BMI and the information
if BMI < 35:
    if BMI > 30:
        print(f'Your BMI is {BMI}. You are obese.')
    elif BMI > 25:
        print(f'Your BMI is {BMI}. You are overweight.')
    elif BMI > 18.5:
        print(f'Your BIM is {BMI}. You have a normal weight.')
    else:
        print(f'Your BMI is {BMI}. You are underweight.')
else:
    print(f'Your BMI is {BMI}. You are clinically Obese.')