import os
import math

os.system("cls")

def getLiteralValue(bits, current):
    ans = ""
    idx = 0
    while True:
        temp = bits[idx:idx+5]
        
        if temp[0] == "1":
            ans += temp[1:]
        elif temp[0] == "0":
            ans += temp[1:]
            idx += 5
            break
        
        idx += 5
    
    return [current + idx, int(ans, 2)]

def evalOperatorInner(bits, current, typeId):
    results = []
    packetVer = 0
    lengthId = 15 if bits[0] == "0" else 11
    idx = 1 + lengthId

    if lengthId == 15:
        subLen = int(bits[1:1 + lengthId], 2) + idx

        while idx < subLen:
            packetVer += int(bits[idx:idx + 3], 2)
            idx += 3
            tI = int(bits[idx:idx + 3], 2)
            idx += 3

            if tI == 4:
                retVal = getLiteralValue(bits[idx:], idx)
                idx = retVal[0]
                results.append(retVal[1])
            else: 
                retVal = evalOperatorInner(bits[idx:], idx, tI)
                idx = retVal[0]
                packetVer += retVal[1]
                results.append(retVal[2])
    
    else:
        subLen = int(bits[1:1+lengthId], 2)

        for _ in range(subLen):
            packetVer += int(bits[idx:idx + 3], 2)
            idx += 3
            tI = int(bits[idx:idx + 3], 2)
            idx += 3

            if tI == 4:
                retVal = getLiteralValue(bits[idx:], idx)
                idx = retVal[0]
                results.append(retVal[1])
            else: 
                retVal = evalOperatorInner(bits[idx:], idx, tI)
                idx = retVal[0]
                packetVer += retVal[1]
                results.append(retVal[2])
    
    if (len(results) > 1):
        if typeId == 0:
            results = sum(results)
        elif typeId == 1:
            results = math.prod(results)
        elif typeId == 2:
            results = min(results)
        elif typeId == 3:
            results = max(results)
        elif typeId == 5:
            if results[0] > results[1]: results = 1
            else: results = 0
        elif typeId == 6:
            if results[0] < results[1]: results = 1
            else: results = 0
        elif typeId == 7:
            if results[0] == results[1]: results = 1
            else: results = 0
    else:
        results = results[0]

    return [current + idx, packetVer, results]

def evalOperatorPacket(bits):
    results = []
    packetVer = int(bits[0:3], 2)
    typeId = int(bits[3:6] , 2)

    lengthId = 15 if bits[6] == "0" else 11
    currentIdx = 7 + lengthId

    if lengthId == 15:
        subLen = int(bits[7:7 + lengthId], 2) + currentIdx

        while currentIdx < subLen:
            packetVer += int(bits[currentIdx:currentIdx + 3], 2)
            currentIdx += 3
            tI = int(bits[currentIdx:currentIdx + 3], 2)
            currentIdx += 3

            if tI == 4:
                retVal = getLiteralValue(bits[currentIdx:], currentIdx)
                currentIdx = retVal[0]
                results.append(retVal[1])
                
            else: 
                retVal = evalOperatorInner(bits[currentIdx:], currentIdx, tI)
                currentIdx = retVal[0] 
                packetVer += retVal[1]
                results.append(retVal[2])
    
    else:
        subLen = int(bits[7:7+lengthId], 2)

        for _ in range(subLen):
            packetVer += int(bits[currentIdx:currentIdx + 3], 2)
            currentIdx += 3
            tI = int(bits[currentIdx:currentIdx + 3], 2)
            currentIdx += 3

            if tI == 4:
                retVal = getLiteralValue(bits[currentIdx:], currentIdx)
                currentIdx = retVal[0]
                results.append(retVal[1])
            else: 
                retVal = evalOperatorInner(bits[currentIdx:], currentIdx, tI)
                currentIdx = retVal[0] 
                packetVer += retVal[1]
                results.append(retVal[2])
    
    print(packetVer)

    if (len(results) > 1):
        if typeId == 0:
            print(sum(results))
        elif typeId == 1:
            print(math.prod(results))
        elif typeId == 2:
            print(min(results))
        elif typeId == 3:
            print(max(results))
        elif typeId == 5:
            if results[0] > results[1]: print(1)
            else: print(0)
        elif typeId == 6:
            if results[0] < results[1]: print(1)
            else: print(0)
        elif typeId == 7:
            if results[0] == results[1]: print(1)
            else: print(0)
    else:
        print(results[0])

fp = open("../Input/16_input2.txt", "r").read().strip()

inputNum = bin(int(fp, 16))[2:]
inputNum = "0" * (len(fp) * 4 - len(inputNum)) + inputNum

evalOperatorPacket(inputNum)
