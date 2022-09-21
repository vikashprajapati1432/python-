# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:23:00 2022

@author: ugly
"""

# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(newList):
	size = len(newList)
	
	# Swapping
	temp = newList[0]
	newList[0] = newList[size - 2]
	newList[size - 2] = temp
	
	return newList
	
# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))
print(len(        ))
