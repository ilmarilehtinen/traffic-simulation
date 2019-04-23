from PyQt5 import QtWidgets, QtGui, QtCore
from vector import Vector



class VehicleGraphics(QtWidgets.QGraphicsPolygonItem):

    def __init__(self, vehicle, size):
        super(VehicleGraphics, self).__init__()

        self.vehicle = vehicle
        self.size = size
        brush = QtGui.QBrush(1)
        self.setBrush(brush)
        self.drawCar()
        self.updatePos()

    def drawCar(self):

        triangle = QtGui.QPolygonF()
        triangle.append(QtCore.QPointF(self.size/2, 0)) # Tip
        triangle.append(QtCore.QPointF(3, self.size)) # Bottom-left
        triangle.append(QtCore.QPointF(self.size - 3, self.size)) # Bottom-right
        triangle.append(QtCore.QPointF(self.size/2, 0)) # Tip

        self.setPolygon(triangle)
        self.setTransformOriginPoint(self.size/2, self.size/2)

    def updatePos(self):

        x = self.vehicle.location.x
        y = self.vehicle.location.y
        QtWidgets.QGraphicsItem.setPos(self, x, y) #

    def updateRotation(self):

        direction = self.vehicle.direction
        degrees = direction.getAngle()
        QtWidgets.QGraphicsItem.setRotation(self, degrees + 90)

