from itertools import permutations

import numpy as np


class Processor:
    def __init__(self, data: np.array, phase: int, extra_input: int = None):
        self.data = data
        self.outputs = []
        self.pos = 0
        self.running = 1
        self.halted = 0
        if extra_input is None:
            self.inputs = [phase]
        else:
            self.inputs = [extra_input, phase]

    @staticmethod
    def process_opcode_and_param(number):
        param = str(number)
        opcode = int(param[-2:])
        mode = param[:-2]
        mode = "0" * (3 - len(mode)) + mode
        return opcode, mode[::-1]

    def get_value(self, mode, delta_pos):
        if mode == "0":
            return self.data[self.data[self.pos + delta_pos]]
        if mode == "1":
            return self.data[self.pos + delta_pos]

    def go(self):
        opcode, mode = self.process_opcode_and_param(self.data[self.pos])

        if opcode == 1:
            self.data[self.data[self.pos + 3]] = self.get_value(
                mode[0], 1
            ) + self.get_value(mode[1], 2)
            self.pos += 4

        elif opcode == 2:
            self.data[self.data[self.pos + 3]] = self.get_value(
                mode[0], 1
            ) * self.get_value(mode[1], 2)
            self.pos += 4

        elif opcode == 3:
            if len(self.inputs) == 0:
                self.running = 0
            else:
                next_input = self.inputs.pop()
                self.data[self.data[self.pos + 1]] = next_input
                self.pos += 2

        elif opcode == 4:
            self.outputs.append(self.get_value(mode[0], 1))
            self.pos += 2

        elif opcode == 5:
            if self.get_value(mode[0], 1) != 0:
                self.pos = self.get_value(mode[1], 2)
            else:
                self.pos += 3

        elif opcode == 6:
            if self.get_value(mode[0], 1) == 0:
                self.pos = self.get_value(mode[1], 2)
            else:
                self.pos += 3

        elif opcode == 7:
            value = 1 if self.get_value(mode[0], 1) < self.get_value(mode[1], 2) else 0
            self.data[self.data[self.pos + 3]] = value
            self.pos += 4

        elif opcode == 8:
            value = 1 if self.get_value(mode[0], 1) == self.get_value(mode[1], 2) else 0
            self.data[self.data[self.pos + 3]] = value
            self.pos += 4

        elif opcode == 99:
            self.halted = 1

        else:
            raise ValueError


def solve_amplifier(data, phase, first_input=None):
    if first_input is None:
        inputs = [first_input]
    else:
        inputs = [first_input, phase]

    amplifier = Processor(data, inputs)

    while not amplifier.halted:
        amplifier.go()

    return amplifier.outputs[0]


def solve_all(data, phases):
    next_inputs = [0] + [None] * 4
    amplifiers = [
        Processor(data.copy(), phase, next_inputs[i]) for i, phase in enumerate(phases)
    ]

    amp_index = 4
    while np.sum([amplifier.halted for amplifier in amplifiers]) < 5:
        amp_index = (amp_index + 1) % 5
        amplifiers[amp_index].go()

        if amplifiers[amp_index].outputs != []:
            output = amplifiers[amp_index].outputs.pop()
            amplifiers[(amp_index + 1) % 5].inputs.insert(0, output)

    return output


if __name__ == "__main__":
    data = np.genfromtxt("day7.txt", delimiter=",", dtype=int)

    max_result = -float("Inf")
    for phases in list(permutations(range(5, 10))):
        result = solve_all(data, phases)
        max_result = max(result, max_result)

    print(max_result)
