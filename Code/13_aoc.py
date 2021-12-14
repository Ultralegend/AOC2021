import os

os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def plotBoard(board):
    width = max([i[0] for i in board]) + 1
    height = max([i[1] for i in board]) + 1

    for j in range(height):
        for i in range(width):
            if (i,j) not in board:
                print(" ", end="")
            else:
                print("█", end="")
        print()

def foldBoard(board, foldIns):
    dots = 0

    for fold, x in foldIns:
        newBoard = set()
        x = int(x)

        for i, j in board:
            if "y" in fold and j > x:
                j = abs(x * 2 - j)
            elif "x" in fold and i > x:
                i = abs(x * 2 - i)
            newBoard.add((i,j))
        
        if dots == 0: dots = len(newBoard)
        
        board = newBoard.copy()
    
    print(dots)
    return board

fp = open("../Input/13_input.txt", "r").read().split("\n\n")

inputNum = [arrayToInt(i.split(",")) for i in fp[0].split("\n")]

foldNum = [i.split("=") for i in fp[1].split("\n")]

board = foldBoard(inputNum, foldNum)
plotBoard(board)