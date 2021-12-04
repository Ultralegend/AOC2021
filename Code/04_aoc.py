import os
os.system("cls")

def arrayToInt(array):
    newArray = []
    for i in array:
        newArray.append(int(i))
    return newArray

def getColumn(matrix, idx):
    return [row[idx] for row in matrix]

def getScore(matrix, matches):
    unmarked = 0
    for i in matrix:
        for j in i:
            if (j not in matches):
                unmarked += j
    return unmarked * matches[-1]

def removeArray(array, matrix):
    newArray = []
    for i in array:
        if (i != matrix):
            newArray.append(i)
    return newArray

def getWinnerScore(boards, numbers):
    increment = 1
    winBoard = []

    while (len(winBoard) == 0):
        matchNums = numbers[0:increment]

        for j in boards:
            for row in j:
                if (set(row).issubset(set(matchNums))): 
                    winBoard = j
                    return getScore(winBoard, matchNums)
 
            for col in range(len(j)):
                if (set(getColumn(j, col)).issubset(set(matchNums))): 
                    winBoard = j
                    return getScore(winBoard, matchNums)
            
        increment += 1

def getLastWinner(boards, numbers):
    increment = 1
    winBoard = []
    limit = len(boards)

    while (len(winBoard) != limit):
        matchNums = numbers[0:increment]

        for j in boards:
            bingoWin = False

            for row in j:
                if (set(row).issubset(set(matchNums))): 
                    winBoard.append(j)
                    boards = removeArray(boards, j)
                    bingoWin = True
 
            if (not bingoWin):
                for col in range(len(j)):
                    if (set(getColumn(j, col)).issubset(set(matchNums))): 
                        winBoard.append(j)
                        boards = removeArray(boards, j)
            
        increment += 1
    
    return getScore(winBoard[-1], matchNums)


fp = open("../Input/04_input.txt").read()

drawNumbers = fp.split("\n\n")[0].split(",")
drawNumbers = arrayToInt(drawNumbers)
bingoBoards = []

for i in fp.split("\n\n")[1:]:
    matrix = []
    for j in i.split("\n"):
        newRow = j.split()
        newRow = arrayToInt(newRow)
        matrix.append(newRow)

    bingoBoards.append(matrix)

print(getWinnerScore(bingoBoards, drawNumbers))
print(getLastWinner(bingoBoards, drawNumbers))