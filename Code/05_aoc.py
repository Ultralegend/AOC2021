import os
os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def drawHVLines(data):
    lineRecord = {}

    for i in range(len(data)):
        x,y = min(data[i][0],data[i][1])
        mx, my = max(data[i][0],data[i][1])

        if (x == mx):
            for j in range(y, my + 1):
                if ((x,j) in lineRecord):
                    lineRecord[(x,j)] += 1
                else:
                    lineRecord[(x,j)] = 1
        elif (y == my):
            for j in range(x, mx + 1):
                if ((j,y) in lineRecord):
                    lineRecord[(j,y)] += 1
                else:
                    lineRecord[(j,y)] = 1
    
    return lineRecord

def drawHVDLines(data):
    lineRecord = {}

    for i in range(len(data)):
        x,y = min(data[i][0],data[i][1])
        mx, my = max(data[i][0],data[i][1])

        if (x == mx):
            for j in range(y, my + 1):
                if ((x,j) in lineRecord):
                    lineRecord[(x,j)] += 1
                else:
                    lineRecord[(x,j)] = 1
        elif (y == my):
            for j in range(x, mx + 1):
                if ((j,y) in lineRecord):
                    lineRecord[(j,y)] += 1
                else:
                    lineRecord[(j,y)] = 1
        elif (abs(x - mx) == abs(y - my)):
            for j in range(0, abs(x - mx) + 1):
                dx = -1 * j if (x > mx) else 1 * j
                dy = -1 * j if (y > my) else 1 * j

                if ((x + dx, y + dy) in lineRecord):
                    lineRecord[(x + dx, y + dy)] += 1
                else:
                    lineRecord[(x + dx, y + dy)] = 1

    return lineRecord

fp = open("../Input/05_input.txt").read()

inputNum = []

for i in fp.split("\n"): 
    newEntry = i.strip().split(" -> ")
    newEntry[0] = arrayToInt(newEntry[0].split(","))
    newEntry[1] = arrayToInt(newEntry[1].split(","))
    inputNum.append(newEntry)

count = 0
for i in drawHVLines(inputNum).values():
    if (i > 1): 
        count += 1
print(count)

count = 0
for i in drawHVDLines(inputNum).values():
    if (i > 1): 
        count += 1
print(count)
