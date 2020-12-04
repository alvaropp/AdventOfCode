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


def fields_valid(passport):
    return len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)


def data_valid(passport):
    byr = 1920 <= int(passport["byr"]) <= 2002
    iyr = 2010 <= int(passport["iyr"]) <= 2020
    eyr = 2020 <= int(passport["eyr"]) <= 2030
    hgt_unit = passport["hgt"][-2:]
    if hgt_unit == "cm":
        hgt = 150 <= int(passport["hgt"][:-2]) <= 193
    elif hgt_unit == "in":
        hgt = 59 <= int(passport["hgt"][:-2]) <= 76
    else:
        hgt = False
    hcl = bool(re.match("^#[0-9a-f]{6}$", passport["hcl"]))
    ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid = bool(re.match("^\d{9}$", passport["pid"]))
    return byr and iyr and eyr and hgt and hcl and ecl and pid


def is_valid(passport):
    return fields_valid(passport) and data_valid(passport)


print(sum(list(map(is_valid, passport_list))))
