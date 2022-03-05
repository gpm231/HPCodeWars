number = int(input())

numberOfFives = 0

for i in range(number):
    for i2 in range(len(str(i+1))):
        if str(i+1)[i2] == "5":
            numberOfFives += 1

print(numberOfFives)