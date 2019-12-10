import matplotlib.pyplot as plt
import numpy as np


width = 25
height = 6

with open("day8.txt") as f:
    data = np.fromstring(" ".join(f.readline().strip()), dtype=int, sep=" ").reshape(
        [-1, width, height]
    )

pic = np.zeros([width, height])
for i in range(width):
    for j in range(height):
        pic[i, j] = data[np.where(data[:, i, j] != 2)[0][0], i, j]

plt.imshow(pic.reshape(height, width))
