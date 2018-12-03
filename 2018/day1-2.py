import numpy as np


data = np.loadtxt('day1.txt', dtype='int')
sequence = np.cumsum(list(data) * 1000)

aset = set()
for element in sequence:
    if element in aset:
        print(element)
        break
    else:   
        aset.add(element)
