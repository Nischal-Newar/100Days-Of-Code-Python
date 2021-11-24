# Create Hangman Game #
# import modules
import os
import random
import hangman_words
import hangman_art

# show the hangman logo
print(hangman_art.logo,'\n')

# choose a random word from the word list
guessWord = random.choice(hangman_words.word_list)

# create a variable to store '_' as the same lenght of the guess word
guess_list = []
for letter in guessWord:
    guess_list.append("_")

# program to loop until the player wins or lose all the lives
lives = 6
end_of_game = False
while not end_of_game:
   
    # show the number of letters to guess and ask user to provide the letter
    print(guess_list,'\n')
    guess = input('Guess a letter: ').lower()

    # clear the console in each loop
    os.system('cls')    
    
    # show the hangman logo
    print(hangman_art.logo,'\n')
    
    # if the letter is not present decrease the lives by 1
    # if the letter is already guessed then provide the same information to the user
    # if the letter is present in the list the swap all the '_' in guess_list with the correct letter
    if guess not in guessWord:
        print(f'You guessed {guess}, that\'s not in the word. You lose a life\n')
        lives -= 1
    elif guess in guess_list:
        print(f'You\'ve already guessed {guess}\n')
    else:
        for i in range(len(guessWord)):
            if guess == guessWord[i]:
                guess_list[i] = guessWord[i]

    # print the hangman art
    print(hangman_art.stages[lives])

    # if the user lives reaches zero then the user lose the game
    if lives == 0:
        end_of_game = True
        print(hangman_art.lose)

    # if the user guessed all the letters then they will win the game
    if '_' not in guess_list:
        print(hangman_art.win)
        end_of_game = True