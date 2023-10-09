from src.errors import *
from src.fundamentals import *

class Circle(Shape):
	def __init__(self,centre,radius):
		self._centre = centre
		self._radius = radius
		self._shapeType = "circle"

	@property
	def Centre(self):
		return self._centre
	
	@property
	def Radius(self):
		return self._radius
		
	def formEquation(self):
		equation = f"\\left(x-{self._centre.x}\\right)^{{2}}+\left(y-{self._centre.y}\\right)^{{2}}=r^{{2}}"
		return equation


class Ellipse(Circle):
	def __init__(self, centre, radius, xStretch = None, yStretch = None):
		super().__init__(centre, radius)
		self._shapeType = "ellipse"
		self._xStretch = xStretch
		self._yStretch = yStretch
	
	def formEquation(self):
		return f"\\left(\\frac{{x-{self.Centre.x}}}{{{self._xStretch}}}\\right)^{{2}}+\\left(\\frac{{y-{self.Centre.y}}}{{{self._yStretch}}}\\right)^{{2}}={self.Radius}^{{2}}"

class Polygon(Shape):
	def __init__(self,points):
		self.Validate(points)
		self.points = points
	
	def Validate(self, points):
		#TODO: avoid duplicates
		if len(points) < 3:
			raise NotEnoughInfo("too few points. please input at least 3 points.")
		pass

	def formEquation(self):
		equation_head = f"\\operatorname{{polygon}}\\left("
		equation_tail = "\\right)"
		equation_body = ""

		for i, point in enumerate(self.points):
			equation_body += str(point)
			if i != len(self.points) - 1:
				equation_body += ","
		
		return f"{equation_head}{equation_body}{equation_tail}"


		

