########################################################################################
### This file is the solution of the ACM 1002 Biorhythms. Fortunately, it can run 
### successfully and the output is precisely correct. Damn! I like kinda experince.
###
### Author:	Lor(a.k.a Butcher Cat);
### E-mail:	wt_lor@163.com (maybe ButcerCat@lortech.com in near future);
### Date:	12-1-2014
### Location:	Room 403, Building 9, Shandong University of Technology, Zibo, Shandong
###
########################################################################################
#! /usr/bin/env python

### List l is used to storet the incoming data from user.
l = []
cond = True
while cond:
	temp = raw_input("Enter your data line by line:")
	l.append(temp)
	if l[len(l) - 1] == '-1 -1 -1 -1':
		cond = False
temp = l.pop(len(l) - 1)
for item in l:
	a,b,c = 1,1,1
	p_v,e_v,i_v,d_v = item.split(" ")
	p = int(p_v)
	e = int(e_v)
	i = int(i_v)
	d = int(d_v)
	if p == 0 and e == 0 and i == 0:
		print "Case %d: the next triple peak occurs in 21252 days" % (l.index(item)+1)
	else:
	### The following procedure is the most important part and the "Kernel" for this solution
		while 23*a+p != 33*c+i or 28*b+e != 33*c+i:
			if 23*a+p < 28*b+e or 23*a+p < 33*c+i:
				a += 1
			if 28*b+e < 23*a+p or 28*b+e < 33*c+i:
				b += 1
			if 33*c+i < 23*a+p or 33*c+i < 28*b+e:
				c += 1
			else:
				pass
		print "Case %d: the next triple peak occurs in %d days" % (l.index(item)+1,33*c + i - d)	
