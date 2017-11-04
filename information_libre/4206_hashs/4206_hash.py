#!usr/bin/env python3
# made by alan chen

def hashmatcher():
    file = open("names.txt", "r")
    allLines = file.readlines()
    nameDict = {}
    for element in allLines:
        nameCombine = element.split()
        #nameDict[nameCombine[0]]
        #for item in nameCombine:
        if nameCombine[0] not in nameDict:
            nameDict[nameCombine[0]] = [nameCombine[1]]
        else:
            nameDict[nameCombine[0]].append(nameCombine[1])

    print(nameDict)



#list of first names that should match

#Aaryan
#Alan
#Alexander
#Brandon
#Daniel






#def main():
#    hashmatcher()

#main()