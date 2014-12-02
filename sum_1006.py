#! /usr/bin/env python

### Customize a function named add to calcualte the summary
def add(n):
	temp = 0
	for i in range(0,n):
		temp += i + 1
	return temp
### Note:
###	List l is used to store the user data. When user enters 'end', 
###	this progran slice stops receiving user data.
l = []
cond = True
while cond:
	temp = raw_input("Enter your data line by line:->")
	l.append(temp)
	if l[len(l) - 1] == 'end':
		cond = False

k = l.pop(len(l) - 1)
for item in l:
	print add(int(item))
