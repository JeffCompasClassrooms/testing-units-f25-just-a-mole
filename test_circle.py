import unittest
import math
from circle import Circle

class testCircle(unittest.TestCase):
    def test_setRadiusPositive(self):
        circle = Circle(5)
        self.assertEqual(circle.setRadius(4), True)

    def test_setRadiusNegative(self):
        circle = Circle(5)
        self.assertEqual(circle.setRadius(-4), False)

    def test_getArea(self):
        circle = Circle(5)
        self.assertEqual(circle.getArea(), 25*math.pi)

    def test_getAreaTwo(self):
        circle = Circle(2)
        self.assertEqual(circle.getArea(), 0)

    def test_getCircumferencePositive(self):
        circle = Circle(5)
        self.assertEqual(circle.getCircumference(), 10 * math.pi)

    def test_getCircumferenceNegative(self):
        circle = Circle(-5)
        self.assertEqual(circle.getCircumference(), -10 * math.pi)

    def test_getCircumferenceZero(self):
        circle = Circle(0)
        self.assertEqual(circle.getCircumference(), 0)

if __name__ == "__main__":
    unittest.main()