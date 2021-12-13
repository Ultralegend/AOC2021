import os

os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def plotBoard(board, height, width):
    for j in range(height):
        for i in range(width):
            if [i,j] not in board:
                print(" ", end="")
            else:
                print("█", end="")
        print()

def foldBoard(board, foldIns):
    width = max([i[0] for i in board])
    height = max([i[1] for i in board])
    dots = 0

    for fold, x in foldIns:
        newBoard = []
        x = int(x)

        if "y" in fold:
            for i,j in board:
                if j > x:
                    newC = [i, abs(j - x * 2)]

                    if newC not in newBoard: newBoard.append(newC)
                elif [i,j] not in newBoard: newBoard.append([i,j])

            height //= height // x

        else:
            for i,j in board:
                if i > x:
                    newC = [abs(i - x * 2), j]

                    if newC not in newBoard: newBoard.append(newC)
                elif [i,j] not in newBoard: newBoard.append([i,j])
            
            width //= width // x
        
        if dots == 0: dots = len(newBoard)
        
        board = newBoard.copy()
    
    print(dots)
    plotBoard(board, height, width)
    return board

fp = open("../Input/13_input.txt", "r").read().split("\n\n")

inputNum = [arrayToInt(i.split(",")) for i in fp[0].split("\n")]

foldNum = [i.split("=") for i in fp[1].split("\n")]

foldBoard(inputNum, foldNum)