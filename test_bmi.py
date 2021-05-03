#!/usr/bin/env python3


import unittest
#import sys

import bmi


class Testbmi(unittest.TestCase):
#put tests in here

	def test_ounces2pounds(self):
        	self.assertEqual(bmi.ounces2pounds(0), 0)
			self.assertEqual(bmi.ounces2pounds(1), 16)
	
	def test_stones2pounds(self):
        self.assertEqual(bmi.stones2pounds(0),0)
		self.assertEqual(bmi.stones2pounds(1),14)

	def test_weight2kg(self):
        self.assertEqual(bmi.weight2kg(0,0,0),0)
		#self.assertEqual(bmi.weight2kg(1,1,1),0)





if __name__ =='__main__':
    unittest.main()
    
    
    
#to run in terminal

#python3 ~/<TestfileDirectoryPath>/<testFile>.py



#assertion Methods
#https://docs.python.org/3.3/library/unittest.html#assert-methods
