#!/usr/bin/env python3


import unittest
import sys
sys.path.append('/home/alan/<moduleDirectoryPath>')    #if testing using Travers CI, will be different
import <Module>

class TestCalc(unittest.TestCase):
#put tests in here

	def test_add(self):
        	self.assertEqual(calc.add(10, 5), 15)





if __name__ =='__main__':
    unittest.main()
    
    
    
    
    
#to run in terminal

python3 ~/<TestfileDirectoryPath>/<testFile>.py



#assertion Methods
https://docs.python.org/3.3/library/unittest.html#assert-methods
