import numpy as np


with open("day3.txt") as f:
    data_ = [x.strip() for x in f.readlines()]
data = np.zeros([len(data_), 3])
for i, trian in enumerate(data_):
    data[i] = np.array([int(x) for x in trian.split()])

combs0 = np.array([[0, 1], [1, 2], [0, 2]])
combs1 = np.array([[2], [0], [1]])

valid = 0
for data_ in data:
    if  (np.sum(data_[combs0[0]]) > np.sum(data_[combs1[0]])) &        (np.sum(data_[combs0[1]]) > np.sum(data_[combs1[1]])) &        (np.sum(data_[combs0[2]]) > np.sum(data_[combs1[2]])):
            valid += 1
print("Result =", valid)

