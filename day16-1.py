with open("day16.txt") as f:
    data = f.readline()
data = data.split(",")

programs = [chr(i) for i in range(97, 113)]
for instruction in data:
    type_ = instruction[0]
    if type_ == "s":
        length = int(instruction[1:])
        programs = programs[-length:] + programs[:len(programs)-length]
    if type_ == "x":
        values = instruction[1:].split('/')
        a = int(values[0])
        b = int(values[1])
        temp = programs[a]
        programs[a] = programs[b]
        programs[b] = temp
    if type_ == "p":
        a, b = instruction[1:].split('/')
        indA = programs.index(a)
        indB = programs.index(b)
        programs[indA] = b
        programs[indB] = a

print("Result =", "".join(programs))

