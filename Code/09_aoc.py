import os
os.system("cls")
print("\n\nNEW INPUT\n")

def arrayToInt(array): return [int(i) for i in array]

def removeArray(array, remove): return [i for i in array if (i != remove)]

fp = open("../Input/09_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(i)

print(inputNum)
