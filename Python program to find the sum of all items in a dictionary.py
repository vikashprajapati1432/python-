# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:38:00 2022

@author: ugly
"""

# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(myDict):

	list = []
	for i in myDict:
		list.append(myDict[i])
	final = sum(list)

	return final


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))






# Python3 Program to find sum of
# all items in a Dictionary

# Function to print sum


def returnSum(dict):

	sum = 0
	for i in dict.values():
		sum = sum + i

	return sum


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))
