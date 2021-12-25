with open("day7.txt", "r") as f:
    positions = [int(n) for n in f.readline().split(",")]


fuels_to_pos = [
    sum(abs(target_pos - position) for position in positions)
    for target_pos in range(max(positions))
]
print(f"Part one: {min(fuels_to_pos)}")

fuels_to_pos = [
    sum(sum(range(1, abs(target_pos - position) + 1)) for position in positions)
    for target_pos in range(max(positions))
]
print(f"Part two: {min(fuels_to_pos)}")
