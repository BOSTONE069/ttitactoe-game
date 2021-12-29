board = [' ' for x in range(10)] #this is a list with string space for inializing the input strings in the board

def insertLetter(letter,pos): # this function is calling for the different postions on the board of the game which will be filled with the letter
    board[pos] = letter

def spaceIsFree(pos): # this fuction help in checking if the space is free use
    return board[pos] == ' '

def printBoard(board):#this is design function for the board that is used in the game
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3]) #this helps in defining the inputs in the game in first middle row
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]) #this helps in defining the inputs in the game in second middle row
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9]) #this helps in defining the inputs in the game in third  middle row
    print('   |   |   ')

def isBoardFull(board):# this is a fuction for determining if the board full
    if board.count(' ') > 1: # this command check where the board if free by counting the empty space
        return False
    else:
        return True

def IsWinner(b,l): # this is fuction for determining the winner of the game
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[7] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove(): # this is fuction for determining the player move
    run = True # this run has been used to define the movement
    while run: # the loop is used to determine the movement of the player
        move = input("Please select a position to enter the X between 1 to 9") # this allows for the input on the player position
        try:
            move = int(move) #this has been used to convert move into integer
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False # this will indicate to the computer that it is its turn
                    insertLetter('X' , move)  # this calling on the defined function on insertLetter
                else:
                    print('Sorry, this space is occupied')
            else:
                print('Please type a number between 1 and 9')
        except:
            print('Please type a number')


def computerMove(): # this is a fuction for generating the computer move the AI
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0] # this generates the possible moves of the computer
    move = 0

    for let in ['O' , 'X']: # this is loop for defining the computer moves
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy, let):
                move = i
                return move

    cornersOpen = [] # this helps the computer to determine the free spaces on the corners of the board
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0: # this helps the computer to select any random value
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves: # this helps the computer to determine if the space is the one at the center
        move = 5
        return move

    edgesOpen = [] # this helps the computer to determine the open edges
    for i in possibleMoves:
        if i in [2 , 4 , 6 , 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0: # this shelps the computer to select the random values from the edges that are open
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li): # this is defining the random fuction that is going to be used by the computer
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def main(): # this defines the logic of the game
    print("Welcome to the game!")
    printBoard(board)

    while not(isBoardFull(board)): #This defines the logic of the computer and player moves
        if not(IsWinner(board , 'O')): #computer logic move
            playerMove()
            printBoard(board)
        else:
            print("Sorry you loose!")
            break

        if not(IsWinner(board , 'X')): # player logic move
            move = computerMove()
            if move == 0:
                print("Tie game")
            else:
                insertLetter('O' , move)
                print('computer placed o on position' , move , ':')
                printBoard(board)
        else:
            print("You win!")
            break

    if isBoardFull(board):
        print("Tie game")


while True: # this is a loop fo preparing the game for both the players
    x = input("Do you want to play the game? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('---------------------')
        main()
    else:
        break
