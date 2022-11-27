# My AI overlord sits before me, but like most games of Tic Tac Toe; can be beaten by starting in the middle.

from threading import Event
import os

board = [' - ',' - ',' - ',
         ' - ',' - ', ' - ',
         ' - ',' - ',' - '];

weights = {
    "h1" : 0,
    "h2" : 0,
    "h3" : 0,
    "v1" : 0,
    "v2" : 0,
    "v3" : 0,
    "d1" : 0,
    "d2" : 0
}


possiblePatterns = {
    "h1" : [0, 1, 2],
    "h2" : [3, 4, 5],
    "h3" : [6, 7, 8],
    "v1" : [0, 3, 6],
    "v2" : [1, 4, 7],
    "v3" : [2, 5, 8],
    "d1" : [0, 4, 8],
    "d2" : [2, 4, 6]
}

user = ' X '
gameOn = True
gameCount = 0


def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------------")
    print(board[6] + " | " + board[7] + " | " + board[8])


def checkWin(board, player):

    i = 0
    while i < 7:
        horizontal = board[i:(i + 3)]
        i += 3
        if horizontal.count(player) == 3:
            print(f"<{player} WINS/>")
            return False
    j = 0
    while j < 3:
        vertical = board[j] + board[j + 3] + board[j + 6]
        j += 1
        if vertical.count(player) == 3:
            print(f"<{player} WINS/>")
            return False
    diag1 = board[0] + board[4] + board[8]
    if diag1.count(player) == 3:
        print(f"<{player} WINS/>")
        return False
    diag2 = board[2] + board[4] + board[6]
    if diag2.count(player) == 3:
            print(f"<{player} WINS/>")
            return False
    return True


def switchUser():
    global user
    if user == " X ":
        user = " O "
    else:
        user = " X "


def checkTaken(board, input):
    if board[input] == " X ":
        return True
    elif board[input] == ' O ':
        return True
    else:    
        return False


def checkNumber(input):
    if input < 1 or input > 9:
        return False
    else:
        return True


def runGame(board):
        global gameCount
        taken = True
        print(" ")
        while True:
            try:
                user_input = input("<YOUR TURN/> ")
                if user_input.isdigit():
                    user_input=int(user_input)
                else:   
                    raise ValueError()
                if 1 <= user_input <= 9:
                    break
                raise ValueError()
            except ValueError:
                print("<INPUT MUST BE A DIGIT 1 - 9/> ")
        user_input = int(user_input) - 1
        
        taken = checkTaken(board, user_input)
        while taken == True:
            user_input = int(input("<THAT SPACE IS TAKEN/> ")) - 1
            taken = checkTaken(board, user_input)
            if taken == False:
                break

        board[user_input] = user
        gameCount += 1

        return 0


def locator (board):
    return [i for i, x in enumerate(board) if x == " X "]


def patternWeights (dictionary, locations, dictionary2):
# now i have the locations of X, itterate through all the combinations
# like i did with the scoring
    for i in locations:
    #HORIZONTALS
        if i in dictionary.get("h1"):
            dictionary2["h1"] += 1
        if i in dictionary.get("h2"):
            dictionary2["h2"] += 1
        if i in dictionary.get("h3"): 
            dictionary2["h3"] += 1
    #VERTICALS
        if i in dictionary.get("v1"):
            dictionary2["v1"] += 1
        if i in dictionary.get("v2"):
            dictionary2["v2"] += 1
        if i in dictionary.get("v3"):
            dictionary2["v3"] += 1
    #DIAGS
        if i in dictionary.get("d1"):
            dictionary2["d1"] += 1
        if i in dictionary.get("d2"):
            dictionary2["d2"] += 1

            
def weightOrderer (weights):
    # copy weights
    weightsCopy = weights.copy()
    # sort weights in descending order
    # sorted function returns a tuple
    weightsCopy = sorted(weightsCopy.items(), key=lambda x:x[1], reverse = True)
    # turn tuple back into dict
    weightsCopy = dict(weightsCopy)
    return weightsCopy


def getPattern(index):
        # had possiblePatterns and Patterns set to the same variable name for far too long
        global possiblePatterns
        x = possiblePatterns.get(index)
        return x


def isFree(list):

    global board
    counter = 0
    for item in list:
        if board[item] != ' - ':
            counter += 1
    if counter == 3:
        return False
    else:
        return True


def freeSpace(list):
    for n in list:
        if board[n] == ' - ':
            return n


def wait(time):
    Event().wait(time) 
    print(". . . . . . ")
    Event().wait(time)
    os.system("clear")  


def thinking():
    print('.')
    Event().wait(0.5)
    os.system("clear")  
    print('. . ')
    Event().wait(0.5)
    os.system("clear")  
    print('. . . ')
    Event().wait(0.5)
    os.system("clear")  
    print('.')
    Event().wait(0.5)
    os.system("clear")  
    print('. . ')
    Event().wait(0.5)
    os.system("clear")  
    print('. . . ')
    Event().wait(0.5)
    os.system("clear") 




## BEGIN

os.system("clear")  
print("<WELCOME HUMAN/> ")
wait(1)

while gameOn == True:

    printBoard(board)

    runGame(board)
    os.system("clear")  
    printBoard(board)

    gameOn = checkWin(board, user)
    if gameOn == False:
        break
           
    if gameCount == 9:
        print("DRAW")
        break

    switchUser()
    print(" ")    
    print("<SWITCHING USER/>")
    wait(1)

    ## AIs TURN    
    thinking()

    locationsX = locator(board)

    patternWeights(possiblePatterns, locationsX, weights)

    orderedWeights = weightOrderer(weights)

    for i in orderedWeights:
        pattern = getPattern(i)

        if isFree(pattern) == False:
            pass
        elif isFree(pattern) == True:
            move = freeSpace(pattern)
            ## AI MAKES MOVE
            board[move] = user
            gameCount += 1
            break
    

    printBoard(board)
    print(f'CPU : {move + 1}')

    gameOn = checkWin(board, user)
    if gameOn == False:
        break

    if gameCount == 9:
        print("DRAW")
        break
    
    
    Event().wait(4)
    switchUser()    
    print("<SWITCHING USER/>")
    wait(1)
    os.system("clear")
