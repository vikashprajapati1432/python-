# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:00:05 2022

@author: ugly
"""

# function to rotate array by d elements using temp array
arr = [1, 2, 3, 4, 5, 6, 7]
def rotateArray(arr, n, d):
	temp = []
	i = 0
	while (i < d):
		temp.append(arr[i])
		i = i + 1
	i = 0
	while (d < n):
		arr[i] = arr[d]
		i = i + 1
		d = d + 1
	arr[:] = arr[: i] + temp
	return arr


# Driver function to test above function

print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 5))

# this code is contributed by Anabhra Tyagi
