import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, end_point):
        return math.sqrt((self.x - end_point.x) ** 2
                         + (self.y - end_point.y) ** 2)
