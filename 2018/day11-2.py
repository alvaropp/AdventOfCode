import numpy as np
from scipy import signal


def createGrid():
    grid = np.zeros([300, 300], dtype=int)
    
    for x in range(300):
        for y in range(300):
            rackID = x + 10
            power = rackID * y
            power += serialNumber
            power *= rackID
            power = (power // 100) % 10
            power -= 5
            grid[x, y] = int(power)

    return grid


def summedAreaTable(grid):
    return grid.cumsum(axis=0).cumsum(axis=1)


def findMaxTable(table, kernelSize):
    
    globalMax = 0
    inds = None
    for i in range(table.shape[0] - kernelSize):
        for j in range(table.shape[1] - kernelSize):
            value = table[i+kernelSize, j+kernelSize] - \
                    table[i, j+kernelSize] - \
                    table[i+kernelSize, j] + \
                    table[i, j]
            if value > globalMax:
                globalMax = value
                inds = [i+1, j+1]

    return globalMax, inds


with open('day11.txt') as f:
    serialNumber = int(f.read().splitlines()[0])

grid = createGrid()
table = summedAreaTable(grid)

globalMax = 0
globalInds = None
globalSize = 0
for size in range(1, 300):
    _max, _inds = findMaxTable(table, size)
    if _max > globalMax:
        globalMax = _max
        globalInds = _inds
        globalSize = size

print(globalInds, globalSize)

