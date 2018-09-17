import numpy as np
import operator


def loadData(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data


data = loadData('2016/day10.txt')
transfers = [instruction[:-1] for instruction in data if instruction[:3] == 'bot']

transfersDict = {}
for item in transfers:
    item = item.split()
    transfersDict[int(item[1])] = [item[5], int(item[6]), item[10], int(item[11])]

# Solve
alloc = {i: [] for i in range(300)}

for instruction in data:
    instruction = instruction[:-1].split()
    
    if instruction[0] == 'value':
        dest = int(instruction[-1])
        val = int(instruction[1])
        alloc[dest].append(val)
        alloc[dest] = sorted(alloc[dest])

# Find bot with two microchips
numChips = {k: len(v) for k, v in alloc.items()}
_bot = max(numChips.items(), key=operator.itemgetter(1))[0]

# Iterate over instructions
found = False
while not found:    
    transfer = transfersDict[_bot]
    
    # Check finished?
    if (alloc[_bot][0] == 17) and (alloc[_bot][1] == 61):
        print("Found:", _bot)
        found = True
    
    # Lower value
    if transfer[0] == 'bot':
        destLow = transfer[1]
        alloc[destLow].append(alloc[_bot][0])
        alloc[destLow] = sorted(alloc[destLow])
    
    # Larger value
    if transfer[2] == 'bot':
        destHigh = transfer[3]
        alloc[destHigh].append(alloc[_bot][1])
        alloc[destHigh] = sorted(alloc[destHigh])
    
    # Delete own
    alloc[_bot] = []  

    # Update _bot
    if len(alloc[destHigh]) == 2:
        _bot = destHigh
    elif len(alloc[destLow]) == 2:
        _bot = destLow
    else:
        numChips = {k: len(v) for k, v in alloc.items()}
        assert max(numChips.values()) == 2
        _bot = max(numChips.items(), key=operator.itemgetter(1))[0]
