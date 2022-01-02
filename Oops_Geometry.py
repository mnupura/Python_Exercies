import math

class Line():
	
	def __init__(self,coord1,coord2):
		self.x1=coord1[0]
		self.y1=coord1[1]
		self.x2=coord2[0]
		self.y2=coord2[1]

	def distance(self):
		return (math.sqrt(((self.x2-self.x1)**2) + (self.y2-self.y1)**2))

	def slope(self):
		return ((self.y2-self.y1)/(self.x2-self.x1))

coordinate1=(1,2)
coordinate2=(4,8)
line1 = Line(coordinate1,coordinate2)
print('Slope: {} '.format(line1.slope()))
print('Distance: {}'.format(line1.distance()))

#-------------------------------------------------------------------------

class Cylinder():
	PI = 3.14

	def __init__(self,height,radius):
		self.height=height
		self.radius=radius

	def volume(self):
		return (self.PI * (self.radius**2) * self.height)

	def surface_area(self):
		return ((2*self.PI * self.radius * self.height) + (2*self.PI * (self.radius**2)))

height=10
radius=5
cyl1 = Cylinder(height,radius)
print('Volume: {}'.format(cyl1.volume()))
print('Surface Area: {}'.format(cyl1.surface_area()))
