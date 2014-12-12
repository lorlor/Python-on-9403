#! /usr/bin/env python

#########################################################################
### This is a solution for ACM 1004-Packets problem. It's done.
### Author: Lor(a.k.a Butcher Cat);
### E-mail: wt_lor@163.com(maybe ButcherCat@lortech.com in near future);
### Date: 12-1-2014;
### Location: Room 403, Building 9, Shandong University of Technology
### 
#########################################################################

### List l is used to store input data from user
l = []
cond = True
while cond:
	temp = []
	temp = raw_input("Enter data line by line:->")
	l.append(temp)
	if l[len(l) - 1]  == '0 0 0 0 0 0':
		cond = False
temp = l.pop(len(l) - 1)
res = []
for item in l:
	### Varialbe sum is used to store the total of products
	sum_l = 0
	pn = 0
	quotient = 0
	remainder = 0
	a_v,b_v,c_v,d_v,e_v,f_v = item.split(" ")
	a = int(a_v)
	b = int(b_v)
	c = int(c_v)
	d = int(d_v)
	e = int(e_v)
	f = int(f_v)
	sum_l += a + b*2**2 + c*3**2 + d*4**2 +e*5**2 + f*6**2
	for i in range(6,0,-1):
		quotient += sum_l / i**2
		remainder = sum_l % i**2
		sum_l = remainder
	res.append(quotient)

for i in range(0,len(res)):
	print res[i]

