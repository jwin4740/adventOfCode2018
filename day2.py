def gatherInput():
    inputList = []
    with open("values2.txt") as input:
        for i in input:
            inputList.append(str(i).strip())
    return inputList


def analyzeId(curId):
    checkSum = {"two": 0, "three": 0}
    myString = curId[0]
    print myString

    for n in curId:
        usedLetters = []
        for i in range(0, len(n)):
            counter = 0
            twoCount = 0
            threeCount = 0
            for j in range(0, len(n)):
                if (n[j] == n[i]):
                    counter = counter + 1
            if counter == 3 and not beenUsed(n[i], usedLetters):
                usedLetters.append(n[i])
                checkSum["three"] = checkSum["three"] + 1
                threeCount = threeCount + 1
                break
            if counter == 2 and not beenUsed(n[i], usedLetters):
                usedLetters.append(n[i])
                checkSum["two"] = checkSum["two"] + 1
                twoCount = twoCount + 1
                break
            print checkSum
    return checkSum


def beenUsed(char, usedLetters):
    for k in range(0, len(usedLetters)):
        if char == usedLetters[k]:
            return True
    return False


test = ['iosnxilssy', 'asdfhasdfjlkhasdjlhfasdf']


def controller():
    l = gatherInput()
    print analyzeId(l)["two"] * analyzeId(l)["three"]


controller()
