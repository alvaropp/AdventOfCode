# %%
from itertools import product
from collections import defaultdict

# %%
def join_rules(rules, numbers):
    return [
        "".join(pair) for pair in product(*(rules[int(number)] for number in numbers))
    ]

def compute_rules(data):
    rules = defaultdict(list)

    populating_rules_0 = 0
    while populating_rules_0 < 4:
        for line in data[:n_rules]:
            i = int(line.split(":")[0])
            if '"' in line:
                rules[i] = [line[-2]]
            elif "|" in line:
                numbers_1 = line.split(":")[1].split("|")[0].split()
                if all(len(rules[int(number)]) > 0 in rules for number in numbers_1):
                    rules[i].extend(join_rules(rules, numbers_1))
                numbers_2 = line.split(":")[1].split("|")[1].split()
                if all(len(rules[int(number)]) > 0 in rules for number in numbers_2):
                    rules[i].extend(join_rules(rules, numbers_2))
                rules[i] = list(set(rules[i]))
            else:
                numbers = line.split(":")[1].split()
                if all(len(rules[int(number)]) > 0 in rules for number in numbers):
                    rules[i] = join_rules(rules, numbers)
                    if i == 0:
                        populating_rules_0 += 1
                rules[i] = list(set(rules[i]))
    rules[0] = set(rules[0])
    return rules
# %%
with open("day19.txt", "r") as f:
    data = f.read().splitlines()

n_rules = data.index("")
# %%
rules = compute_rules(data[:n_rules])
# %%
messages = data[n_rules + 1 :]

print(len([message for message in messages if message in rules[0]]))
# %%
