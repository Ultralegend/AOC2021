import os
os.system("cls")

def errorScore(data):
    closePair = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
    score = 0

    for i in data:
        stack = []
        
        for j in i:
            if (j in "([{<"):
                stack.append(j)
            else:
                if (closePair[stack.pop()] == j): continue

                if (j == ")"): score += 3
                elif (j == "]"): score += 57
                elif (j == "}"): score += 1197
                else: score += 25137

                break
    
    return score

def incompleteScore(data):
    closePair = {"(" : ")", "[" : "]", "{" : "}", "<" : ">"}
    scores = []

    for i in data:
        error = False
        stack = []
        score = 0
        
        for j in i:
            if (j in "([{<"):
                stack.append(j)
            else:
                if (closePair[stack.pop()] == j): continue

                error = True
                break

        if (not error):
            for i in reversed(stack):
                score *= 5

                if (i == "("): score += 1
                elif (i == "["): score += 2
                elif (i == "{"): score += 3
                else: score += 4
        
            scores.append(score)
    
    return sorted(scores)[len(scores) // 2]

fp = open("../Input/10_input.txt", "r").read().split("\n")

inputNum = [i for i in fp]

print(errorScore(inputNum))
print(incompleteScore(inputNum))
