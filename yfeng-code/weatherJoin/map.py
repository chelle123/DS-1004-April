#!/usr/bin/python

import sys
import string


for line in sys.stdin:
	key,value = line.strip().split("\t")
	value = value.strip().split(" ")
	if key:
		print key+"\t"+str(value)
