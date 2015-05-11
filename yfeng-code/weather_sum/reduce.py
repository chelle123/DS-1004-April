#!/usr/bin/python

import sys

def isfloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False


def convertEnumerate(str_seems_list):
	str_seems_list = eval(str_seems_list)
	for x in str_seems_list:
		if not isfloat(x):
			return []
	return [float(x) for x in str_seems_list]

def increment(l1,l2):
	if not(l1) and l2:
		return l2
	if l1 and not(l2):
		return l1;	
	return map(lambda x, y: x + y, l1, l2)


current_daytime = None
current_sum = []

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	daytime, revenue = line.strip().split("\t")

	# convert revenue from string to a list of float numbers
	revenue = convertEnumerate(revenue)

	if daytime == current_daytime:
		if current_sum:
			current_sum = increment(current_sum, revenue)
	else:
		if current_daytime:
			# output goes to STDOUT (stream data that the program writes)
			total_revenue = " ".join(format(x,'.2f') for x in current_sum)
			print current_daytime+"\t"+total_revenue
		current_daytime = daytime
		current_sum = revenue
        
# output goes to STDOUT (stream data that the program writes)
total_revenue = " ".join(format(x,'.2f') for x in current_sum)
print current_daytime+"\t"+total_revenue



