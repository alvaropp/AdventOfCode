import numpy as np


with open("day1.txt", "r") as f:
    data = [int(line.strip()) for line in f.readlines()]

print(f"Part 1: {sum(np.diff(data) > 0)}")
print(f"Part 2: {sum(np.diff(np.convolve(data, np.ones(3, dtype=int), 'valid')) > 0)}")
