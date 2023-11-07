class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.value = []

        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(0)
            self.value.append(row)


    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            return self.value[row][col]
        else:
            return None

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.columns:
            self.value[row][col] = value



    def transpose(self):
        transposed = Matrix(self.columns, self.rows)
        for i in range(self.rows):
            for j in range(self.columns):
                transposed.set(i, j, self.get(j, i))
        return transposed

    def mul(self, matrix2):
        if self.columns != matrix2.rows:
            return None

        result = Matrix(self.rows, matrix2.columns)

        for i in range(self.rows):
            for j in range(matrix2.columns):
                sum_val = 0
                for k in range(self.columns):
                    sum_val += self.get(i, k) * matrix2.get(k, j)
                result.set(i, j, sum_val)

        return result


    def transf(self, transform):
        for i in range(self.rows):
            for j in range(self.columns):
                self.set(i, j, transform(self.get(i, j)))

    def print(self):
        for i in range(self.rows):
            for j in range(self.columns):
                print(self.get(i, j), end=" ")
            print()



matrix = Matrix(3, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)
matrix.set(2, 0, 7)
matrix.set(2, 1, 8)
matrix.set(2, 2, 9)
matrix.print()

print("transpusa")
transposed = matrix.transpose()
transposed.print()

matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 2)
matrix2.set(0, 1, 3)
matrix2.set(1, 0, 4)
matrix2.set(1, 1, 5)
matrix2.set(2, 0, 6)
matrix2.set(2, 1, 7)

print("inmultire:")
result = matrix.mul(matrix2)
result.print()

print("transform: toate elementele 0")
transform = lambda x: x - x
matrix.transf(transform)
matrix.print()
