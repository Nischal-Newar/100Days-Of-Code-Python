#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ''

# randomize the list to get random letters, number and symbol each time
random.shuffle(letters)
random.shuffle(symbols)
random.shuffle(numbers)

# store the password in sequence
for i in range(0, nr_letters):
    easy_password += letters[i]

for i in range(0, nr_symbols):
    easy_password += symbols[i]

for i in range(0, nr_numbers):
    easy_password += numbers[i]

print(f'Sequential password: {easy_password}')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password_list = []
hard_password = ''

# store the password in sequence inside a list
for i in range(0, nr_letters):
    hard_password_list.append(letters[i])

for i in range(0, nr_symbols):
    hard_password_list.append(symbols[i])

for i in range(0, nr_numbers):
    hard_password_list.append(numbers[i])

# shuffle the password list
random.shuffle(hard_password_list)

# store the randomized password
for i in range(0, len(hard_password_list)):
    hard_password += hard_password_list[i]

print(f'Random password: {hard_password}')