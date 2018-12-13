import numpy as np
from copy import deepcopy


orientationToVel = {'^': np.array([-1, 0]), 
                    '>': np.array([0, 1]), 
                    'v': np.array([1, 0]),
                    '<': np.array([0, -1])}

turnDict = {0: {'^': '<', '>': '^', 'v': '>', '<': 'v'},
            1: {'^': '^', '>': '>', 'v': 'v', '<': '<'},
            2: {'^': '>', '>': 'v', 'v': '<', '<': '^'},
            '\\': {'^': '<', '<': '^', '>': 'v', 'v': '>'},
            '/': {'^': '>', '>': '^', 'v': '<', '<': 'v'}}

validDict = {'>': {'-'},
             '<': {'-'},
             '^': {'|'},
             'v': {'|'}}


def sortPos(posList, orientationList, turnList):
    inds = np.lexsort(np.rot90(posList))
    return posList[inds], list(np.array(orientationList)[inds]), list(np.array(turnList)[inds])


def initialise():
    posList = []
    orientationList = []

    for Y in range(len(data)):
        for X in range(len(data[0])):
            if (data[Y][X] == 'v') or (data[Y][X] == '^'):
                posList.append(np.array([Y, X]))
                orientationList.append(data[Y][X])
                data[Y][X] = '|'
            elif (data[Y][X] == '<') or (data[Y][X] == '>'):
                posList.append(np.array([Y, X]))
                orientationList.append(data[Y][X])
                data[Y][X] = '-'

    posList = np.asarray(posList)
    turnList = [0] * len(posList)
    posList, orientationList, turnList = sortPos(posList, orientationList, turnList)

    
    return posList, orientationList, turnList


def visualise():
    dataPrint = deepcopy(data)
    for i, pos in enumerate(posList):
        dataPrint[pos[0]][pos[1]] = orientationList[i]
    for line in dataPrint:
        print(''.join(line))


def step(posList, orientationList, turnList):
    
    toRemove = []

    for i, pos in enumerate(posList):
        # Perform step
        pos += orientationToVel[orientationList[i]]

        # Check for collision
        posSet = set([tuple(indPos) for indPos in posList])
        collision = not(len(posSet) == len(posList))

        if collision:
            for j in range(len(posList)):
                if j != i:
                    if np.array_equal(posList[i], posList[j]):
                        toRemove.append(i)
                        toRemove.append(j)

        # Update orientation if necessary
        if data[pos[0]][pos[1]] == '+':
            orientationList[i] = turnDict[turnList[i]][orientationList[i]]
            turnList[i] = (turnList[i] + 1) % 3
        elif data[pos[0]][pos[1]] == '\\':
            orientationList[i] = turnDict['\\'][orientationList[i]]
        elif data[pos[0]][pos[1]] == '/':
            orientationList[i] = turnDict['/'][orientationList[i]]
        
    if toRemove:
        toRemove = sorted(list(set(toRemove)))[::-1]
        
    for j in toRemove:
        posList = np.delete(posList, j, 0)
        orientationList.pop(j)
        turnList.pop(j)
    
    return posList, orientationList, turnList


with open('day13.txt') as f:
    dataRaw = f.read().splitlines()
data = [list(line) for line in dataRaw]

posList, orientationList, turnList = initialise()

t = 0
while len(posList) > 1:
    posList, orientationList, turnList = step(posList, orientationList, turnList)
    posList, orientationList, turnList = sortPos(posList, orientationList, turnList)
    t += 1

print("{},{}".format(posList[0][1], posList[0][0]))

