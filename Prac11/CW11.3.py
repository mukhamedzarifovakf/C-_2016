import math
class Point:
    x = 0
    y = 0
    def __init__(self, str = '0,0'):
        self.x, self.y = str.split(',')
        self.x, self.y = float(self.x), float(self.y)
    def __str__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
    def Distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __add__(self, other):
        return Point(str(self.x +other.x) + ',' + str(self.y + other.y))
    def __truediv__(self, number):
        return Point(str(self.x / number) + ',' + str(self.y / number))
N = int(input())
Points = []
for i in range(N):
    Points.append(Point(input()))
Center_of_mass = Point()
for i in range(N):
    Center_of_mass = Center_of_mass + Points[i]
Center_of_mass = Center_of_mass / N
print(str(Center_of_mass))