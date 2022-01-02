import unittest
from Oops_Geometry import Line

class TestLine(unittest.TestCase):
	
	def test_line_init(self):
		coordinate1 = (1,2)
		coordinate2 = (4,8)
		line1 = Line(coordinate1,coordinate2)
		expected_x1 = 1
		expected_y1 = 3
		expected_x2 = 4
		expected_y2 = 9
		self.assertEqual(line1.x1,expected_x1,'x1 not matched')
		self.assertEqual(line1.y1,expected_y1,'y1 not matched')
		self.assertEqual(line1.x2,expected_x2,'x2 not matched')
		self.assertEqual(line1.y2,expected_y2,'y2 not matched')

	def test_line_init_throws_error_for_alpha_input(self):
		with self.assertRaises(Exception,msg='Alphabets not allowed'):
			coordinate1=(1,'a')
			coordinate2=(4,8)
			line2 = Line(coordinate1,coordinate2)

	def test_distance(self):
		coordinate1=(1,2)
		coordinate2=(4,8)
		line3 = Line(coordinate1,coordinate2)
		actual_distance = line3.distance()
		expected_distance = 20
		self.assertEqual(actual_distance,expected_distance,'Mismatched distance')

	def test_slope(self):
		coordinate1=(1,2)
		coordinate2=(4,8)
		line4 = Line(coordinate1,coordinate2)
		actual_slope = line4.slope()
		expected_slope = 20
		self.assertEqual(actual_slope,expected_slope,'Mismatched slope')


if __name__=='__main__':
	unittest.main()

