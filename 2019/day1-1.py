import numpy as np

print(np.sum([np.floor(mass / 3) - 2 for mass in np.genfromtxt("day1.txt")]))

