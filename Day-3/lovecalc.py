#### Write a program to calculate love score between two people ####
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
# Then check for the number of times the letter in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
# Additional condition ->
# If score is less than 10 or greater than 90, then message should be :
# "Your score is x, you go together like coke and mentos."
# Love score between 40 and 50, the message should be:
# "Your score is y, you are alright together."
# Otherwise, the message should be:
# "your score is z."
##### 

print('Welcome to the Love Calculator!')
your_name = input('What is your name?\n')
lover_name = input('What is their name?\n')

combine_name = your_name.lower() + ' ' + lover_name.lower()

# calculate the score
true_word_count = combine_name.count('t') + combine_name.count('r') + combine_name.count('u') + combine_name.count('e')
love_word_count = combine_name.count('l') + combine_name.count('o') + combine_name.count('v') + combine_name.count('e')

total_score = true_word_count * 10 + love_word_count

if (total_score < 10) or (total_score > 90):
    print(f'Your score is: {total_score}, you go together like coke and mentos.')
elif (total_score >= 40) and (total_score <= 50):
    print(f'Your score is {total_score}, you are alright together.')
else:
    print(f'Your score is {total_score}')