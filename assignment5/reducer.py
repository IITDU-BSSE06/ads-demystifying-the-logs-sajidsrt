#!/usr/bin/python
import sys
from sets import Set

path_list = Set();

for line in sys.stdin:
	path = line.strip()
	path_list.add(path);

print len(path_list)
