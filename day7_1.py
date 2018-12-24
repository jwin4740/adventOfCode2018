from collections import defaultdict

#                                        CEVWL


# def progress(stepDict):
#     for i, val in stepDict.items():
#         if 'C' in val or 'E' in val or 'V' in val or 'N' in val or 'L' in val:


# def substitute(stepDict, processing, counter):
#     action = False
#     tmpList = []
#     letter = ""
#     for i, val in stepDict.items():
#         if len(val) == counter:
#             print i, val

#             action = True
#         # return letter, action
#     return "", action


def process(stepDict):
    letList = []
    while (len(stepDict.items()) > 0):
        # find last step
        firstInAlphabet = 'Z'
        for i, val in stepDict.items():
            if val == "":
                if ord(i) < ord(firstInAlphabet):
                    firstInAlphabet = i
        del stepDict[firstInAlphabet]
        letList.append(firstInAlphabet)
        for i, val in stepDict.items():
            stepDict[i] = val.replace(firstInAlphabet, "")
    print "".join(letList)


def parse():
    stepDict = defaultdict(str)
    stepList = None
    with open("values7.txt") as steps:
        stepList = [x.strip() for x in steps.readlines()]

    for i in stepList:
        j = i.split()
        stepDict[j[7]] += j[1]
        stepDict[j[1]] += ""
    for i, val in stepDict.items():
        pass
    return stepDict


def controller():

    process(parse())


#  not MOUYZBFTRXIJNDKQAHSGPCEVWL
#  not LWVECPGSHAQKDNJIXRTFBZYUOM
#  not LWCEVPGAHSDKQIJNRXBFTOUYZM
#  not MNOUBYITKXZFHRJDSQAGCPEVWL
#  not LWCEVPGAHKQSDIJNRFXBOTUMYZ
controller()
# s = "MOUYZBFTRXIJNDKQAHSGPCEVWL"
# rl = list(s)

# rl.reverse()
# print "".join(rl)
