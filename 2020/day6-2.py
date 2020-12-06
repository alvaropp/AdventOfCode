with open("day6.txt", "r") as f:
    group_answers = [group.split("\n") for group in f.read().strip().split("\n\n")]


group_answers = [[set(answer) for answer in answers] for answers in group_answers]

print(sum(len(set.intersection(*answers)) for answers in group_answers))
