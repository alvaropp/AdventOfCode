with open("day20.txt", "r") as f:
    ips = [tuple(map(int, line.split("-"))) for line in f.read().splitlines()]

limits = [[0, 4294967295]]
numbers_found = []

for ip_range in ips:
    start, end = ip_range

    new_limits = []
    to_remove = []
    for limit in limits:
        if (start < limit[0]) and (limit[0] <= end < limit[1]):
            new_limits.append([end + 1, limit[1]])
            to_remove.append(limit)

        if (start < limit[0]) and (end == limit[1]):
            to_remove.append(limit)

        if (start == limit[0]) and (limit[1] < end):
            to_remove.append(limit)

        if (limit[0] < start <= limit[1]) and (limit[1] < end):
            new_limits.append([limit[0], start - 1])
            to_remove.append(limit)

        if (start == limit[0]) and (end == limit[1]):
            to_remove.append(limit)

        if (start < limit[0]) and (end > limit[1]):
            to_remove.append(limit)

        if (limit[0] <= start < limit[1]) and (limit[0] < end <= limit[1]):
            new_limits.append([limit[0], start - 1])
            new_limits.append([end + 1, limit[1]])
            to_remove.append(limit)

    for limit in to_remove:
        try:
            limits.remove(limit)
        except:
            pass

    new_limits_equal = [
        new_limit[0] for new_limit in new_limits if new_limit[0] == new_limit[1]
    ]
    new_limits_non_equal = [
        new_limit for new_limit in new_limits if new_limit[0] != new_limit[1]
    ]
    numbers_found.extend(new_limits_equal)
    limits.extend(new_limits_non_equal)

print(min(numbers_found))
