import random

board = [' O ',' - ',' X ',
         ' - ',' - ',' X ',
         ' - ',' - ',' - ' ];
count = [0, 0, 0, 0, 0, 0, 0, 0]

pattern = {
    "h1" : [0, 1, 2],
    "h2" : [3, 4, 5],
    "h3" : [6, 7, 8],
    "v1" : [0, 3, 6],
    "v2" : [1, 4, 7],
    "v3" : [2, 5, 8],
    "d1" : [0, 4, 8],
    "d2" : [2, 4, 6]
}
def locator (board):
    return [i for i, x in enumerate(board) if x == " X "]
    # Oloc = [j for j, y in enumerate(board) if y == " O "]


def cpuChoice(counter):
#going through count list, searching for largest nunber
    selection = [i for i, x in enumerate(counter) if x == 2]
    print(f'selection before Oloc : {selection}')
#random choice from selection
    pattPick = random.choice(selection)
    print(f'pattPick : {pattPick}')

    # getting list of indexes from dict Pattern
    pattKeys = list(pattern)
    # Convert dictionary to a list
    check = pattKeys[pattPick]

    move = 0

    for i in pattern.get(check):
        if board[i] == " - ":
            move = i
            print(f'MOVE TO : {move}')
     

def patternCount (counter, dictionary, locations):
# now i have the locations of X, itterate through all the combinations
# like i did with the scoring
    for i in locations:
    #HORIZONTALS
        if i in dictionary.get("h1"):
            counter[0] += 1
        if i in dictionary.get("h2"):
            counter[1] += 1
        if i in dictionary.get("h3"): 
            counter[2] += 1
    #VERTICALS
        if i in dictionary.get("v1"):
            counter[3] += 1
        if i in dictionary.get("v2"):
            counter[4] += 1
        if i in dictionary.get("v3"):
            counter[5] += 1
    #DIAGS
        if i in dictionary.get("d1"):
            counter[6] += 1
        if i in dictionary.get("d2"):
            counter[7] += 1



#* ACTUAL PROGRAM

Xloc = locator(board)

patternCount(count, pattern, Xloc)

print(f'count : {count}')

cpuChoice(count)




