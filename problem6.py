number = int(input())

numberOfFives = 0

for i in range(0, number):
    for i2 in range(len(str(i))):
        if str(i)[i2] == "5":
            numberOfFives += 1

print(numberOfFives)