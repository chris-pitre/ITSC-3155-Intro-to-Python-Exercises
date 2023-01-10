intList = []

for i in range(10):
    intList.append(int(input("Enter number {}: ".format(i+1))))

print("Original List: {}".format(intList))

singleNum = list({i for i in intList if intList.count(i) == 1})

print("Nums that appear once: {}".format(singleNum))