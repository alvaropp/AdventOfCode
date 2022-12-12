calories = []

current_calories = 0
for line in open("day1.txt"):
    if line == "\n":
        calories.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(line)
calories.append(current_calories)

calories = sorted(calories, reverse=True)

print(f"Part one: {calories[0]}")
print(f"Part two: {sum(calories[:3])}")
