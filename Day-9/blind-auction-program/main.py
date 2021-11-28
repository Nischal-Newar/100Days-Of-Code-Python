# Create blind auction program #
# import modules
import os
import random
from art import logo

# print the logo
print(logo, '\n')

# dictionary to store the key value pair
bidding_value = {}

# function to find the highest bid
def highest_bid():
    highest_bid_value = 0
    highest_bid_name = ''
    for key in bidding_value:
        if highest_bid_value < bidding_value[key]:
            highest_bid_value = bidding_value[key]
            highest_bid_name = key

    print(f'The highest bid is {highest_bid_value} and the winner is: {highest_bid_name}')

# ask user to provide the bidder name and value
continue_bid = True
while (continue_bid):
    name = input("Please provide the name: ")
    bid_value = int(input("Please provide the bidding price: "))
    bidding_value[name] = bid_value
    user_choice = input('Is there another user who want to bid? (Yes or No): ').lower()
    if user_choice == 'yes':
        os.system('cls')
        print(logo,  '\n')
    else:
        highest_bid()
        continue_bid = False


