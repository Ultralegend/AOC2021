import os
os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def inc2dArray(array, x = 1): return [[j + x for j in i] for i in array]

def incNeighbors2d(data, c):
    directions = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1)
    ]
    neighbors = []


    if (c[0] >= len(data) or c[1] >= len(data[0])): return

    for i, j in directions:
        if (c[0] + i != -1 and c[1] + j != -1 and c[0] + i < len(data) and c[1] + j < len(data[0])):
            neighbors.append([c[0] + i, c[1] + j])

    for i, j in neighbors:
        data[i][j] += 1

    return data
            
def countFlashes(data, limit):
    dayCounter = 0
    count = 0

    while (dayCounter < limit):
        dayCounter += 1
        flashed = []
        energy = True

        data = inc2dArray(data)

        while (energy):
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if (data[i][j] > 9 and [i, j] not in flashed):
                        data = incNeighbors2d(data, [i, j])
                        data[i][j] = -9
                        flashed.append([i, j])
            
            energy = False

            for i in data:
                for j in i:
                    if (j > 9): 
                        energy = True
                        break

        for i, j in flashed:
            data[i][j] = 0
            count += 1

    return count

def getSyncDay(data):
    dayCounter = 0

    while (sum([sum(i) for i in data]) != 0):
        dayCounter += 1
        flashed = []
        energy = True

        data = inc2dArray(data)

        while (energy):
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if (data[i][j] > 9 and [i, j] not in flashed):
                        data = incNeighbors2d(data, [i, j])
                        data[i][j] = -9
                        flashed.append([i, j])
            
            energy = False

            for i in data:
                for j in i:
                    if (j > 9): 
                        energy = True
                        break

        for i, j in flashed:
            data[i][j] = 0

    return dayCounter
        

fp = open("../Input/11_input.txt", "r").read().split("\n")

inputNum = [arrayToInt(list(i)) for i in fp]

print(countFlashes(inputNum, 100))
print(getSyncDay(inputNum))
