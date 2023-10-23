
# Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.
def ex9(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    badSeats = []

    for row in range(rows - 1):
        for column in range(columns):
            if matrix[row][column] >= matrix[row + 1][column]:
                matrix[row][column], matrix[row + 1][column] = matrix[row + 1][column], matrix[row][column]
                badSeats.append((row+1,column))

    return badSeats

matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]


print(ex9(matrix))
