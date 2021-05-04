import unittest
import avg



class Tester(unittest.TestCase):
	def test_average1(self):
		result=avg.average([1,2,3,4,5,6,7,8,9,10],10)
		self.assertEqual(result,5.5)

	def test_average2(self):
		result=avg.average([1,2,3,4,5,6,7,8,9,10],5)
		self.assertEqual(result,4)

	def test_average3(self):
		result=avg.average([],0)
		self.assertEqual(result,1)
