filename = "day8.txt"
ops = {"inc": "+=", "dec": "-="}

# Initialise registers to zero
regs = {}
with open(filename) as f:
    for line in f.readlines():
        data = line.split(' ')
        reg = data[0]
        if reg not in regs:
            regs[reg] = 0

# Follow the instructions
with open(filename) as f:
    for line in f.readlines():
        reg, op, value, _, condReg, condOp, condValue = line.split(' ')
        if eval(str(regs[condReg])+condOp+condValue):
            exec("regs['{}']".format(reg) + ops[op] + value)

print("Result = ", max(list(regs.values())))
