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
    while game_condition:
        print(f'Player Deck: {player}')
        print(f'Dealer Deck: {dealer}')
        if sum(player) == 21:
            print('You win!')
        elif sum(dealer) == 21:
            print('Dealer win')    
        if sum(player) < 21:
            user_choice = input('Select an option: Hit or Stand?').lower()
            if user_choice == 'hit':
                player.append(random.choice(cards))
            elif sum(player) == sum(dealer):
                print('Draw game!')
            elif sum(player) > sum(dealer):
                print('You win!')
            elif sum(dealer) > sum(player):
                print('Dealer win!')
            else:
                print('Bust')
                
        
        game_condition = False
        user_preferences = False
