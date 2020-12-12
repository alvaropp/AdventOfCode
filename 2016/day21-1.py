from collections import deque
import re


def scramble(word, instruction):
    if "swap letter" in instruction:
        letter_1, letter_2 = re.findall("(?<=letter\s)(\w+)", instruction)
        idx_1, idx_2 = word.index(letter_1), word.index(letter_2)
        word[idx_2], word[idx_1] = word[idx_1], word[idx_2]

    elif "swap position" in instruction:
        idx_1, idx_2 = [*map(int, re.findall("(\d+)", instruction))]
        word[idx_2], word[idx_1] = word[idx_1], word[idx_2]

    elif "rotate based" in instruction:
        letter = instruction.split(" ")[-1]
        value = word.index(letter)
        value = value + 2 if value >= 4 else value + 1
        word.rotate(rotate_dict["right"] * value)

    elif "rotate" in instruction:
        instruction_split = instruction.split(" ")
        sense = instruction_split[1]
        value = int(instruction_split[2])
        word.rotate(rotate_dict[sense] * value)

    elif "reverse positions" in instruction:
        instruction_split = instruction.split(" ")
        idx_1 = int(instruction_split[-3])
        idx_2 = int(instruction_split[-1]) + 1
        word = list(word)
        word[idx_1:idx_2] = word[idx_1:idx_2][::-1]
        word = deque(word)

    elif "move position" in instruction:
        instruction_split = instruction.split(" ")
        idx_1 = int(instruction_split[2])
        idx_2 = int(instruction_split[-1])
        letter = word[idx_1]
        word.remove(letter)
        word.insert(idx_2, letter)

    else:
        raise ValueError

    if set(word) != set("abcdefgh"):
        raise ValueError(f"Word {word} is missing letters.")

    return word


rotate_dict = {"left": -1, "right": 1}

with open("day21.txt", "r") as f:
    instructions = f.read().splitlines()

word = deque("abcdefgh")
for instruction in instructions:
    word = scramble(word, instruction)

print("".join(word))
