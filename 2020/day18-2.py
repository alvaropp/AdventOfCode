def solve_expression(expression):
    ops = []
    values = []

    for symbol in expression:
        if symbol.isdigit():
            values.append(int(symbol))
        elif symbol == "(":
            ops.append("(")
        elif symbol == ")":
            while True:
                v1 = values.pop()
                v2 = values.pop()
                op = ops.pop()
                values.append(eval(f"{v1} {op} {v2}"))
                if ops[-1] == "(":
                    ops.pop()
                    break
        elif symbol == "+":
            ops.append("+")
        elif symbol == "*":
            while True:
                if not ops or ops[-1] != "+":
                    break
                v1 = values.pop()
                v2 = values.pop()
                op = ops.pop()
                values.append(eval(f"{v1} {op} {v2}"))
            ops.append("*")

    while len(values) > 1:
        v1 = values.pop()
        v2 = values.pop()
        op = ops.pop()
        values.append(eval(f"{v1} {op} {v2}"))

    return values[0]


with open("day18.txt", "r") as f:
    expressions = f.read().strip().splitlines()

total = 0
for expression in expressions:
    expression = [item for sublist in expression for item in sublist]
    total += solve_expression(expression)

print(total)
