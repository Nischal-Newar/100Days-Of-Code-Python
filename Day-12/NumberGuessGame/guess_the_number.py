# import the logo
import random
from art import logo, win, lose

# print the logo
print(logo)

# function to return the total chance the user can have depending on the level
def user_chance(user_level_selected):
    if user_level_selected == 'easy':
        return 10
    else:
        return 5

# ask user to select the game level
user_level = input('Select the level: easy or hard\n').lower()

# calculate the number of chances user will have
total_chances = user_chance(user_level)

# select a random number between 1 and 100
number = random.randint(1,101)

# game condition to check if user win or lose
game_status = False

# loop will keep running till the total_chances reaches 0
while (total_chances != 0):
    user_guess = int(input('Guess a number between 1 and 100.\n'))
    if number > user_guess and number - user_guess > 10:
        print('The number you guessed is too low.')
        total_chances -= 1
    elif number > user_guess and number - user_guess <= 10:
        print('The number you guessed is close to the actual number.')
        total_chances -= 1
    elif number < user_guess and user_guess - number > 10:
        print('The number you guessed is too high.')
        total_chances -= 1
    elif number < user_guess and user_guess - number <= 10:
        print('The number you guessed is close to the actual number.')
        total_chances -= 1
    else:
        print('You guessed the correct number')
        total_chances = 0
        game_status = True

# depending on the game status decided whether the user won or lost
if game_status:
    print(win)
else:
    print(lose)