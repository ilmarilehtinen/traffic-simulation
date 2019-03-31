from vector import Vector

class World():
    def __init__(self, width, heigth):

        self.width = width
        self.heigth = heigth
        self.vehicles = []

    def addVehicle(self, vehicle):
        self.vehicles.append(vehicle)

class Path():
    def __init__(self, points, radius):

        self.points = points
        self.radius = radius

    def addPoints(self, x, y):

        point = Vector(x, y)
        self.points.append(point)

