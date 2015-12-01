class Matrix:
    def __init__(self, m, n = None):
        if isinstance(m, int):
            if not isinstance(n, int):
                raise ValueError()
            if n <= 0 or m <= 0:
                raise ValueError()
            self.m = m
            self.n = n
            self.matrix = [[0] * n for i in range(m)]
        elif not isinstance(m, list):
            raise ValueError()
        else:
            if len(m) == 0 or n != None:
                raise ValueError()
            self.matrix = m
            self.m = len(m)
            self.n = len(m[0])

    def __add__(self, other):
        if type(other) != Matrix:
            raise TypeError
        if self.m != other.m or self.n != other.n:
            raise ValueError()
        New_Matrix = [[None] * self.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                New_Matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(New_Matrix)

    def __eq__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError()
        for i in range(self.m):
            for j in range(self.n):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True

    def __sub__(self, other):
        if self.m != other.m or self.n != other.n:
            raise ValueError()
        New_Matrix = [[None] * self.n for i in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                New_Matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return Matrix(New_Matrix)

    def get(self, i, j):
        return self.matrix[i][j]

    def get_m(self):
        return self.m

    def get_n(self):
        return self.n

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def get_size(self):
        A = (self.m, self.n)
        return A

    def transpose(self):
        New_Matrix = [[None] * self.m for i in range(self.n)]
        for i in range(self.m):
            for j in range(self.n):
                New_Matrix[j][i] = self.matrix[i][j]
        return Matrix(New_Matrix)

    def __mul__(self, other):
        if type(other) != int and type(other) != float and type(other) != Matrix:
            raise TypeError()
        elif type(other) == int or type(other) == float:
             New_Matrix = self.matrix
             for i in range(self.m):
                for j in range(self.n):
                    New_Matrix[i][j] *= other
        else:
            if self.n != other.m: raise ValueError()
            New_Matrix = [[None] * other.n for i in range(self.m)]
            for i in range(self.m):
                for j in range(other.n):
                    New_Matrix[i][j] = 1
                    for k in range(self.n):
                        New_Matrix[i][j] += self.matrix[i][k]*other.matrix[k][j]
        return Matrix(New_Matrix)


    def __truediv__(self, other):
        if type(other) != int and type(other) != float:
            raise TypeError
        else:
            return self * (1/other)

    def __str__(self):
        return str(self.matrix)
