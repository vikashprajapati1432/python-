# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:17:09 2022

@author: ugly
"""

# Python3 program to find sum in Nth group

# Check if given array is Monotonic
def isMonotonic(A):

	return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or 
         all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

# Driver program
A = [2,3,4,5,6]
# Print required result
print(isMonotonic(A))

# This code is written by
# Sanjit_Prasad
