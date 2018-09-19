import numpy as np
import gmpy2
import queue


# Code partially based on the great solution by *godarderik*
# https://www.reddit.com/r/adventofcode/comments/5i1q0h/2016_day_13_solutions/


def checkEmptySpace(node):
    x, y = int(node[0]), int(node[1])
    num1Bits = gmpy2.popcount(x*x + 3*x + 2*x*y + y + y*y + magicNum)
    return num1Bits % 2 - 1


def bfs():
    explored = {}
    q = queue.Queue()
    q.put(start)

    explored[(start[0], start[1])] = start[2]
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while not q.empty():
        current = q.get()
        for move in moves:
            following = (current[0] + move[0], current[1] + move[1], current[2] + 1)
            if (not ((following[0], following[1]) in explored)) and (checkEmptySpace(following)) and \
               (following[0] >= 0) and (following[1] >= 0):
                explored[following[0], following[1]] = current[2] + 1
                q.put(following)

    return explored


magicNum = 1352
start = (1, 1, 0)
end = (31, 39)
explored = bfs()

print("Solution is:", explored[(31, 39)])
