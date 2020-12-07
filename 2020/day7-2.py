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
my_bag = "shiny gold"


def count_bags_dfs(graph, start):
    """DFS. `queue` contains (node, multiplier) tuples."""
    total_bags = 0
    queue = [(start, 1)]
    while len(queue):
        at, multiplier = queue.pop()
        total_bags += multiplier
        for next in graph[at].keys():
            queue.append((next, multiplier * graph[at][next]))
    return total_bags - 1  # we are also counting the outer bag, so remove one


count = count_bags_dfs(rules, my_bag)
print(count)
