#### Program to mark an X in a 2D List at a location specified by user ####
#### User will provide the location as two digit number ####

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}')
position = input('Where do you want to put the treasure? ')

first_position = int(position[0])
second_position = int(position[1])

map[first_position - 1][second_position - 1] = 'X'

print(f'{row1}\n{row2}\n{row3}')