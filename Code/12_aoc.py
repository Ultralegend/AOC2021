import os
os.system("cls")

def getPaths(graph, start, record, path):
    path.append(start)

    if (start == "end"):
        record.append(path.copy())
    else:
        for i in graph[start]:
            if (i.islower() and i in path): continue
            getPaths(graph, i, record, path.copy())
    
    return record

def getPaths2(graph, start, record, path):
    path.append(start)
    flag = False

    for i in path:
        if (i.islower() and path.count(i) > 1): 
            flag = True
            break

    if (start == "end"):
        record.append(path.copy())
    else:
        for i in graph[start]:
            if (i == "start" or (i.islower() and flag and i in path)): continue
            getPaths2(graph, i, record, path.copy())
    
    return record

fp = open("../Input/12_input.txt", "r").read().split("\n")

inputNum = [i.split("-") for i in fp]

path = {}
for i,j in inputNum:
    if (i not in path):
        path[i] = [j]
    else:
        path[i].append(j)

    if (j not in path):
        path[j] = [i]
    else:
        path[j].append(i)

print(len(getPaths(path, "start", [], [])))
print(len(getPaths2(path, "start", [], [])))
