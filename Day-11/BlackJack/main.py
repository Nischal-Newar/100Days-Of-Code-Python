# Import logo of BlackJack
import random
from art import logo

user_preferences = True
while user_preferences:
    # Print the initial Black Jack Logo
    print(logo,'\n')
    player = []
    dealer = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    game_condition = True
    player.append(random.choice(cards))
    player.append(random.choice(cards))
    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))
    if sum(player) == 21:
        print('Player wins')
        break
    if sum(dealer) == 21:
        print('Dealer wins')
        break

    while game_condition:
        print(f'Player cards: {player}')
        print(f'Dealer cards: {dealer}')
        if sum(player) < 21:
            user_input = input('Please select Hit or Stand: ').lower()
            if user_input == 'hit':
                player.append(random.choice(cards))
                dealer.append(random.choice(cards))
            else:
                if sum(player) > sum(dealer):
                    print('Player Wins')
                    game_condition = False
                else:
                    print('Dealer Wins')
                    game_condition = False
        else:
            print('Dealer wins')
            game_condition = False
    user_preferences = False