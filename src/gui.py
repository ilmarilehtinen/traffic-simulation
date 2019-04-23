import sys, random
from vehicle import Vehicle
from vector import Vector
from world import World
from vehicle_graphics import VehicleGraphics

from PyQt5 import Qt, QtGui, QtCore, QtWidgets

class GUI(QtWidgets.QMainWindow):

    def __init__(self, world):

        super().__init__()
        self.world = world
        self.paths = world.paths
        self.mouse = Vector(0,0)
        self.vehicleGraphicsItems = []
        self.vehicles = world.vehicles
        self.isPaused = True
        self.timer = QtCore.QBasicTimer()
        self.timerSpeed = 10
        self.action = "follow"
        
        self.dw = QtWidgets.QDesktopWidget()
        self.initUI()

    def initUI(self):
        """ Initialize user interface """

        w = self.dw.width() * 0.9   #Find the resolution of the screen
        h = self.dw.height() * 0.8
        
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)
        self.horizontal = QtWidgets.QHBoxLayout()
        self.vertical = QtWidgets.QVBoxLayout()
        self.grid = QtWidgets.QGridLayout()
        self.centralWidget().setLayout(self.horizontal)

        self.setGeometry(0,0,w, h)
        self.setWindowTitle("Traffic Simulator")

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0,w*0.8, h)

        #Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.viewport().installEventFilter(self)
        self.view.setFrameStyle(0)
        self.view.setFixedSize(w*0.8, h)
        self.view.show()
        
        self.horizontal.addWidget(self.view)
        self.vertical.addStretch()
        self.initButtons()
        self.horizontal.addLayout(self.grid)
       
        self.setMenus()
        self.drawPaths()
        self.add_vehicle_graphics()
        self.show()
        self.view.setMouseTracking(True)

        
    def eventFilter(self, source, event):
        """ Adds mouse tracking """

        if event.type() == QtCore.QEvent.MouseMove and source is self.view.viewport():
            pos = event.pos()
            mouse = Vector(pos.x(), pos.y())
            self.mouse = mouse
        return QtWidgets.QWidget.eventFilter(self, source, event)

    def drawPaths(self):
        """ Draws all the paths/roads to screen"""
    
        for i in range(len(self.paths)):
            points = self.paths[i].points
            for j in range(len(points) - 1):

                line = QtWidgets.QGraphicsLineItem(points[j].x, points[j].y, points[j+1].x, points[j+1].y)
                #line.setBrush()
                self.scene.addItem(line)

        

    def add_vehicle_graphics(self):
        """ Adds graphicsItems for each vehicle """

        for vehicle in self.world.vehicles:
            vehicleGraphicsItem = VehicleGraphics(vehicle, vehicle.size)
            self.scene.addItem(vehicleGraphicsItem)
            self.vehicleGraphicsItems.append(vehicleGraphicsItem)

            

    def updateVehicles(self):
        """ Updates the graphics for each Vehicle """

        for vehicleGraphicsItem in self.vehicleGraphicsItems:
            vehicleGraphicsItem.updatePos()
            vehicleGraphicsItem.updateRotation()

    def initButtons(self):
        """ Function to add buttons to MainWindow """

        self.startButton = QtWidgets.QPushButton("Start Simulation")
        self.startButton.clicked.connect(self.start)
        self.grid.addWidget(self.startButton, 0, 0)
        
        self.pauseButton = QtWidgets.QPushButton("Pause")
        self.pauseButton.clicked.connect(self.pause)
        self.grid.addWidget(self.pauseButton, 0, 1)

        self.resumeButton = QtWidgets.QPushButton("Resume")
        self.resumeButton.clicked.connect(self.start)
        self.grid.addWidget(self.resumeButton, 1, 0)

        self.quitButton = QtWidgets.QPushButton("Quit")
        self.quitButton.clicked.connect(QtWidgets.qApp.quit)
        self.grid.addWidget(self.quitButton, 1, 1)

        self.addCarButton1 = QtWidgets.QPushButton("Add car to Path 1")
        self.addCarButton1.clicked.connect(lambda : self.addVehicle(0))
        self.grid.addWidget(self.addCarButton1, 2, 0)

        self.addCarButton2 = QtWidgets.QPushButton("Add car to Path 2")
        self.addCarButton2.clicked.connect(lambda : self.addVehicle(1))
        self.grid.addWidget(self.addCarButton2, 2, 1)

        self.addCarButton3 = QtWidgets.QPushButton("Add car to Path 3")
        self.addCarButton3.clicked.connect(lambda : self.addVehicle(2))
        self.grid.addWidget(self.addCarButton3, 3, 0)

        self.addCarButton4 = QtWidgets.QPushButton("Add car to Path 4")
        self.addCarButton4.clicked.connect(lambda : self.addVehicle(3))
        self.grid.addWidget(self.addCarButton4, 3, 1)

        self.addCarButton5 = QtWidgets.QPushButton("Add car to Path 5")
        self.addCarButton5.clicked.connect(lambda : self.addVehicle(4))
        self.grid.addWidget(self.addCarButton5, 4, 0)

        self.addCarButton6 = QtWidgets.QPushButton("Add car to Path 6")
        self.addCarButton6.clicked.connect(lambda : self.addVehicle(5))
        self.grid.addWidget(self.addCarButton6, 4, 1)

        self.addCarButton7 = QtWidgets.QPushButton("Add car to Path 7")
        self.addCarButton7.clicked.connect(lambda : self.addVehicle(6))
        self.grid.addWidget(self.addCarButton7, 5, 0)

        self.addCarButton8 = QtWidgets.QPushButton("Add car to Path 8")
        self.addCarButton8.clicked.connect(lambda : self.addVehicle(7))
        self.grid.addWidget(self.addCarButton8, 5, 1)

        self.addCarsBtn = QtWidgets.QPushButton("Add cars to all Paths")
        self.addCarsBtn.clicked.connect(self.addVehicles)
        self.grid.addWidget(self.addCarsBtn, 6, 0, QtCore.Qt.AlignTop)

        self.actionbutton0 = QtWidgets.QPushButton("Follow")
        self.actionbutton0.clicked.connect(lambda : self.setAction(0))
        self.grid.addWidget(self.actionbutton0, 8, 0)

        self.actionbutton1 = QtWidgets.QPushButton("Arrive")
        self.actionbutton1.clicked.connect(lambda : self.setAction(1))
        self.grid.addWidget(self.actionbutton1, 9, 0)

        self.actionbutton2 = QtWidgets.QPushButton("Seek Mouse")
        self.actionbutton2.clicked.connect(lambda : self.setAction(2))
        self.grid.addWidget(self.actionbutton2, 10, 0)




    def setMenus(self):

        newAct = QtWidgets.QAction("New simulation", self)
        newAct.triggered.connect(self.start)

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

    def setAction(self, i):
        if i == 0:
            self.action = "follow"
        elif i == 1:
            self.action = "arrive"
        elif i == 2:
            self.action = "seek_mouse"



    def start(self):

        self.isPaused = False
        self.timer = QtCore.QBasicTimer()
        self.timerSpeed = 10
        self.timer.start(self.timerSpeed, self)
        self.update()

    def pause(self):
        self.isPaused = True
        self.timer.stop()
        self.update()

    def addVehicle(self, i):
        v0 = Vector(0,0)
        vel = Vector(10, 10)

        self.world.addVehicle(Vehicle(self.paths[i].start ,vel , v0, 2, 20, 20, self.paths[i]))
        self.add_vehicle_graphics()


    def addVehicles(self):
        for i in range(len(self.paths)):
            self.addVehicle(i)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        if not self.isPaused:
            if event.key() == QtCore.Qt.Key_Space:
                self.pause()
        elif event.key() == QtCore.Qt.Key_Space:
            self.start()
      

    def timerEvent(self, event):

        if event.timerId() == self.timer.timerId():
            for vehicle in self.world.vehicles:
                vehicle.combineBehaviors(self.vehicles, vehicle.path, self.action, self.mouse)
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

