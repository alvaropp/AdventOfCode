import numpy as np


def getMeasurements(entry):
    entry = entry.split('@ ')[1]
    padLeft, padTop = entry.split(': ')[0].split(',')
    width, height = entry.split(': ')[1].split('x')
    return int(padLeft), int(padTop), int(width), int(height)


fabric = np.zeros([1000, 1000])

with open('day3.txt') as f:
    data = f.read().splitlines()

for entry in data:
    padLeft, padTop, width, height = getMeasurements(entry)
    fabric[padLeft:padLeft+width, padTop:padTop+height] += 1

print(len(np.where(fabric > 1)[0]))
