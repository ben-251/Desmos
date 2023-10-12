from src.errors import *
from src.fundamentals import *

class Line(Shape):
	def __init__(self, points, gradient = None):
		self.Validate(points,gradient)
		self.points = points
		self.gradient = gradient
		self._shapeType = "line"

	def Validate(self, points, gradient): #TODO: check that if there are more than 2 points, they are actually collinear
		if not any(isinstance(gradient, type_) for type_ in (int, float, type(None))):
			raise ValueError("Gradient should be a number")
		elif len(points) == 1 and gradient is None:
			raise NotEnoughInfo("No Gradient Provided For Single Point")
		elif len(points) == 0:
			raise NotEnoughInfo("No Points provided.")
		elif not self.isCollinear(points):
			raise NotCollinear("Points are not collinear.")
		return

	def isCollinear(self, points):
		if len(points) < 3:
			return True
		pass #TODO: finish this.

	def getRawEquation(self):
		#TODO: simplify horizontals to y = a
		firstPoint = self.points[0]
		try:
			if self.gradient is None:
				self.gradient = self.findGradient()	
			equation = f"y-{firstPoint.y}={self.gradient}\\left(x-{firstPoint.x}\\right)"
		except UndefinedGradient:
			equation = f"x={firstPoint.x}"
		return equation

	def findGradient(self): 
		#TODO: handle gradient undefined as an UndefinedGradient error and then write the code for handling that exception in the form equation method 
		firstPoint = self.points[0]
		secondPoint = self.points[1]
		try:
			gradient = (secondPoint.y - firstPoint.y)/(secondPoint.x - firstPoint.x)
		except ZeroDivisionError:
			raise UndefinedGradient
		return gradient

class BezierCurve(Shape):
	def __init__(self,points):
		pass