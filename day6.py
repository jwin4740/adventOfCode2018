# https://www.meta-chart.com/share/untitled-chart-12319
# import matplotlib
# from matplotlib import pylab
# import profile


def mains():
    data = None
    with open("values6.txt") as f:
        data = f.read().splitlines()

    # establish min and max coordinates
    coords = []
    max_x = -5000
    min_x = 5000
    max_y = -5000
    min_y = 5000

    for line in data:
        j = line.split(', ')
        print(j)
        k = [int(x) for x in line.split(', ')]
        min_x = min(min_x, k[0])
        min_y = min(min_y, k[1])
        max_x = max(max_x, k[0])
        max_y = max(max_y, k[1])
        coords.append(k)

    width = max_x - min_x
    height = max_y - min_y

    # printing grid

    print('grid', min_x, min_y, ' =>', max_x, max_y)

    areas = [0 for x in range(len(coords))]

    for x in range(width):
        # grid.append([])
        for y in range(height):
            location = []

            for c in coords:
                absX = abs((min_x + x) - c[0])
                absY = abs((min_y + y) - c[1])
                d = absX + absY
                location.append(d)
            minDist = min(location)
            # get the closest, if shared, it's -1

            if location.count(minDist) == 1:
                owner = location.index(minDist)
                # grid[y].append(owner)

                areas[owner] += 1
            # else:
            #     grid[y].append('*')# def idx(x,y):
    #     return (x + y) * width

    # con = map(lambda x: abs(x - 43), grid[1])
    # print con
    # print sum(con)
    largest = max(areas)
    largestOwner = areas.index(largest)

    print(largestOwner, coords[largestOwner], 'has most area: ', largest)


mains()
