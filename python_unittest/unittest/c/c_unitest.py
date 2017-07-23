#!/usr/bin/python3.5
# coding=utf-8

import ctypes
import unittest

##mylib = ctypes.CDLL("/media/sf_vbox/python/unittest/myMathlib.so")
mylib = ctypes.CDLL("./myMathlib.so")


class myCMathTestCase(unittest.TestCase):
	def test_c_sum(self):
		self.assertEqual(mylib.c_sum(6,4), 10)
		
	def test_c_mod(self):
		self.assertEqual(mylib.c_mod(6,4), 2)
	
	def test_c_max(self):
		self.assertEqual(mylib.c_max(6,7), 7)
	
	def test_c_min(self):
		self.assertEqual(mylib.c_min(65,123), 65)
		
	def test_c_isTrue(self):
		self.assertTrue(mylib.c_isTrue())
	
	def test_c_isFalse(self):
		self.assertFalse(mylib.c_isFalse())
		
		
if __name__== '__main__':
	unittest.main()

