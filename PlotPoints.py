from math import *
import math


# class Points:
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b

#     def translate(self, delta_x, delta_y):
#         self.x += delta_x
#         self.y += delta_y
#         return (self.x, self.y)

#     def odistance(self):
#         return (sqrt((self.x*self.x)+(self.y*self.y)))
#         # print(dist)


class Point:
    def __init__(self, a, b):
        self.r = sqrt((a*a)+(b*b))
        if a == 0:
            self.theta = 0
        else:
            self.theta = atan(b/a)

    def odistance(self):
        return (self.r)

    def translate(self, delta_x, delta_y):
        x = self.r * math.cos(self.delta_x)
        y = self.r * math.sin(self.delta_y)
        return (x, y)


data = Point(0, 0)
j = data.translate(7, 2)
print(j)
print(data.odistance)
