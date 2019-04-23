import sys, random
from vehicle import Vehicle
from vector import Vector as v
from world import World, Path
from gui import GUI


from PyQt5 import QtGui, QtCore, QtWidgets



if __name__ == "__main__":
        
    app = QtWidgets.QApplication(sys.argv)
    dw = QtWidgets.QDesktopWidget()
    
    w = dw.width() * 0.9
    h = dw.height() * 0.8

    v0 = v(0,0)
    vel = v(10, 10)
    v1 = v(20, 20)
    paths = []
    
    vehicleCount = 8

    path1 = Path([v(100, 100), v(200, 100), v(300, 100), v(400, 100), v(500, 100),
                v(500, 200), v(500, 300), v(500, 400), v(500, 500),
                v(600, 500), v(700, 500), v(800, 500), v(900, 500), v(1000, 500),
                v(1000, 400), v(1000, 300), v(1000, 200), v(1000, 100),
                v(1100, 100), v(1200, 100), v(1300, 100)], 5)

    points1_reverse = list(reversed(path1.points))
    path1_reverse = Path(points1_reverse, 5)
    

    path2 = Path([v(250, 100), v(250, 200), v(250, 300), v(250, 400), v(250, 450), v(300, 500),
                v(350, 500), v(400, 500), v(450, 500), v(550, 500), v(650, 500), v(750, 500),
                v(750, 400), v(750, 300), v(750, 250),
                v(850, 250), v(950, 250), v(1050, 250), v(1200, 250), v(1300, 250)], 5)

    points2_reverse = list(reversed(path2.points))
    path2_reverse = Path(points2_reverse, 5)

    path3 = Path([v(100, 250), v(200, 250), v(300, 250), v(400, 250), v(500, 250), v(600, 250), v(750, 250), 
                v(750, 350), v(750, 450), v(750, 550), v(750, 650), v(750, 750),
                v(850, 750), v(950, 750), v(1000, 700), 
                v(1000, 650), v(1000, 550), v(1000, 500),
                v(1100, 500), v(1200, 500), v(1300, 500)], 5)

    points3_reverse = list(reversed(path3.points))
    path3_reverse = Path(points3_reverse, 5)

    path4 = Path([v(100, 650), v(200, 650), v(250, 630), v(250, 600), v(250, 550), v(300, 500),
                v(400, 500), v(500, 500), v(500, 600), v(500, 650), 
                v(600, 650), v(700, 650), v(800, 650), v(900, 650), v(1000, 650),
                v(1000, 600), v(1000, 500),
                v(1150, 500), v(1150, 600), v(1150, 750)], 5)

    points4_reverse = list(reversed(path4.points))
    path4_reverse = Path(points4_reverse, 5)
    
    paths.append(path1)
    paths.append(path2)
    paths.append(path3)
    paths.append(path4)
    paths.append(path4_reverse)
    paths.append(path3_reverse)
    paths.append(path2_reverse)
    paths.append(path1_reverse)
   
    world = World(w, h, paths)

    for i in range(vehicleCount):
        world.addVehicle(Vehicle(paths[(i%len(paths))].start, vel, v0, 2, 25, 20, paths[i%len(paths)]))
        
    ex = GUI(world)
    sys.exit(app.exec_())