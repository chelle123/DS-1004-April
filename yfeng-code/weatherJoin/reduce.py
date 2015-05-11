#!/usr/bin/python

import sys

def isfloat(value):
	try:
		float(value)
		return True
	except ValueError:
		return False


def convertEnumerate(listlike_str):
	listlike_str = eval(listlike_str)
	if len(listlike_str) <= 6: # if current list is fare data
		# remove % in tip_percenatge
		listlike_str[-1] = listlike_str[-1][:-1]
	for x in listlike_str:
		if not isfloat(x):
			return []
	return [float(x) for x in listlike_str]

'''
def increment(l1,l2):
	if not(l1) and l2:
		return l2
	if l1 and not(l2):
		return l1;	
	return map(lambda x, y: x + y, l1, l2)
'''

current_date = None
current_join = []
curr_weather = []

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	date, value = line.strip().split("\t")

	# convert value from string to a list of float numbers
	value = convertEnumerate(value)

	if date == current_date:
		if current_join: 
		# if revenue already exists
			if len(value) <= 6:
				# if current value is from fares
				current_join = value+current_join
			else:
				# if current value is from weather
				current_join = current_join+value
	else:
		if current_date and len(current_join)>11:
			# output goes to STDOUT (stream data that the program writes)
			current_join = current_join[4:]
			weather_join = ",".join(format(x,'.2f') for x in current_join)
			print current_date+","+weather_join
		
		# if current date is a new date
		current_date = date
		current_join = value

current_join = current_join[4:]
# output goes to STDOUT (stream data that the program writes)
weather_join = ",".join(format(x,'.2f') for x in current_join)
print current_date+","+weather_join



