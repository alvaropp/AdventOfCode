buffer = [0]
pos = 0
step = 371

for num in range(1, 2018):
    # Advance
    pos = (pos + step)%len(buffer)
    # Insert
    if pos == len(buffer) - 1:
        buffer.append(num)
    else:
        buffer.insert(pos + 1, num)
    pos += 1

print("Result =", buffer[buffer.index(2017) + 1])
