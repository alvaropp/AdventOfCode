from collections import defaultdict
import numpy as np


with open('day7.txt') as f:
    data = f.read().splitlines()


graph = defaultdict(list)
graphRev = defaultdict(list)
steps = []

for instruction in data:
    instruction = instruction.split(' ')
    steps.append(instruction[1])
    graph[instruction[1]].append(instruction[7])
    steps.append(instruction[7])
    graphRev[instruction[7]].append(instruction[1])
    
steps = set(steps)
times = {step: 60+ord(step)-64 for step in steps}


notAvailable = set([item for sublist in graph.values() for item in sublist])
available = steps - notAvailable
available = sorted(list(available))
notAvailable = sorted(list(notAvailable))
inQueue = []

nPeople = 5
orderedSteps = []
doing = [None] * nPeople
doingTime = np.ones(nPeople)*9999

allTime = 0
while len(orderedSteps) != len(steps):
    
    # While there are idle people
    while (None in doing) and (len(available) > 0):
        ind = doing.index(None)
        # Find available step and allocate it
        step = available.pop(0)
        doing[ind] = step
        doingTime[ind] = times[step]

    # Advance time
    minTime = min(doingTime)
    doingTime -= minTime
    allTime += minTime
    
    # If step is finished, save it
    ind = np.where(doingTime == 0)[0][0]
    orderedSteps.append(doing[ind])
    step = doing[ind]
    doing[ind] = None
    doingTime[ind] = 9999
    
    # Get the newly available steps
    for newStep in inQueue:
        if (newStep not in orderedSteps) and (newStep not in doing) and (set(graphRev[newStep]).issubset(orderedSteps)):
            available.append(newStep)

    for newStep in graph[step]:
        if (newStep not in orderedSteps) and (set(graphRev[newStep]).issubset(orderedSteps)):
            available.append(newStep)
        elif (newStep not in orderedSteps):
            inQueue.append(newStep)
    inQueue = sorted(list(set(inQueue)))

    available = sorted(list(set(available)))

print(int(allTime))

