from collections import defaultdict

# 917

# That's not the right answer; your answer is too high. Curiously, it's the right answer for someone else; you're either logged in to the wrong account, unlucky, or cheating. In any case, you need to be using your puzzle input. If you're stuck, there are some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 917.) [Return to Day 7]


# 891

# That's not the right answer; your answer is too low. Curiously, it's the right answer for someone else; you're either logged in to the wrong account, unlucky, or cheating. In any case, you need to be using your puzzle input. If you're stuck, there are some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 891.) [Return to Day 7]


def assignToWorkers(workers, availableSteps):
    for i in availableSteps:
        assigned = False
        for j, val in workers.items():
            if assigned:
                assigned = False
                break
            if val == "":
                workers[j] = i
                # workers[j]["progress"] = True
                assigned = True
    return workers


def decrementWorkers(workers):
    completedStepsString = ""

    for i, val in workers.items():
        if val != "":
            if not workers[i]["progress"]:
                print "assigning to true: " + workers[i]["self"]
                workers[i]["progress"] = True
            if workers[i]["time"] > 0:
                if workers[i]["progress"]:

                    workers[i]["time"] -= 1
                    print "working on: " + workers[i]["self"],
            if workers[i]["time"] < 1:
                completedStepsString += workers[i]["self"]
                workers[i] = ""

    if completedStepsString != "":
        print "completed"
    return completedStepsString


def replaceFinishedJobs(stepDict, k):
    for l, va in stepDict.items():
        stepDict[l]["dependencies"] = stepDict[l]["dependencies"].replace(
            k, "")


def process(stepDict):
    completedSteps = []
    globalCounter = 0
    print "time: " + str(globalCounter),
    availableSteps = []
    workers = {1: "", 2: "", 3: "", 4: "", 5: ""}
    while (len(stepDict.items()) > 0):
        for i, val in stepDict.items():
            if val["dependencies"] == "" and val["progress"] == False:

                availableSteps.append(val)
        assignments = assignToWorkers(workers, availableSteps)
        cs = decrementWorkers(assignments)
        availableSteps = []
        if cs:
            firstInAlphabet = 'Z'
            tList = []
            compString = ""
            for k in cs:
                if k <= firstInAlphabet:
                    firstInAlphabet = k
                    tList.insert(0, k)
                else:
                    tList.append(k)
            # o = tList.index(k)
            # tList.pop(o)
            # for g in tList:
            #     availableSteps.append(stepDict[g])
            for i in tList:
                replaceFinishedJobs(stepDict, i)
                completedSteps.append(i)
                del stepDict[i]

        globalCounter += 1
        print "time: " + str(globalCounter),

        # del stepDict[firstInAlphabet]
        # letList.append(firstInAlphabet)
        # for i, val in stepDict.items():
        #     stepDict[i] = val.replace(firstInAlphabet, "")

    print "done"
    print globalCounter


def parse():
    stepDict = defaultdict(lambda: defaultdict(str))
    stepList = None
    letterCheck = []
    keyList = []
    with open("values7.txt") as steps:
        stepList = [x.strip() for x in steps.readlines()]

    for i in stepList:
        j = i.split()
        time = ord(j[7]) - 4
        stepDict[j[7]]["dependencies"] += j[1]
        stepDict[j[7]]["time"] = time
        stepDict[j[7]]["self"] = j[7]
        stepDict[j[7]]["progress"] = False
        letterCheck.append(j[1])
        keyList.append(j[7])
    for a in list(set(letterCheck) - set(keyList)):
        stepDict[a]["dependencies"] = ""
        stepDict[a]["time"] = ord(a) - 4
        stepDict[a]["self"] = a
        stepDict[a]["progress"] = False
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
