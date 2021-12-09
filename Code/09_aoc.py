import os
os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def checkSides(data, num, c):
    if (c[0] - 1 != -1 and num >= data[c[0] - 1][c[1]]):
        return False
    
    if (c[0] + 1 != len(data) and num >= data[c[0] + 1][c[1]]):
        return False

    if (c[1] - 1 != -1 and num >= data[c[0]][c[1] - 1]):
        return False

    if (c[1] + 1 != len(data[0]) and num >= data[c[0]][c[1] + 1]):
        return False

    return True

def formBasin(data, c):
    frontier = c
    visited = []
    basin = []

    while (len(frontier) != 0):
        x, y = frontier.pop(0)
        num = data[x][y]
        
        if ([x, y] not in visited): 
            visited.append([x, y])
            basin.append(num)

        if (x - 1 != -1 and data[x - 1][y] != 9 and num < data[x - 1][y]):
            if ([x - 1, y] not in visited): 
                frontier.append([x - 1, y])
    
        if (x + 1 != len(data) and data[x + 1][y] != 9 and num < data[x + 1][y]):
            if ([x + 1, y] not in visited): 
                frontier.append([x + 1, y])

        if (y - 1 != -1 and data[x][y - 1] != 9 and num < data[x][y - 1] ):
            if ([x, y - 1] not in visited): 
                frontier.append([x, y - 1])

        if (y + 1 != len(data[0]) and data[x][y + 1] != 9 and num < data[x][y + 1]):
            if ([x, y + 1] not in visited): 
                frontier.append([x, y + 1])

    return len(basin)

def getRiskLevel(data):
    count = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if checkSides(data, data[i][j],[i,j]):
                count += data[i][j] + 1
    
    return count

def getMulBasins(data):
    basins = []

    for i in range(len(data)):
        for j in range(len(data[i])):
            if checkSides(data, data[i][j],[i,j]):
                basins.append(formBasin(data, [[i,j]]))

    basins.sort(reverse = True)
    return basins[0] * basins[1] * basins[2]

fp = open("../Input/09_input.txt", "r").read().split("\n")

inputNum = [arrayToInt(list(i)) for i in fp]

print(getRiskLevel(inputNum))
print(getMulBasins(inputNum))