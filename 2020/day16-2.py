import re
from collections import defaultdict


def parse_data(data):
    rules = {}
    line_idx = 0
    while data[line_idx] != "":
        name = data[line_idx].split(":")[0]
        ranges = re.findall("(\d+)", data[line_idx])
        rules_ = [
            [int(ranges[i]), int(ranges[i + 1])] for i in range(0, len(ranges), 2)
        ]
        rules[name] = rules_
        line_idx += 1

    nearby_tickets_line = data.index("nearby tickets:")
    nearby_tickets = [
        [*map(int, ticket.split(","))] for ticket in data[nearby_tickets_line + 1 :]
    ]

    my_ticket_idx = data.index("your ticket:")
    my_ticket = [*map(int, data[my_ticket_idx + 1].split(","))]

    return rules, nearby_tickets, my_ticket


def ticket_valid(ticket, rules):
    valid_fields = [False] * len(ticket)
    for idx, value in enumerate(ticket):
        for _, rule in rules.items():
            for ranges in rule:
                if ranges[0] <= value <= ranges[1]:
                    valid_fields[idx] = True
    return all(valid_fields)


def find_valid_tickets(tickets, rules):
    valid_tickets = [*(ticket_valid(ticket, rules) for ticket in tickets)]
    return [ticket for i, ticket in enumerate(tickets) if valid_tickets[i]]


def find_field_names(tickets, rules):
    rules_idx = defaultdict(list)
    for field_idx in range(len(tickets[0])):
        all_values = [ticket[field_idx] for ticket in tickets]
        for name, rule in rules.items():
            valid_values = [False] * len(all_values)
            for idx, value in enumerate(all_values):
                for ranges in rule:
                    if ranges[0] <= value <= ranges[1]:
                        valid_values[idx] = True
            if all(valid_values):
                rules_idx[name].append(field_idx)

    rules_idx = dict(sorted(rules_idx.items(), key=lambda item: len(item[1])))

    final_rules = {}
    used_idx = set()
    for rule, values in rules_idx.items():
        available_values = [value for value in values if value not in used_idx]
        final_rules[rule] = available_values[0]
        used_idx.add(available_values[0])

    return final_rules


with open("day16.txt", "r") as f:
    data = f.read().splitlines()

rules, nearby_tickets, my_ticket = parse_data(data)
valid_tickets = find_valid_tickets(nearby_tickets, rules)
fields = find_field_names(valid_tickets, rules)

final_idx = [v for k, v in fields.items() if "departure" in k]

total = 1
for idx in final_idx:
    total *= my_ticket[idx]

print(total)
