with open("day2.txt", "r") as f:
    problem_input = [pwd.split("\n")[0] for pwd in f.readlines()]
    counts = [[*map(int, item.split(" ")[0].split("-"))] for item in problem_input]
    letters = [item.split(": ")[0][-1] for item in problem_input]
    pwds = [item.split(": ")[-1] for item in problem_input]


def check_pwd(data):
    pwd, count, letter = data
    return (pwd[count[0] - 1] == letter) != (pwd[count[1] - 1] == letter)


print(sum([*map(check_pwd, zip(pwds, counts, letters))]))
