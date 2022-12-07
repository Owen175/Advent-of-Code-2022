stackList = [['H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'],
             ['M', 'Q', 'H'],
             ['N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'],
             ['Z', 'T', 'F', 'Q', 'M', 'W', 'G'],
             ['M', 'T', 'H', 'P'],
             ['C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'],
             ['M', 'N', 'B', 'F', 'V', 'R'],
             ['P', 'L', 'H', 'M', 'R', 'G', 'S'],
             ['P', 'D', 'B', 'C', 'N']]


def move(a, b, c, stackList):
    for i in range(a):
        stackList[c - 1].append(stackList[b - 1].pop(len(stackList[b - 1]) - a + i))
    # print(stackList)
    return stackList


with open('instructions.txt', 'r') as f:
    for line in f:
        line = line.replace('move ', '')
        line = line.replace('from ', '')
        line = line.replace('to ', '')
        currentNum = ''
        numsList = []
        for num in line:
            if num != ' ':
                if num != '\n':
                    currentNum = currentNum + num
            else:
                numsList.append(currentNum)
                currentNum = ''
        numsList.append(currentNum)
        stackList = move(int(numsList[0]), int(numsList[1]), int(numsList[2]), stackList)

for row in stackList:
    print(row)
