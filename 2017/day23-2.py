import numpy as np


# Initialise regs
regs = {chr(i): 0 for i in range(97, 105)}

# Straight from the code
regs['a'] = 1
regs['b'] = 93
regs['c'] = 93
regs['g'] = 1

if regs['a'] != 0:
    regs['b']  = regs['b']*100 + 100000
    regs['c'] = regs['b'] + 17000

while regs['g'] != 0:
    regs['f'] = 1
    regs['d'] = 2
    regs['e'] = 2
    for d in range(2, int(np.ceil(regs['b']))):
        if regs['b'] % d == 0:
            regs['f'] = 0
            regs['h'] += 1
            break
    regs['g'] = regs['b'] - regs['c']
    regs['b'] += 17

print("Result =", regs['h'])
