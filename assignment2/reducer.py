#!/usr/bin/python
import sys

pathCount = 0
for line in sys.stdin:
	thisPath = line.strip()

	if thisPath == "/assets/js/the-associates.js":
		pathCount += 1

print pathCount
