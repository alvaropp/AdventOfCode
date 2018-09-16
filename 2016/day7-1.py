import numpy as np
import re


def loadData(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data

def findABBA(s):
    found = False
    i = 0
    while not found and i < len(s)-3:
        found = (s[i] == s[i+3]) and (s[i+1] == s[i+2]) and (s[i] != s[i+1]) and (s[i+2] != s[i+3])
        i += 1
    return found

def checkString(s):
    ended = False
    # Inside brackets
    inside = re.findall('\[.*?\]', s)
    for substring in inside:
        ended = findABBA(substring)
        if ended:
            return False
        s = s.replace(substring[1:], '')
    # Outside brackets if not ended
    result = findABBA(s)
        
    return result

def test_cases():
    assert checkString('abba[mnop]qrst') == True
    assert checkString('abcd[bddb]xyyx') == False
    assert checkString('aaaa[qwer]tyui') == False
    assert checkString('ioxxoj[asdfgh]zxcvbn') == True


data = loadData('day7.txt')

total = 0
for string in data:
    total += checkString(string)
print(total)
