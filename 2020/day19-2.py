# I solved part 1 in a brittle way and couldn't get it to work for part 2,
# so had a look at Reddit and adapted someone's approach:

import re

with open("day19.txt", "r") as f:
    data = f.read().splitlines()

n_rules = data.index("")
list_rules = data[:n_rules]
messages = data[n_rules + 1 :]

rules = {}
for rule in list_rules:
    name, rule = rule.split(": ")
    rules[name] = rule.split()

# Add part-2 changes
rules["8"] = ["42", "|", "42", "8"]
rules["11"] = ["42", "31", "|", "42", "11", "31"]


def resolve_rule(rules, i, depth=0):
    s = ""
    for r in rules[i]:
        if r.isdigit():
            if r == i:
                depth += 1
            if depth != max_depth:
                s += resolve_rule(rules, r, depth)
        elif r == "|":
            s += r
        else:
            s += re.search(r'"([ab])"', r)[1]
    return "(?:{})".format(s)


max_depth = (
    5  # found experimentally: number of matched messages plateaus for max_depth >= 5
)
regex_0 = resolve_rule(rules, "0")

print(len([message for message in messages if re.match(f"^{regex_0}$", message)]))
