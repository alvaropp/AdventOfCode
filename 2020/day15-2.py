from collections import defaultdict


def solve(numbers, n_iter):
    number_idx = defaultdict(list)
    [number_idx[number].append(idx) for idx, number in enumerate(numbers)]

    idx = len(numbers)
    last_number = numbers[-1]
    while idx < n_iter:
        if len(number_idx[last_number]) < 2:
            last_number = 0
        else:
            last_number = number_idx[last_number][-1] - number_idx[last_number][-2]
            number_idx[last_number]
        number_idx[last_number].append(idx)
        idx += 1

    return last_number


with open("day15.txt", "r") as f:
    numbers = [int(number) for number in f.read().strip().split(",")]

print(solve(numbers, 30000000))
