with open('Chars.txt', 'r') as f:
    charString = f.readline()

charList = []

def check(numList):
    for i, num in enumerate(numList):
        tempNumList = numList[i+1:]
        for j in range(len(tempNumList)):
            if numList[i] == tempNumList[j]:
                return True
    return False
    #if num1 == num2 or num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4 or num3 == num4:
    #    return True
    #return False

numList = []
for char in charString:
    charList.append(char)
for i, char in enumerate(charList):
    char = [char]
    char.extend(numList)
    numList = char
    #print(numList)
    if len(numList) == 14:
        bool = check(numList)
        #print(bool)
        if not bool:
            print(i+1)
        numList.pop()
