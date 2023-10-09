from enum import Enum, auto
from src.errors import *

class lineType(Enum):
	HORIZONTAL = auto()
	VERTICAL = auto()
	DIAGONAL = auto()

class Point:
	def __init__(self,x,y):
			self.x = x
			self.y = y

class Shape:
	_shapeType = "default"

	def formEquation(self):		
		raise NotImplementedError

	def writeEquation(self,filename):
		equation = self.formEquation()
		with open(filename,"w") as f:
			f.write(equation)

	@property
	def shapeType(self):
		return self._shapeType

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
		return

	def formEquation(self):
		#TODO: simplify horizontals to y = a
		if self.gradient is None:
			self.gradient = self.findGradient()

		firstPoint = self.points[0]
		equation = f"y\\ -\\ {firstPoint.y}={self.gradient}\\left(x-{firstPoint.x}\\right)"
		return equation

	def findGradient(self): 
		#TODO: handle gradient undefined as an UndefinedGradient error and then write the code for handling that exception in the form equation method 
		firstPoint = self.points[0]
		secondPoint = self.points[1]
		gradient = (secondPoint.y - firstPoint.y)/(secondPoint.x - firstPoint.x)
		return gradient

class Circle(Shape):
	def __init__(self,centre,radius):
		self._centre = centre
		self._radius = radius
		self._shapeType = "circle"

	def getCentre(self):
		return self._centre
	
	def getRadius(self):
		return self._radius
		
	def formEquation(self):
		equation = f"\left(x-{self._centre.x}\\right)^{{2}}+\left(y-{self._centre.y}\\right)^{{2}}=r^{{2}}"
		return equation




