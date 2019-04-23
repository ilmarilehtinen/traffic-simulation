
import unittest
from vector import Vector

class VectorTest(unittest.TestCase):
    """ Test class to test the custom Vector class """

    def testNorm(self):
        self.assertEqual(Vector(3,4).norm(), 5)

    def testNormZero(self):
        self.assertEqual(Vector(0,0).norm(), 0)

    def testDistance(self):
        dist = Vector(0,0).distance(Vector(2,0))
        self.assertEqual(dist, 2)

    def testPerdendicular(self):
        dot = Vector(2,6).dot(Vector(6,-2))
        self.assertEqual(dot, 0)

    def testinCircle(self):
        circle = Vector(3,3)
        r = 2
        self.assertTrue(Vector(4,4).inCircle(circle, r))

    def testNormalPoint(self):
        a = Vector(0, 0)
        b = Vector(3, 0)
        c = Vector(2 ,1)
        np = c.normalPoint(a,b)
        self.assertEqual((np.x, np.y), (2,0))

    def testGetAngle(self):
        pass
    
    def testSquareNorm(self):
        self.assertEqual(Vector(2,2).squareNorm(), 8)

    def testNormalize(self):
        a = Vector(2,3)
        a.normalize()
        self.assertEqual(a.norm(), 1)

    def testSetMagnitude(self):
        a = Vector(1,3)
        a.setMagnitude(5)
        self.assertEqual(a.norm(), 5)

    def testDot(self):
        self.assertEqual(Vector(1,2).dot(Vector(2,3)), 8)

    def testMult(self):
        a = Vector(1,4)
        a.mult(2)
        self.assertEqual((a.x, a.y), (2,8))

    def testLimit(self):
        a = Vector(2,5)
        a.limit(2)
        self.assertEqual(a.norm(), 2)

    def testAdd(self):
        a = Vector(1,2)
        b = Vector(2,3)
        c = a+b
        self.assertEqual((c.x, c.y), (3, 5))

    def testSub(self):
        a = Vector(1,2)
        b = Vector(2,3)
        c = a-b
        self.assertEqual((c.x, c.y), (-1, -1))

    def testMul(self):
        a = Vector(1,2)
        b = Vector(2,3)
        c = a*b
        self.assertEqual(c, 8)

    def testrMul(self):
        pass
    
    def testDiv(self):
        a = Vector(4,6)
        a = a/2
        self.assertEqual((a.x, a.y), (2,3))

    def testStr(self):
        a = Vector(3,6)
        self.assertEqual(str(a),'(3, 6)')



if __name__ == "__main__":
    unittest.main()