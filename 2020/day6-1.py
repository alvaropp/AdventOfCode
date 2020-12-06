with open("day6.txt", "r") as f:
    group_answers = [group.replace("\n", "") for group in f.read().split("\n\n")]

print(sum(len(set(answers)) for answers in group_answers))
