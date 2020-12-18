def solve_expression(expression):
    total = 0
    previous_op = None
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            if previous_op is None or previous_op == "+":
                total += int(expression[i])
            elif previous_op == "*":
                total *= int(expression[i])
            i += 1
        elif expression[i] in "+*":
            previous_op = expression[i]
            i += 1
        elif "(" in expression[i]:
            n_open_brackets = expression[i].count("(")
            j = i
            while n_open_brackets > 0:
                j += 1
                if "(" in expression[j]:
                    n_open_brackets += expression[j].count("(")
                if ")" in expression[j]:
                    n_open_brackets -= expression[j].count(")")
                if n_open_brackets == 0:
                    subexpression = expression[i : j + 1]
                    subexpression[0] = subexpression[0][1:]
                    subexpression[-1] = subexpression[-1][:-1]
                    subtotal = solve_expression(subexpression)
                    if previous_op is None or previous_op == "+":
                        total += int(subtotal)
                    elif previous_op == "*":
                        total *= int(subtotal)
                    i = j + 1
    return total


with open("day18.txt", "r") as f:
    expressions = f.read().strip().splitlines()

print(sum(solve_expression(expression.split(" ")) for expression in expressions))
