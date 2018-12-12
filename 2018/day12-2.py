import numpy as np


def updateState(state, patterns):

    newState = [None]*len(state)
    for pos in range(2, len(state) - 2):
        newState[pos] = patterns[state[pos-2:pos+3]]
    newState[-2:] = ['.', '.']
    newState[:2] = ['.', '.']
    newState = ''.join(newState)
    
    return newState


nPadding = 10000

with open('day12.txt') as f:
    data = f.read().splitlines()
    padding = '.' * nPadding
    state = padding + data[0].split('state: ')[1] + padding
    patterns = {pattern.split(' => ')[0]: pattern.split(' => ')[1] for pattern in data[2:]}

nIter = 200
potNumbers = np.arange(-nPadding, len(data[0].split('state: ')[1])+nPadding)

sums = np.zeros(nIter)
for t in range(1, nIter+1):
    state = updateState(state, patterns)
    stateList = np.array([letter for letter in state])
    sums[t-1] = np.sum(potNumbers[stateList == '#'])


print("Visual inspection")
print(np.diff(sums))

maxIters = 50000000000
print(int((maxIters - nIter) * 62 + sums[-1]))

