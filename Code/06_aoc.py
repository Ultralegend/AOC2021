import os
os.system("cls")

def arrayToInt(array): return [int(i) for i in array]

def removeArray(array, remove): return [i for i in array if (i != remove)]

fp = open("../Input/06_input.txt", "r")

inputNum = []
for i in fp: 
    inputNum.append(i)

fp.close()
print(inputNum)
