import numpy as np


def iterate(value, factor, divisor):
    while True:
        value = (value*factor)%2147483647
        if value%divisor == 0:
            return value

def solve(valueA, valueB):
    factorA = 16807
    factorB = 48271
    divisorA = 4
    divisorB = 8

    matches = 0
    for t in range(int(5e6)):
        valueA = iterate(valueA, factorA, divisorA)
        valueB = iterate(valueB, factorB, divisorB)
        if format(valueA, '#034b')[-16:] == format(valueB, '#034b')[-16:]:
            matches += 1
    return matches

valueA = 722
valueB = 354
print("Result =", solve(valueA, valueB))
