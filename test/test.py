import unittest as test
from src.desmosShapes import *

class Circles(test.TestCase):
	def testPointCoordinates(self):
		newPoint = Point(1,2)
		actual = newPoint.x, newPoint.y
		self.assertEqual(actual,(1,2))
	
	def testCircleCentre(self):
		newShape = Circle(Point(1,2),3)
		actual = newShape.getCentre().x, newShape.getCentre().y
		self.assertEqual(actual, (1,2))

	def testCircleShapeType(self):
		newShape = Circle(Point(1,2),2)
		actual = newShape.shapeType
		self.assertEqual(actual, "circle")
		

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
			[ Point(1,3), Point(1,4) ]
		)
		self.assertEqual(newLine.shapeType,"line")

	def testOnePointWithGradient(self):
		newLine = Line(
			[Point(1,3)],
			gradient=2
		)
	
	def testDecimalTwoPoint(self):
		newLine = Line(
			[ Point(1.1,3), Point(1,4.2) ]
		)		

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
	
	def testMakeEquationOnePoint(self):
		newLine = Line(
			[Point(0.2,4)],
			gradient=0.5
		)
		newLine.writeEquation("OnePoint.txt")
	
	def testMakeEquationTwoPoints(self):
		newLine = Line(
			[Point(1,3),Point(2,5)]
		)
		newLine.writeEquation("TwoPoint.txt")

	def testZeroGradientTwoPoint(self):
		newLine = Line(
			[Point(0,0), Point(2,0)]
		)
	
	def testZeroGradientOnePoint(self):
		newLine = Line(
			[Point(0,0)],gradient=0
		)		