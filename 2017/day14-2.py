import numpy as np
from day10_2 import computeHash


def DFS(x, y, region=[]):
    grid[x][y] = 0;
    # Iterate over neighbours
    for delta in deltas:
        newPos = np.array([x, y]) + delta
        if grid[newPos[0], newPos[1]] == 1:
            region.extend(newPos)
            DFS(newPos[0], newPos[1], region)
    return region

inputCode = "xlqgujun"
hashes = [computeHash(list(range(256)), inputCode + "-{}".format(i)) for i in range(128)]
binHashes = ["".join([bin(int(letter, 16))[2:].zfill(4) for letter in hash_]) for hash_ in hashes]

n = 128
deltas = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])

# Put everything in a grid with a layer of zero padding
grid = np.zeros([n+2, n+2])
for i in range(1, n+1):
    for j in range(1, n+1):
        if binHashes[i-1][j-1] == '1':
            grid[i][j] = 1

# Solve
regions = []
for i in range(1, n+1):
    for j in range(1, n+1):
        if grid[i][j] == 1:
            regions.append(DFS(i, j, []))
print("Result = {}".format(len(regions)))
