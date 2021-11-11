# print first statement in python
print("Welcome to python 100 days \n")

# print the input value
name = input("What is your name? \n")

print("Welcome", name, "\n")

# print the length of string
print("Name Length", len(name));

# swap the values of two variables using third variable
value1 = input("a:")
value2 = input("b:")

print("\nBefore swap")
print("First Value:",value1)
print('Second value:',value2)

temp = value1
value1 = value2
value2 = temp

print('\nAfter swap')
print('First Value:',value1)
print('Second Value:',value2)