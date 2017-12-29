import numpy as np


x = []
v = []
a = []

with open("day20.txt") as f:
    data = f.readlines()
    for line in data:
        line = [x.strip()[5:] for x in (", " + line).split(">")][:-1]
        x.append([int(x) for x in line[0].split(',')])
        v.append([int(x) for x in line[1].split(',')])
        a.append([int(x) for x in line[2].split(',')])

x = np.array(x)
v = np.array(v)
a = np.array(a)
dist = np.array([sum(abs(pos)) for pos in x])

for i in range(10000):
    v += a
    x += v
    dist = np.array([sum(abs(pos)) for pos in x])

print("Result =", np.argmin(dist))
