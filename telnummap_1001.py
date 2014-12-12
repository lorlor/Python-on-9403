### This source file is used to solve the ACM-487-3279 question.
### For me, it is a wonderful process to improve my skill of
### programming with python. Fortunately, this file could run 
### successfully and efficiently.

### Author: Lor(a.k.a ButcherCat);
### E-mail: wt_lor@163.com(maybe ButcherCat@lortech.com);
### Date: 11-30-2014;
### Location: Room 403, Building 9, Shandong University of Technology, Zibo, Shandong

#! /usr/bin/env python

### The function map() is used to map 24 letter
def map(ch):
	res = 0
	if ch == 'A' or ch == 'B' or ch == 'C':
		res = 2
	elif ch == 'D' or ch == 'E' or ch == 'F':
		res = 3
	elif ch == 'G' or ch == 'H' or ch == 'I':
		res = 4
	elif ch == 'J' or ch == 'K' or ch == 'L':
		res = 5
	elif ch == 'M' or ch == 'N' or ch == 'O':
		res = 6
	elif ch == 'P' or ch == 'R' or ch == 'S':
		res = 7
	elif ch == 'T' or ch == 'U' or ch == 'V':
		res = 8
	elif ch == 'W' or ch == 'X' or ch == 'Y':
		res = 9
	elif ch != 'Q' and ch != 'Z':
		res = int(ch)
	else:
		pass
	
	return res

### The following total_num means the total of phone numbers, which is at 
### the frist line in case, and the empty list is a "container" of instance
### of phone numbers. And the variable case represents the "case" in description.
total_num = int(raw_input("Enter the total of phone numbers in dictionary:"))
container = []
case = {"total":total_num,"context":container}
for i in range(0,total_num):
	k = raw_input("Enter the phone number:=>")
	container.append(k)

### Start to map "literal-nums" into "numerical-nums"
### Variable n_num represents "numerical-nums", which stores the 
### numerical telephone numbers
n_num = []
for item in case["context"]:
	temp = []
	for elem in item:
		if elem == '-':
			pass
		else:
			temp.append(str(map(elem)))
	temp.insert(3,'-')
	print temp
	string = ''.join(temp)
	n_num.append(string)
### Prepare for output
count = []
output = []
for item in n_num:
	if item in output:
		count[output.index(item)] += 1
	else:
		output.append(item)
		count.append(1)

for item in output:
	print item,count[output.index(item)]
