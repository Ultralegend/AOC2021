import os
import heapq as hq

os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def inc2dArray(array, x = 1): return [[j + x for j in i] for i in array]

def checkSides(array, c):
    neighbors = []

    if c[0] + 1 < len(array):
        neighbors.append([c[0] + 1,c[1]])

    if c[0] - 1 != -1:
        neighbors.append([c[0] - 1,c[1]])

    if c[1] + 1 < len(array[0]):
        neighbors.append([c[0],c[1] + 1])
    
    if c[1] - 1 != -1:
        neighbors.append([c[0],c[1] - 1])

    return neighbors

def djikstra(array, start):
    distRec = {}
    distRec[(start[0], start[1])] = 0
    pq = []
    hq.heappush(pq, [0, start])

    while len(pq) != 0:
        index = hq.heappop(pq)[1]

        for i in checkSides(array, index):
            if (i[0], i[1]) in distRec: continue

            newDist = distRec[(index[0], index[1])] + int(array[i[0]][i[1]])

            if (i[0], i[1]) not in distRec or newDist < distRec[(i[0], i[1])]:
                distRec[(i[0], i[1])] = newDist
                hq.heappush(pq, [newDist, i])

    print(distRec[(len(array) - 1, len(array[0]) - 1)])

def expandArray(array):
    nb = array.copy()
    for i in range(len(nb)):
        intA = arrayToInt(list(nb[i]))

        for _ in range(4):
            k = []
            for j in intA:
                if (j == 9): k.append(1)
                else: k.append(j + 1)

            intA = k
            for j in k: nb[i] += str(j)

    height = len(nb)
    for i in range(len(nb), len(nb) * 5):
        nb.append("")

    for i in range(height):
        intA = arrayToInt(list(nb[i]))
        
        for j in range(4):
            temp = []
            for k in intA:
                if k == 9: temp.append(1)
                else: temp.append(k + 1)
            
            intA = temp
            for k in temp: nb[((height * (j + 1)) + i)] += str(k)
    
    return nb

fp = open("../Input/15_input.txt", "r").read().split("\n")

inputNum = [i for i in fp]
newArray = expandArray(inputNum)

djikstra(inputNum, [0,0])
djikstra(newArray, [0,0])