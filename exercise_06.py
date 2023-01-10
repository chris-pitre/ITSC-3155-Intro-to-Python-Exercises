matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

x = int(input("Enter a row num from 1 to 5: ")) - 1
y = int(input("Enter a col num from 1 to 5: ")) - 1

matrix[x][y] = 1

for i in matrix:
    print(" ".join(map(str, i)))