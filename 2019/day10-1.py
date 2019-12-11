import numpy as np
from numpy.linalg import norm


def find_duplicate_angles(angles):
    # https://stackoverflow.com/a/30003565/6109283
    _, inverse, count = np.unique(angles, return_inverse=True, return_counts=True)
    idx_vals_repeated = np.where(count > 1)[0]
    rows, cols = np.where(inverse == idx_vals_repeated[:, np.newaxis])
    _, inverse_rows = np.unique(rows, return_index=True)
    res = np.split(cols, inverse_rows[1:])
    return res


with open("day10.txt") as f:
    data = [line.strip() for line in f.readlines()]

data = np.array([[point for point in line] for line in data])

asteroids = [(i, j) for i, j in zip(*np.where(data == "#"))]
n = len(asteroids)
seen = np.ones([n, n])

for i in range(n):
    others = [j for j in range(n) if j != i]

    dists = np.array(
        [norm(np.array(asteroids[i]) - np.array(asteroids[j])) for j in others]
    )
    angles = [
        np.arctan2(
            np.array([asteroids[i][0] - asteroids[j][0]]),
            np.array([asteroids[i][1] - asteroids[j][1]]),
        )[0]
        for j in others
    ]

    for duplicates in find_duplicate_angles(angles):
        seen[i][duplicates] = 0
        seen[i][duplicates[np.argmin(dists[duplicates])]] = 1

    seen[i][i] = 0

print(int(np.max(np.sum(seen, axis=1))))
