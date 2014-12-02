#! /usr/bin/env python

def add(n):
	res = 0	
	if n == 1:
		res = 1	
	else:
		res = add(n-1) + n
	return res

temp = int(raw_input("Enter your num:"))
print add(temp)
