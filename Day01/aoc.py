import os
os.system("cls")

fp = open("Data/input.txt", "r")

prev = int(fp.readline().strip())
counter = 0

for i in fp:
    current = int(i.strip())
    
    if (current > prev):
        counter += 1

    prev = current

fp.close()

print(counter)

