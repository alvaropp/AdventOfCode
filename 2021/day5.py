# %%
import re
from dataclasses import dataclass

import numpy as np


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int



lines = []
max_coord = 0
with open("day5.txt", "r") as f:
    for line in f:
        line_coords = list(map(int, re.findall(r"\d+", line)))
        max_coord = max(max_coord, max(line_coords))
        lines.append(Line(*line_coords))


hor_or_ver_lines = [
    line for line in lines if ((line.x1 == line.x2) or (line.y1 == line.y2))
]

grid = np.zeros([max_coord + 1, max_coord + 1])
for line in hor_or_ver_lines:
    xs = sorted([line.x1, line.x2])
    ys = sorted([line.y1, line.y2])
    grid[ys[0] : ys[1] + 1, xs[0] : xs[1] + 1] += 1

print(f"Part 1: {sum(sum(grid > 1))}")


diag_lines = [line for line in lines if line not in hor_or_ver_lines]

for line in diag_lines:
    delta_x = line.x2 - line.x1
    delta_y = line.y2 - line.y1
    steps = abs(delta_x) + 1
    for step in range(steps):
        grid[line.y1 + step * np.sign(delta_y), line.x1 + step * np.sign(delta_x)] += 1

print(f"Part 2: {sum(sum(grid > 1))}")
