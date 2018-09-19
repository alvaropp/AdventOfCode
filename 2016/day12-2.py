import numpy as np


def loadData(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data

def solve(data):
    
    def parseInstruction(inst):
        inst = inst[:-1].split()
        command = inst[0]
        arg1 = inst[1]
        try:
            arg2 = inst[2]
        except:
            pass

        jump = None
        if command == 'cpy':
            if arg1.isdigit():
                regs[arg2] = int(arg1)
            else:
                regs[arg2] = regs[arg1]
        elif command == 'inc':
            regs[arg1] += 1
        elif command == 'dec':
            regs[arg1] -= 1
        elif command == 'jnz':
            if arg1.isdigit() and int(arg1) != 0:
                jump = int(arg2)
            elif regs[arg1] != 0:
                jump = int(arg2)
        
        return jump
    
    regs = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    
    i = 0
    while i < len(data):
        jump = parseInstruction(data[i])
        if jump is None:
            i += 1
        elif jump <= 0:
            i += jump
        elif jump > 0:
            i += jump
    
    return regs['a']


data = loadData('2016/day12.txt')
solve(data)
