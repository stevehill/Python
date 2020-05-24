######################
# tictactoe.py  
# From the book: "Invent Your Own Computer Games With Python 2nd Edition"
# Page 152-156
# Typed up by Steve on September 2nd, 2019
#   I also added many comments not from the book
# Modified by Steve September 7, 2019 (version 2)
#   Modified function drawboard() by adding the square numbers
#   to the right of the tic tac toe board.  e.g. [1][2][3]
######################
# 

######################
## Import Python Modules
######################
import random


######################
## Global Variable Definitions 
######################
## currently no global variables 

######################
## Function Definitions 
######################

## This function prints to the screen the 'board' parameters passed to the function
## 'board' is a list of 10 strings representing the tictactoe X's and O's on the board
## ingore index 0 
def drawBoard(board):
    print('')
    print('')
    print('')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + '     [7][8][9]')
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + '     [4][5][6]')
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + '     [1][2][3]')
    print('   |   |')
    print('')
    print('')

## Lets the player choose and type which letter X or O that they want to 
## play.  Returns a list data type with 2 elements to the caller.  Returns
## ['X','O'] if the player chooses to play 'X' otherwise returns ['O','X']     
## ['player selection','computer selection'] 
def inputPlayerLetter():
    print('')
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print("Do you want to play X's or O's?")
        letter = input().upper()
    if letter == 'X':
        return ['X','O']  ## returns a list, [player letter, computer letter]
    else:
        return ['O','X']  ## returns a list, [player letter, computer letter]
    
    
## Choose which player will go first; uses random like a coin flip.  If the
## random function returns 0 the computer will go first, 1 means player goes first
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

## This function returns True if the player wants to play again, otherwise it returns Flase.
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter

## This function returns True is a player has one.  
## Input parameters to this function are:
## The current board moves, paramenter name = 'bo'
## A letter (X or O), paramenter name =  'le'      
def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or ## across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or         ## across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or         ## across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or         ## down left side 
    (bo[8] == le and bo[5] == le and bo[2] == le) or         ## down middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or         ## Down right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or         ## diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le))           ## diagonal
    
## Makes a duplicate of the current board moves,
## returns an array copy of the current board moves,
def getBoardCopy(board):
    dupeBoard = []
    
    for i in board:
        dupeBoard.append(i)
        
    return dupeBoard        

## returns True if the board position is free (empty, no X or O)
## input parameters passed are the current board state and a move
def isSpaceFree(board, move):
    return board[move] == ' ' ## True, if position is space

## Get player's next move, verifies that the move is valid
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (Please enter a number 1-9)')
        move = input()
    return int(move)

## returns a valid and random move, from a list of moves
## if there is no valide move found, returns None
## input parameters passed are the current board state and a move list
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
            
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None ## None is a special data type NoneType 
                    ## None has no value similar to null in other languages

## Gets the computer's next move
## input is the current state of the playing board
## and the letter (X/O) that the computer is playing.
## returns the move (int numbers 1-9) or 'None' if no valid move
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    
    ## Check to see if computer can win with next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i  ## winning move found, exit function and return that move
                
    ## A winning move was not found, so check to see if humanCheck
    ## player has a winning move, and return the blocking move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i  ## a blocking move found, exit function and return that move
                
    ## At this point, no winning move or blocking move was found.
    ## So find the best alternative; Check corners, center then sides.
    
    ## The code in the book checks corners first, but I might change/test the
    ## code to check the center first and take it if it's open.
    
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:  ## None has no value similar to null in other languages
        return move
        
    ## Try to take the center if it's free
    if isSpaceFree(board, 5):
        return 5
        
    ## last alternative, randomly choose an open side
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])    
                
## Checks to see if the board is full already
## return true if full, otherwise return false
## input parameter is the variable containing the current state of the board                
def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False ## open space found, exit func and return False
    return True ## for loop did not find an open space, exit func return True

######################
## End of Function Definitions 
######################



## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

######################
## Program Start
######################
print (' ')
print (' ')
print ('Welcome to ~ Tic Tac Toe ~')

while True:
    ## Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter() ## splits returned list into two vars
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True
    
    while gameIsPlaying:
        if turn == 'player':  ## Player Move
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                print(' ')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie, nobody wins!')
                    print(' ')
                    break
                else:
                    turn = 'computer'    
        else:                 ## Computer Move
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose :-( ')
                print(' ')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie, nobody wins!')
                    print(' ')
                    break
                else:
                    turn = 'player'    
            
    if not playAgain():
        print(' ')
        print('Thanks for playing...')
        print('...come back soon!')
        print(' ')
        break

######################
## Program End
######################
    
    
