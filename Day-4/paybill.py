#### Program to randomly pick a name who will pay the bill ####
#### User will provide the list of name ####
import random
print('Who will pay the bill?')

# variable to store the number of people they will add to list
choice = int(input('How many names you will add? '))

names = []
for i in range(choice):
    names.append(input('Provide the name: '))

print(f'{random.choice(names)} will pay the bill.')