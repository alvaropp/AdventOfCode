from functools import lru_cache

with open("day10.txt", "r") as f:
    adapters = sorted([*map(int, f.read().splitlines())])

# Add start (wall) and end (devide) points
adapters = [0] + adapters + [max(adapters) + 3]


@lru_cache(maxsize=None)
def find_all_arrangements_after(adapter):
    """Find all possible arrangements from a given adapter."""
    if adapter == adapters[-1]:
        # we have reached the end
        return 1

    adapter_index = adapters.index(adapter)

    next_adapters = [
        adapters[adapter_index + i]
        for i in range(1, 4)
        if (adapter_index + i < len(adapters))
        and ((adapters[adapter_index + i] - adapter) <= 3)
    ]

    return sum(
        find_all_arrangements_after(next_adapter) for next_adapter in next_adapters
    )


print(find_all_arrangements_after(0))
