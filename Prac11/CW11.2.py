import math
class Point:
    x = 0
    y = 0
    def __init__(self, str):
        self.x, self.y = str.split(',')
        self.x, self.y = int(self.x), int(self.y)
    def __str__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'
    def Distance(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
N = int(input())
Points = []
for i in range(N):
    Points.append(Point(input()))
Max_distance = Points[0].Distance()
Furthest_point = Points[0]
for i in range(N):
    if Points[i].Distance() > Max_distance:
        Furthest_point = Points[i]
        Max_distance = Points[i].Distance()
print(str(Furthest_point))