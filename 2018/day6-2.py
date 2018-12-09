import collections


with open('day6.txt') as f:
    data = f.read().splitlines()
coords = np.array([(int(entry.split(', ')[0]), int(entry.split(', ')[1])) for entry in data])

maxDist = 10000

nCoords = len(coords)
dim = max(max(coords[:, 0]), max(coords[:, 1]))
grid = np.zeros([dim, dim], dtype=int)

counter = 0
for i in range(dim):
    for j in range(dim):
        dists = np.zeros(nCoords)
        for k, coord in enumerate(coords):
            dists[k] = abs(coord[0] - i) + abs(coord[1] - j)
        if sum(dists) < maxDist:
            counter += 1

print(counter)

