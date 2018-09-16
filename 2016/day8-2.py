import numpy as np
import re
import matplotlib.pyplot as plt


def loadData(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data

def exe1(A, B):
    grid[:B, :A] = 1

def exe2(y, A):
    grid[y, :] = np.roll(grid[y, :], A)
    
def exe3(x, A):
    grid[:, x] = np.roll(grid[:, x], A)

def parseInstruction(s):
    s = s.split()
    if s[0] == 'rect':
        A, B = s[1].split('x')
        exe1(int(A), int(B))
    elif s[1] == 'row':
        A = s[-1]
        y = s[2].split('=')[-1]
        exe2(int(y), int(A))
    elif s[1] == 'column':
        A = s[-1]
        x = s[2].split('=')[-1]
        exe3(int(x), int(A))


grid = np.zeros([6, 50])
data = loadData('2016/day8.txt')

for instruction in data:
    parseInstruction(instruction)

plt.imshow(grid)
