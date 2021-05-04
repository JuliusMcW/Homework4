import unittest
import volume

class Tester(unittest.TestCase):
	def test_vol1(self):
		result = volume.vol(10,20,30)
		self.assertEqual(result,6000) 


	def test_vol2(self):
		result = volume.vol(-10,20,30)
		self.assertEqual(result,6000)

	def test_vol3(self):
		result = volume.vol('a','b','c')
		self.assertEqual(result,"6000")
