import os
os.system("cls")
print("\n\nNEW INPUT\n")

def arrayToInt(array): return [int(i) for i in array]

def removeArray(array, remove): return [i for i in array if (i != remove)]

fp = open("../Input/07_input.txt", "r").read()

inputNum = []
for i in fp.split("\n"): 
    inputNum.append(i)

print(inputNum)
