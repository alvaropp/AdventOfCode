from hashlib import md5
import re


def solve(salt):

    def generateHash(i):
        word = salt + str(i)
        md5Hash = md5(word.encode()).hexdigest()
        return md5Hash

    def findRepeatedDigit(md5Hash):
        digit = re.search('([a-z\\d])\\1\\1', md5Hash).group(1)
        return digit

    def findFollowUpDigit(digit, followUpMd5Hash):
        return digit*5 in followUpMd5Hash

    numFound = 0
    i = 0
    while numFound < 64:
        md5Hash = generateHash(i)
        try:
            digit = findRepeatedDigit(md5Hash)
            for j in range(1, 1001):
                followUpMd5Hash = generateHash(i+j)
                if findFollowUpDigit(digit, followUpMd5Hash):
                    numFound += 1
        except:
            pass
        i += 1

    return i-1


salt = 'cuanljph'
solve(salt)
