import os
os.system("cls")

fp = open("Data/input.txt", "r")

counter = 0

inputNum = []
for i in fp:
    inputNum.append(int(i.strip()))
fp.close()

for i in range(0, len(inputNum)):
    if (i + 3 < len(inputNum)):
        sumA = inputNum[i] + inputNum[i + 1] + inputNum[i + 2]
        sumB = inputNum[i + 1] + inputNum[i + 2] + inputNum [i + 3]

        if (sumA < sumB):
            counter += 1

print(counter)
