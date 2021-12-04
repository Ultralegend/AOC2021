import os
os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def removeArray(array, remove): return [i for i in array if (i != remove)]

fp = open("../Input/05_input2.txt").read()

inputNum = []
for i in fp.split("\n"): 
    inputNum.append(i)

print(inputNum)
