import unittest
import add

class TestCalc(unittest.TestCase):
	
	def test_add(self):
		result = add.add(10,5)
		self.assertEqual(result, 15)
		
	def test_sub(self):
		result = add.sub(10,5)
		self.assertEqual(result, 5)
	
	def test_mul(self):
		result = add.mul(10,5)
		self.assertEqual(result, 50)
		
	def test_div(self):
		result = add.div(10,5)
		self.assertEqual(result, 2)
		
if 	__name__ == '__main__':
	unittest.main()