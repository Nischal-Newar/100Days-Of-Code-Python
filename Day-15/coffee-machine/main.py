# define variables for current resources for machine
machine_resources = {
    "current_water_value": 1000,
    "current_milk_value": 1000,
    "current_coffee_value": 1000,
    "current_money": 1000.0,
    "latte_cost": 2.50,
    "espresso_cost": 3.50,
    "cappuccino_cost": 4.50
}


# function to perform administration operation
def administrator(user_input):
    if user_input == 'off':
        exit()
    elif user_input == 'report':
        print(f'Water: {machine_resources["current_water_value"]}ml')
        print(f'Milk: {machine_resources["current_milk_value"]}ml')
        print(f'Coffee: {machine_resources["current_coffee_value"]}g')
        print(f'Money: ${machine_resources["current_money"]}')


def espresso_drink():
    espresso_water = 50
    espresso_milk = 50
    espresso_coffee = 5

    if machine_resources["current_coffee_value"] < espresso_coffee or \
            machine_resources["current_milk_value"] < espresso_milk or \
            machine_resources["current_water_value"] < espresso_water:
        return False
    else:
        machine_resources["current_water_value"] -= espresso_water
        machine_resources["current_milk_value"] -= espresso_milk
        machine_resources["current_coffee_value"] -= espresso_coffee
        return True


def latte_drink():
    latte_water = 50
    latte_milk = 50
    latte_coffee = 5

    if machine_resources["current_coffee_value"] < latte_coffee or \
            machine_resources["current_milk_value"] < latte_milk or \
            machine_resources["current_water_value"] < latte_water:
        return False
    else:
        machine_resources["current_water_value"] -= latte_water
        machine_resources["current_milk_value"] -= latte_milk
        machine_resources["current_coffee_value"] -= latte_coffee
        return True


def cappuccino_drink():
    cappuccino_water = 50
    cappuccino_milk = 50
    cappuccino_coffee = 5

    if machine_resources["current_coffee_value"] < cappuccino_coffee or \
            machine_resources["current_milk_value"] < cappuccino_milk or \
            machine_resources["current_water_value"] < cappuccino_water:
        return False
    else:
        machine_resources["current_water_value"] -= cappuccino_water
        machine_resources["current_milk_value"] -= cappuccino_milk
        machine_resources["current_coffee_value"] -= cappuccino_coffee
        return True


# main code to process all the execution
while True:
    # ask user to provide their choice.
    # If the input is 'off' or 'report' then perform the required actions
    user_choice = input('What would you like? (espresso/latte/cappuccino):\n').lower()
    administrator(user_choice)

    # variable to check if the coffee processed or not
    response = {
        "status": False,
        "coffee": '',
    }
    if user_choice == 'latte':
        response["status"] = latte_drink()
        response["coffee"] = "latte"
    elif user_choice == 'cappuccino':
        response["status"] = cappuccino_drink()
        response["coffee"] = "cappuccino"
    else:
        response["status"] = espresso_drink()
        response["coffee"] = "espresso"

    if response["status"]:
        coffee_cost = machine_resources[response["coffee"]+"_cost"]
        user_coffee_cost = 0.0
        print(f'Please pay {coffee_cost} for your coffee.')
        while user_coffee_cost != coffee_cost:
            user_coffee_cost = float(input('Pay: '))
            if coffee_cost < user_coffee_cost:
                print(f'Here is your change {user_coffee_cost - coffee_cost}')
                machine_resources["current_money"] += user_coffee_cost - coffee_cost
                print(f'Hello, here is your {response["coffee"]}. Please enjoy!')
            elif coffee_cost > user_coffee_cost:
                coffee_cost -= user_coffee_cost
                print(f'Please pay the remaining {coffee_cost} amount.')
            else:
                print(f'Hello, here is your {response["coffee"]}. Please enjoy!')
                machine_resources["current_money"] += user_coffee_cost
    else:
        print(f'Hello, we do not have sufficient resources for {response["coffee"]}')
