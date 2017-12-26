with open("day23.txt") as f:
    instructions = [x.strip() for x in f.readlines()]
regs = {chr(i): 0 for i in range(97, 105)}

i = 0
timesMul = 0
while i < len(instructions) and i >= 0:
    instruct = instructions[i].split()
    op = instruct[0]
    reg = instruct[1]
    if len(instruct) == 3:
        val = instruct[2]
    else:
        val = None

    if op == "set":
        try:
            val = int(val)
            regs[reg] = val
        except:
            regs[reg] = regs[val]
    elif op == "sub":
        try:
            regs[reg] -= int(val)
        except:
            regs[reg] -= regs[val]
    elif op == "mul":
        timesMul += 1
        try:
            val = int(val)
            regs[reg] *= val
        except:
            regs[reg] *= regs[reg]
    elif op == "jnz":
        # Get X value
        try:
            reg = int(reg)
        except:
            reg = regs[reg]
        # Get Y value
        try:
            val = int(val)
        except:
            val = regs[val]
        # Do
        if reg != 0:
            i += val
        else:
            i += 1
    if op != "jnz":
        i += 1

print("Result =", timesMul)

