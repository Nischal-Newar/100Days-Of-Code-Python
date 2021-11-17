#### Program to play rock, paper and scissor game ####
import random

# ASCII arts stored in variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# store the art in list
randomGesture = [rock, paper, scissor]

user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. '))
computer_choice =  random.randint(0,2)

print('\nYou choose:')
print(f'{randomGesture[user_choice]}','\n')
print('Computer choose:')
print(f'{randomGesture[computer_choice]}', '\n')

if (user_choice == computer_choice):
    print('It\'s a tie')
elif (user_choice == 0 and computer_choice == 1):
    print('Computer won the match')
elif (user_choice == 0 and computer_choice == 2):
    print('You won the match')
elif (user_choice == 1 and computer_choice == 0):
    print('You won the match')
elif (user_choice == 1 and computer_choice == 2):
    print('Computer won the match')
elif (user_choice == 2 and computer_choice == 0):
    print('You won the match')
else:
    print('Computer won the match')


