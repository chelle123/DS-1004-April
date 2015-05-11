#!/usr/bin/python

import sys
import string

#split line into key and value
#transfrom key and value from string to list
def convertToList(line):
	key,value = line.strip().split("\t")
	value = value.strip().split(" ")
	return (key,value)

for line in sys.stdin:
	key,value = convertToList(line)
	if key:
		print key+"\t"+str(value)
