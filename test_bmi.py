


import unittest
import sys
import bmi


class Testbmi(unittest.TestCase):
	#put tests in here
	def test_Ounces2pounds(self):
    	self.assertEqual(bmi.ounces2pounds(0),0)
		self.assertEqual(bmi.ounces2pounds(1),16)
	
	def test_Stones2pounds(self):
        self.assertEqual(bmi.stones2pounds(0),0)
		self.assertEqual(bmi.stones2pounds(1),14)

	def test_Weight2kg(self):
        self.assertEqual(bmi.weight2kg(0,0,0),0)
		#self.assertEqual(bmi.weight2kg(1,1,1),0)
	
	def test_Height2meters(self):
		self.assertEqual(bmi.height2metres(0,0),0)
		self.assertEqual(bmi.height2metres(3.82,0),1)

	def test_Categorise(self):
		self.assertEqual(bmi.categorise(0,0),'A')
		self.assertEqual(bmi.categorise(1,1),'A')

if __name__ =='__main__':
	unittest.main()
    
    
    
#to run in terminal

#python3 ~/<TestfileDirectoryPath>/<testFile>.py



#assertion Methods
#https://docs.python.org/3.3/library/unittest.html#assert-methods
