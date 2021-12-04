import os
os.system("cls")

def getCourse(array):
    hpos = depth = 0

    for i in array:
        currentLine = i.strip().split(" ")
        if (currentLine[0] == "down"):
            depth += int(currentLine[1])
        elif (currentLine[0] == "up"):
            depth -= int(currentLine[1])
        elif (currentLine[0] == "forward"):
            hpos += int(currentLine[1])
    
    return hpos * depth

def getCourseAim(array):
    hpos = depth = aim = 0

    for i in array:
        currentLine = i.strip().split(" ")
        if (currentLine[0] == "down"):
            aim += int(currentLine[1])
        elif (currentLine[0] == "up"):
            aim -= int(currentLine[1])
        elif (currentLine[0] == "forward"):
            hpos += int(currentLine[1])
            depth += aim * int(currentLine[1])

    return hpos * depth

fp = open("../Input/02_input.txt", "r")
inputData = [i for i in fp]
fp.close()

print(getCourse(inputData))
print(getCourseAim(inputData))
