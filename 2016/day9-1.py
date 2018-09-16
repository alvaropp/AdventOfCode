import numpy as np
import re


def loadData(file):
    with open(file, 'r') as f:
        data = f.readline()
    return data[:-1]

data = loadData('day9.txt')
sol = ''

i = 0
while i < len(data):
    if data[i] == "(":
        end = data[i:].find(')')
        numChars, mult = data[i+1:i+end].split('x')
        sol += data[i+end+1:i+end+1+int(numChars)] * int(mult)
        i += int(numChars) + end + 1
    else:
        sol += data[i]
        i += 1

print(len(sol))
