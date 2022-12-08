from anytree import Node, RenderTree

def dirSize(directory):
    global dirSizeList
    tS = 0
    for file in directory.children:
        #print(file)
        try:
            if file.size != 0:
                tS += int(file.size)
        except AttributeError:
            directorySize = dirSize(file)
            tS += directorySize
            dirSizeList.append(directorySize)
    return tS
'''
Problem:
I am getting the directory size, but if the directory's size is over 100,000, I am deleting it. 

'''

with open('inputData.txt', 'r') as f:
    dirList = []
    for line in f:
        line = line.strip()
        if line[0] == '$':
            if '$ cd ..' in line:
                dirList.pop()
            elif '$ cd' in line:
                # print(dirList)
                if not dirList:
                    dirList.append(Node(name='num1', parent=None))
                else:
                    parent = dirList[-1]
                    dirList.append(Node(name=line[5:len(line)], parent=parent))

                # if '$ cd ..' not in line:
                #     if cDir != '':
                #         directoryDict[cDir] = cDirList
                #     cDirList = []
                #     cDir = line[5:len(line)]
        else:
            if line[0] != 'd':
                size, name = line.split(' ')
                Node(name, parent=dirList[-1], size=size)

# print(base)

# for pre, fill, node in RenderTree(dirList[0]):
#     print(f'{pre,node.name}')
# y = dirList[-1].children
# y = list(y)
# print(y[0].size)

dirSizeList = []
allDirSize = dirSize(dirList[0])
maxList = 0
for size in dirSizeList:
    if size > maxList:
        maxList = size
totalSize = 0
for size in dirSizeList:
    if size <= 100_000:
        totalSize += size

print(totalSize)

a = 30000000 - (70000000 - allDirSize)
bestSoFar = 30000000000
for size in dirSizeList:
    if size >= a:
        if size < bestSoFar:
            bestSoFar = size

print(bestSoFar)