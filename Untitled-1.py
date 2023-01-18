userInput = input("Enter a word: ")

caseList = [i for i in userInput if i.islower()]
caseList.extend([i for i in userInput if i.isupper()])

print(''.join(caseList))
