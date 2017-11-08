#!/usr/bin/python
import sys

countMethod = 0
for line in sys.stdin:
	thisMethod = line.strip()

	if thisMethod == '"GET':
		countMethod += 1

print countMethod
