# Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
def ex5(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if i > j:
                matrix[i][j] = 0

matrix = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]]

ex5(matrix)
for row in matrix:
    print(row)
