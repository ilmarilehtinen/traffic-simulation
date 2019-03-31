import sys, random
from vehicle import Vehicle
from vector import Vector
from world import World, Path
from gui import Testi2

from PyQt5 import QtGui, QtCore, QtWidgets



if __name__ == "__main__":

    v0 = Vector(0,0)
    vel = Vector(10, 10)
    v1 = Vector(20, 20)
    world = World(800, 700)

    path = Path([Vector(1,2), Vector(20,20), Vector(40, 40), Vector(400, 600), Vector(500, 100)], 2)
    p1 = Vector(120,120)


    for _ in range(10):
        randVect = Vector(random.randint(1, world.width-1), random.randint(1,world.heigth-1))
        vehicle = Vehicle(randVect, vel, v0, 2, 1)
        world.vehicles.append(vehicle)

    app = QtWidgets.QApplication(sys.argv)
    ex = Testi2(world, path)
    #ex = Testi()
    sys.exit(app.exec_())