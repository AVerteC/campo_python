#!usr/bin/env python3
# made by alan chen

def getfileLines():
    file = open("capitals.txt", "r")
    allLines = file.readlines()
    return allLines


def fileInterpret(allLines):
    StateDict = {}
    for element in allLines:
        statecap = element.split(", ")
        StateDict[str(statecap[0])]=str(statecap[1].replace('\n',''))
    return StateDict


def uinput(nameDict):
    inputu = "ayy"
    while inputu != "Done":
        inputu = input('Ready: ')
        if str(inputu) in nameDict:
            a = str(nameDict.get(str(inputu)))
            print(a)
        else:
            for v, k in nameDict.items():
                if k == inputu:
                    print(v)

    else:
        exit()

def main():
    b = fileInterpret(getfileLines())
    uinput(b)


main()
