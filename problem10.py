sendOrReceive = str(input())

priorities = ["Admiral", "Captain", "Commander", "Lieutenant", "Officer"]

if sendOrReceive == "S":
    data = {"nameSender": str(input()), "rankSender": str(input()), "nameRecv": str(input()), "rankRecv": str(input()), "msg": str(input()), "time": str(input())}

    finalStr = ""

    if priorities.index(data["rankRecv"]) > priorities.index(data["rankSender"]):
        finalStr += "URGENT,"

    ii = 0
    for i in data:
        finalStr += data[i]
        if ii < len(data)-1:
            finalStr += ","
        ii += 1

    print(finalStr)
elif sendOrReceive == "R":
    data = str(input()).split(",")

    if priorities.index(data[3]) > priorities.index(data[1]):
        print("<<< URGENT >>>")

        print("From: " + data[0])
        print("From rank: " + data[1])
        print("To: " + data[2])
        print("To rank: " + data[3])
        print("Content: " + data[4])
        print("Timestamp: " + data[5])
else:
    print("Invalid input.")