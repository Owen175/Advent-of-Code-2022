def dirSize(directory):
    tS = 0
    for file in directoryDict[directory]:
        x, y = file
        if x == 'dir':
            tS += dirSize(y)
        else:
            tS += int(x)
    return int(tS)


directoryDict = {}


with open('inputData.txt', 'r') as f:
    cDir = ''
    for line in f:
        line = line.strip()
        if line[0] == '$':
            if '$ cd' in line:
                if '$ cd ..' not in line:
                    if cDir != '':
                        directoryDict[cDir] = cDirList
                    cDirList = []
                    cDir = line[5:len(line)]
        else:
            try:
                if int(line[0]):
                    size, name = line.split(' ')
                    cDirList.append((int(size), name))
            except ValueError:
                _, dirName = line.split(' ')
                cDirList.append(('dir', dirName))

directoryDict[cDir] = cDirList
# print(directoryDict['d'])
print(directoryDict)

sizeDict = {}
totalSize = 0
for i, k in enumerate(directoryDict.keys()):
    # print(i, k, type(k))
    #print(dirSize(k))

    sizeDict[k] = dirSize(k)


for k in sizeDict.keys():
    if sizeDict[k] <= 100000:
        totalSize += sizeDict[k]
        #print(sizeDict[key])

print(totalSize)
