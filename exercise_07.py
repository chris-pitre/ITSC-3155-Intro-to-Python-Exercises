numList = []
evenNums = []
quitCase = True
temp = None

while quitCase:
    temp = input("Enter a number or QUIT to quit: ")
    if temp == "QUIT":
        quitCase = False
    else:
        numList.append(int(temp))

print("All Nums: {}".format(numList))

for i in numList:
    if i % 2 == 0:
        evenNums.append(i)

print("Even Nums: {}".format(evenNums))