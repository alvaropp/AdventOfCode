import re

with open("day7.txt", "r") as f:
    rules = f.read().splitlines()

rules = [rule.replace(" bags contain ", ", ") for rule in rules]
bags = [rule.split(", ")[0] for rule in rules]
options = [
    {pair[1]: int(pair[0]) for pair in re.findall(r"(\d+) (\w+ \w+)", rule)}
    for rule in rules
]
rules_graph = {bag: options for bag, options in zip(bags, options)}

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


count = count_bags_dfs(rules_graph, my_bag)
print(count)
