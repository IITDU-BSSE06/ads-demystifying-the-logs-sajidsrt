#!/usr/bin/python
import sys
hitsTotal = 0
oldKey = None

maxHits = 0
maxPath = None

for line in sys.stdin:
    thisKey = line.strip()
    
    if oldKey and oldKey != thisKey:
        if hitsTotal > maxHits:
            maxHits = hitsTotal
            maxPath = oldKey
        oldKey = thisKey;
        hitsTotal = 0

    oldKey = thisKey
    hitsTotal += 1

if oldKey != None:
    if hitsTotal > maxHits:
        maxHits = hitsTotal

print maxHits
