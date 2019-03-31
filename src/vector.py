
import math, random

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, other):
        return (self - other).norm()

    def normalPoint(self, start, end):
        ab = end - start       
        ac = self - start       

        ab.normalize()
        ab.mult(ab.dot(ac))
        normalPoint = start + ab
        return normalPoint

    def squareNorm(self):
        return self.x**2 + self.y**2

    def normalize(self):
        norm = self.norm()
        if norm == 0:
            self.x = 0
            self.y = 0
        else:
            self.x = self.x/norm
            self.y = self.y/norm

    def dot(self, other):
        return (self.x * other.x + self.y * other.y)

    def angle(self, other):
        dot = self.dot(other)
        theta = math.acos(dot / (self.norm() * other.norm()))
        return theta
    
    def mult(self, other):
        if type(other) in (int, float):
            self.x *= other
            self.y *= other
    
    def limit(self, maxValue):
        if self.squareNorm() > maxValue*maxValue:
            self.normalize()
            self.x *= maxValue
            self.y *= maxValue

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other): 
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(self) == Vector and type(other) == Vector:
            return self.dot(other)
        elif type(other) in (int, float):
            return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in (int, float):
            return Vector(self.x / other, self.y / other)

    def __str__(self):
        return "(%g, %g)" %(self.x, self.y)

"""def main():
    a = Vector(1,2)
    b = Vector(3,2)
    c = Vector(5,2)
    d=a-a
    print(a - b)
    a1 = Vector(10, 20)
    b1 = Vector(60, 80)
    print(a1.distance(b1))
    print((b1-a1).norm())
    print(a-a)
    d.normalize()
    print(d.norm())
    print(d)
    theta = a.angle(b)
    print(theta)

    a.normalize()
    print(a)
    print(a.norm())
    a.mult(8)
    print(a)
    a.limit(0.5)
    print(a)

    

main()"""
