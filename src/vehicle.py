from vector import Vector

class Vehicle:
    def __init__(self, location, velocity, acceleration, maxspeed, maxforce):

        self.location = location
        self.velocity = velocity
        self.acceleration = acceleration
        self.maxspeed = maxspeed
        self.maxforce = maxforce

    def seek(self, target):
        desired = target - self.location
        desired.normalize()
        desired.mult(self.maxspeed)
        
        steer = desired - self.velocity
        steer.limit(self.maxforce)
        self.applyForce(steer)

    def flee(self, target):
        desired = target - self.location
        desired.normalize()
        desired.mult(self.maxspeed)
        steer = desired - self.velocity
        steer.limit(self.maxforce)
        invSteer = Vector(-steer.x, -steer.y)
        self.applyForce(invSteer)


    def arrive(self, target):
        desired = target- self.location
        distance = desired.norm()
        if distance == 0:
            print(distance)
        desired.normalize()
        """if distance < 8:
            desired.mult(0)"""
        if distance < 100:
            clippedSpeed = self.translate(distance, 0, 100, 0, self.maxspeed)
            print(clippedSpeed)
            desired.mult(clippedSpeed)
        else:
            clippedSpeed = self.maxspeed
            desired.mult(self.maxspeed)


        if clippedSpeed <= 0.2:
            self.location = target
            return
        steer = desired - self.velocity
        steer.limit(self.maxforce)
        self.applyForce(steer)

    
    def followPath(self, path):

        predict = self.velocity
        predict.normalize()
        predict.mult(25)
        futureLocation = self.location + predict
        
        for i in range(len(path.points) - 1):
            a = path.points[i]
            b = path.points[i+1]

            normalPoint = futureLocation.normalPoint(a, b)
            if normalPoint.x < a.x or normalPoint.x > b.x:
                normalPoint = b

            distance = futureLocation.distance(normalPoint)
            direction = b-a
            direction.normalize()
            direction.mult(5)

            target = normalPoint + direction
        
            if distance > path.radius:
                self.seek(target)

    def move(self):
        self.velocity += self.acceleration
        self.velocity.limit(self.maxspeed)
        self.location += self.velocity
        self.acceleration * 0

    def applyForce(self, force):
        self.acceleration = self.acceleration + force

    def translate(self, value, leftMin, leftMax, rightMin, rightMax):
        # Figure out how 'wide' each range is
        leftSpan = leftMax - leftMin
        rightSpan = rightMax - rightMin

        # Convert the left range into a 0-1 range (float)
        valueScaled = float(value - leftMin) / float(leftSpan)

        # Convert the 0-1 range into a value in the right range.
        return rightMin + (valueScaled * rightSpan)
        


"""def main():
    
    v1 = Vector(40,70)
    v2 = Vector(0, 0)

    l1 = Vector(0, 100)



    car1 = Vehicle(v2, v2, Vector(0,0), 30, 2)
    car2 = car1
    print(car1.velocity)
    car1.seek(l1)
    print(car1.velocity)
    print(car1.location)
    car1.move()
    print(car1.velocity)
    print(car1.location)
    car1.move()
    print(car1.velocity)
    print(car1.location)
    
    v3 = Vector()
    print(v3)
    

main()"""

