import os

os.system("cls")

def addLeft(array, val):
    for i in range(len(array) - 1, 0, -1):
        if type(array[i]) == int: 
            array[i] += val
            break
    
    return array

def addRight(array, val, idx):
    for i in range(idx, len(array)):
        if type(array[i]) == int:
            array[i] += val
            break
    
    return array

def explode(array):
    stack = []
    idx = parenCount = 0

    while idx < len(array):
        current = array[idx]
        idx += 1

        if parenCount >= 5 and type(current) == int and type(array[idx]) == int:
            stack.pop()

            stack = addLeft(stack, current)
            array = addRight(array, array[idx], idx + 1)
            stack.append(0)

            idx += 2
            parenCount -= 1
            continue

        stack.append(current)

        if current == "[": parenCount += 1
        elif current == "]": parenCount -= 1
    
    return stack

def split(array):
    stack = []
    hasSplit = False

    for i in array:
        if type(i) == int and i > 9 and not hasSplit:
            stack.append("[")
            stack.append(i // 2)
            stack.append(i // 2 if i % 2 == 0 else i // 2 + 1)
            stack.append("]")

            hasSplit = True
        else: stack.append(i)
    
    return stack

def hasBrace(array):
    count = 0
    
    for i in array:
        if i == "[": count += 1
        elif i == "]": count -= 1

        if count == 5: return True

    return False

def hasHighest(array):
    for i in array:
        if type(i) == int and i > 9: return True

    else: return False

def getMagnitude(array):
    nums = []

    for i in array:
        if type(i) == int:
            nums.append(i)
        elif i == "]":
            nums.append(nums.pop() * 2 + nums.pop() * 3) 
    
    if len(nums) == 1: return nums[0]
    return nums.pop() * 2 + nums.pop() * 3

def overallMagnitude(data):
    current = data[0].copy()
    for i in range(1, len(data)):
        current.insert(0, "[")
        for j in data[i]: current.append(j)
        current.append("]")

        while hasBrace(current) or hasHighest(current):
            if hasBrace(current): current = explode(current)
            if hasHighest(current): current = split(current)

    return getMagnitude(current)

def maxMagnitude(data):
    maxM = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if i == j: continue

            current = data[i].copy()

            current.insert(0, "[")
            for k in data[j]: current.append(k)
            current.append("]")

            while hasBrace(current) or hasHighest(current):
                if hasBrace(current): current = explode(current)
                if hasHighest(current): current = split(current)
            
            temp = getMagnitude(current)
            if temp > maxM: maxM = temp

    return maxM

fp = open("../Input/18_input.txt", "r").read().split("\n")

inputNum = []
for i in fp: 
    newEntry = []

    for j in list(i):
        if j in "1234567890":
            newEntry.append(int(j))
        elif j == "[" or j == "]":
            newEntry.append(j)

    inputNum.append(newEntry)

print(overallMagnitude(inputNum))
print(maxMagnitude(inputNum))