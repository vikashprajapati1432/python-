# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:14:13 2022

@author: ugly
"""

# Python program to split array and move first
# part to end.

def splitArr(a, n, k):
       b = a[:k]
       return (a[k::]+b[::])
		

# main
arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n):
	print(arr[i], end = ' ')
