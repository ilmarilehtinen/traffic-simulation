from vector import Vector

class World():
    """ Class to hold information about the world status """
    def __init__(self, width, heigth, paths):

        
        self.heigth = heigth
        self.width = width
        self.vehicles = []
        self.paths = paths

    def addVehicle(self, vehicle):
        self.vehicles.append(vehicle)
    
    def addPath(self, path):
        self.paths.append(path)

    def setGeometry(self, width, heigth):
        self.width = width
        self.height = heigth


class Path():
    """ Class to represent a Path, a list of points(Vectors) """
    def __init__(self, points, radius):

        self.points = points
        self.radius = radius
        self.start = points[0]
        self.end = points[len(points) - 1]

    def addPoints(self, x, y):

        point = Vector(x, y)
        self.points.append(point)

