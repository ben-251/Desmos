class Point:
	def __init__(self,x,y):
			self.x = x
			self.y = y

	def __str__(self):
		return f"\\left({self.x},{self.y}\\right)"

class Shape:
	_shapeType = "default"

	def formEquation(self):		
		equation = self.getRawEquation()
		equation = self.removeDoubleNegatives(equation)
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

	def getRawEquation(self):
		return NotImplementedError

	@property
	def shapeType(self):
		return self._shapeType