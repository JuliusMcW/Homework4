import unittest
import name



class Tester(unittest.TestCase):
    def test_fullname1(self):
        result = name.fullname("John","Smith")
        self.assertEqual(result, "John Smith")
    def test_fullname2(self):
        result = name.fullname(1,"Jones")
        self.assertEqual(result,"1 Jones")
    def test_fullname3(self):
        result = name.fullname("John"," Smith")
        self.assertEqual(result,"John Smith")
