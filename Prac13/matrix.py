class Matrix:
    matrix = []
    columns = 0
    lines = 0
    def __init__(self, m, n = None):
        if not isinstance(m, int):
            raise ValueError()
        elif m <= 0:
            raise ValueError()
        elif n == None:
            self.matrix.append(x for x in m.split())
            columns = len(m[0])
            lines = len(m)
        elif not isinstance(n, int):
            raise ValueError()
        elif n <= 0:
            raise ValueError()
        else:
            self.matrix.append([0] * n for i in range(m))
            lines = m
            columns = n
    def __add__(self, other):
        other_matrix = Matrix(other)
        if other_matrix.columns != self.columns or other_matrix.lines != self.lines:
            raise ValueError()
        else:
            for i in range(self.columns):
                for j in range(self.lines):
                    self.matrix[i][j] += other_matrix.matrix[i][j]
    def set(self, ):