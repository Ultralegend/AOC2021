import os
os.system("cls")

def getPowerRating(array):
    gamma = ""
    epsilon = ""
    record = {}

    for i in range(0, len(array[0])):
        record[0] = 0
        record[1] = 0

        for j in array:
            if (j[i] == "1"):
                record[1] += 1
            else:
                record[0] += 1

        if (record[1] > record[0]):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    
    return int(gamma, 2) * int(epsilon, 2)

def getO2Rating(array):
    record = {}

    for i in range(0, len(array[0])):
        newArray = []
        record[0] = 0
        record[1] = 0

        for j in array:
            if (j[i] == "1"):
                record[1] += 1
            else:
                record[0] += 1

        if (record[0] > record[1]):
            for j in array:
                if (j[i] == "0"):
                    newArray.append(j)
        else:
            for j in array:
                if (j[i] == "1"):
                    newArray.append(j)

        
        array = newArray

        if (len(array) == 1):
            return int(array[0], 2)

def getCO2Rating(array):
    record = {}

    for i in range(0, len(array[0])):
        newArray = []
        record[0] = 0
        record[1] = 0

        for j in array:
            if (j[i] == "1"):
                record[1] += 1
            else:
                record[0] += 1

        if (record[1] < record[0]):
            for j in array:
                if (j[i] == "1"):
                    newArray.append(j)
        else:
            for j in array:
                if (j[i] == "0"):
                    newArray.append(j)

        
        array = newArray

        if (len(array) == 1):
            return int(array[0], 2)
            

fp = open("../Input/03_input.txt", "r")
inputNum = [i.strip() for i in fp]
fp.close()

print(getPowerRating(inputNum))
print(getO2Rating(inputNum) * getCO2Rating(inputNum))
