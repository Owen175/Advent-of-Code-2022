'''
import string

alphabet = string.ascii_lowercase
upperAlphabet = alphabet.upper()
allCasesAlphabet = alphabet+upperAlphabet
charList = []

with open('rucksackData.txt', 'r') as t:
    for line in t:
        length = len(line)
        firstHalf = line[:int(length/2)]
        secondHalf = line[int(length/2):]
        for char in allCasesAlphabet:
            if char in firstHalf and char in secondHalf:
                charList.append(char)

totalScore = 0
for char in charList:
    totalScore += allCasesAlphabet.find(char) + 1

print(totalScore)
'''

# Part 2

import string

alphabet = string.ascii_lowercase
upperAlphabet = alphabet.upper()
allCasesAlphabet = alphabet+upperAlphabet
charList = []
lineList = []
with open('rucksackData.txt', 'r') as t:
    for line in t:
        lineList.append(line)
    #print(len(lineList))
    for i in range(100):
        line1 = lineList[3*i]
        line2 = lineList[3*i+1]
        line3 = lineList[3*i+2]
        print(line1)
        print(line2)
        print(line3)
        for char in allCasesAlphabet:
            if char in line1 and char in line2 and char in line3:
                charList.append(char)
                #print(char)
        print()

totalScore = 0
for char in charList:
    totalScore += allCasesAlphabet.find(char) + 1

print(totalScore)