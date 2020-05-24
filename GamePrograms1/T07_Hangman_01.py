######################
# hangman_v1.py  
# From the book: "Invent Your Own Computer Games With Python 2nd Edition"
# Page 103-106
# Typed up by Steve on August 24, 2019
#   I also added many comments that were not from the book
#   I'm thinking of adding feet to the hangman and two more guesses
#   Also I found that when you guess word, the last letter you type is
#   is not display in the word that you guessed. Want to fix that.
#   When all letters are guessed, displaying the board again should fix it. 
######################
# 

######################
## Import Python Modules
######################
import random
##import time


######################
## Global Variable Definitions 
######################

## This variable is a python 'list'. Learn more here: https://www.w3schools.com/python/python_lists.asp
HANGMANPICS = ['''

   +---+
   |   |
       |
       |
       |
       |
 =========''','''


   +---+
   |   |
   O   |
       |
       |
       |
 =========''','''

   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''','''

   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''','''

   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''','''

   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''','''

   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''']

## Note: at the very end of this string there is a split() function, which divides the list of words into an array.  
## Learn about the split() function here.  https://www.w3schools.com/python/python_strings.asp
## Beacause of the split() at the end of this string 'words' is an array variable.   https://www.w3schools.com/python/python_arrays.asp
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

######################
## Function Definitions 
######################
## This function returns a random string from the passed list of strings.
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
    
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)]) ## counts up len missed letters
    print('')
    
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print('')
    
    blanks = '_' * len(secretWord)
    
    for i in range(len(secretWord)): ## replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            
    for letter in blanks: ## show the secret word with spaces in between each letter
        print(letter, end=' ')
    print('')
    
## Returns the letter the player entered. This function makes sure the payer entered a single letter, and not something else.
def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a single LETTER.')
        else:
            return guess

## This function returns True if the player wants to play again, otherwise it returns Flase.
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

######################
## Program Start
######################
print ('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    
    ## Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        
        ## Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        ## Check to see if the player has guessed too many times an lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and '  + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True
            
    ## Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(words)
            gameIsDone = False
        else:
            break
                    
######################
## Program End
######################
    
    
