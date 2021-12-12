# define global variables for current water, milk, coffee and money status
current_water_value = 100
current_milk_value = 100
current_coffee_value = 100
current_money = 100


def shutdown(user_input):
    if user_input == 'off':
        exit()


def report(user_input):
    if user_input == 'report':
        print(f'Water: {current_water_value}')


# ask user to provide their choice. And if the input is 'off' or 'report' then perform the required actions
user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
shutdown(user_choice)
report(user_choice)


