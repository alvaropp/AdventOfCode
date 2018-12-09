import numpy as np
import collections


with open('day6.txt') as f:
    data = f.read().splitlines()
coords = np.array([(int(entry.split(', ')[0]), int(entry.split(', ')[1])) for entry in data])

nCoords = len(coords)
dim = max(max(coords[:, 0]), max(coords[:, 1]))
grid = np.zeros([dim, dim], dtype=int)


for i in range(dim):
    for j in range(dim):
        dists = np.zeros(nCoords)
        for k, coord in enumerate(coords):
            dists[k] = abs(coord[0] - i) + abs(coord[1] - j)
        if sum(dists == min(dists)) == 1:
            grid[i, j] = np.argmin(dists)

# Find groups in the boundaries and exclude them (they're infinite)
excluded = set(list(grid[0, :]) + list(grid[-1, :]) + list(grid[:, 0]) + list(grid[:, -1]))
_, counts = np.unique(grid, return_counts=True)


result = 0
for i in range(nCoords):
    if i not in excluded:
        if counts[i] > result:
            result = counts[i]
print(result)

