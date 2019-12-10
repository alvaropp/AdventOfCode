import numpy as np


width = 25
height = 6

with open("day8.txt") as f:
    data = np.fromstring(" ".join(f.readline().strip()), dtype=int, sep=" ").reshape(
        [-1, width, height]
    )

index = np.argmin(
    [np.unique(data[i], return_counts=True)[1][0] for i in range(len(data))]
)

_, counts = np.unique(data[index], return_counts=True)

print(counts[1] * counts[2])
