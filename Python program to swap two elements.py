# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:23:52 2022

@author: ugly
"""

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	
	first = list.pop(0)
	last = list.pop(-1)
	
	list.insert(0, last)
	list.append(first)
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
