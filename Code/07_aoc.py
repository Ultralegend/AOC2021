import os
os.system("cls")
print("\n\nNEW INPUT\n")

def arrayToInt(array): return [int(i) for i in array]

def getFuel(data):
    minFuel = -1
    
    for i in range(1, max(data)):
        fuel = 0

        for j in data:
            fuel += abs(i - j)

            if (minFuel != -1 and fuel >= minFuel): break

        if (minFuel == -1 or fuel < minFuel):
            minFuel = fuel

    return minFuel

def getFuel2(data):
    minFuel = -1
    
    for i in range(1, max(data)):
        fuel = 0

        for j in data:
            fuel += sum(range(abs(i - j) + 1))

            if (minFuel != -1 and fuel >= minFuel): break

        if (minFuel == -1 or fuel < minFuel):
            minFuel = fuel

    return minFuel


fp = open("../Input/07_input.txt", "r").read().split(",")

inputNum = arrayToInt(fp)

print(getFuel(inputNum))
print(getFuel2(inputNum))

