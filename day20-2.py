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

for i in range(50):
    v += a
    x += v
    
    # Collisions
    inds = []
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if all(x[i] == x[j]):
                inds.append(i)
                inds.append(j)
    x = np.delete(x, inds, 0)
    v = np.delete(v, inds, 0)
    a = np.delete(a, inds, 0)

print("Result =", len(x))
