import re
from itertools import product

with open("day14.txt", "r") as f:
    data = f.read().splitlines()


def apply_mask(mask, value):
    # Convert
    binary_value = f"{value:>036b}"
    masked_value = [
        value if mask_value == "0" else "1" if mask_value == "1" else "X"
        for value, mask_value in zip(binary_value, mask)
    ]
    # Deal with floating bits
    floating_bits = [i for i, bit in enumerate(masked_value) if bit == "X"]

    results = []
    for bits in product(range(2), repeat=masked_value.count("X")):
        address = masked_value.copy()
        for idx, bit in enumerate(floating_bits):
            address[bit] = str(bits[idx])
        results.append("".join(address))

    return [int(address, 2) for address in results]


memory = {}
for line in data:
    if "mask" in line:
        mask = line.split(" = ")[-1]
    else:
        address, value = re.findall("(\d+)", line)
        all_addresses = apply_mask(mask, int(address))
        for address in all_addresses:
            memory[address] = int(value)

print(sum(memory.values()))

