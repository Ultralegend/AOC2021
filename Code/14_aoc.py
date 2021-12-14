import os
os.system("cls")

def getPolymerChart(chart, rules, limit):
    stepCount = 1

    while stepCount <= limit:
        stepCount += 1
        newDict = {}

        for i, j in chart.items():
            if (chart[i] == 0): continue
            i = str(i)

            pair1 = i[0] + rules[i][-1]
            pair2 = rules[i][0] + i[-1]
            
            if pair1 not in newDict:
                newDict[pair1] = j
            else:
                newDict[pair1] += j

            if pair2 not in newDict:
                newDict[pair2] = j
            else:
                newDict[pair2] += j
        
        chart = newDict

    return chart

def getPolymerCount(chart, string):
    polyCount = {}
    polyCount[string[-1]] = 1

    for i, j in chart.items():
        i = str(i)

        if i[0] not in polyCount:
            polyCount[i[0]] = j 
        else:
            polyCount[i[0]] += j

    return max(polyCount.values()) - min(polyCount.values())

fp = open("../Input/14_input.txt", "r").read().split("\n\n")

inputString = fp[0].strip()

inputNum = {}
for i in fp[1].split("\n"):
    x, y = (i.split(" -> "))
    inputNum[x] = y

chart = {}
for i in range(len(inputString) - 1):
    newEntry = inputString[i] + inputString[i + 1]

    if newEntry not in chart:
        chart[newEntry] = 1
    else:
        chart[newEntry] += 1

print(getPolymerCount(getPolymerChart(chart, inputNum, 10), inputString))
print(getPolymerCount(getPolymerChart(chart, inputNum, 40), inputString))
