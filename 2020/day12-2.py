with open("day12.txt", "r") as f:
    instructions = [(line[0], int(line[1:])) for line in f.read().splitlines()]

move_dict = {"N": -1j, "S": 1j, "E": 1, "W": -1}
turn_dict = {"L": {90: -1j, 180: -1, 270: 1j}, "R": {90: 1j, 180: -1, 270: -1j}}

ship_pos = 0j
wp_rel_pos = 10 - 1j

for (move, value) in instructions:
    if move in "NSEW":
        wp_rel_pos += move_dict[move] * value
    elif move in "LR":
        wp_rel_pos *= turn_dict[move][value]
    elif move == "F":
        ship_pos += wp_rel_pos * value

print(int(ship_pos.real + ship_pos.imag))
