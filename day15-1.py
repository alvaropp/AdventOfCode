import numpy as np


def iterate(value, factor):
    return (value*factor)%2147483647

def solve(valueA, valueB):
    factorA = 16807
    factorB = 48271

    matches = 0
    for t in range(40000000):
        valueA = (valueA*factorA)%2147483647
        valueB = (valueB*factorB)%2147483647
        if format(valueA, '#034b')[-16:] == format(valueB, '#034b')[-16:]:
            matches += 1
    return matches

valueA = 722
valueB = 354
print("Result =", solve(valueA, valueB))
