firstList = []
secondList = []

for i in range(5):
    firstList.append(int(input("Enter a number for the first list: ")))

for i in range(5):
    secondList.append(int(input("Enter a number for the second list: ")))

print("First List: {}".format(firstList))
print("Second List: {}".format(secondList))

commonList = list(set(firstList).intersection(secondList))

print("Common List: {}".format(commonList))