#!/usr/bin/python
import sys

countHit1 = 0
countHit2 = 0
countHit3 = 0
year = " "
maxHit = 0

for line in sys.stdin:
	data = line.strip().split(":")
    year = str(data[0])
	if year == "2009":
		countHit1 += 1
	else if year == "2010":
		countHit2 += 1
	else:
		countHit3 += 1

if countHit1 > countHit2:
	if countHit1 > countHit3:
		maxHit = countHit1
		year = "2009"
	else:
		maxHit = countHit3
		year = "2011"

else:
	if countHit2 > countHit3:
		maxHit = countHit2
		year = "2010"
	else:
		maxHit = countHit3
		year = "2011"	

print "2009"+ countHit1
print "2010"+ countHit2
print "2011"+ countHit3
print "year"+year+ "had most number of hits" + maxHit

