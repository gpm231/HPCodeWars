numberOfPoints = int(input())

points = []

for i in range(numberOfPoints):
    points.append(str(input()).split(" "))

for v in points:
    v[0] = int(v[0])
    v[1] = int(v[1])

lastPoint = [0, 0]

def getGreater(n, n2):
    if n > n2:
        return n
    else:
        return n2

def getAxis(number, axis):
    if number > 0:
        if axis == "y":
            return "north"
        else:
            return "east"
    else:
        if axis == "y":
            return "south"
        else:
            return "west"


for i, v in enumerate(points):
    x = v[0] - lastPoint[0]
    y = v[1] - lastPoint[1]

    xstr = getGreater(v[0] - lastPoint[0], lastPoint[0] - v[0])
    ystr = getGreater(v[1] - lastPoint[1], lastPoint[1] - v[1])

    if y != 0:
        print("Walk {} steps {}".format(ystr, getAxis(y, "y")))

    if x != 0:
        print("Walk {} steps {}".format(xstr, getAxis(x, "x")))

    lastPoint = v
