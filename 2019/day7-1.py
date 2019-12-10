from itertools import permutations

import numpy as np


class Processor:
    def __init__(self, data: np.array, inputs: list):
        self.data = data
        self.inputs = inputs
        self.outputs = []
        self.pos = 0
        self.running = 1

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
            self.pos = -1

        else:
            raise ValueError


def solve_amplifier(data, phase, first_input):
    inputs = [first_input, phase]
    amplifier = Processor(data, inputs)

    while amplifier.pos >= 0:
        amplifier.go()

    return amplifier.outputs[0]


def solve_all(data, phases):
    data_copy = data.copy()
    next_input = 0
    for phase in phases:
        next_input = solve_amplifier(data_copy, phase, next_input)
    return next_input


if __name__ == "__main__":
    data = np.genfromtxt("day7.txt", delimiter=",", dtype=int)

    max_result = -float("Inf")
    for phases in list(permutations(range(5))):
        result = solve_all(data, phases)
        max_result = max(result, max_result)

    print(max_result)
