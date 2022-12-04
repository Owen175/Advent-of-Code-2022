'''
with open('areas.txt', 'r') as f:
    count = 0
    for line in f:
        num1=0
        num2=0
        num3=0
        num4=0
        numsList = []
        numberList = []
        currentNum = ''
        for char in line:
            if char != '-' and char != ',':
                numsList.append(char)
            else:
                numsList.append(' ')
        #print(numsList)
        for num in numsList:
            if num == ' ':
                numberList.append(int(currentNum))
                currentNum = ''
            else:
                currentNum = currentNum + num
        numberList.append(int(currentNum))
        print(numberList)
        num1 = numberList[0]
        num2 = numberList[1]
        num3 = numberList[2]
        num4 = numberList[3]

        if num1<=num3 and num2>=num4:
            count += 1
        elif num3<= num1 and num4>=num2:
            count+= 1
print(count)
'''

#Part 2:

with open('areas.txt', 'r') as f:
    count = 0
    for line in f:
        num1=0
        num2=0
        num3=0
        num4=0
        numsList = []
        numberList = []
        currentNum = ''
        for char in line:
            if char != '-' and char != ',':
                numsList.append(char)
            else:
                numsList.append(' ')
        #print(numsList)
        for num in numsList:
            if num == ' ':
                numberList.append(int(currentNum))
                currentNum = ''
            else:
                currentNum = currentNum + num
        numberList.append(int(currentNum))
        print(numberList)
        num1 = numberList[0]
        num2 = numberList[1]
        num3 = numberList[2]
        num4 = numberList[3]

        if num3<=num2 and num3>=num1 or num4<=num2 and num4>=num1:
            count += 1
        elif num1<=num4 and num1>=num3 or num2<=num4 and num2>=num3:
            count+= 1
print(count)