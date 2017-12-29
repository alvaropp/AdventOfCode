with open("day18.txt") as f:
    instructions = [x.strip() for x in f.readlines()]

lastPlayed = None
i = 0

regs = {chr(i): 0 for i in range(97, 117)}
while i < len(instructions):
    instruct = instructions[i].split()
    op = instruct[0]
    reg = instruct[1]
    if len(instruct) == 3:
        val = instruct[2]
    else:
        val = None

    if op == "snd":
        try:
            reg = int(reg)
        except:
            reg = regs[reg]
        lastPlayed = reg
    if op == "set":
        try:
            val = int(val)
            regs[reg] = val
        except:
            regs[reg] = regs[val]
    if op == "add":
        try:
            regs[reg] += int(val)
        except:
            regs[reg] += regs[val]
    if op == "mul":
        try:
            val = int(val)
            regs[reg] *= val
        except:
            regs[reg] *= regs[reg]
    if op == "mod":
        try:
            val = int(val)
            regs[reg] = regs[reg] % val
        except:
            regs[reg] = regs[reg] % regs[val]
    if op == "rcv":
        # Get X value
        try:
            reg = int(reg)
        except:
            reg = regs[reg]
        # Do
        if reg > 0:
            print("Recovered =", lastPlayed)
            i = len(instructions)
            break
    if op == "jgz":
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
        if reg > 0:
            i += val
        else:
            i += 1
    if op != "jgz":
        i += 1

