
from collections import defaultdict
from collections import Counter
import re
abs(s[i] - s[i + 1]) == 32 and
# def parseInput(l):

#     d = map(lambda s: map(int, re.findall(r'-?\d+', s)), l)

#     for i in d:
#         print(i)
#     dictPlans = {}
#     for i in l:
#         plan = {}
#         identifier = re.compile(r"#(\d+)\s")
#         x = re.compile(r"@\s(\d+),")
#         y = re.compile(r"@\s\d+,(\d+):")
#         topLeftCoord = re.compile(r"@\s(\d+,\d+):")
#         width = re.compile(r":\s(\d+)x")
#         height = re.compile(r":\s\d+x(\d+)")
#         xOrig = int(x.findall(i)[0])
#         yOrig = int(y.findall(i)[0])
#         width = int(width.findall(i)[0])
#         height = int(height.findall(i)[0])
#         ids = int(identifier.findall(i)[0])
#         # plan["xOrig"] = xOrig
#         # plan["yOrig"] = yOrig
#         # plan["orig"] = {"x": xOrig, "y": yOrig}
#         for w in range(width):
#             for h in range(height):
#                 point = {"x": xOrig + w, "y": yOrig + h}
#                 plan[str(point["x"]) + str(point["y"])
#                      ] = {"x": xOrig + w, "y": yOrig + h}

#         dictPlans[ids] = plan

#     analyzeGrid(dictPlans)


# def checkDuplicates(coordinateDict):
#     area = 0
#     for keys, value in coordinateDict.items():
#         if value >= 1:
#             area += 1

#     removeSingles(coordinateDict)


# def analyzeGrid(dictPlans):
#     coordinateDict = {}
#     ct = Counter()
#     for key, plan in dictPlans.items():
#         for key2, coords in plan.items():
#             # if "xOrig" in plan:
#             #     del plan["xOrig"]
#             # if "yOrig" in plan:
#             #     del plan["yOrig"]
#             if key2 != "xOrig" and key2 != "yOrig":
#                 # if key2 in coordinateDict:
#                 #     coordinateDict[key2] += 1
#                 # else:
#                 #     coordinateDict[key2] = 1
#                 ct[key2] += 1
#     print(ct)
#     area = 0
#     for key in ct:
#         if ct[key] > 1:
#             area += 1

#     print(area)


# def controller():

#     parseInput(gatherInput())


# controller()


# 1 @ 1,3: 4x4


# def gatherInput():

#     data = None
#     with open("values3.txt") as lines:
#         data = [i.strip() for i in lines.readlines()]
#     return data


# 3 @ 5,5: 2x2
def claims():
    ctr = Counter()

    for line in open('values3.txt'):
        words = line.split()
        x, y = words[2].split(',')
        x, y = int(x), int(y[:-1])
        w, h = words[3].split('x')
        w, h = int(w), int(h)
        for dx in range(w):
            for dy in range(h):
                ctr[(x+dx, y+dy)] += 1

    area = 0
    for i in ctr:
        if ctr[i] > 1:
            area += 1
    return area


print(claims())
