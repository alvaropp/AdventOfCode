from collections import defaultdict, deque

import numpy as np


def get_orbit(string):
    return string.split(")")


def find_dist(name):
    count = 1
    while parent[name] != "COM":
        count += 1
        name = parent[name]
    return count


with open("day6.txt") as f:
    data = [line.strip() for line in f.readlines()]

parent = {}
for datum in data:
    o1, o2 = get_orbit(datum)
    parent[o2] = o1

print(np.sum([find_dist(planet) for planet in parent.keys()]))
