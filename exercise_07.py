#Chris Pitre
#Intro to Python Exercises
#Exercise 7

numList = []
quitCase = True
temp = None

while quitCase:
    temp = input("Enter a number or QUIT to quit: ")
    if temp == "QUIT":
        quitCase = False
    else:
        numList.append(int(temp))

print("All Nums: {}".format(numList))

evenNums = [i for i in numList if i % 2 == 0]

print("Even Nums: {}".format(evenNums))