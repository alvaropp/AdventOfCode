from collections import deque


with open("day6.txt", "r") as f:
    fish = list(map(int, f.readline().split(",")))

fish_ages = deque([0]*9)
for age in fish:
    fish_ages[age] += 1

for _ in range(80):
    new_fish = fish_ages[0]
    fish_ages.rotate(-1)
    fish_ages[6] += fish_ages[-1]
    fish_ages[-1] = new_fish


print(f"Part 1: {sum(fish_ages)}")

for _ in range(256-80):
    new_fish = fish_ages[0]
    fish_ages.rotate(-1)
    fish_ages[6] += fish_ages[-1]
    fish_ages[-1] = new_fish

print(f"Part 2: {sum(fish_ages)}")
