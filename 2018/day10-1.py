import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist


with open('day10.txt') as f:
    data = f.read().splitlines()
    nPoints = len(data)

def iterate(pos, vel):
    pos += vel

def plot(pos):
    maxDim = np.max(np.abs(pos))
    grid = np.zeros([maxDim+1, maxDim+1])
    for point in pos:
        grid[point[0], point[1]] = 1
        plt.imshow(grid.T);

def computeDistances(pos):
    return np.sum(pdist(pos))


def solve(numberIters):
    pos = np.zeros([nPoints, 2], dtype=int)
    vel = np.zeros([nPoints, 2], dtype=int)

    for i in range(nPoints):
        point = data[i].split('position=<')[1].split('> velocity=<')
        pos[i] = [int(x) for x in point[0].split(', ')]
        vel[i] = [int(x) for x in point[1][:-1].split(', ')]

    dispersions = []
    for t in range(numberIters):
        maxDim = np.max(np.abs(pos))
        dispersions.append(computeDistances(pos))
        iterate(pos, vel)
    
    return dispersions, pos


dispersions, _ = solve(20000)  
nIter = np.argmin(dispersions)
_, pos = solve(nIter)
plot(pos, )

solution = 'FPZKLJZG'
print(solution)

