stringToSplit = input("Enter a string: ")

stringToSplit = [*stringToSplit]

splitString = [stringToSplit[i:i+3] for i in range(0, len(stringToSplit), 3)]

print(splitString)
