with open("day16.txt") as f:
    data = f.readline()
data = data.split(",")
programs = [chr(i) for i in range(97, 113)]

typeList = []
dataList = []
for instruction in data:
    type_ = instruction[0]
    if type_ == "s":
        # Type: 0
        typeList.append(0)
        dataList.append([int(instruction[1:])])
    if type_ == "x":
        # Type 1
        typeList.append(1)
        values = instruction[1:].split('/')
        dataList.append(values)
    if type_ == "p":
        # Type 2
        typeList.append(2)
        values = instruction[1:].split('/')
        dataList.append(values)

with open("day16_type.txt", 'w') as f:
    for element in typeList:
        f.write(str(element) + '\n')

with open("day16_data1.txt", 'w') as f:
    for element in dataList:
        f.write(str(element[0]) + '\n')

with open("day16_data2.txt", 'w') as f:
    for element in dataList:
        if len(element) > 1:
            f.write(str(element[1d]) + '\n')
        else:
            f.write("9999\n")
