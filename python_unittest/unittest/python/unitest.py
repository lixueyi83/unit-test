#!/usr/bin/python3.5

import unittest 
from myMath import *

''' 
this is a test
The standard workflow is:
1. You define your own class derived from unittest.TestCase.
2. Then you fill it with functions that start with 'test_'.
3. You run the tests by placing unittest.main() in your file, usually at the bottom.

Note:
	Passing the -v option to your test script will instruct unittest.main() to enable a higher level of verbosity. 
''' 

class TestStringMethods(unittest.TestCase):
	
	def test_upper(self):
		self.assertEqual('foo'.upper(),'FOO')
		
	def test_isupper(self):
		self.assertTrue('FOO'.isupper())
		self.assertFalse('Foo'.isupper())
	
	def test_split(self):
		s = 'hello world'
		self.assertEqual(s.split(), ['hello', 'world'])
		## check that s.split fails when the separator is not a string 
		with self.assertRaises(TypeError):
			s.split(2)
			
	def test_mymath(self):
		x = 6
		y = 4
		self.assertEqual(p_add(x,y), 10)
		self.assertEqual(p_mul(x,y), 24)
		self.assertEqual(p_mod(x,y), 2)
		self.assertEqual(p_div(x,y), 1.5)
		self.assertEqual(p_max(x,y), x)
		self.assertEqual(p_min(x,y), y)
		self.assertTrue(p_isTrue())
		self.assertFalse(p_isFalse())
		
			
if __name__== '__main__':
	unittest.main()
	
		
		
		
		
