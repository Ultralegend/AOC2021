import os
os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def getFishCount(data, limit):
    dayCounter = 1
    fishCount = {}

    for i in range(9):
        fishCount[i] = 0

    for i in data:
        fishCount[i] += 1

    while (dayCounter <= limit):
        newFish = 0

        for i in fishCount.keys():
            if (fishCount[i] != 0):

                if (i): 
                    fishCount[i-1] += fishCount[i]
                else: 
                    newFish = fishCount[i]
                
                fishCount[i] = 0

        fishCount[8] += newFish
        fishCount[6] += newFish
        
        dayCounter += 1

    return (sum(fishCount.values()))


fp = open("../Input/06_input.txt", "r").read().split(",")

inputNum = arrayToInt(fp)

print(getFishCount(inputNum, 80))
print(getFishCount(inputNum, 256))
