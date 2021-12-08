import os
os.system("cls")

def removeArray(array, remove): return [i for i in array if (i != remove)]

def decode(data, segments):
    uniqueSegments = {
        2: "1",
        4: "4",
        3: "7",
        7: "8"
    }

    for i in data:
        if (len(i) in uniqueSegments.keys()):
            segments[uniqueSegments[len(i)]] = sorted(i)
            data = removeArray(data, i)

    for i in data:
        i = sorted(i)
        if (len(i) == 6):
            if (set(i).issuperset(set(segments["4"]))):
                segments["9"] = i
            elif (set(i).issuperset(set(segments["7"]))):
                segments["0"] = i
            else:
                segments["6"] = i
        else:
            if (set(i).issuperset(set(segments["7"]))):
                segments["3"] = i
            elif (len(set(segments["4"]) - set(i)) == 1):
                segments["5"] = i 
            else:
                segments["2"] = i

    return segments
    
def getOutputCount(data):
    data = [j for i in data for j in i]
    count = len([i for i in data if (len(i) in [2,3,4,7])])
    return count

def getOutputSum(input, output):
    segments = {
        "0" : "",
        "1" : "",
        "2" : "",
        "3" : "",
        "4" : "",
        "5" : "",
        "6" : "",
        "7" : "",
        "8" : "",
        "9" : ""
    }

    count = 0
    digit = ""
    for i in range(len(input)):
        dataset = [j for j in input[i]]
        for j in output[i]: dataset.append(j)

        segments = decode(dataset, segments)

        for j in output[i]:
            for k, v in segments.items():
                if (sorted(j) == v):
                    digit += k

        if (len(digit) == 4):
            count += int(digit)
            digit = ""

    return count

fp = open("../Input/08_input.txt", "r").read().split("\n")

inputNum = []
inputNum2 = []
for i in fp: 
    currentLine = i.split("|")
    inputNum.append([j for j in currentLine[0].split()])
    inputNum2.append([j for j in currentLine[1].split()])


print(getOutputCount(inputNum2))
print(getOutputSum(inputNum, inputNum2))