'''
with open("Calories.txt", 'r') as f:
    totalCalories = 0
    topCalories = 0
    for line in f:
        if line != '\n':
            line = int(line)
            totalCalories += line
        else:
            if topCalories < totalCalories:
                topCalories = totalCalories
            totalCalories = 0
            print(topCalories)
    if topCalories < totalCalories:
        topCalories = totalCalories

print(topCalories)
'''

#Part 2

with open("Calories.txt", 'r') as f:
    totalCalories = 0
    topCalories = 0
    secondCalories = 0
    thirdCalories = 0
    for line in f:
        if line != '\n':
            line = int(line)
            totalCalories += line
        else:
            if topCalories < totalCalories:
                thirdCalories = secondCalories
                secondCalories = topCalories
                topCalories = totalCalories
            elif secondCalories < totalCalories:
                thirdCalories = secondCalories
                secondCalories = totalCalories
            elif thirdCalories < totalCalories:
                thirdCalories = totalCalories

            totalCalories = 0

if topCalories < totalCalories:
    thirdCalories = secondCalories
    secondCalories = topCalories
    topCalories = totalCalories
elif secondCalories < totalCalories:
    thirdCalories = secondCalories
    secondCalories = totalCalories
elif thirdCalories < totalCalories:
    thirdCalories = totalCalories

print(topCalories+ secondCalories+thirdCalories)