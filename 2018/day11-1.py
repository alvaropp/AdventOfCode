import numpy as np
from scipy import signal


with open('day11.txt') as f:
    serialNumber = int(f.read().splitlines()[0])


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


kernel = np.ones([3, 3])
grid = signal.convolve2d(grid, kernel)

print(np.array(np.unravel_index(np.argmax(grid, axis=None), grid.shape)) - 2)

