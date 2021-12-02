import os
os.system("cls")

fp = open("../Input/03_input.txt", "r")
inputNum = [int(i) for i in fp]
#inputNum = []
#for i in fp: inputNum.append(int(i))
fp.close()

print(inputNum)