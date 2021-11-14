#### Write a program to check if the year is leap year ####
# if the year is divisible by 4, 100 and 400 then it's a leap year
# and if it is divisible by 4 but not 100 then it's a leap year
####

year = int(input('Please provide the year to check if it is a leap year or not: '))

# calculate the leap year condition
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('It\'s a leap year')
        else:
            print('Not a leap year')
    else:
        print('It\'s a leap year')
else:
    print('Not a leap year')