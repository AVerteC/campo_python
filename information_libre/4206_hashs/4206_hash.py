#!usr/bin/env python3
# made by alan chen

def getfileLines():
    file = open("names.txt", "r")
    allLines = file.readlines()
    return allLines


def fileInterpret(allLines):
    nameDict = {}
    for element in allLines:
        nameCombine = element.split()
        if nameCombine[0] not in nameDict:
            nameDict[nameCombine[0]] = [nameCombine[1]]
        else:
            nameDict[nameCombine[0]].append(nameCombine[1])
    return nameDict


def printDupResult(nameDict):
        for key in nameDict:
            if len(nameDict.get(key)) > 1:
                print(str(key) + " (" + str(len(nameDict.get(key))) + "): " + str(nameDict.get(key)).replace("'",""))


#list of first names that should match
#Aaryan
#Alan
#Alexander
#Brandon
#Daniel

def main():
    d = fileInterpret(getfileLines())
    printDupResult(d)

main()
