# Don't know much about compilers, etc. so had to look online!
# by inspecting the input I directly replaced looped-additions with
# new instructions: mul and nop.

def parse_instruction(idx, inst):
    inst = inst.split()
    if len(inst) == 1:
        command = inst[0]
    if len(inst) < 4:
        try:
            arg1 = inst[1]
            arg2 = inst[2]
        except:
            arg2 = None
    else:
        arg1 = inst[1]
        arg2 = inst[2]
        arg3 = inst[3]

    command = inst[0]
    jump = None
    if command == "nop":  # optimise in order to be able to run part 2
        pass
    elif command == "cpy":
        try:
            arg1 = int(arg1)
        except:
            arg1 = regs[arg1]
        regs[arg2] = arg1
    elif command == "inc":
        regs[arg1] += 1
    elif command == "dec":
        regs[arg1] -= 1
    elif command == "mul":  # optimise in order to be able to run part 2
        regs[arg1] += abs(regs[arg2] * regs[arg3])
    elif command == "jnz":
        try:
            arg2 = int(arg2)
        except:
            arg2 = regs[arg2]
        if arg1.isdigit() and int(arg1) != 0:
            jump = int(arg2)
        elif regs[arg1] != 0:
            jump = int(arg2)
    elif command == "tgl":
        try:
            arg1 = int(arg1) if arg1.isdigit() else regs[arg1]
            inst_to_modify = instructions[idx + arg1].split(" ")
            inst_to_modify[0] = toggle_dict[inst_to_modify[0]]
            instructions[idx + arg1] = " ".join(inst_to_modify)
        except:
            pass

    return jump


def solve(regs, instructions):
    idx = 0
    while idx < len(instructions):
        (instructions[idx])
        jump = parse_instruction(idx, instructions[idx])
        idx += 1 if jump is None else jump

    return regs["a"]


# %%
toggle_dict = {"inc": "dec", "dec": "inc", "tgl": "inc", "jnz": "cpy", "cpy": "jnz"}
regs = {"a": 12}

with open("day23-2.txt", "r") as f:
    instructions = f.read().splitlines()

solve(regs, instructions)
