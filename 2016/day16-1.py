disc_size = 272

with open("day16.txt", "r") as f:
    data = list(map(int, list(f.read())))

while len(data) < disc_size:
    data.extend([0] + [1 - value for value in data[::-1]])
data = data[:disc_size]


def compute_checksum(data):
    if len(data) % 2 == 1:
        return data
    new_data = [int(data[i] == data[i + 1]) for i in range(0, len(data), 2)]
    return compute_checksum(new_data)


checksum = compute_checksum(data)
print("".join(map(str, checksum)))
