#!/usr/bin/python3.5
# coding=utf-8


def p_add(x,y):
	return x+y 
	
def p_mul(x,y):
	return x*y

def p_mod(x,y):
	return x%y

def p_div(x,y):
	return x/y 
	
def p_max(x,y):
	if x>y:
		return x 
	else:
		return y 

def p_min(x,y):
	if x<y:
		return x 
	else: 
		return y 
		
def p_isTrue():
	return 1 
	
def p_isFalse():
	return 0



