import os
import math
import re

os.system("cls")
print("\n\nNEW INPUT\n")

def arrayToInt(array): return [int(i) for i in array]

def inc2dArray(array, x = 1): return [[j + x for j in i] for i in array]

fp = open("../Input/19_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    inputNum.append(i)

print(inputNum)
