#! /usr/bin/env python

### List l is used to store the closing balance for the 12 months
### Each line represents a month.
l = []
for i in range(0,12):
	tmp = float(raw_input("Enter your monthly closing balance:=>"))
	l.append(tmp)

avr = 0.0
for item in l:
	avr += item
print "$%.2f" % (avr/12)
