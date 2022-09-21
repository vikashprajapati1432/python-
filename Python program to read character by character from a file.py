# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:11:12 2022

@author: ugly
"""

# Demonstrated Python Program
# to read file character by character


file = open('file.txt', 'r')

while 1:
	
	# read by character
	char = file.read(1)		
	if not char:
		break
		
	print(char)

file.close()
