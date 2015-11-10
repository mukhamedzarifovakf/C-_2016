class Point:
    x = 0
    y = 0
    def __init__(self, str):
        self.x, self.y = str.split(',')
        self.x, self.y = int(self.x), int(self.y)
    def __str__(self):
        return 'Point(' + str(self.x) + ', ' + str(self.y) + ')'