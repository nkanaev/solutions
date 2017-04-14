#!/usr/bin/env python

monthranges = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_monthrange(year, month):
	if year == 1:	
		if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
			return 29
	return monthranges[month]

sundays = 0
weekday = 0  # Monday
for year in range(1900, 2001):
	for month in range(12):
		weekday += get_monthrange(year, month)
		weekday %= 7
		if weekday == 6 and year != 1900:
			sundays += 1

print sundays