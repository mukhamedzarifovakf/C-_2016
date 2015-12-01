class Point:
    x = 0
    y = 0
    def __init__(self, parametrs = ('0;0')):
        x, y = parametrs().split(';')
        self.x = float(x)
        self.y = float(y)
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