with open("day18.txt") as f:
    instructions = [x.strip() for x in f.readlines()]

def step0():
    global i0, end0, waiting0

    instruct = instructions[i0].split()
    op = instruct[0]
    reg = instruct[1]
    if len(instruct) == 3:
        val = instruct[2]
    else:
        val = None

    if op == "snd":
        try:
            reg = int(reg)
            queue1.append(reg)
        except:
            queue1.append(regs0[reg])
    if op == "set":
        try:
            val = int(val)
            regs0[reg] = val
        except:
            regs0[reg] = regs0[val]
    if op == "add":
        try:
            regs0[reg] += int(val)
        except:
            regs0[reg] += regs0[val]
    if op == "mul":
        try:
            val = int(val)
            regs0[reg] *= val
        except:
            regs0[reg] *= regs0[reg]
    if op == "mod":
        try:
            val = int(val)
            regs0[reg] = regs0[reg] % val
        except:
            regs0[reg] = regs0[reg] % regs0[val]
    if op == "rcv":
        if len(queue0) > 0:
            regs0[reg] = queue0.pop(0)
        else:
            waiting0 = 1
            return
    if op == "jgz":
        # Get X value
        try:
            reg = int(reg)
        except:
            reg = regs0[reg]
        # Get Y value
        try:
            val = int(val)
        except:
            val = regs0[val]
        # Do
        if reg > 0:
            i0 += val
        else:
            i0 += 1
    if op != "jgz":
        i0 += 1
    if i0<0 or i0>=len(instructions):
        end0 = 1
    return

def step1():
    global i1, sent1, end1, waiting1

    instruct = instructions[i1].split()
    op = instruct[0]
    reg = instruct[1]
    if len(instruct) == 3:
        val = instruct[2]
    else:
        val = None

    if op == "snd":
        try:
            reg = int(reg)
            queue0.append(reg)
        except:
            queue0.append(regs1[reg])
        sent1 += 1
    if op == "set":
        try:
            val = int(val)
            regs1[reg] = val
        except:
            regs1[reg] = regs1[val]
    if op == "add":
        try:
            regs1[reg] += int(val)
        except:
            regs1[reg] += regs1[val]
    if op == "mul":
        try:
            val = int(val)
            regs1[reg] *= val
        except:
            regs1[reg] *= regs1[reg]
    if op == "mod":
        try:
            val = int(val)
            regs1[reg] = regs1[reg] % val
        except:
            regs1[reg] = regs1[reg] % regs1[val]
    if op == "rcv":
        if len(queue1) > 0:
            regs1[reg] = queue1.pop(0)
        else:
            waiting1 = 1
            return
    if op == "jgz":
        # Get X value
        try:
            reg = int(reg)
        except:
            reg = regs1[reg]
        # Get Y value
        try:
            val = int(val)
        except:
            val = regs1[val]
        # Do
        if reg > 0:
            i1 += val
        else:
            i1 += 1
    if op != "jgz":
        i1 += 1
    if i1<0 or i1>=len(instructions):
        end1 = 1


regs0 = {chr(i): 0 for i in range(97, 117)}
regs0['p'] = 0
queue0 = []
regs1 = {chr(i): 0 for i in range(97, 117)}
regs1['p'] = 1
queue0 = []
queue1 = []
end0 = 0
end1 = 0
waiting0 = 0
waiting1 = 0
i0 = 0
i1 = 0
sent1 = 0

while (not(end0 and end1)) and (not(waiting0 and waiting1)):
    step0()
    step1()

print("Result =", sent1)

