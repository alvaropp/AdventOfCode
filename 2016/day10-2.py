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

outputs = {i: [] for i in range(300)}

found = False
while not found:    
    transfer = transfersDict[_bot]
    print(transfer)
    
    # Check finished?
    
    # Lower value
    if transfer[0] == 'bot':
        destLow = transfer[1]
        alloc[destLow].append(alloc[_bot][0])
        alloc[destLow] = sorted(alloc[destLow])
    else:
        destLow = transfer[1]
        print(destLow, outputs[destLow])
        outputs[destLow].append(alloc[_bot][0])
        print(destLow, outputs[destLow])

    
    # Larger value
    if transfer[2] == 'bot':
        destHigh = transfer[3]
        alloc[destHigh].append(alloc[_bot][1])
        alloc[destHigh] = sorted(alloc[destHigh])
    else:
        destHigh = transfer[3]
        print(destHigh, outputs[destHigh])
        outputs[destHigh].append(alloc[_bot][1])
        print(destHigh, outputs[destHigh])

    
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


print(outputs[0][0] * outputs[1][0] * outputs[2][0])
