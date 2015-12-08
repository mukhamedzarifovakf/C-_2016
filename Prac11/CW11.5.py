class Point:
    def __init__(self, parametrs = ('0;0')):
        a, b = parametrs.split(';')
        self.x = float(a)
        self.y = float(b)
    def Distance(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def DistanceTo(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
    def __str__(self):
        return str(self.x) + ',' + str(self.y)
    def __add__ (self, other):
        return Point(str(self.x + other.x) + ';' + str(self.y + other. y))
    def __sub__ (self, other):
        return Point(str(self.x - other.x) + ';' + str(self.y - other. y))
    def __eq__ (self, other):
        return self. x == other. x and other. y == other.y
    def Perimetr (self, point2, point3):
        return (self.DistanceTo(point2) + point2.DistanceTo(point3) + point3.DistanceTo(self))
    def Square(self, point2, point3):
        p = self.Perimetr(point2, point3) / 2
        a = self.DistanceTo(point2)
        b = point2.DistanceTo(point3)
        c = point3.DistanceTo(self)
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5
N = int(input())
Points = []
for i in range(N):
    Points.append(Point(input()))
max_s = 0
for i in Points:
    for j in Points:
        for k in Points:
            if i.Square(k, j) > max_s:
                print(i.Square(k, j))
                max_s = i.Square(k, j)
print(max_s)