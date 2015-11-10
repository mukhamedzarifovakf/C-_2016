import math
class Point:
    x = 0
    y = 0
    def __init__(self, str = '0,0'):
        self.x, self.y = str.split(',')
        self.x, self.y = float(self.x), float(self.y)
    def __str__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
    def __add__(self, other):
        return Point(str(self.x +other.x) + ',' + str(self.y + other.y))
    def __truediv__(self, number):
        return Point(str(self.x / number) + ',' + str(self.y / number))
    def Distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def DistanceTo(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    def perimetr(self, other1, other2):
        return self.DistanceTo(other1) + other1.DistanceTo(other2) + other2.DistanceTo(self)
N = int(input())
Points = []
for i in range(N):
    Points.append(Point(input()))
Max_perimetr = Points[0].perimetr(Points[1], Points[2])
for point1 in Points:
      for point2 in Points:
          for point3 in Points:
              if point1.perimetr(point2, point3) > Max_perimetr:
                  Max_perimetr = point1.perimetr(point2, point3)
print(Max_perimetr)