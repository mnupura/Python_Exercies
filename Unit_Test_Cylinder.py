import unittest
from Oops_Geometry import Cylinder

class TestCylinder(unittest.TestCase):

	def test_cylinder_init(self):
		height = 10
		radius = 5
		cylnd1 = Cylinder(height,radius)
		expected_height = 20
		expected_radius = 5
		self.assertEqual(cylnd1.height,expected_height,'Height incorrect')
		self.assertEqual(cylnd1.radius,expected_radius,'Radius incorrect')

	def test_volume(self):
		height = 10
		radius = 5
		cylnd2 = Cylinder(height,radius)
		actual_volume = cylnd2.volume()
		expected_volume = 20
		self.assertEqual(actual_volume,expected_volume,'Volume incorrect')

	def test_surface_area(self):
		height = 10
		radius = 5
		cylnd3 = Cylinder(height,radius)
		actual_area = cylnd3.surface_area()
		expected_area = 20
		self.assertEqual(actual_area,expected_area,'Surface area incorrect')

if __name__=='__main__':
	unittest.main()