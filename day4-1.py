result = 0

with open("day4.txt") as f:
    for line in f.readlines():
        words = line.strip().split(" ")
        if len(words) == len(set(words)):
            result += 1

print("Result = ", result)
