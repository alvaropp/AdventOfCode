import time


with open("day5.txt") as f:
    maze = f.readlines()
    maze = [int(x.strip()) for x in maze]

pos = 0
jumps = 0
t0 = time.time()
while pos >= 0 and pos < len(maze):
    if maze[pos] >= 3:
        maze[pos] -= 1
        pos = pos + maze[pos] + 1
    else:
        maze[pos] += 1
        pos = pos + maze[pos] - 1
    jumps += 1
t1 = time.time()

print("Solution = ", jumps)
print("Elapsed time = ", t1-t0)
