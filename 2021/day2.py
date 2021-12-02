with open("day2.txt", "r") as f:
    instructions = [line.strip().split(" ") for line in f.readlines()]

depth = 0
position = 0

for instruction in instructions:
    if instruction[0] == "down":
        depth += int(instruction[1])
    elif instruction[0] == "up":
        depth -= int(instruction[1])
    elif instruction[0] == "forward":
        position += int(instruction[1])

print(f"Part 1: {depth * position}")


aim = 0
depth = 0
position = 0

for instruction in instructions:
    if instruction[0] == "down":
        aim += int(instruction[1])
    elif instruction[0] == "up":
        aim -= int(instruction[1])
    elif instruction[0] == "forward":
        position += int(instruction[1])
        depth += aim * int(instruction[1])

print(f"Part 2: {depth * position}")
