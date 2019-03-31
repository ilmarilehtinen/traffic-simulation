import sys, random
from vehicle import Vehicle
from vector import Vector
from world import World
from vehicle_graphics import VehicleGraphics

from PyQt5 import QtGui, QtCore, QtWidgets

class Testi2(QtWidgets.QMainWindow):

    def __init__(self, world, path):

        super().__init__()
        self.world = world
        self.path = path
        self.mouse = Vector(0,0)
        self.vehicleGraphicItems = []
        self.timer = QtCore.QBasicTimer()
        self.isPaused = True

        self.initUI()

    def initUI(self):

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.horizontal)

        
        
        
        
        self.setGeometry(300,300,800,800)
        self.setWindowTitle("Traffic Simulator")
        self.center()

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 700, 700)

        #Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.viewport().installEventFilter(self)
        self.view.setFrameStyle(0)

        self.view.adjustSize()
        self.view.show()
        self.horizontal.addWidget(self.view)

        #self.newSimulation()
        #self.initButtons()
        self.setMenus()
        self.add_vehicle_graphics()
        #self.showMaximized()
        self.show()
        size = self.size()
        self.view.setMouseTracking(True)

        #scene needed later?

    def eventFilter(self, source, event):
        """ Adds mouse tracking """

        if event.type() == QtCore.QEvent.MouseMove and source is self.view.viewport():
            pos = event.pos()
            mouse = Vector(pos.x(), pos.y())
            self.mouse = mouse
            print('mouse move: (%d, %d)' % (pos.x(), pos.y()))
        return QtWidgets.QWidget.eventFilter(self, source, event)

        

    def add_vehicle_graphics(self):

        for vehicle in self.world.vehicles:
            vehicleGraphicItem = VehicleGraphics(vehicle, 10)
            self.scene.addItem(vehicleGraphicItem)
            self.vehicleGraphicItems.append(vehicleGraphicItem)

            

    def updateVehicles(self):
        """ Updates the graphics for each Vehicle """

        for vehicleGraphicItem in self.vehicleGraphicItems:
            vehicleGraphicItem.updatePos()

    def initButtons(self):
        """ Function to init buttons to MainWindow """

        self.startButton = QtWidgets.QPushButton("Start Simulation")
        self.startButton.clicked.connect(self.newSimulation)
        self.horizontal.addWidget(self.startButton)
        
        self.pauseButton = QtWidgets.QPushButton("Pause")
        self.pauseButton.clicked.connect(self.pause)
        self.horizontal.addWidget(self.pauseButton)

        self.resumeButton = QtWidgets.QPushButton("Resume")
        self.resumeButton.clicked.connect(self.start)
        self.horizontal.addWidget(self.resumeButton)



    def setMenus(self):

        newAct = QtWidgets.QAction("New simulation", self)
        newAct.triggered.connect(self.newSimulation)

        exitAct = QtWidgets.QAction("Exit", self)
        exitAct.setShortcut("Esc")
        exitAct.triggered.connect(QtWidgets.qApp.quit)

        pauseAct = QtWidgets.QAction("Pause", self)
        pauseAct.triggered.connect(self.pause)

        resumeAct = QtWidgets.QAction("Resume", self)
        resumeAct.triggered.connect(self.start)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")
        fileMenu.addAction(newAct)
        fileMenu.addAction(pauseAct)
        fileMenu.addAction(resumeAct)
        fileMenu.addAction(exitAct)


    def newSimulation(self):

        
        self.isPaused = False
        self.start()

    def start(self):
        self.isPaused = False
        self.timer.start(10, self)
        self.update()

    def pause(self):
        self.isPaused = True
        self.timer.stop()
        self.update()


    """def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        
        qp.end()

    def drawPoints(self, qp):
        qp.setPen(QtCore.Qt.blue)
        for vehicle in self.world.vehicles:
            qp.drawEllipse(vehicle.location.x, vehicle.location.y, 8, 8)

        
        for i in range(len(self.path.points) - 1):
            point = self.path.points[i]
            qp.drawLine(point.x, point.y, self.path.points[i+1].x, self.path.points[i+1].y)
            
        #for i in range(500):
        x = random.randint(1, size.width()-1)
        y = random.randint(1, size.height()-1)
        qp.drawEllipse(x, y, 5, 5)"""

        

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        if not self.isPaused:
            if event.key() == QtCore.Qt.Key_Space:
                self.pause()
        elif event.key() == QtCore.Qt.Key_Space:
            self.start()
    
    """def mouseMoveEvent(self, event):
        mouse = Vector(event.x(), event.y())
        text = "x: {0} y: {1}".format(mouse.x, mouse.y)
        self.setWindowTitle(text)
        self.mouse = mouse"""
        
        
        

    def timerEvent(self, event):

        if event.timerId() == self.timer.timerId():
            
            for vehicle in self.world.vehicles:
                print(vehicle.location)
                vehicle.arrive(self.mouse)
                vehicle.move()

            self.updateVehicles()
            self.update()
            
        else: 
            QtWidgets.QWidget.timerEvent(self, event)
            


    def center(self):
        
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

