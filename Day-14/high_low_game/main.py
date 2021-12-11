# import libraries and files
import os, random
from art import logo, vs
from questions import data

def game():
    
    # declare game condition and initial score value
    game_condition = True
    score = 0

    while game_condition:
        # clear the console log after each loop
        os.system('clear')

        # print the logo
        print(logo)

        # select two random records
        choiceA = random.choice(data)
        choiceB = random.choice(data)

        # print the details
        print(f"Name: {choiceA['name']}")
        print(f"Description: {choiceA['description']}")
        print(f"Country: {choiceA['country']}")
        print(vs)
        print(f"Name: {choiceB['name']}")
        print(f"Description: {choiceB['description']}")
        print(f"Country: {choiceB['country']}")
        print('\n')

        # ask the question
        print('Who has the highest Instagram follower?')
        player_choice = input('A or B? ')

        if player_choice == 'A' and choiceA['follower_count'] > choiceB['follower_count']:
            print('You chose the right answer!')
            score += 1
        elif player_choice == 'A' and choiceA['follower_count'] < choiceB['follower_count']:
            print('You chose the wrong answer')
            game_condition = False
        elif player_choice == 'B' and choiceA['follower_count'] > choiceB['follower_count']:
            print('You chose the right answer!')
            score += 1
        else:
            print('You chose the wrong answer')
            game_condition = False

    return score

# call the game function and then display the final score
final_score = game()
print(f'Your final score is: {final_score}')

    
