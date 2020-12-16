import re


def ticket_valid(ticket, rules):
    valid_fields = [False] * len(ticket)
    for idx, value in enumerate(ticket):
        for rule in rules:
            for ranges in rule:
                if ranges[0] <= value <= ranges[1]:
                    valid_fields[idx] = True
    if all(valid_fields):
        return 0
    idx = valid_fields.index(False)
    return ticket[idx]


with open("day16.txt", "r") as f:
    data = f.read().splitlines()

rules = []
line_idx = 0
while data[line_idx] != "":
    ranges = re.findall("(\d+)", data[line_idx])
    rules_ = [[int(ranges[i]), int(ranges[i + 1])] for i in range(0, len(ranges), 2)]
    rules.append(rules_)
    line_idx += 1

nearby_tickets_line = data.index("nearby tickets:")
nearby_tickets = [
    [*map(int, ticket.split(","))] for ticket in data[nearby_tickets_line + 1 :]
]

print(sum(ticket_valid(ticket, rules) for ticket in nearby_tickets))
