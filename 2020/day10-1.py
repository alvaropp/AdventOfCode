import numpy as np


with open("day10.txt", "r") as f:
    adapters = [0] + sorted([*map(int, f.read().splitlines())])
adapters += [adapters[-1] + 3]
adapters = np.array(adapters)

_, counts = np.unique(np.diff(adapters), return_counts=True)
print(np.prod(counts))
