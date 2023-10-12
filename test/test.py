import unittest as test
from src.closedShapes import *
from src.openShapes import *

class Circles(test.TestCase):
	def testPointCoordinates(self):
		newPoint = Point(1,2)
		actual = newPoint.x, newPoint.y
		self.assertEqual(actual,(1,2))
	
	def testCircleCentre(self):
		newShape = Circle(Point(1,2),3)
		actual = newShape.Centre.x, newShape.Centre.y
		self.assertEqual(actual, (1,2))

	def testCircleShapeType(self):
		newShape = Circle(Point(1,2),2)
		actual = newShape.shapeType
		self.assertEqual(actual, "circle")

	def testEllipse(self):
		newShape = Ellipse(Point(5,1),1.4,xStretch=2,yStretch=1)
		newShape.writeEquation("output/EllipseTest")
		self.assertEqual(newShape.formEquation(),r"\left(\frac{x-5}{2}\right)^{2}+\left(\frac{y-1}{1}\right)^{2}=1.4^{2}")

class Lines(test.TestCase):
	def testNoPoints(self):
		with self.assertRaises(NotEnoughInfo):
			newLine = Line(
				[],
				gradient=2
			)

	def testNoGradient(self):
		with self.assertRaises(NotEnoughInfo):
			newLine = Line( [Point(1,2)] )
	
	def testTwoPointLine(self):
		newLine = Line(
			[ Point(1,3), Point(2,5) ]
		)
		self.assertEqual(newLine.formEquation(),r"y-3=2\left(x-1\right)")

	def testOnePointWithGradient(self):
		newLine = Line(
			[Point(-2,5)],
			gradient=2
		)
		self.assertEqual(newLine.formEquation(),r"y-5=2\left(x+2\right)")
		
	
	def testDecimalTwoPoint(self):
		newLine = Line(
			[ Point(1.1,3), Point(2.1,4) ]
		)		
		self.assertEqual(newLine.formEquation(),r"y-3=1\left(x-1.1\right)")

	def testDecimalGradient(self):
		newLine = Line(
			[Point(1,3)],
			gradient=1.5
		)		

	def testGradientNotNumber(self):
		with self.assertRaises(ValueError):
			newLine = Line(
				[Point(1,2)],
				gradient="a"
			)

	def testZeroGradientTwoPoint(self):
		newLine = Line(
			[Point(0,0), Point(2,0)]
		)
		self.assertEqual(newLine.formEquation(),r"y-0=0\left(x-0\right)")
	
	def testZeroGradientOnePoint(self):
		newLine = Line(
			[Point(0,0)],gradient=0
		)
		self.assertEqual(newLine.formEquation(),r"y-0=0\left(x-0\right)")		

	def testVertical(self):
		newLine = Line(
			[Point(2,0), Point(2,3)]
		)
		self.assertEqual(newLine.formEquation(),r"x=2")

class Polygons(test.TestCase):
	def testPolygonCreation(self):
		newShape = Polygon([Point(1,2),Point(3,4),Point(3,6)])
		self.assertEqual(newShape.formEquation(),r"\operatorname{polygon}\left(\left(1,2\right),\left(3,4\right),\left(3,6\right)\right)")

	def testTwoPointPolygon(self):
		with self.assertRaises(NotEnoughInfo):
			newShape = Polygon([Point(1,2),Point(3,4)])

	def testTwoPointPolygon(self):
		with self.assertRaises(NotEnoughInfo):
			newShape = Polygon([Point(1,2),Point(3,4)])