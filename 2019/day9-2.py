from itertools import permutations

import numpy as np


class Processor:
    def __init__(self, data: np.array, inputs: list):
        self.data = np.append(data, np.zeros(200000, dtype=int))
        self.inputs = inputs
        self.outputs = []
        self.pos = 0
        self.base = 0
        self.halted = 0

    @staticmethod
    def process_opcode_and_param(number):
        param = str(number)
        opcode = int(param[-2:])
        mode = param[:-2]
        mode = "0" * (3 - len(mode)) + mode
        return opcode, mode[::-1]

    def get_index(self, mode, index):
        if mode == "0":
            return self.data[index]
        elif mode == "1":
            return index
        elif mode == "2":
            return self.data[index] + self.base

    def get_value(self, mode, index):
        return self.data[self.get_index(mode, index)]

    def go(self):
        opcode, mode = self.process_opcode_and_param(self.data[self.pos])

        if opcode == 1:
            self.data[self.get_index(mode[2], self.pos + 3)] = self.get_value(
                mode[0], self.pos + 1
            ) + self.get_value(mode[1], self.pos + 2)

            self.pos += 4

        elif opcode == 2:
            self.data[self.get_index(mode[2], self.pos + 3)] = self.get_value(
                mode[0], self.pos + 1
            ) * self.get_value(mode[1], self.pos + 2)
            self.pos += 4

        elif opcode == 3:
            if len(self.inputs) == 0:
                raise ValueError("No more inputs!")
            next_input = self.inputs.pop()
            self.data[self.get_index(mode[0], self.pos + 1)] = next_input
            self.pos += 2

        elif opcode == 4:
            self.outputs.append(self.get_value(mode[0], self.pos + 1))
            self.pos += 2

        elif opcode == 5:
            if self.get_value(mode[0], self.pos + 1) != 0:
                self.pos = self.get_value(mode[1], self.pos + 2)
            else:
                self.pos += 3

        elif opcode == 6:
            if self.get_value(mode[0], self.pos + 1) == 0:
                self.pos = self.get_value(mode[1], self.pos + 2)
            else:
                self.pos += 3

        elif opcode == 7:
            value = (
                1
                if self.get_value(mode[0], self.pos + 1)
                < self.get_value(mode[1], self.pos + 2)
                else 0
            )
            self.data[self.get_index(mode[2], self.pos + 3)] = value
            self.pos += 4

        elif opcode == 8:
            value = (
                1
                if self.get_value(mode[0], self.pos + 1)
                == self.get_value(mode[1], self.pos + 2)
                else 0
            )
            self.data[self.get_index(mode[2], self.pos + 3)] = value
            self.pos += 4

        elif opcode == 9:
            self.base += self.get_value(mode[0], self.pos + 1)
            self.pos += 2

        elif opcode == 99:
            self.halted = 1

        else:
            print(f"opcode: {opcode}, mode: {mode}")
            raise ValueError


def solve_amplifier(data, single_input):
    amplifier = Processor(data, single_input)
    while not amplifier.halted:
        amplifier.go()
    return amplifier


if __name__ == "__main__":
    data = np.genfromtxt("day9.txt", delimiter=",", dtype=int)
    inputs = [2]

    amplifier = solve_amplifier(data, inputs)
    print(amplifier.outputs[0])
