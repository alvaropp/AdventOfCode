import re


with open("day4.txt", "r") as f:
    passport_list = [
        {
            k: v
            for k, v in [
                field.split(":")
                for field in list(filter(None, re.split("[, \n]+", passport)))
            ]
        }
        for passport in f.read().split("\n\n")
    ]


def is_valid(passport):
    return len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)


print(sum(map(is_valid, passport_list)))

