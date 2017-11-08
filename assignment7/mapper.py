#!/usr/bin/python
import sys
for line in sys.stdin:
	data = line.strip().split(" ")
	if len(data) == 10:
		method = str(data[5])
		print method
