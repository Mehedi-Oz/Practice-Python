matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0][2] = 99

# print(matrix)
# print(matrix[0][2])

for row in matrix:
  for column in row:
    print(column)