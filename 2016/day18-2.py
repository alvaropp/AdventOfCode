with open("day18.txt", "r") as f:
    row = ["."] + list(f.read().strip()) + ["."]


def span_new_tile(tiles_above):
    left, centre, right = tiles_above
    if (
        (left == "^" and centre == "^" and right != "^")
        or (left != "^" and centre == "^" and right == "^")
        or (left == "^" and centre != "^" and right != "^")
        or (left != "^" and centre != "^" and right == "^")
    ):
        return "^"
    else:
        return "."


def span_new_row(row_above):
    return (
        ["."]
        + [
            span_new_tile(row_above[i - 1 : i + 2])
            for i in range(1, len(row_above) - 1)
        ]
        + ["."]
    )


# Can save memory by counting on the fly and rewriting on the same row,
# but no need here given the size of the problem
all_rows = [row]
for _ in range(400000 - 1):
    all_rows.append(span_new_row(all_rows[-1]))

total_safe_tiles = sum(row.count(".") - 2 for row in all_rows)
print(total_safe_tiles)
