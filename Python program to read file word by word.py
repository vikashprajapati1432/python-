# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:10:51 2022

@author: ugly
"""

# Python program to read
# file word by word

# opening the text file
with open('GFG.txt','r') as file:

	# reading each line	
	for line in file:

		# reading each word		
		for word in line.split():

			# displaying the words		
			print(word)
