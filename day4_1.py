# 30224 is too low (1889 * 16)
# 126617 is too high (2389 * 53)
# 32975 it too low (1319 * 25)


# PART 2
# 30224 is too low
# 58559  (1889 * 31)

import time
import datetime
from collections import defaultdict
import re


def dataToDict():
    data = None
    with open("values4.txt") as lines:
        data = [x.strip() for x in lines.readlines()]

    dd = []
    for i in range(len(data)):
        ln = {}
        o = data[i].split("] ")
        o[0] = o[0].replace("[", "")
        ln["time"] = o[0]
        ln["message"] = o[1]
        ln["timestamp"] = convertTimes(o[0])
        dd.append(ln)
    sorted_list = sorted(dd, key=lambda k: k['timestamp'])

    return sorted_list


def convertTimes(o):

    d = datetime.datetime.strptime(o, "%Y-%m-%d %H:%M").timetuple()
    dtime = datetime.datetime(d[0]/1000, d[1], d[2], d[3], d[4])
    tt = time.mktime(dtime.timetuple())

    return tt


def groupData(d):
    t = defaultdict(str)
    onGuard = False
    curGaurd = ""
    sle = re.compile(r':(\d+)')
    for e in range(len(d)):
        k = defaultdict(int)

        if d < len(d) - 1:
            break

        if "Guard" in d[e]["message"]:
            li = d[e]["message"].split()[1].replace("#", "")
            onGuard = True
            curGaurd = li
            if curGaurd not in t:
                t[curGaurd] = k
        elif "falls" in d[e]["message"]:
            sleepStart = int(sle.findall(d[e]["time"])[0])
            wake = int(sle.findall(d[e + 1]["time"])[0])
            totalSleep = wake - sleepStart
            for j in range(sleepStart, wake):
                k[j] += 1
                t[curGaurd][j] += 1

        else:
            onGuard = False
            continue

        if onGuard:
            if d[e]["message"]:
                time = d[e]["message"]
    findMaxMinute(t)


def findMax(t):
    maxGuard = 0
    maxMinute = 0
    curMaxGaurd = ''

    for key, val in t.items():
        counter = 0
        for key2, val2 in val.items():
            counter += val2
            if (val2 >= maxMinute):
                maxMinute = val2
                curMaxGaurd = key
    print maxMinute
    # for key, val in t.items():
    #     if val["totalSlept"] > maxGuard:
    #         maxGuard = val["totalSlept"]
    #         curMaxGaurd = key
    print curMaxGaurd
    # else:
    #     continue
    # minute = ''
    # for key, val in t[curMaxGaurd].items():
    #     if (val > maxMinute):
    #         maxMinute = val
    #         minute = key
    #     else:
    #         continue
    # print {"guard": int(curMaxGaurd),
    #        "maxMinute": minute
    #        }
    # print (int(curMaxGaurd) * minute)


def findMaxMinute(t):
    maxMinute = 0
    maxMinuteKey = 0
    curGuard = ""
    for key, val in t.items():
        counter = 0
        for key2, val2 in val.items():

            if (val2 >= maxMinute):
                maxMinute = val2
                maxMinuteKey = key2
                curGuard = key

    print maxMinute
    print maxMinuteKey
    print curGuard


def controller():
    groupData(dataToDict())


controller()
