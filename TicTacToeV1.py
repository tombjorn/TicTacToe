import os;


board = [' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ',' - ' ];


user1 = " X "
user2 = " O "
gameOn = True
gameCount = 0
taken = True

horizontal = [""]
vertical = [""]
diag1 = [""]
diag2 = [""]

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
            print(f"{player} wins!")
            return False
    j = 0
    while j < 3:
        vertical = board[j] + board[j + 3] + board[j + 6]
        j += 1
        if vertical.count(player) == 3:
            print(f"{player} WINS")
            return False
    diag1 = board[0] + board[4] + board[8]
    if diag1.count(player) == 3:
        print(f"{player} WINS")
        return False
    diag2 = board[2] + board[4] + board[6]
    if diag2.count(player) == 3:
            print(f"{player} WINS!")
            return False
    return True


def checkTaken(board, input):
    if board[input] == " X ":
        return True
    elif board[input] == ' O ':
        return True
    else:    
        return False


def runGame (state):
    global gameCount
    while state == True:

        taken = True
        user1_input = int(input("Player 1 : ")) - 1
        taken = checkTaken(board, user1_input)

        while taken == True:
            user1_input = int(input("Play an empty space! : ")) - 1
            taken = checkTaken(board, user1_input)
            if taken == False:
                break

        board.pop(user1_input)
        board.insert(user1_input, user1)
        gameCount += 1

        printBoard(board)

        state = checkWin(board, user1)
        if state == False:
            break

        
        if gameCount == 9:
            print("DRAW")
            break
        
        # REPEAT FOR PLAYER 2
        user2_input = int(input("Player 2 : ")) - 1
        taken = checkTaken(board, user2_input)

        while taken == True:
            user2_input = int(input("Play an empty space! : ")) - 1
            taken = checkTaken(board, user2_input)
            if taken == False:
                break

        board.pop(user2_input)
        board.insert(user2_input, user2)
        gameCount += 1
        
        # os.system("clear")
        printBoard(board)

        state = checkWin(board, user2)
        if state == False:
            break
        
        if gameCount == 9:
            print("DRAW")
            break


print(" ")
print("WELCOME!")
print(" ")
printBoard(board)
runGame(gameOn)




