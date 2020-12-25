def find_loop_size(target):
    loop_size = 1
    value = 1
    mult = 7
    while True:
        value = (value * mult) % 20201227
        if value == target:
            break
        loop_size += 1
    return loop_size


def compute_subject_number(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = (subject_number * value) % 20201227
    return value


with open("day25.txt", "r") as f:
    card_key = int(f.readline().strip())
    door_key = int(f.readline().strip())


card_loop_size = find_loop_size(card_key)
door_loop_size = find_loop_size(door_key)

result_card = compute_subject_number(door_key, card_loop_size)
result_door = compute_subject_number(card_key, door_loop_size)

assert result_card == result_door
print(result_card)

