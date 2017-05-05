#!/bin/bash

X = 5
def Access():
	print X 
	return 0  

def Assign():
	global X 
	X = 10 
	return 0 

if __name__ == '__main__':
	Assign() 
	Access() 

