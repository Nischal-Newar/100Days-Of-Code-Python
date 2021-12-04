# import modules
from art import logo

# print the logo
print(f'{logo}', '\n')

# add function
def add(n1, n2):
    return n1 + n2

# subtract function
def subtract(n1, n2):
    return n1 - n2

# multiply function
def multiply(n1, n2):
    return n1 * n2

# divide function
def divide(n1, n2):
    return n1 / n2

# dictionary to store operations 
operations = {
    '+': 'add',
    '-': 'subtract',
    '*': 'multiply',
    '/': 'divide'
}

# calculator function
def calculator():
        # number as input from the user
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))

    # print the symbols and select the symbols
    for key in operations:
        print(key)
    operation_symbol = input("Pick an operation from the line above: ")

    # store the result
    answer = 0

    # different operation call depending on the symbol
    if operations[operation_symbol] == 'add':
        answer = add(num1, num2)
    elif operations[operation_symbol] == 'subtract': 
        answer = subtract(num1, num2)
    elif operations[operation_symbol] == 'multiply': 
        answer = multiply(num1, num2)
    else: 
        answer = divide(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {round(answer, 3)}")

should_continue = True
while should_continue:
    calculator()
    user_choice = input("Type 'y' to continue calculating: ")
    if user_choice != 'y':
        should_continue = False
