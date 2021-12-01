import os

os.system("cls")

fp = open("input.txt", "r")

for i in fp:
    print(i)

fp.close()