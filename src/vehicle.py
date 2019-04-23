from vector import Vector

class Vehicle:
    """ Class to represent a vehicle in the simulation """
    def __init__(self, location, velocity, acceleration, maxspeed, maxforce, size, path):

        self.location = location
        self.velocity = velocity
        self.direction = velocity
        self.acceleration = acceleration
        self.maxspeed = maxspeed
        self.maxforce = maxforce
        self.size = size
        self.target = path.end
        self.path = path

    def seek(self, target):
        """ Seek given target """
        
        desired = target - self.location
        desired.setMagnitude(self.maxspeed)
        
        steer = desired - self.velocity
        steer.limit(self.maxforce)
        return steer

    
    def arrive(self, target):
        """ Arrive smoothly to given target, velocity decreases linearly """

        desired = target - self.location
        distance = desired.norm()
        desired.setMagnitude(self.maxspeed)

        if distance < 150:
            clippedSpeed = self.maxspeed - (self.maxspeed/150) * (150 - distance)
            desired.setMagnitude(clippedSpeed)
        else:
            desired.setMagnitude(self.maxspeed)

        steer = desired - self.velocity
        steer.limit(self.maxforce)
        return steer

    
    def followPath(self, path):
        """ Follow the given path """

        target = self.velocity
        predict = self.velocity
        predict.setMagnitude(28)
        futureLocation = self.location + predict

        highestDist = 1000000   #variable used to find the closest normalpoint in the whole path
        
        for i in range(len(path.points) - 1):
            a = path.points[i]
            b = path.points[i+1]

            normalPoint = futureLocation.normalPoint(a, b)
            
            if normalPoint.x < min(a.x, b.x) or normalPoint.x > max(a.x, b.x) \
                or normalPoint.y < min(a.y, b.y) or normalPoint.y > max(a.x, b.x):  #Check if normalpoint is in the line
                    normalPoint = b
                   
            distance = futureLocation.distance(normalPoint)
            
            if distance < highestDist:
                highestDist = distance
                direction = b-a
                direction.setMagnitude(20)
                target = normalPoint
                target = target + direction
        
        if highestDist > path.radius:
            return self.seek(target)
        else:
            return Vector(0, 0)

    def separation(self, vehicles):
        """ Separate vehicle from other nearby vehicles """

        separationDist = self.size * 1.5
        count = 0
        separationSum = Vector(0,0)
        steer = Vector(0,0)
        for vehicle in vehicles:
            dist = self.location.distance(vehicle.location)
            if dist < separationDist and dist > 0:
                away = self.location - vehicle.location
                away.normalize()
                away = away/dist
                separationSum += away
                count += 1
        if count > 0:
            separationSum.mult(1/count)    #count the average separation vector
            separationSum.setMagnitude(self.maxspeed)
            steer = separationSum - self.velocity
            steer.limit(self.maxforce)
            return steer
        return steer



    def brake(self, vehicles):
        predict = self.velocity
        desired = self.velocity
        predict.setMagnitude(40)
        futureLocation = self.location + predict

        for vehicle in vehicles:
            oldLoc = vehicle.location
            if futureLocation.inCircle(vehicle.location, 20):
                desired.setMagnitude(self.maxspeed * 0.2)
        steer = desired - self.velocity
        offset = steer.getPerpendicular()
        offset.setMagnitude(10)
        steer = steer + offset
        steer.limit(self.maxforce)
        return steer

  

    def combineBehaviors(self, vehicles, path, *args):
        """ Check for action and call the moving algorithms """

        if args[0] == "follow":

            force = self.decideAction(path, path.end, vehicles)
        
            brake = self.brake(vehicles)        
            brake.mult(2)
        
            self.acceleration += force
            self.acceleration += brake
        elif args[0] == "arrive":
            arrive = self.arrive(self.path.end)
            separation = self.separation(vehicles)
            self.acceleration += separation
            self.acceleration += arrive
        elif args[0] == "seek_mouse":
            seek = self.seek(args[1])
            separation = self.separation(vehicles)
            self.acceleration += separation
            self.acceleration += seek


    def decideAction(self, path, target, vehicles):

        distance = self.location.distance(target)
        if distance < 30:
            vehicles.remove(self)

            return self.arrive(target)
        else:
            return self.followPath(path)
           

    def move(self):
        """ Update vehicle parameters, aka "move" the vehicle """

        self.velocity = self.velocity + self.acceleration
        self.velocity.limit(self.maxspeed)
        self.location = self.location + self.velocity
        self.direction = self.velocity
        self.acceleration.mult(0)



