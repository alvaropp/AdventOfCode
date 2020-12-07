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


def are_connected(graph, start, end):
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


count = sum(
    1 for bag in bags if (bag != my_bag) and are_connected(rules_graph, bag, my_bag)
)
print(count)
