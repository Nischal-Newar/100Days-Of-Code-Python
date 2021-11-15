#### Write a program to order pizza and show the total price ####
# Small -> $15, Medium -> $20 and Large -> $25
# Pepperoni -> + $4 for small and + $5 for large or Medium
# Cheese -> + $1

print('Welcome to the Pizza Delivery Service!','\n')
size = input('Which Pizza do you want? S, M or L ')
add_pepperoni = input('Do you want pepperoni? Y or N ')
extra_cheese = input('Do you want extra cheese? Y or N ')

# calculate the total price
total_bill = 0
if size == 'S':
    total_bill += 15
elif size == 'M':
    total_bill += 20
else:
    total_bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        total_bill += 4
    else:
        total_bill += 5

if extra_cheese == 'Y':
    total_bill += 1

print(f'Your final bill is: {total_bill}')
