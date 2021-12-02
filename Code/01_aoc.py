import os
os.system("cls")

def countIncrease(array):
    increase = 0
    for i in range(0, len(array) - 1):
        if (array[i] < array[i+1]):
            increase += 1
    return increase

def countIncreaseBy3(array):
    increase = 0
    for i in range(0, len(array) - 3):
        sumA = inputNum[i] + inputNum[i + 1] + inputNum[i + 2]
        sumB = inputNum[i + 1] + inputNum[i + 2] + inputNum [i + 3]
        if (sumA < sumB):
            increase += 1
    return increase


fp = open("../Input/01_input.txt", "r")
inputNum = [int(i) for i in fp]
fp.close()

print(countIncrease(inputNum))
print(countIncreaseBy3(inputNum))
