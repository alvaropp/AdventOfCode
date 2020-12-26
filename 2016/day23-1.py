def parse_instruction(idx, inst):
    inst = inst.split()
    command = inst[0]
    arg1 = inst[1]
    try:
        arg2 = inst[2]
    except:
        arg2 = None

    jump = None
    if command == "cpy":
        try:
            arg1 = int(arg1)
        except:
            arg1 = regs[arg1]
        regs[arg2] = arg1
    elif command == "inc":
        regs[arg1] += 1
    elif command == "dec":
        regs[arg1] -= 1
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


toggle_dict = {"inc": "dec", "dec": "inc", "tgl": "inc", "jnz": "cpy", "cpy": "jnz"}

with open("day23.txt", "r") as f:
    instructions = f.read().splitlines()

instructions
regs = {"a": 7}

idx = 0
while idx < len(instructions):
    jump = parse_instruction(idx, instructions[idx])
    idx += 1 if jump is None else jump

print(regs["a"])
