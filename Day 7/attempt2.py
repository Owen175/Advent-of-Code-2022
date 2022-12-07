class File:
    def __init__(self, size, dirList, name):
        self.size = size
        self.dirList = dirList
        self.name = name


with open('inputData.txt', 'r') as f:
    files = []
    dirsList = []
    uniqueDirsList = []
    for line in f:
        print(dirsList)
        line = line.strip()
        if line[0] == '$':
            if '$ cd ..' in line:
                dirsList.pop()
            elif '$ cd' in line:
                dirsList.append(line[5:len(line)])
                if line[5:len(line)] not in uniqueDirsList:
                    uniqueDirsList.append(line[5:len(line)])
        else:
            try:
                if int(line[0]):
                    size, name = line.split(' ')
                    file = File(int(size), dirsList, name)
                    files.append(file)
            except ValueError:
                pass

sumScore = 0

for uniqueDir in uniqueDirsList:
    totalForDir = 0
    for file in files:
        if uniqueDir in file.dirList:
            totalForDir += file.size
    print(totalForDir)
    if totalForDir <= 100_000:
        sumScore += totalForDir

print(sumScore)
