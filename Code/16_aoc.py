import os
from math import prod

os.system("cls")

def hextobin(hex):
    htob = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111"
    }
    result = ""

    for i in hex: result += htob[i]
    
    return result

def getLiteralValue(bits):
    packetVer = int(bits[0:3], 2)
    currentIdx = 6
    literal = ""
    
    while True:
        temp = bits[currentIdx:currentIdx + 5]
        
        literal += temp[1:]
        currentIdx += 5

        if temp[0] == "0": break
    
    return [currentIdx, packetVer, int(literal, 2)]

def evalOperatorPacket(bits, currentIdx):
    packetVer = int(bits[0:3], 2)
    typeId = int(bits[3:6] , 2)
    operands = []

    lengthId = 15 if bits[6] == "0" else 11
    currentIdx = 7 + lengthId

    if lengthId == 15:
        subLen = int(bits[7:7 + lengthId], 2) + currentIdx

        while currentIdx < subLen:
            tI = int(bits[currentIdx + 3:currentIdx + 6], 2)

            if tI == 4:
                retVal = getLiteralValue(bits[currentIdx:])
            else: 
                retVal = evalOperatorPacket(bits[currentIdx:], 0)
            
            currentIdx += retVal[0]
            packetVer += retVal[1]
            operands.append(retVal[2])
    
    else:
        subLen = int(bits[7:7 + lengthId], 2)

        for _ in range(subLen):
            tI = int(bits[currentIdx + 3:currentIdx + 6], 2)

            if tI == 4:
                retVal = getLiteralValue(bits[currentIdx:])
            else: 
                retVal = evalOperatorPacket(bits[currentIdx:], 0)
            
            currentIdx += retVal[0]
            packetVer += retVal[1]
            operands.append(retVal[2])

    result = {
        0: sum,
        1: prod,
        2: min,
        3: max,
        5: lambda v: int(v[0] > v[1]),
        6: lambda v: int(v[0] < v[1]),
        7: lambda v: int(v[0] == v[1])
    }

    return [currentIdx, packetVer, result[typeId](operands)]

fp = open("../Input/16_input.txt", "r").read().strip()

result = evalOperatorPacket(hextobin(fp), 0)
print(result[1], result[2])
