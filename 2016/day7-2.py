import numpy as np
import re


def loadData(file):
    with open(file, 'r') as f:
        data = f.readlines()
    return data

def findABAs(s):
    found = []
    i = 0
    for i in range(len(s)-2):
        if (s[i] == s[i+2]) and (s[i] != s[i+1]):
            found.append(s[i:i+3])
    return found

def findBAB(s, found):
    for i in range(len(s)-2):
        for pattern in found:
            if (s[i] == pattern[1]) and (s[i+1] == pattern[0]) and (s[i+2] == pattern[1]):
                return True
    return False

def checkString(s):
    # Inside brackets, look for ABA
    inside = re.findall('\[.*?\]', s)
    allFound = []
    for substring in inside:
        allFound += findABAs(substring)
        s = s.replace(substring[1:], '')
    # Outside brackets, look for BAB
    result = findBAB(s, allFound)
        
    return result

def test_cases():
    assert checkString('aba[bab]xyz') == True
    assert checkString('xyx[xyx]xyx') == False
    assert checkString('aaa[kek]eke') == True
    assert checkString('zazbz[bzb]cdb') == True


data = loadData('day7.txt')

total = 0
for string in data:
    total += checkString(string)
print(total)
