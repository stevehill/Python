######################
# dragon_v3.py  
# From the book: "Invent Your Own Computer Games With Python 2nd Edition"
# Page 58-59
# Typed up by Steve on August 15, 2019
# Modified by Steve August 18, 2019 (version 2)
#   Added more caves, and made the dragon tell some jokes before eating you
#   or giving you the treasure.
# Modified by Steve August 18, 2019 (version 3) 
#   Made it so that the jokes don't repeat until each one has been randomly
#   selected and displayed.  See "selectJoke()" function and notes.  
######################
# 

######################
## Import Python Modules
######################
import random
import time


######################
## Global Variable Definitions 
######################

## This variable is a python dictionary learn more here: https://www.w3schools.com/python/python_dictionaries.asp
## A dictionary data structure is an associative array and sometimes call a "map" or symbol table or multimap 
dragonResponses =	{   
  1: "and says,\nWhy do the French like to eat snails?  They don't like fast food. \n\nThen the dragon...",
  2: "and says,\nA physics teacher breaks up with the biology teacher. There was no chemistry. \n\nThen the dragon...",
  3: "and says,\nWhy did the donut visit the dentist? To get a new filling. \n\nThen the dragon...",
  4: "and says,\nWhy did the bee get married?  He finally found his honey.  \n\nThen the dragon...",
  5: "and says,\nWhy is the sky so high? So the birds don't hit their heads. \n\nThen the dragon...",
  6: "and says,\nWhat happens when a cop gets into bed?  He becomes an undercover cop. \n\nThen the dragon...",
  7: "and says,\nDon't you hate it when someone answers their own questions? I do. \n\nThen the dragon...",
  8: "and says,\nI hate Russian dolls, they're so full of themselves. \n\nThen the dragon...",
  9: "and says,\nVelcro ... what a rip-off!  \n\nThen the dragon...",
  10: "and says,\nWhat is the best season to jump on a trampoline?  Spring time. \n\nThen the dragon...",
  11: "and says,\nWhy don’t snails fart?  Their houses don’t have any windows. \n\nThen the dragon...",
  12: "and says,\nWhere do pencils spend their vacations?  In Pencilvania. \n\nThen the dragon...",
  13: "and says,\nHey, you know what’s COOL?  Winter. \n\nThen the dragon...",
  14: "and says,\nWhat fish is the best fighter?  The swordfish. \n\nThen the dragon...",
  15: "and says,\nI lost some weight last month. But now it found me again. \n\nThen the dragon...",
  16: "and says,\nWould you like to hear a construction joke?  I’m still working on it. \n\nThen the dragon...",
  17: "and says,\nDo you know what’s up? The ceiling. \n\nThen the dragon...",
  18: "and says,\nWhat is red and flies through the air? A tomato in a helicopter. \n\nThen the dragon...",
  19: "and says,\nThey are testing a revolutionary new blender, but they’re getting mixed results. \n\nThen the dragon...",
  20: "and says,\nWhat is a bunny without a carrot?  Hungry! \n\nThen the dragon...",
  21: "and says,\nI am a magic dragon. (~POOF!~) And I just made you into an expert Python programmer. \n\nThen the dragon...",
}

## Another python dictionary variable that will be used to count/track each time a joke is selected and displayed
jokeCounterCheck =	{   
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
  10: 0,
  11: 0,
  12: 0,
  13: 0,
  14: 0,
  15: 0,
  16: 0,
  17: 0,
  18: 0,
  19: 0,
  20: 0,
  21: 0,
}

######################
## Function Definitions 
######################
def displayIntro():
    print('')
    print('')
    print('You are in a land full of dragons. In front of you,')
    print('you are five caves.  In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other caves have')
    print('greedy and hungry dragons, and they will eat you on sight.')
    print('')
    print('')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2' and cave != '3' and cave != '4' and cave != '5':
        print('Which cave will you go into? (1, 2, 3, 4 or 5)')
        cave = input()
        
    return cave
    
    
def checkCave(chosenCave):
    print('')
    print('')
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws... ')
    print('')
    time.sleep(2)

    ## Select a joke to tell
    randomNumber = selectJoke()
    print(dragonResponses[randomNumber])

    ## Randomly select which cave is the friently dragon cave.
    ## If the number the user enters is the same as the random number
    ## then the player gets the treasure, if not the cave has a greedy dragon. 
    friendlyCave = random.randint(1, 5)
    time.sleep(5)
    
    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')
        
    time.sleep(2)

##
## This function randomly selects a joke.  However the function will also select
## a different joke that has not been select yet.  Example: When joke 9 is selected and displayed, 
## it will not be selected and displayed again until all other jokes have been displayed.  
##
def selectJoke():
    randomNumber = random.randint(1, 21)
    for x in jokeCounterCheck:
      if jokeCounterCheck[x] < jokeCounterCheck[randomNumber]:
          randomNumber = x
          break
    jokeCounterCheck[randomNumber] = jokeCounterCheck[randomNumber] + 1
##  print(jokeCounterCheck)  ## for testing
    return randomNumber


######################
## Program Start
######################
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    
    print('')
    print('')
    print('Do you want to play again? (yes or no)')
    print('')
    print('')
    playAgain = input()
######################
## Program End
######################
    
    
