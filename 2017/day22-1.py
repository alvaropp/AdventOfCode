import numpy as np


with open("day22.txt") as f:
    data = f.readlines()
    data = [x.strip() for x in data]

grid_ = np.zeros([len(data), len(data)])
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "#":
            grid_[i][j] = 1
# Add padding
grid = np.pad(grid_, 200, 'constant')

dirs = {'u': np.array([-1, 0]), 'd': np.array([1, 0]), 'l': np.array([0, -1]), 'r': np.array([0, 1])}
turnR = {'u': 'r', 'r': 'd', 'd': 'l', 'l': 'u'}
turnL = {'u': 'l', 'l': 'd', 'd': 'r', 'r': 'u'}

# Pos and dir
pos = np.array([int(np.floor(len(grid)/2)), int(np.floor(len(grid)/2))])
direc = 'u'

totalInfected = 0
for t in range(10000):
    # Turn
    if grid[int(pos[0]), int(pos[1])]:
        # Infected, turn right
        direc = turnR[direc]
    else:
        # Clean, turn left
        direc = turnL[direc]

    # Change status
    if grid[int(pos[0]), int(pos[1])] == 0:
        grid[int(pos[0]), int(pos[1])] = 1
        totalInfected += 1
    else:
        grid[int(pos[0]), int(pos[1])] = 0

    # Move
    pos += dirs[direc]

print("Result =", totalInfected)

