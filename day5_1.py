# # f = None
# # with open("values5.txt") as lines:
# #     f = lines.read()

# # print f


# def readPolymer():
#     f = open("values5.txt")
#     s = f.read()
#     f.close()
#     react(s)


# def loop(s):

#     reaction = True
#     skip = False
#     l = len(s)
#     indicesToPop = []
#     for i in range(l):
#         if i < l - 1:
#             if s[i].lower() == s[i + 1].lower() and abs(ord(s[i]) - ord(s[i + 1])) == 32:
#                 # adjacent reaction
#                 reaction = True
#                 return s[:i] + s[i + 2:], True
#             else:
#                 continue


# def react(s):

#     # if (init):
#     #     newPolymer = ""
#     #     init = False
#     # else:
#     #     newPolymer = s
#     counter = 0
#     reaction = True
#     while reaction:
#         counter += 1
#         print counter
#         reaction = False
#         try:
#             s, reaction = loop(s)
#         except:
#             print "error"

#     print s


# print len(pList)


# f = None
# with open("values5.txt") as lines:
#     f = lines.read()

# print f


# def readPolymer():
#     f = open("values5.txt")
#     s = f.read()
#     f.close()
#     react(s, True, True)


# def react(s, reaction, init):
#     newPolymer = ""

#     if (init):
#         newPolymer = ""
#         init = False
#     else:
#         newPolymer = s
#     if (reaction):
#         l = len(s)
#         skip = False
#         reaction = False
#         for i in range(l):
#             if i < l - 1:
#                 if skip:
#                     skip = False
#                     break
#                 elif s[i].lower() == s[i + 1].lower() and abs(ord(s[i]) - ord(s[i + 1])) == 32:
#                     reaction = True
#                     skip = True
#                 else:
#                     newPolymer += s[i]
#         print newPolymer
#         react(newPolymer, reaction, False)
#     print newPolymer


# readPolymer()

def chooseShortest(s):


def main():
    s = None
    with open("values5.txt") as lines:
        s = lines.read()
    stk = []
    for c in s:
        popped = False
        if stk:
            bk = stk[-1]

            if (('A' <= bk <= 'Z' and 'a' <= c <= 'z') or ('A' <= c <= 'Z' and 'a' <= bk <= 'z')) and bk.lower() == c.lower():
                stk.pop()
                popped = True
        if not popped:
            stk.append(c)
    print len(stk)


main()
