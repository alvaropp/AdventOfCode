import numpy as np


def compute_fuel(mass):
    fuel = np.floor(mass / 3) - 2
    if fuel > 0:
        return fuel + compute_fuel(fuel)
    return 0


print(np.sum([compute_fuel(mass) for mass in np.genfromtxt("day1.txt")]))
