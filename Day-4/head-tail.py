#### Program to randomly say 'Heads' or 'Tails' ####
import random
value = random.randint(0, 1)

if value == 0:
    print('\nHeads')
else:
    print('\nTails')