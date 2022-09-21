# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 17:06:00 2022

@author: ugly
"""

# _importing module
import re
def check(str, pattern):
	
	# _matching the strings
	if re.search(pattern, str):
		print("Valid String")
	else:
		print("Invalid String")
# _driver code
pattern = re.compile('^[1234]+$')
check('2134', pattern)
check('349', pattern)
