# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:50:11 2022

@author: ugly
"""

# Python3 code to demonstrate working of
# Adding Tuple to List and vice - versa
# Using += operator (list + tuple)

# initializing list
test_list = [5, 6, 7]

# printing original list
print("The original list is : " + str(test_list))
# initializing tuple
test_tup = (9, 10)
print(test_tup)
# Adding Tuple to List and vice - versa
# Using += operator (list + tuple)
test_list += test_tup

# printing result
print("The container after addition : " + str(test_list))

