from collections import Counter, defaultdict


def checkIsolatedClaims(claims, ctr):
    d = defaultdict(dict)
    for tup, val in ctr.items():
        if val >= 2:
            d[tup] = tup
    for claimId in claims:
        if claimId < 525:
            continue
        match = cmpTuples(claimId, claims, d)
        if not match:
            print(claimId)
            return claimId


def cmpTuples(claimId, claims, d):
    for claim in claims[claimId]:
        if d[claim] == claim:
            return True
    return False


def claims():
    ctr = Counter()
    claims = defaultdict(lambda: "hello")

    for line in open('values3.txt'):
        claim = defaultdict(str)
        words = line.split()
        claimId = int(words[0][1:])

        x, y = words[2].split(',')
        x, y = int(x), int(y[:-1])
        w, h = words[3].split('x')
        w, h = int(w), int(h)
        for dx in range(w):
            for dy in range(h):
                claim[(x+dx, y+dy)] = 1
                ctr[(x+dx, y+dy)] += 1
        claims[claimId] = claim

    checkIsolatedClaims(claims, ctr)


claims()
