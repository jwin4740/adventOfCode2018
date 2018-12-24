from collections import defaultdict
import gc


def react(s, upper, lower):
    polymer = []
    for c in s:
        if c == upper or c == lower:
            continue
        popped = False
        if polymer:
            bk = polymer[-1]
            if c.lower() == bk.lower() and abs(ord(c) - ord(bk)) == 32:
                polymer.pop()
                popped = True
        if not popped:
            polymer.append(c)
    return len(polymer)


def chooseShortest(s):
    seq = defaultdict(int)
    ans = 100000000
    for upper in range(65, 91):
        u = chr(upper)
        l = chr(upper + 32)
        # seq[u + l] = react(s, u, l)
        ans = min(ans, react(s, u, l))
    print ans
    # react(s)


def main():
    s = None
    with open("values5.txt") as lines:
        s = lines.read()
    chooseShortest(s)


main()
