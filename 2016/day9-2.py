import numpy as np
import re


def loadData(file):
    with open(file, 'r') as f:
        data = f.readline()
    return data[:-1]

def decompress(data):
    sol = 0
    i = 0
    while i < len(data):
        if data[i] == "(":
            end = data[i:].find(')')
            numChars, mult = data[i+1:i+end].split('x')
            sol += int(mult)*decompress(data[i+end+1:i+end+1+int(numChars)])
            i += int(numChars) + end + 1
        else:
            sol += 1
            i += 1
    return sol


data = loadData('2016/day9.txt')
data[:100]
decompress(data)
