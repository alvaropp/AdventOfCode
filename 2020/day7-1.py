with open("day7.txt", "r") as f:
    rules = f.read().splitlines()

bags = [" ".join(bag.split(" ", 2)[:2]) for bag in rules]
options = [
    [
        " ".join(bag.strip().split(" ", 3)[:-1])
        for bag in rule.split("contain ")[1].split(",")
    ]
    for rule in rules
]
options = [[bag.split(" ", 1)[::-1] for bag in option] for option in options]
options = [
    {bag[0]: int(bag[1]) if "no" not in bag[1] else None for bag in option}
    for option in options
]
rules = {
    bag: options if "other" not in options else {}
    for bag, options in zip(bags, options)
}


def find_connection_path(graph, start, end):
    """DFS."""
    visited = set()
    q = [start]
    while len(q):
        at = q.pop()
        visited.add(at)
        for next in graph[at].keys():
            if next not in visited:
                q.append(next)
    return end in visited


my_bag = "shiny gold"

count = sum(
    1 for bag in bags if (bag != my_bag) and find_connection_path(rules, bag, my_bag)
)
print(count)
