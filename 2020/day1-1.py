with open("day1.txt", "r") as f:
    data = [int(number[:-1]) for number in f.readlines()]

for i, n1 in enumerate(data):
    for j, n2 in enumerate(data[i:]):
        if n1 + n2 == 2020:
            print(n1 * n2)
