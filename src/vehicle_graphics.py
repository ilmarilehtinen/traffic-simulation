from PyQt5 import QtWidgets, QtGui, QtCore


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
        triangle.append(QtCore.QPointF(0, self.size)) # Bottom-left
        triangle.append(QtCore.QPointF(self.size, self.size)) # Bottom-right
        triangle.append(QtCore.QPointF(self.size/2, 0)) # Tip

        """triangle.append(QtCore.QPointF(self.size/2, 0))
        triangle.append(QtCore.QpointF(0, self.size))
        triangle.append(QtCore.QPointF(self.size, self.size))
        triangle.append(QtCore.QpointF(self.size/2, 0))"""

        self.setPolygon(triangle)
        self.setTransformOriginPoint(self.size/2, self.size/2)

    def updatePos(self):

        x = self.vehicle.location.x
        y = self.vehicle.location.y

        QtWidgets.QGraphicsItem.setPos(self, x - 40, y - 30) #

