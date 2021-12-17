import os

os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def getXbound(xlimit):
    sum = 0

    for i in range(min(xlimit)):
        sum += i

        if sum >= min(xlimit): return i

def checkLanding(c, xlimit, ylimit):
    pos = [0,0]
    maxHeight = 0

    while True:
        pos[0] += c[0]
        pos[1] += c[1]

        if pos[1] > maxHeight: maxHeight = pos[1]

        if c[0] > 0: c[0] -= 1
        elif c[0] < 0: c[0] += 1

        c[1] -= 1

        if pos[0] <= max(xlimit) and pos[0] >= min(xlimit) and pos[1] <= max(ylimit) and pos[1] >= min(ylimit): 
            return maxHeight
        elif pos[0] > max(xlimit) or pos[1] < min(ylimit):
            return -1

fp = open("../Input/17_input.txt", "r").read().strip()

inputX, inputY = fp.split(", ")

inputX = arrayToInt(inputX[15:].split(".."))
inputY = arrayToInt(inputY[2:].split(".."))

yBound = abs(min(inputY))
maxHeight = 0
count = 0

for i in range(getXbound(inputX), max(inputX) + 1):
    for j in range(min(inputY), yBound):
        curHeight = checkLanding([i,j], inputX, inputY)
        
        if curHeight != -1: count += 1
        if curHeight > maxHeight: 
            maxHeight = curHeight
            yBound = j + 1

print(maxHeight)
print(count)
