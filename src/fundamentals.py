class Point:
	def __init__(self,x,y):
			self.x = x
			self.y = y

	def __str__(self):
		return f"\\left({self.x},{self.y}\\right)"

class Shape:
	_shapeType = "default"

	def formEquation(self,x_limits = None, y_limits = None):
		if x_limits is None:
			x_limits = []
		if y_limits is None:
			y_limits = []

		equation = self.getRawEquation()
		equation = self.removeDoubleNegatives(equation)
		equation = self.stripIntegers(equation)
		equation = self.attachLimits(equation,x_limits,y_limits)
		return equation

	def writeEquation(self,filename):
		equation = self.formEquation()
		with open(filename,"w") as f:
			f.write(equation)

	def removeDoubleNegatives(self,equation):
		newEquation = ""
		skip = False
		for index in range(len(equation)):
			if skip:
				skip = False
				continue
			if equation[index] == "-" and equation[index+1] == "-":
				newEquation += "+"
				skip = True
				continue
			newEquation += equation[index]
			skip = False
		return newEquation

	def stripIntegers(self,equation):
		newEquation = ""
		skip = False
		for index in range(len(equation)):
			if skip:
				skip = False
				continue
			if equation[index] == "." and equation[index+1] == "0":
				skip = True
				continue
			newEquation += equation[index]
			skip = False
		return newEquation

	def getRawEquation(self):
		return NotImplementedError

	def attachLimits(self,equation,x_limits,y_limits):
		# limits are assumed to be in ascending order
		x_statement = ""; y_statement = ""
		if len(x_limits) == 2:
			x_statement = f"\\left\\{{{x_limits[0]}<x<{x_limits[1]}\\right\}}"
		elif len(x_limits) == 1:
			x_statement = f"\\left\\{{x<{x_limits[0]}\\right\}}"
		if len(y_limits) == 2:
			y_statement = f"\\left\\{{{y_limits[0]}<y<{y_limits[1]}\\right\}}"
		elif len(y_limits) ==1:
			y_statement = f"\\left\\{{y<{y_limits[0]}\\right\}}"
		return equation + x_statement + y_statement

	@property
	def shapeType(self):
		return self._shapeType