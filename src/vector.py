
import math, random

class Vector:
    """ Custom class to represent 2D vectors with x, y """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        """ Euclidian norm """
        return math.sqrt(self.x**2 + self.y**2)

    def distance(self, other):
        return (self - other).norm()

    def getPerpendicular(self):
        return Vector(self.y, -self.x)

    def inCircle(self, circle, r):
        """ Check if a Vector object is in a circle with radius r """

        squareDistance = (circle.x - self.x)**2 + (circle.y - self.y)**2
        if squareDistance < r**2:
            return True

    def normalPoint(self, start, end):
        """ Get the normal point from point(self) to line start-end """

        ab = end - start       
        ac = self - start       

        ab.normalize()
        ab.mult(ab.dot(ac))
        normalPoint = start + ab
        return normalPoint

    def getAngle(self):
        rad = math.atan2(self.y, self.x)
        deg = math.degrees(rad)
        return deg

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

    def setMagnitude(self, magnitude):
        self.normalize()
        self.mult(magnitude)

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
