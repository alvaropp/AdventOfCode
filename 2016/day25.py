def get_value(x):
    try:
        return int(x)
    except:
        return regs[x]


def parse_instruction(inst):
    inst = inst.split()
    command = inst[0]

    args = inst[1:]

    jump = None
    out = None
    if command == "cpy":
        regs[args[1]] = get_value(args[0])
    elif command == "inc":
        regs[args[0]] += 1
    elif command == "dec":
        regs[args[0]] -= 1
    elif command == "jnz":
        if get_value(args[0]) != 0:
            jump = get_value(args[1])
    elif command == "out":
        out = regs["b"]

    return jump, out


with open("day25.txt", "r") as f:
    instructions = f.read().splitlines()

length = 4

integer = 0
while True:
    regs = {"a": integer, "b": 0, "c": 0, "d": 0}

    signal = []
    idx = 0
    while (len(signal) < 2 * length) and (idx < len(instructions)):
        jump, out = parse_instruction(instructions[idx])
        if out is not None:
            signal.append(out)
        idx += 1 if jump is None else jump
    if signal == [0, 1] * length:
        break
    integer += 1

print(integer)
