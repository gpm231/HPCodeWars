xSize = int(input())
ySize = int(input())

def getGreater(n, n2):
    if n > n2:
        return n, n2
    else:
        return n2, n

greater, smaller = getGreater(xSize, ySize)

testSize = 1
tileSize = 0

if greater % smaller == 0:
    print(smaller)
else:
    while True:
        if testSize > greater and testSize > smaller:
            break

        if greater%testSize == 0 and smaller%testSize == 0:
            tileSize = testSize

        testSize += 1

    print(tileSize)