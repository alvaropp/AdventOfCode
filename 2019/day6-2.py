from collections import defaultdict

import numpy as np


def get_orbit(string):
    return string.split(")")


with open("day6.txt") as f:
    data = [line.strip() for line in f.readlines()]

graph = defaultdict(list)
for datum in data:
    o1, o2 = get_orbit(datum)
    graph[o2].append(o1)
    graph[o1].append(o2)


start = "YOU"
end = "SAN"

distances = {thing: float("inf") for thing in graph.keys()}
distances[start] = 0

to_visit = [start]
while distances[end] == float("inf"):
    at = to_visit.pop()
    for place in graph[at]:
        if distances[place] == float("inf"):
            to_visit.append(place)
            distances[place] = distances[at] + 1

print(distances["SAN"] - 2)
