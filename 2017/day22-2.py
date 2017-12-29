import numpy as np


# 0: clean
# 1: weakened
# 2: infected
# 3: flagged

def iterate(pos, direc, totalInfected, nIter):
    for t in range(nIter):
        # Turn
        if grid[int(pos[0]), int(pos[1])] == 0:
            # Clean, turn left
            direc = turnL[direc]
        elif grid[int(pos[0]), int(pos[1])] == 2:
            # Infected, turn right
            direc = turnR[direc]
        elif grid[int(pos[0]), int(pos[1])] == 3:
            # Reverae
            direc = reverse[direc]

        # Change status
        if grid[int(pos[0]), int(pos[1])] == 0:
            grid[int(pos[0]), int(pos[1])] = 1
        elif grid[int(pos[0]), int(pos[1])] == 1:
            grid[int(pos[0]), int(pos[1])] = 2
            totalInfected += 1
        elif grid[int(pos[0]), int(pos[1])] == 2:
            grid[int(pos[0]), int(pos[1])] = 3
        elif grid[int(pos[0]), int(pos[1])] == 3:
            grid[int(pos[0]), int(pos[1])] = 0
        # Move
        pos += dirs[direc]
    return totalInfected


with open("day22.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

grid_ = np.zeros([len(data), len(data)])
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "#":
            grid_[i][j] = 2
# Add padding
grid = np.pad(grid_, 3000, 'constant')

dirs = {'u': np.array([-1, 0]), 'd': np.array([1, 0]), 'l': np.array([0, -1]), 'r': np.array([0, 1])}
turnR = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
turnL = {'u': 'l', 'l': 'd', 'd': 'r', 'r': 'u'}
reverse = {'u': 'd', 'l': 'r', 'd': 'u', 'r': 'l'}

# Pos and dir
pos = np.array([int(np.floor(len(grid)/2)), int(np.floor(len(grid)/2))])
direc = 'u'

# Run
nIter = 10000000
totalInfected = iterate(pos, direc, 0, nIter)
print("Result =", totalInfected)

