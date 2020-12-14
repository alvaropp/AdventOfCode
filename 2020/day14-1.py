import re

with open("day14.txt", "r") as f:
    data = f.read().splitlines()


def apply_mask(mask, value):
    binary_value = f"{value:>036b}"
    masked_value = "".join(
        value if mask_value == "X" else mask_value
        for value, mask_value in zip(binary_value, mask)
    )
    return int(masked_value, 2)


memory = {}
for line in data:
    if "mask" in line:
        mask = line.split(" = ")[-1]
    else:
        address, value = re.findall("(\d+)", line)
        memory[address] = apply_mask(mask, int(value))

print(sum(memory.values()))

