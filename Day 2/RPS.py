with open('strategy.txt', 'r') as f:
    totalScore = 0
    for line in f:
        expected = line[0]
        answer = line[2]

        match expected:
            case 'A':
                expected = 1
            case 'B':
                expected = 2
            case 'C':
                expected = 3

        if answer == 'X':
            #lose
            if expected == 1:
                totalScore += 3
            elif expected == 2:
                totalScore += 1
            elif expected == 3:
                totalScore += 2

        if answer == 'Y':
            #draw
            totalScore += 3
            totalScore += expected
        if answer == 'Z':
            #win
            totalScore += 6
            if expected == 1:
                totalScore += 2
            elif expected == 2:
                totalScore += 3
            elif expected == 3:
                totalScore += 1

print(totalScore)


