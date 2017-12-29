with open("day5.txt") as f:
    maze = f.readlines()
    maze = [int(x.strip()) for x in maze]

pos = 0
jumps = 0
while pos >= 0 and pos < len(maze):
    maze[pos] += 1
    pos = pos + maze[pos] - 1
    jumps += 1

print("Solution = ", jumps)
