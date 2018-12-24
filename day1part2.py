import os
import sys


def readNums():
    with open("values.txt") as file:
        return [int(x) for x in file]


def checkRepeats(countList):
    leng = len(countList)
    print len(countList)

    for j in range(0, leng):
        for i in range(0, leng):
            if countList[j] == countList[i] and j != i:
                print countList[j]
                return {"found": True, "count": countList[j]}
    return {"found": False, "count": "nothing"}

    # for j in range(0, leng):
    #     for i in range(0, leng):
    #         if countList[j] == countList[i] and j != i:
    #             print countList[j]
    #             return {"found": True, "count": countList[j]}
    # return {"found": False, "count": "nothing"}


def storeCounts(l, lLength, count):
    countList = []
    curCount = count
    for j in range(0, lLength):
        curCount = curCount + l[j]
        countList.append(curCount)
        # if j == 0:
        #     countList.append(count)

        # if j < leng - 1:
        #     freqChange = l[j + 1] - l[j]
        #     countList.append(freqChange)
    return {"countList": countList, "currentCount": curCount}


def controller():
    l = readNums()
    foundDict = {"found": False, "count": 0}
    found = False
    rollingCountList = []
    count = 0
    myKey = l
    leng = len(l)

    looper = 0

    while(looper < 1000):
        subcount = 0
        countDict = storeCounts(l, leng, count)
        rollingCountList = rollingCountList + countDict["countList"]
        count = countDict["currentCount"]
        rollingCountList.sort()
        looper = looper + 1

        if count in rollingCountList:
            subcount = subcount + 1

        if subcount == 2:
            print "found it"

    # for i in range(0, len(rollingCountList)):
    #     if rollingCountList[i] == rollingCountList[i + 1]:
    #         print "found"
    #         found = True

    # nList = rollingCountList.sort(reverse=True)
    # print nList[0]
    # foundDictReturned = checkRepeats(rollingCountList)
    # foundDict["found"] = foundDictReturned["found"]
    print "you will be found"


controller()


# def readNums():
#     with open("values.txt") as file:
#         return [int(x) for x in file]


# def checkRepeats(countList):
#     leng = len(countList)
#     print len(countList)

#     for j in range(0, leng):
#         for i in range(0, leng):
#             if countList[j] == countList[i] and j != i:
#                 print countList[j]
#                 return {"found": True, "count": countList[j]}
#     return {"found": False, "count": "nothing"}

#     # for j in range(0, leng):
#     #     for i in range(0, leng):
#     #         if countList[j] == countList[i] and j != i:
#     #             print countList[j]
#     #             return {"found": True, "count": countList[j]}
#     # return {"found": False, "count": "nothing"}


# def storeCounts(l, lLength, count):
#     countList = []
#     curCount = count
#     for j in range(0, lLength):
#         curCount = curCount + l[j]
#         countList.append(curCount)
#         # if j == 0:
#         #     countList.append(count)

#         # if j < leng - 1:
#         #     freqChange = l[j + 1] - l[j]
#         #     countList.append(freqChange)
#     return {"countList": countList, "currentCount": curCount}


# def controller():
#     l = readNums()
#     foundDict = {"found": False, "count": 0}
#     rollingCountList = []
#     count = 0
#     myKey = l
#     leng = len(l)
#     while(not foundDict["found"]):
#         countDict = storeCounts(l, leng, count)
#         rollingCountList = rollingCountList + countDict["countList"]
#         count = countDict["currentCount"]
#         foundDictReturned = checkRepeats(rollingCountList)
#         foundDict["found"] = foundDictReturned["found"]
#         print "you will be found"
