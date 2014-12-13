#! /usr/bin/env python

### Note - 
### 	Essentially speaking, the total of methods how to paving the 
###	sidewalk is a Fibonacci number sequence. Because we can get a
### 	recurrsion equation f(n) = f(n-1) + f(n-2)

def Fib(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		t1, t2 = 1, 1
		tmp = 0
		for i in range(2,n):
			tmp = t1 + t2
			t1 = t2
			t2 = tmp
		return tmp

l = []
cond = True
while cond:
	tmp = raw_input("Enter your data line by line:->")
	l.append(tmp)
	if tmp == '':
		cond = False
for i in range(0,len(l)-1):
	print int(l[i])

print '--------------'
	
for i in range(0,len(l)-1):
	print Fib(int(l[i])+1)
