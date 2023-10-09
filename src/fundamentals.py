class Point:
	def __init__(self,x,y):
			self.x = x
			self.y = y

	def __str__(self):
		return f"\\left({self.x},{self.y}\\right)"

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