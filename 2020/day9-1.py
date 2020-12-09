from collections import deque
from itertools import combinations

n_numbers = 25

with open("day9.txt", "r") as f:
    numbers = [*map(int, f.read().splitlines())]


current_numbers = deque(numbers[:n_numbers])
invalid_number = None

for new_number in numbers[n_numbers:]:
    available_sums = [sum(_sum) for _sum in combinations(current_numbers, 2)]
    if new_number in available_sums:
        current_numbers.append(new_number)
    else:
        invalid_number = new_number
        break
    _ = current_numbers.popleft()

print(invalid_number)
